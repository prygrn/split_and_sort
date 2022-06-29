import json
from split_and_sort import split_and_sort

# Opening JSON file
f = open("./split_and_sort_test_scenarii.json")

# returns JSON object as a dictionary
scenarii = json.load(f)

for scenario in scenarii:
    s_name = scenario["name"]
    print(f"Playing scenario {s_name}")
    out = split_and_sort(scenario["sentence"], scenario["size"])
    if str(out) == str(scenario["expected"]):
        print("Test OK")
    else:
        print("Test NOK")
        print(f"Returned value : {out}")
