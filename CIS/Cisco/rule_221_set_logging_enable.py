
import pytest
from comfy.compliance import Source, medium

@medium(
  name = rule_221_set_logging_enable,
  platform = ['cisco_ios']
)
def rule_221_set_logging_enable(configuration,commands,device):
    assert 'hostname#show run | i logging host' in configuration  

#Remediation: hostname(config)#archive  

#References: 
