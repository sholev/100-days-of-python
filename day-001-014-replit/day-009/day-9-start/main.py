dict_empty = {}

dict = {
    "key_1": "value_1",
    "key_2": "value_2",
}

dict["key_3"] = "value_3"
dict[5] = "value_5"

print(dict["key_3"])
print(dict)

for key in dict:
  print(f"{key}: {dict[key]}")

for value in dict.values():
  print(value)

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
  },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
  }
}
print(travel_log["Germany"]["total_visits"])

travel_log_list = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
  }
]
print(travel_log_list[1]["country"])