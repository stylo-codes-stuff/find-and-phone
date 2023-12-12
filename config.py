import yaml

def update_keys():
    with open("config.yaml") as f:
        cfg = yaml.safe_load(f)
    print("enter your twilio SID")
    SID = input()
    print("enter your twilio authentication key")
    auth_key = input()
    cfg['SID'] = SID
    cfg['auth_key'] = auth_key
    with open("config.yaml", "w") as f:
        cfg = yaml.dump(
            cfg, stream=f, default_flow_style=False, sort_keys=False
    )
def dialer_config():

update_keys()
