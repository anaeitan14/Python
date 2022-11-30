person = {"first_name":"Mariah", "last_name":"Carey", "birth_date":"27.03.1970",
          "hobbies":["Sing", "Compose", "Act"]}

print(person["last_name"])
print(person["birth_date"][3:5])
print(len(person["hobbies"]))
print(person["hobbies"][-1])
person["hobbies"].append("Cooking")
print(person["hobbies"])
birthday = person["birth_date"].split(".")
birthday_tuple = birthday[0],birthday[1],birthday[2]
person["birth_date"] = birthday_tuple
print(type(person["birth_date"]))
print(person)
person["age"]="52"
print(person["age"])
