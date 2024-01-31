import pytest
from comfy.compliance import *

@medium(
  name = 'rule_21114_set_seconds_for_ip_ssh_timeout_for_60_seconds_or_less',
  platform = ['cisco_ios'],
  commands=dict(check_command='sh ip ssh')
)
def rule_21114_set_seconds_for_ip_ssh_timeout_for_60_seconds_or_less(configuration, commands, device):
    assert 'hostname#sh ip ssh' in configuration

# Remediation: hostname(config)#ip ssh time-out [<em>60</em>]  

# References: 1.http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-i3.html#GUID-5BAC7A2B-0A25-400F-AEE9-C22AE08513C6
