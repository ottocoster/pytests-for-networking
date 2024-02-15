from comfy.compliance import low


@low(
  name='rule_3311_set_key_chain',
  platform=['cisco_ios', 'cisco_xe'],
  commands=dict(chk_cmd='sh run | sec key chain')
)
def rule_3311_set_key_chain(commands):
    uri = (
        "http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_pi/command/iri-cr-ahtml#GUID-A62E89F5-"
        "0B8B-4CF0-B4EB-08F2762D88BB"
    )

    remediation = (f"""
    Remediation: hostname(config)#key chain {{<em>key-chain_name</em>}}

    References: {uri}

    """)

    assert ' key chain' in commands.chk_cmd, remediation