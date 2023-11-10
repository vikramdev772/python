# print()
# print simple text    print("Welcome")
# print variable value print(x)
# print expression     print(x+5*3)
# print multiple vlaue print(x,y)

print("\n\t Hello world \n")
print(3+4)
print(5)
a="Welcome"
print(a)
print(a*3)

# Hello world 

# 7
# 5
# Welcome
# WelcomeWelcomeWelcome

x=5
y=4
p=3
print(x,y,p)
# 5 4 3

# Seprator

print(x,y,p,sep="")
print(x,y,p,sep="\t\t")
print(x,y,p,sep="\n")
# 543
# 5		4		3
# 5
# 4
# 3
c=9
print(x,y)
print("Hello")
print(c)
# 5 4
# Hello         next line changing line
# 9



print(x) #9
print(x,y,end='000')
print("inline")  #5 4000inline

# print("\n\t x : ",x+" y : ",y,end=" ")  error
# print("value")

print("\n\t x : "+str(x)+" y : "+str(y),end=" " )
print("values")         # x : 5 y : 4 values

print(f" x : {x}  y : {y} ",end="")
print("This way, you don't need to explicitly convert variables to strings; f-strings handle it automatically.")

