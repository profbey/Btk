# her platformun anladigi bir veri tipidir.
# dict yapisina benzerdir

########## Dict yapisi ########## 
person =  {
    "name"      :   "Ali",
    "languages" :   ["Python","C#"]
    }



rst = person['name']
rst = person['languages']
rst = person['languages'][0]
rst = person['languages'][1]



########## JSON yapisi ##########
# bu veri yapisi string ifadeler ile calisir.

import json

person_str = '{"name":"Ali", "languages":["Python","C#"]}'                  # string json bilgisi

# JSON to Dict  ->  tek tirnak cift tirnak olayina dikkat et
rst_str = json.loads(person_str)                                            # {'name': 'Ali', 'languages': ['Python', 'C#']}

rst = rst_str['name']
rst = rst_str['languages'] 


with open("person.json") as file:
    data = json.load (file)
    print(data["name"])
    print(data["languages"])


# Dict to JSON

person_string = {"name":"Ali","languages":["Python","C#"]}

result = json.dumps(person_string)

with open('person.json','w') as f:
    json.dump(person_string,f)

person_dict = json.loads(person_string)

result = json.dumps(person_dict,indent=4 ,sort_keys=True  )

print(result)