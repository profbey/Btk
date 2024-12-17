# her platformun anladigi bir veri tipidir.
# dict yapisina benzerdir

########## Dict yapisi ########## 
person = person_str = {
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
rst_str = json.loads(person_str)                                                # {'name': 'Ali', 'languages': ['Python', 'C#']}

rst = rst_str['name']
rst = rst_str['languages']


with open("person.json") as file:
    data = json.loads(file)
    print(data["name"])
    print(data["languages"])





print(rst)
