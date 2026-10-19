empolyees={
1:{"name":"omkar", "salary":[500]},
2:{"name":"mahi","salary":[400]},
3:{"name":"ajay","salary":[300]},
4:{"name":"anil","salary":[200]}
}
for empid,details in empolyees.items():
    avg=sum(details["salary"])/len(details["salary"])
    details["average"]=avg
    details["promation"]= avg>=250

print("are you eligble for promation:")
for empid,details in empolyees.items():
    if details["promation"]:
        print(details["name"])
