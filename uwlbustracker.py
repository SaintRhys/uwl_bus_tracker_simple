import requests
from bs4 import BeautifulSoup
import re
import json

URL = "http://uwlshuttle.utrack.com/stop-finder/"
r = requests.get(URL).text

soup = BeautifulSoup(r, "lxml")

script = soup.findAll("script")[-1].prettify()
linkName = re.findall(r'"name".*,', script)
id = re.findall(r'"id".*,', script)

for i in range(0, len(linkName)):
    linkName[i] = linkName[i].split('"')[3]
    print(str(i) + ": " + linkName[i])
for i in range(0, len(id)):
    id[i] = id[i].split('"')[3]

bus = input("What bus? ")

#for spam in linkName:
#    print(spam + " : " + id[0])

URL = "http://uwlshuttle.utrack.com/api/eta/stops/" + id[int(bus)] +"?callback"
r = requests.get(URL)

data = r.text[1:-2]
parsed = json.loads(data)
for i in parsed['services']:
    print(i['time']['arrive']['dateTime'])
#print(json.dumps(parsed, indent=4))


