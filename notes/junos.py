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


class jdevice():
    def __init__(self, hostname):
        try:
            self.dev = Device(host=hostname, user='root', password='Embe1mpls', gather_facts=True)
            self.dev.open()
        except ConnectError as err:
            print("Cannot connect to device: {0}".format(err))
            return
        with Config(self.dev) as self.cu:
            diff = self.cu.diff()
            if diff:
                self.cu.rollback()

    def push_cfg(self, file):
        try:
            self.cu.load(path=file, format ='set')
        except (ConfigLoadError, Exception) as err:
            print("Config load error : {0} {1}".format(err, cfg))
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


    def shell(self, cmd):
        with StartShell(self.dev) as ss:
            #cprod -A fpc0 -c "show npu memory info" >> /var/tmp/npu.stats
            result = ss.run(cmd)
            self.write_result('npu.stats', result)
            #self.recv_scp('/var/tmp/npu.stats')
            #version = ss.run('cli -c "show version"')
            #print(version)

    def send_scp(self, localfile, remotefile):
        with SCP(self.dev, progress=True) as scp:
            scp.put(localfile, remote_path=remotefile)

    def recv_scp(self, remotefile):
        with SCP(self.dev, progress=True) as scp:
            scp.get(remote_path=remotefile)
