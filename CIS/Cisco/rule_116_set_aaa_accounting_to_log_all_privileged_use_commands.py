
import pytest
from comfy.compliance import Source, low

@low(
  name = rule_116_set_aaa_accounting_to_log_all_privileged_use_commands,
  platform = ['cisco_ios']
)
def rule_116_set_aaa_accounting_to_log_all_privileged_use_commands(configuration,commands,device):
    assert 'aaa accounting commands' in configuration  

#Remediation: hostname(config)#aaa accounting commands 15 {default | list -name | guarantee -

#References: 
