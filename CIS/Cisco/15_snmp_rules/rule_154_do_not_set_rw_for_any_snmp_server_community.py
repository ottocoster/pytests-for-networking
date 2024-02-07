from comfy.compliance import medium

uri = (
    "http://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-shtml#GUID-2F3F13E4-EE81-4"
    "590-871D-6AE1043473DE"
)

remediation = (f"""
    Remediation: hostname(config)#no s nmp-server community {{<em>write_community_string</em>}}

    References: {uri}

    """)


@medium(
  name='rule_154_do_not_set_rw_for_any_snmp_server_community',
  platform=['cisco_ios', 'cisco_xe']
)
def rule_154_do_not_set_rw_for_any_snmp_server_community(configuration):
    assert 'snmp-server community' in configuration, remediation
