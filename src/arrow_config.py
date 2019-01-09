import re
import json

conf = {}

i = 1
while i < 3:
    while(True):
        print("OLL {}\nAUF? [U, U2, U', None]".format(i))
        auf = input().upper()
        if auf in ["U", "U2", "U\'", "NONE"]:
            break
    while(True):
        print("Arrow between:")
        arrow = input().upper()
        if re.fullmatch("[URF][0-9][URF][0-9]", arrow):
            break
    while(True):
        print("type? [same, diag]")
        colortype = input().lower()
        if colortype in ["same", "diag"]:
            break
    print("OLL {} done. ".format(i))
    conf["OLL{}".format(i)] = {"AUF": auf,
                               "arrow": arrow,
                               "type": colortype}
    i += 1

with open("../data/arrow_config.json", "w") as f:
    json.dump(conf, f, ensure_ascii=False, indent=4)
