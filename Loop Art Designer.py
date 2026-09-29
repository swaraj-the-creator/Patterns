print("===== T Pattern =====")
print("Half Pyramid Pattern of Stars (T):")
n = int(input("Enter the number of rows: "))
for t in range(n):
    for p in range(t+1):
        print("T ",end="")
    print()
print("\n===== Floyd's triangle =====")
rows = int(input("Please enter the total number of rows: "))
number = 1
print("Floyd's Triangle")
for f in range(1,rows + 1):
    for t in range(1,f +1):
        print(number ,end=" ")
        number = number + 1
    print()
print("\n===== Diamond Pattern =====")
print("Looks best when the value is over 30!")
rowSize = int(input("Enter the number of rows: "))
if rowSize % 2 == 0:
    halfDiamondRow = rowSize // 2
else:
    halfDiamondRow = rowSize // 2 + 1
space = halfDiamondRow-1
for i in range(1,halfDiamondRow + 1):
    for j in range(1,space+1):
        print(" ",end=" ")
    space = space - 1
    num = 1
    for j in range(2*i-1):
        print(num,end=" ")
        num = num+1
    print()
space = 1
for i in range (1,halfDiamondRow):
    for j in range(1,space+1):
        print(end=" ")
    space = space+1
    num = 1
    for j in range(1,2*(halfDiamondRow-i)):
        print(num,end=" ")
        num = num+1 
    print()
print("\n Loop Art Design Complete.")
