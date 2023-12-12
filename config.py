import yaml
import os
def update_keys():
    print("enter your twilio SID")
    SID = input()
    print("enter your twilio authentication key")
    auth_key = input()
    os.environ['SID'] = SID
    os.environ['twilio_auth_key'] = auth_key
def dialer_config():
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
            cfg, stream=f, default_flow_style=False, sort_keys=False)
update_keys()
