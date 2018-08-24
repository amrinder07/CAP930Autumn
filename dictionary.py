name={"fname":'Amrinder',"lname":'Singh'}
print(name)
print(name["lname"])
name["age"]=23
print(name["age"])
print(name)
name["qualifications"]=['BCA','MCA']
print(name)
print(name.get("fname"))

del name["age"]  #deletion of a key
print(name)
name.pop("lname")  #remove and return dfault values if not in the map
print(name)
name.popitem()
print(name.keys())
print(name.values())
print(name.items())
print(len(name.items()))
for value in name.values():
    print(value)
