# Hobbies=("reading","writing","cooking","cycling","trucking")
# b=(1,2,3)
# for loop in Hobbies:
#     print(loop)
# print(Hobbies[2])
# c=Hobbies+b
# print(c)
class menu:
    # @staticmethod
    def menu_items(restaurant):
        print("menu card")
        a = {"chicken curry": 180, "fried chicken": 190, "dragon chicken": 250}
        for i, j in a.items():
            print(i, j)

    # @staticmethod
    def table_reservation(restaurant):
        while True:
            c = int(input("ENTER YOUR CHOOSING TABLE NUMBER FOR YOUR DINNER: "))
            if c == 10 or c == 5 or c == 3:
                print("SUCCESSFULLY BOOKED YOUR TABLE SLOT FOR DINNER")
                return c
            else:
                print("THIS SLOT IS NOT AVAILABLE")

    # @staticmethod
    def customer_order(restaurant):
        d = input("Enter your order for the dinner: ")
        print("Your orders for the dinner are:", d)


restaurant_name = "Example Restaurant"
menu_obj = menu()
menu_obj.menu_items(restaurant_name)
table_number = menu_obj.table_reservation(restaurant_name)
menu_obj.customer_order(restaurant_name)

print("Table number chosen:", table_number)
