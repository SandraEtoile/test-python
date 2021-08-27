import json

with open("travel.json", "r") as j:
    travel_data = json.load(j)
    print(travel_data)

travel_data['destinations'].append('Belarus')

print(travel_data)

with open("travel_new.json", 'w') as fp:
    json.dump(travel_data, fp, indent=2)