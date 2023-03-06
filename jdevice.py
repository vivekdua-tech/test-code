from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import LockError
from jnpr.junos.exception import UnlockError
from jnpr.junos.exception import ConfigLoadError
from jnpr.junos.exception import CommitError
from jnpr.junos.exception import RpcError
from jnpr.junos.utils.scp import SCP
from jnpr.junos.utils.start_shell import StartShell
from lxml import etree
import time
import os


class jdevice():

    def __init__(self, hostname):
        self.dev = Device(host=hostname, user='root', password='Embe1mpls', gather_facts=True)
        self.dev.open()
        self.cu = Config(self.dev)
        self.hosttype = 'brackla' if 'brackla' in self.dev.hostname else 'scapa'
        self.fpclist = []
        lst = self.cli_command('show chass fpc')
        for entry in lst[2:]:
            self.fpclist.append(f"fpc{entry.split()[0]}")


    def rollback_cfg(self):
        try:
            print("Rolling back the configuration")
            self.cu.rollback(rb_id=1)
            print("Committing the configuration")
            self.cu.commit()
        except CommitError as err:
            print("Error: Unable to commit configuration: {0}".format(err))
        except RpcError as err:
            print("Unable to roll back configuration changes: {0}".format(err))

    def display_filters(self, command):
        with StartShell(self.dev) as shel:
            cmd = "cli -c 'show firewall'"
            result = shel.run(cmd)
            return result

    def cli_command(self, command):
        with StartShell(self.dev) as shel:
            cmd = f"cli -c '{command}'"
            result = shel.run(cmd)
            lst = result[1].split('\r\n')
            return lst[1:-1]
            #for i in range(1, len(lst) - 1):
            #    print(lst[i])


    def evo_aftman_pid(self):
        with StartShell(self.dev) as shel:
            if self.hosttype is 'brackla':
                cmd = 'ps aux | grep evo-aftmand-zx'
                result = shel.run(cmd)
                for  i in result[1].split('\r\n'):
                    if '/usr/sbin/evo-aftmand' in i:
                        return i.split()[1]
            else:
                if  self.hosttype is 'scapa':
                    pidList = {}
                    for fpc in self.fpclist:
                        cmd = f"chvrf iri rsh {fpc} 'ps aux | grep evo-aftmand-bt' "
                        result = shel.run(cmd)
                        for i in result[1].split('\r\n'):
                            if '/usr/sbin/evo-aftmand' in i:
                                pidList[fpc] = i.split()[1]
                    return pidList


    def run_show_firewall_with_perf(self, timeout):

        with StartShell(self.dev) as shel:
            if self.hosttype is 'brackla':
                pid = int(self.evo_aftman_pid())
                result = shel.run('cd /home/root')
                result = shel.run('rm -rf perf.*')
                cmd = f"perf record --call-graph fp -p {pid} -- sleep {timeout} &"
                result = shel.run(cmd)
                cmd = "cli -c 'show firewall'"
                result = shel.run(cmd)
                time.sleep(timeout + 20)
            else:
                if self.hosttype is 'scapa':
                    for fpc in self.fpclist:
                        pid = int(self.evo_aftman_pid()[fpc])
                        result = shel.run(f"chvrf iri rsh {fpc} 'cd /home/root'")
                        result = shel.run(f"chvrf iri rsh {fpc} 'rm -rf perf.*'")
                        cmd = f"perf record --call-graph fp -p {pid} -- sleep {timeout} &"
                        result = shel.run(f"chvrf iri rsh {fpc} '{cmd}'")
                        cmd = "cli -c 'show firewall'"
                        result = shel.run(cmd)
                        time.sleep(timeout + 20)


    def run_perf_script(self):
        with StartShell(self.dev) as shel:
            if self.hosttype is 'brackla':
                cmd = f"perf script -i /home/root/perf.data > /home/root/perf.scr"
                result = shel.run(cmd)
                self.recv_scp('/home/root/perf.scr')
                os.system('/Users/vivekdua/PycharmProjects/pyclass/FlameGraph/perf_scr_to_flame perf.scr > ./perf.svg')

            else:
                if self.hosttype is 'scapa':
                    for fpc in self.fpclist:
                        cmd = f"perf script -i /home/root/perf.data > /home/root/perf.scr"
                        result = shel.run(f"chvrf iri rsh {fpc} '{cmd}'")
                        result = shel.run(f"chvrf iri rcp root@{fpc}:/home/root/perf.scr perf.scr.{fpc}")
                        self.recv_scp(f"perf.scr.{fpc}")
                        os.system(f'/Users/vivekdua/PycharmProjects/pyclass/FlameGraph/perf_scr_to_flame perf.scr.{fpc} > perf.{fpc}.svg')

    def push_cfg_file(self, file):
        try:
            self.cu.load(path=file, format ='set')
        except (ConfigLoadError, Exception) as err:
            print("Config load error : {0} ".format(err))
            print("Unlocking the configuration")
            try:
                self.cu.unlock()
            except UnlockError:
                print("Unable to unlock configuration: {0}".format(err))
            return
        try:
            self.cu.commit(comment='Loaded by example.')
        except CommitError as err:
            print("Unable to commit configuration: {0}".format(err))
            print("Unlocking the configuration")
            try:
                self.cu.unlock()
            except UnlockError as err:
                print("Unable to unlock configuration: {0}".format(err))
            return

    def push_cfg(self, cfgStr):
        try:
            self.cu.load(cfgStr, format ='set')
        except (ConfigLoadError, Exception) as err:
            print("Config load error : {0}".format(err))
            print("Unlocking the configuration")
            try:
                self.cu.unlock()
            except UnlockError:
                print("Unable to unlock configuration: {0}".format(err))
            return
        try:
            self.cu.commit(comment='Loaded by example.')
        except CommitError as err:
            print("Unable to commit configuration: {0}".format(err))
            print("Unlocking the configuration")
            try:
                self.cu.unlock()
            except UnlockError as err:
                print("Unable to unlock configuration: {0}".format(err))
            return


    def write_result(self, filename, result):
            try:
                with open(filename, 'a') as file:
                    file.write(result)
                    file.write('\n')
            except (OSError, FileNotFoundError, IOError) as e:
                print(f"Exception:{e.errno}")


    def pfe_shell(self, fpc_index, cmd, resultfile):
        with StartShell(self.dev) as ss:
            #cprod -A fpc0 -c "show npu memory info" >> /var/tmp/npu.stats
            finalcmd = f"cprod -A fpc{fpc_index} -c '{cmd}' >> {resultfile}"
            print(finalcmd)
            result = ss.run(finalcmd)
            self.recv_scp(f"{resultfile}")
            #self.write_result('npu.stats', result[1])
            #self.recv_scp('/var/tmp/npu.stats')
            #version = ss.run('cli -c "show version"')
            #print(version)

    def send_scp(self, localfile, remotefile):
        with SCP(self.dev, progress=True) as scp:
            scp.put(local_path=localfile, remote_path=remotefile)

    def recv_scp(self, remotefile):
        with SCP(self.dev, progress=True) as scp:
            scp.get(remote_path=remotefile)




