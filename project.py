student=["Mirzan","Anojan","Ravi","Suresh","Ranjan"]
subject=["Maths","Science","English"]
marks=[[95,86,75],[93,87,69],[83,72,56],[72,45,63],[97,87,78]]
total=[]
average=[]
result=[]
for x in range(len(student)):
    tot=ave=0
    for y in range(len(subject)):
        tot = tot+ marks[x][y]
    total.append(tot)
    
    ave=tot/len(subject)
    average.append(ave)
    
    if (ave>=75):
        re = "A"
    elif (ave>=65 and ave<75):
        re=  "B"
    elif (ave>=55 and ave <65):
        re = "C"
    elif (ave>= 35 and ave <55):
        re = "S"
    elif (ave < 35):
        re = "F"
    else :
        print("invalid numbers are not allowed")
    result.append(re)

        

print(f"{'StudentName':<15}{'Maths':<8}{'Science':<10}{'English':<10}{'Total':<8}{'Average':<12}{'Result':<9}")
for x in range(5):
    print(f"{student[x]:<15}",end="")
    for y in range(3):
        print(f"{marks[x][y]:<10}",end="")
    print(f"{total[x]:<8}{average[x]:<10,.2f}{result[x]:<5}")