import json
import requests

#1. Send get request
response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
print("Status code:      ", response.status_code)
print("Response content: ", response.content)
print("Response text:",response.text)
print("Response Json:", response.json())
if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not Found.")


#2. Print all response headers
print(response.headers)

#3. Get specific header value
print("Content-Type: ",response.headers["Content-Type"])

#4. print the JSON value of the response
response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
json_data = response.json()
print(json_data)
#print("emails_url: ",json_data["emails_url"])


#5. Pretty print json data
response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
json_data = response.json()
pretty_json = json.dumps(json_data, indent=4)
print (pretty_json)

#6. Json data extraction-1
response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
#[{'ability': {'name': 'limber', 'url': 'https://pokeapi.co/api/v2/ability/7/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'imposter', 'url': 'https://pokeapi.co/api/v2/ability/150/'}, 'is_hidden': True, 'slot': 3}]

json_data = response.json()
print("Level 1: ",json_data["abilities"][0])

json_data = response.json()
print("Level 2: ",json_data["abilities"][1])

print("Attribute 1: ",json_data["abilities"][0]["ability"]["name"])


#7. Looping through json data
response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
#[{'ability': {'name': 'limber', 'url': 'https://pokeapi.co/api/v2/ability/7/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'imposter', 'url': 'https://pokeapi.co/api/v2/ability/150/'}, 'is_hidden': True, 'slot': 3}]
json_data = response.json()
for ability in json_data["abilities"]:
    print (ability['ability']['name'])

for gI in json_data["game_indices"]:
    print(gI["version"]["url"])

#8. Looping through json data to extract data if it matches condition
response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
json_data = response.json()
for gI in json_data["game_indices"]:
    if gI["game_index"] == 76:
        print(gI["version"]["url"])

for gI in json_data["game_indices"]:
    if gI["game_index"] == 132:
        print(gI["version"]["url"])

for stat in json_data["stats"]:
     print(stat["stat"]["name"])

#9. Looping through json data to extract data if it matches condition
response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
json_data = response.json()
for stat in json_data["stats"]:
    if stat["stat"]["name"] == "hp":
        print(stat["base_stat"])


#10. Extract and Print Pokémon Name and ID
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
json_data = response.json()
i=0
for result in json_data["results"]:
    i=i+1
    print(str(i)+". "+ result["name"]+"; "+result["url"])

#11. List All Abilities of a Pokémon
response = requests.get("https://pokeapi.co/api/v2/pokemon/moltres")
json_data = response.json()
for ability in json_data["abilities"]:
    print(ability["ability"]["name"])

#12. Filter and Print Hidden Abilities
response = requests.get("https://pokeapi.co/api/v2/pokemon/exeggutor")
json_data = response.json()
for ability in json_data["abilities"]:
    if (ability["is_hidden"]==True):
        print("Hidden ability:", ability["ability"]["name"])

#13. List All Game Indices
response = requests.get("https://pokeapi.co/api/v2/pokemon/exeggutor")
json_data = response.json()
for gI in json_data["game_indices"]:
    print(gI["version"]["name"])

#14. Filter Game Indices by Version
response = requests.get("https://pokeapi.co/api/v2/pokemon/exeggutor")
json_data = response.json()
for gI in json_data["game_indices"]:
    if gI["version"]["name"] == "gold":
        print(gI["version"]["name"])
        print(gI["version"]["url"])

#15. Extract and Print Base Stats
response = requests.get("https://pokeapi.co/api/v2/pokemon/exeggutor")
json_data = response.json()
for stat in json_data["stats"]:
    print(stat["base_stat"])

#16. Extract and print stats that are above a certain threshold (e.g., base stat > 50).
response = requests.get("https://pokeapi.co/api/v2/pokemon/exeggutor")
json_data = response.json()
for stat in json_data["stats"]:
    if (stat["base_stat"]) >50:
        print(stat["stat"]["name"])

#17. Count the Number of Moves
response = requests.get("https://pokeapi.co/api/v2/pokemon/exeggutor")
json_data = response.json()
print("number of moves: ", len(json_data["moves"]))

#18. Extract and Print Move Names
response = requests.get("https://pokeapi.co/api/v2/pokemon/exeggutor")
json_data = response.json()
for move in json_data["moves"]:
    print(move["move"]["name"])