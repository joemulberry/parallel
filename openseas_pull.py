import requests
import json

call_offsets = ['0', '50', '100', '150', '200', '250', '300]
dicts = []

for call_offset in call_offsets:
  url = "https://api.opensea.io/api/v1/assets"
  querystring = {"asset_contract_address": "0x76be3b62873462d2142405439777e971754e8e77",
                 "order_direction": "asc", "offset": call_offset, "limit": "50"}
  response = requests.request("GET", url, params=querystring)
  responses = response.json()
  dicts += responses['assets']

with open('data/opensea_parallel_dumps.json', 'w') as fout:
    json.dump(dicts, fout)
