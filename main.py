#Name: Aryan Karthik
#Use JSON package to read file
import json

#Open JSON file and read to json
with open("file.json") as f:
  json = json.load(f)

#Define dictionary to store values
dict1 = {
  "INC NUMBER": "",
  "OCCURED ON": "",
  "OCCURRED TO": "",
  "UCR CRIME CATEGORY": "",
  "100 BLOCK ADDR": "",
  "ZIP": "",
  "PREMISE TYPE": "",
}

#Initiate lists to temporarily store values
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []

#Define increment variable to insert values
i = 0

#Loop through json and assign each value to temp lists
while i < len(json["records"]):
  list1.insert(i, json["records"][i][0])
  list2.insert(i, json["records"][i][1])
  list3.insert(i, json["records"][i][2])
  list4.insert(i, json["records"][i][3])
  list5.insert(i, json["records"][i][4])
  list6.insert(i, json["records"][i][5])
  list7.insert(i, json["records"][i][6])
  i += 1
  

#Assign lists to dictionary
dict1["INC NUMBER"] = list1
dict1["OCCURED ON"] = list2
dict1["OCCURRED TO"] = list3
dict1["UCR CRIME CATEGORY"] = list4
dict1["100 BLOCK ADDR"] = list5
dict1["ZIP"] = list6
dict1["PREMISE TYPE"] = list7
