import json
with open("./columns.json", "r") as readit: 
    x = json.load(readit)
    x=x['data_column'] 




lis=[]
for i in  x:
    lis.append((i,i))
print(lis)