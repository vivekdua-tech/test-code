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
from jdevice import *
import os
import time

class v4Estimator():

    def __init__(self, hostname):
        self.jd = jdevice.jdevice(hostname)

    def run(self, config):
        index = 0
        for cfg in config:
            self.jd.push_cfg(cfg)
            time.sleep(20)
            self.jd.pfe_shell(1, 'show npu memory info', f"/tmp/npu{index}.stats")
            index += 1
            self.rollback_cfg()
            time.sleep(10)




