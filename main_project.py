
import json
import getpass
from logging import exception

class Store:

    def __init__(self, name):
        self.store_name = name
        self.food = {}
        self.food_id = 0
        self.user_details = {}
        self.user_id = 0
        self.ordered_item=[]

# admin functionality
#ADDING ITEMS
    def add_food_items(self):
        try:
            name = input("Enter the food name :")
            quantity = float(input("Enter the quantity in kg : "))
            price = float(input("Enter the price per kg : "))
            discount = float(input("Enter the discount in Rs only : "))
            stock =  float(input("Enter the available stock : "))
            food_item = {"Name": name, "Quantity":quantity, "Price":price,"Discount": discount,"Stock":stock}
            self.food_id = len(self.food) + 1
            self.food[self.food_id] = food_item
            print("\n-----Item is successfully added-----")
            json_obj = json.dumps(self.food, indent = 5)
            with open("python_project/food.json", "w") as f:
                f.write(f'\n{json_obj}')
            self.food
        except Exception:
            print("\n!! Something went wrong please try again !!(2)\n")
        
        

#EDITING ITEMS
    def edit_food_item(self):
        try:

            id = int(input("Enter the food id: "))
            print("\n1. Edit food name\n2. Edit Quantity \n3. Edit Price \n4. Edit Discount \n5. Edit Stock \n")
            y= input("Enter what want to do :")
            if id in self.food.keys():
                if y=="1":
                    self.food[id]["Name"] = input("Updated food name will be: ")
                    print("---Name updated successfully---")
                elif y=="2":
                    self.food[id]["Quantity"] = input("Updated quantity name will be: ")
                    print("---Quantity updated successfully---")
                elif y=="3":
                    self.food[id]["Price"] = input("Updated price name will be: ")
                    print("---Price updated successfully---")
                elif y=="4":
                    self.food[id]["Discount"] = input("Updated discount name will be: ")
                    print("---Discount updated successfully---")
                elif y=="5":
                    self.food[id]["Stock"] = input("Updated stock name will be: ")
                    print("---Stock updated successfully---")
            else:
                print("Sorry invalid keys, try again(3)")
            json_obj = json.dumps(self.food, indent = 5)
            with open("python_project/food.json", "w") as f:
                f.write(f'\n{json_obj}')
            self.food
        except exception:
            print("\n!! Something went wrong please try again !!(3)\n")



#VIEWING ITEMS
    def view_food_items(self):
        try:
            if len(self.food)!=0:
                for i in self.food:
                    print(f"Food Id {i}")
                    for j in self.food[i]:
                        print(j,":", self.food[i][j])
                    print(" \n ")
                    json_obj = json.load(self.food, indent = 5)
                    with open("python_project/food.json", "r") as f:
                        f.write(f'\n{json_obj}')
                        self.food
            else:
                print("\n --- THERE ARE NO FOOD TO DISPLAY, PLEASE ADD FOOD ---(4)\n")
            
        except exception:
            print("\n!! Something went wrong please try again !!(4)\n")
            



#REMOVING ITEMS
    def delete_food_items(self):
        try:
            print("\n -----WARNING----- \n---FOOD ITEMS WILL BE DELETED PERMANENTLY---")
            id =input("Enter the Food ID you wish to delete: ")
            file = open("python_project/food.json", 'r')
            content = json.load(file)
            if content[id]== self.food_id:
                del self.food[id]
                json_obj = json.dumps(self.food)
                with open("python_project/food.json", "w") as f:
                    f.write(f'\n{json_obj}')
                self.food
                
            
                print("\n!! Food item deleted successfully !!\n")
                print("Updated Food List\n", self.food)
            else:
                print("\n ----- Incorrect Food ID-----\n ")

        except Exception as e:
            print("\n!! Something went wrong please try again !!(5)\n")


#---------------------------------------------USER FUNCTIONALITY------------------------------------------------------
#USER REGISTRATION
    def user_register(self):
        try:

            user_name = input("Enter your full name : ")
            phone_no = int(input("Enter your 10 digit phone number : "))
            email = input("Enter your email id : ")
            password = input("Enter your password : ")
            address = input("Enter your address : ")
            user_details = {"User Name": user_name, "Phone No.": phone_no, "Email_ID": email,"Password": password, "Address": address}
            self.user_id = len(self.user_details) + 1
            self.user_details[self.user_id] = user_details
            for i in self.user_details:
                print(i, ":", self.user_details[i])
                print("***Registration Successfull***")
                break
            json_obj = json.dumps(self.user_details, indent = 5)
            with open("python_project/user.json", "w") as f:
                f.write(f'\n{json_obj}')
            self.user_details
        except exception:
            print("-----Something went wrong-----(5)")



#USER LOGIN :-
    def user_login(self):
        try:
            while True:
                print("\n---Welcome to Restro---\n")
                print("--Please provide Email-Id and Password for enjoying benefits of Restro--")
                user_id = input("Enter your user_Id: ")
                email = input("Enter your Email Id: ")
                password = input("Enter your Password: ")
                file = open("python_project/user.json", 'r')
                content = json.load(file)
                if content[user_id]['Email_ID'] == email and content[user_id]['Password'] == password:
                    print("\n!! Login successfully !! \n")
                    print(f"Welcome {content[user_id] ['User Name']} ")
                    while True:
                        print("1. Place New Order\n2. Check  Your Order History\n3. Update Your Profile Details\n4. Exit")
                        z = input("Enter Key Accordingly: ")
                        if z == '1':
                            self.place_order()
                        elif z == '2':
                            self.order_history()
                        elif z == '3':
                            self.update_profile()
                        elif z == '4':
                            break
                        else:
                                print("\nplease check your input again\n")
                else:
                    print("\n Please check username and password\n")
                break
        except Exception as e:
            print("\n!! Something went wrong please try again !!(6)")
        


#PLACING ORDER
    def place_order(self):
        try:
            if len(self.food) != 0:
                menu = []
                for items in self.food:
                    menu.append([self.food[items]["Name"], self.food[items]["Quantity"], self.food[items]["Price"]])
                for i in menu:
                    print(i)
                while True:
                    print("\nEnter 1 to Place the Order\nEnter 2 to Exit ")
                    x = input()
                    if x == "1":
                        print("Enter the Food ID to Order your Food : ")
                        y = input().split(",")
                        for i in y:
                            z = int(i)
                            if z <= len(menu):
                                self.ordered_item.append(menu[z - 1])
                            else:
                                print("We Don't have this Food Item : ", z)
                        print("List of food item you selected : \n")
                        for j in self.ordered_item:
                            print(j)
                    elif x == "2":
                        break
                    else:
                        print("!! Invalid Number !!\n")
            else:
                print("\n!! Sorry! No Food Items are available Now !!\n")

        except Exception as e:
            print("\n!! Something went wrong try again !!")



#ORDER HISTORY
    def order_history(self):
        print("\nList of Previous ordered : ")
        for i in self.ordered_item:
            print(i)



#UPDATING USER DETAILS
    def update_profile(self):
        try:
            while True:
                print("Select Below Options to Update Your Profile Details\n")
                print("1. Name\n2. Phone number\n3. Email ID\n4. Password\n5. Address\n6. Exit\n")
                x = input()
                if x == "1":
                    self.user_details["User Name"] = input("Enter your updated full name : ")
                    print("\n!! Detail Updated Successfully !!\n")
                elif x == "2":
                    self.user_details["Phone No."] = int(input("Enter your updated 10 digit phone number : "))
                    print("\n!! Detail Updated Successfully !!\n")
                elif x == "3":
                    self.user_details["Email_ID"] = input("Enter your updated email id : ")
                    print("\n!! Detail Updated Successfully !!")

                elif x == "4":
                    self.user_details["Password"] = input("Enter your updated password : ")
                    print("\n!! Detail Updated Successfully !!\n")

                elif x == "5":
                    self.user_details["Address"] = input("Enter your updated address with area PIN code ")
                    print("\n!! Detail Updated Successfully !!\n")

                elif x == "6":
                    break
                else:
                    print("\n!! Invalid Number Entered !!\n")

                if x in ["1", "2", "3", '4', "5"]:
                    for i in self.user_details:
                        print(i, ":", self.user_details[i])
                else:
                    print("\nPlease Enter correct Input\n")
        except Exception as e:
            print("\n!! Something went wrong please try again !!\n ") 



#MAIN FUNCTION
def main():
    try:
        obj = Store("Restro")
        print("*****Welcome to the Restro***** ")
        while True:
            print("1. Admin \n2. User \n3. Exit")
            key = input("Enter :")
            if key =='1':
                fp = open("python_project/admin.json", "r")
                content = json.load(fp)
                username = input("Enter Admin's Username: ")
                password = getpass.getpass("Enter Admin's Password: ")
                if content["name"]==username and content["password"]==password:
                    print("\n ----Welcome Admin---- \n")
                    while True:
                        print("\n1. Add New item \n2. Edit Item\n3.View food\n4. Remove items \n5.Exit ")
                        key_a = input("\nEnter :")
                        if key_a == '1':
                            obj.add_food_items()
                        elif key_a == '2':
                            obj.edit_food_item()
                        elif key_a == '3':
                            obj.view_food_items()
                        elif key_a == '4':
                            obj.delete_food_items()
                        elif key_a == '5':
                            break
                else:
                    print("\n -----please check username and password----- \n")
            elif key == '2':
                while True:
                    print("\n-----WELCOME-----\n")
                    print("1. Register\n2. Login\n3. Exit\n")
                    y = input("Enter key acordingly: ")
                    if y == '1':
                        obj.user_register()
                    elif y =='2':
                        obj.user_login()
                    elif y == '3':
                        break
                    else:
                        print("\n Check the input again")
            elif key == '3':
                print("\n-----Have a nice day, Please visit soon-----")
                break
    except Exception:
        print("\n-----Something went wrong please try again-----(1)\n")

if __name__ == '__main__':
    main()