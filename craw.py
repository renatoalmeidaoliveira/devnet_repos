import requests
import json

request = requests.get('https://devnet.cisco.com/v1/metadata/catalogs/search')
data = request.json()
types = []

for item in data['items']:
	if item['type'] not in types:
		types.append(item['type'])

files = {}
for doc_type in types:
	files[doc_type] = open(f"{doc_type}.txt", "w")


for item in data['items']:
	doc_type = item['type']
	name = item['name']
	desc = item['description']
	url = item['url']
	line = f"name: {name}\ndescription: {desc}\nurl: {url}\n\n"
	file = files[doc_type]
	file.write(line)

for file_type in files:
	file = files[file_type]
	file.close()

