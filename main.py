#Name: Aryan Karthik
#Use JSON package to read file
import json

#Open JSON file and read to json
with open("file.json") as f:
  json = json.load(f)

#Define dictionary to store values
dict1 = {
  "INC NUMBER": [],
  "OCCURED ON": [],
  "OCCURRED TO": [],
  "UCR CRIME CATEGORY": [],
  "100 BLOCK ADDR": [],
  "ZIP": [],
  "PREMISE TYPE": [],
}


#Loop through json and assign each value to correct dictionary key
for value in json["records"]:
  j = 0
  for key in dict1.keys():
    dict1[key].append(value[j])
    j += 1

  
  
  

