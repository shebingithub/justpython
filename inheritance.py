# INIT METHOD

# class bank:
#    def __init__(self,a,b,c):
#       self.accountholder=a
#       self.ifsccode=b
#       self.tablenumber=c
#       while True:
#        self.tablenumber=int(input("ENTER YOUR CHOOSING TABLE NUMBER FOR YOUR DINNER "))
#        if self.tablenumber==10 or self.tablenumber==5 or self.tablenumber==3:
#           print("SUCCESSFULLY BOOKED YOUR TABLE SLOT FOR DINNER ")
#           break
#        else :
#           print("THIS SLOT IS NOT AVAILABLE")
#       print(self.ifsccode,self.accountholder)

#    def customer_order(self):
       
#       d=int(input("Enter your amount to withdraw :"))
#       print("Amount to withdraw :",d)

#       print("table number",self.tablenumber)
# obj=bank(78891,"shebi",'self.tablename')
# obj.customer_order()


# # initexample 

# class car: # parent class
#     def _init_(self,fname):
#         self.firstname=fname

#     def body(self):
#         print(self.firstname)

# class childcar(car):  # child class
#     def user(self):
#         print(self.firstname,"hello")


# x=childcar("jithu")
# x.body()
# x.user()

# task

# class yesudas():
#    def __init__(self,name):
#       self.singer=name
#    def legend(self):
#       print(self.singer)

# class vijay_yesudas(yesudas):
#    def jrsinger(self):
#      print( "son of ",self.singer)

# obj=vijay_yesudas("gana gandhervan")
# obj.legend()
# obj.jrsinger()

# # super init

# class Yesudas:
#    def __init__(self, name, add):
#       self.singer = name
#       self.super = add
   
#    def legend(self):
      
#       print(self.singer,self.super,self.family)


# class VijayYesudas(Yesudas):
   
#    def __init__(self, name, add, dis):
#       super().__init__(name, add)
#       self.family=dis


# obj = VijayYesudas("Gana Gandhervan","sarigama","my")
# obj.legend()

# Redoing super init

# class Yesudas:
#    def __init__(self, name, add):
#       self.singer = name
#       self.super = add
   
#    def legend(self):
#       self.singer=int(input("enter first number "))
#       self.super=int(input("enter second number "))
#       self.family=int(input("enter third number "))
#       print(self.singer+self.super+self.family)


# class VijayYesudas(Yesudas):
   
#    def __init__(self, name, add, dis):
#       super().__init__(name, add)
#       self.family=dis
#     #   self.singer = name
#     #   self.super = add


# obj = VijayYesudas(4,5,5)
# obj.legend()


# Redoing super init

# class Yesudas:
# #    def __init__(self, name, add):
# #       self.singer = name
# #       self.super = add
   
# #    def legend(self):

# #       print(self.singer+self.super+self.family)

#   def __init__(self,a,b,c):
#       self.accountholder=a
#       self.ifsccode=b
#       self.tablenumber=c
#       while True:
#        self.tablenumber=int(input("ENTER YOUR CHOOSING TABLE NUMBER FOR YOUR DINNER "))
#        if self.tablenumber==10 or self.tablenumber==5 or self.tablenumber==3:
#           print("SUCCESSFULLY BOOKED YOUR TABLE SLOT FOR DINNER ")
#           break
#        else :
#           print("THIS SLOT IS NOT AVAILABLE")


# class VijayYesudas(Yesudas):
   
#    def __init__(self, a, b,self.tablenumber):
#       super().__init__(a, b)
# while True:
#        self.tablenumber=int(input("ENTER YOUR CHOOSING TABLE NUMBER FOR YOUR DINNER "))
#        if self.tablenumber==10 or self.tablenumber==5 or self.tablenumber==3:
#           print("SUCCESSFULLY BOOKED YOUR TABLE SLOT FOR DINNER ")
#           break
#        else :
#           print("THIS SLOT IS NOT AVAILABLE")
    
#    print("table number",self.tablenumber)
#     #   self.singer = name
#     #   self.super = add


# obj = VijayYesudas(4,5,5)
# # obj.legend()









# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print("Animal speaks.")


# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def speak(self):
#         print("Woof!")


# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def speak(self):
#         print("Meow!")


# # Create instances of the classes
# animal = Animal("Generic Animal")
# dog = Dog("Buddy")
# cat = Cat("Fluffy")

# # Call the speak() method
# animal.speak()  # Output: Animal speaks.
# dog.speak()     # Output: Woof!
# cat.speak()     # Output: Meow!




# # Method overloading

# class Yesudas:
#    def __init__(self, a, b,c):
#       self.ab= a
#       self.bc = b
#       self.family=c
      

#    def sum(a,b):
#        print("sum",a+b)
#    def sum(a,b,c):
#     print("sum",a+b+c)
   
   
#     print(self.ab+self.bc+self.c)


# # class VijayYesudas(Yesudas):
   
# #    def __init__(self, a, b, c):
# #       super().__init__(a, b)
# #       self.family=c
#     #   self.singer = name
#     #   self.super = add


# obj = Yesudas(4,5,5)
# obj.sum()

# def sum(a,b):
#     print("sum",a+b)
# def sum(a,b,c):
#     print("sum",a+b+c)

# sum(5,4,4)
# First product method.
# Takes two argument and print their
# product


# def product(type,*args):
# 	p = a * b
# 	print(p)

# # Second product method
# # Takes three argument and print their
# # product



# # Uncommenting the below line shows an error
# # product(4, 5)


# # This line will call the second product method
# product(4, 5)


# # Function to take multiple arguments/ need or not
# def add(datatype, *args):

# 	# if datatype is int
# 	# initialize answer as 0
# 	if datatype == 'int':
# 	    answer = 0

# 	# if datatype is str
# 	# initialize answer as ''
# 	if datatype == 'str':
# 		answer = ''

# 	# Traverse through the arguments
# for  in args: 

# 		# This will do addition if the
# 		# arguments are int. Or concatenation
# 		# if the arguments are str
# 		answer = answer + x

# print(answer)
# # Integer
# add('int', 5, 6,2,546566)

# # String
# add('str', 'Hi ', 'Geeks')


# import multipledispatch/ NEED OR NOT 