# pattern

row=int(input("enter the number of rows"))

for z in range(row):
    for x in range(z+1):
        print(x+1,end="")
    
    print("\n")

# A
# BB
# CCC
# DDDD
# EEEEE

# row=int(input("enter the number of rows"))

# A=65

# for i in range(row):
#     for j in range(i+1):
#         alphabet=chr(A)
#         print(alphabet,end="")
#     A=A+1
    
#     print("\n")

# *
# **
# ***
# ****
# *****
# inverted piramid

# *****
# ****
# ***
# **
# *
      
# row=int(input("enter the number of rows"))


# for i in range(row,0,-1):
#     for j in range(i):
#         print("1",end="")
    
#     print("\n")

# normal triangle 

rows = int(input("Enter number of rows: "))

k=0

for i in range(1, rows+1):
    for j in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k=k+1
    k=0
   
    print()

#     # inverted normal triangle 

# rows = int(input("Enter number of rows: "))

# for i in range(rows, 1, -1):
#     for space in range(0, rows-i):
#         print("  ", end="")
#     for j in range(i, 2*i-1):
#         print("* ", end="")
#     for j in range(1, i-1):
#         print("* ", end="")
#     print()


# rows = int(input("Enter number of rows: "))

# k = 0
# count=0
# count1=0

# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print("  ", end="")
#         count+=1
    
#     while k!=((2*i)-1):
#         if count<=rows-1:
#             print(i+k, end=" ")
#             count+=1
#         else:
#             count1+=1
#             print(i+k-(2*count1), end=" ")
#         k += 1
    
#     count1 = count = k = 0
#     print()


# row=int(input("enter the number of row :"))


# for i in range(row,0,-1):
#     for j in range(i):

#         print("=",end=" ")
    
#     print("\n")
      