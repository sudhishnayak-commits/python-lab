l=[]
n=int(input("Enter the number of students:"))
for i in range(1,n+1):
    name=input("Enter the name of the student:")
    usn=input("Enter the usn:")
    m1=int(input("Enter the mark in CS:"))
    m2=int(input("Enter the mark in physics:"))
    m3=int(input("Enter the mark in maths:"))
    total=m1+m2+m3
    avg=total/3
    l.extend([i,name,usn,m1,m2,m3,total,avg])
print("        student details             ")
print("--------------------------------------")
print("sl.no",'name','usn','cs','physics','maths','total','avg',sep="\t")
print('--------------------------------------------------------------------------')
for i in range(0,len(l),8):
    print(l[i],l[i+1],l[i+2],l[i+3],l[i+4],l[i+5],l[i+6],l[i+7],sep="\t")
    






    