"""
    Continue is a keyword 
    it can only be used in the body of loop 
    continue transfer the control immedeatly to the next iteration .

"""
i=1
x=int(input("\n\t Enter a num : "))
while i<10:
    if x%2==0:
        continue
    print(i,"x=",x)
    i+=1
    