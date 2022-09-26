#!/usr/bin/env python3

import json

cars_without_images = []

print("\nFinding Cars Missing Images:")
with open("collections.json", "r") as cfh:

  collections = json.load(cfh)

  for i in collections:
    if collections[i]['img_src'] == '':
      cars_without_images.append(str(i)+" "+collections[i]["title"])
      print("  * "+str(i)+" "+collections[i]["title"])

  with open("cars_without_images.json", "w") as cwoih:
    cars_without_images.sort()
    cwoih.write(json.dumps(cars_without_images))
print()