import requests
import pandas as pd
import collections
from collections import OrderedDict
orderedDict = collections.OrderedDict()

url = 'https://query.wikidata.org/sparql'
query = """

SELECT ?item ?itemLabel 
WHERE 
{
  ?item wdt:P31 wd:Q5.        #this line targets the property 'instance' then 'human'
   ?item wdt:P140 wd:Q9316.   #this line targets 'religion' then 'Sikhism'
  ?item wdt:P106 wd:Q484260.   #this line targets 'occupation' then 'guru'
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""
r = requests.get(url, params = {'format': 'json', 'query': query})
data = r.json()
print (data)      #see the data only finds two Guru's from the wikidata but we can modify this query 

guru = []
for item in data['results']['bindings']:
    guru.append(OrderedDict({
        label : item[label]['value'] if label in item else None
        for label in ['itemLabel']}))
df = pd.DataFrame(guru)
df.set_index('itemLabel', inplace=True)
df.head()

