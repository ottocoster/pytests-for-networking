from comfy.compliance import medium


@medium(
  name='rule_157_set_snmp_server_host_when_using_snmp',
  platform=['cisco_ios', 'cisco_xe']
)
def rule_157_set_snmp_server_host_when_using_snmp(configuration):
    uri = (
        "http://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-s5.html#GUID-D84B2AB5-"
        "6485-4A23-8C26-73E50F73EE61"
    )

    remediation = (f"""
    Remediation: hostname(config)#snmp-server host {{ip_address}} {{trap_community_string}}

    References: {uri}

    """)

    assert 'snmp-server' in configuration, remediation
