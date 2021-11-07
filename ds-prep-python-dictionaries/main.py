person = {"first_name": "James", "last_name": "Nakano", "hobby": "Snowboarding"}
print(person)
first_name = person["first_name"]
last_name = person.get("last_name")
middle_name = person.get("middle_name")
print(first_name, middle_name, last_name)
person["job"] = "Instructor"
print(person["job"])
person["hobby"] = "Chess"
print(person["hobby"])
person.pop("last_name")
print(person)
