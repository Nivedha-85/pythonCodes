import json
person={"name":"Nivedha","sem":7,"College":"RNSIT","Placed":False,"Technologies":["MySQL","OS","DS"]}
personJson = json.dumps(person,indent=4)#dumps our object to json string
print(personJson)

with open('person.json','w') as file:
    json.dump(person,file,indent=4)

#from json to python code i.e the dictionary
person1=json.loads(personJson)
print(person1)

with open('person.json','r') as file:
    person1=json.load(file)
print(person1)
