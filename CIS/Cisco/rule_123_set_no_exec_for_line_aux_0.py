
import pytest
from comfy.compliance import Source, medium

@medium(
  name = rule_123_set_no_exec_for_line_aux_0,
  platform = ['cisco_ios']
)
def rule_123_set_no_exec_for_line_aux_0(configuration,commands,device):
    assert 'hostname#show line aux 0 | incl exec' in configuration  

#Remediation: hostname(config)#line aux 0  

#References: 1. http://www.cisco.com/en/US/docs/ios -
