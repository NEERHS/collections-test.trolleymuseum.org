#!/usr/bin/env python3

##
## Read in the collections json file.
## Create unique indexes for the search form.
##

import json

cities = []
states = []
categories  = []

with open("collections.json", "r") as cfh:

  collections = json.load(cfh)

  for c in collections:
    city = collections[c]['source_city']
    state = collections[c]['source_state']
    category = collections[c]['category']

    if city not in cities and city != "":
      cities.append(city)
    if state not in states and state != "":
      states.append(state)
    if category not in categories and category != "":
      categories.append(category)

  cities.sort()
  states.sort()
  categories.sort()

  with open("cities.json", "w") as fh:
    fh.write(json.dumps(cities))

  with open("states.json", "w") as fh:
    fh.write(json.dumps(states))

  with open("categories.json", "w") as fh:
    fh.write(json.dumps(categories))

