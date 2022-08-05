import json
countries = {}
countries["Austria"] = {"Austrian Airlines":{"aircraft": ["B737", "A320"]}, "Eurowings Europe":{"aircraft": ["B737", "A320"]}, "easyJet Europe":{"aircraft": ["B737", "A320"]}}
# countries["Belgium"] = {"Air Belgium", "Brussels Airlines", "TUIfly Belgium"}


y = json.dumps(countries, indent=4, sort_keys=True)
print(y)





# filename = "airlines.json"

# with open(filename) as f:
#     data = json.load(f)

# print(data)