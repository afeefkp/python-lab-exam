import csv 
dict_value = [
{"name":"Afeef","Malayalam":90,"English":90,"Urdu":90,"Maths":100},
{"name":"Athul","Malayalam":96,"English":99,"Urdu":90,"Maths":100},
{"name":"Sahad","Malayalam":76,"English":98,"Urdu":90,"Maths":100},
{"name":"Arjun","Malayalam":80,"English":98,"Urdu":90,"Maths":100},
{"name":"Nourin","Malayalam":86,"English":89,"Urdu":90,"Maths":100},
{"name":"Nida","Malayalam":45,"English":82,"Urdu":90,"Maths":100},
{"name":"Santhosh","Malayalam":90,"English":75,"Urdu":90,"Maths":100},
{"name":"Komalan","Malayalam":87,"English":88,"Urdu":90,"Maths":100},
{"name":"Janaki","Malayalam":93,"English":77,"Urdu":90,"Maths":100},
{"name":"Vasu","Malayalam":92,"English":66,"Urdu":90,"Maths":100},]

fields = ["name","Malayalam","English","Urdu","Maths"]

with open('Student_details.csv','w') as c:
    writer = csv.DictWriter(c,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    c.close()
Malayalam=0
English=0
Urdu=0
Maths=0
with open('Student_details.csv','r') as cfiles:
     reader = csv.DictReader(cfiles)
     for row in reader:
         print(row['name'],":",(int(int(row["Malayalam"])+int(row["English"])+int(row["Urdu"])+int(row["Maths"]))/400)*100)
         Malayalam=Malayalam+int(row["Malayalam"])
         English=English+int(row["English"])
         Maths=Maths+int(row["Maths"])
         Urdu=Urdu+int(row["Urdu"])
print("\n\nAverage of subjcts")
print("Malayalam",Malayalam/10)
print("English",English/10)
print("Urdu",Urdu/10)
print("Maths",Maths/10)
