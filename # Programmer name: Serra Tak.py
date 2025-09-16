# Programmer name: Serra Tak
# 03/06/2025
# Lab 5 Part 1: Functions


#variables and constants
plain = 11.50
pepperoni = 13.50
veggie = 12.50
delivery_fee = 5.00
sales_tax = 0.06 

def main():
    cost_total = 0
    order = 0

    #Welcome text/ Opening text
    print('Welcome to the CMSY-156 Pizza Shop')
    #order type input
    order_type=int(input("Enter 1 for delivery or 2 for pickup: "))
    #loop and condition for order type
    while order_type < 1 or order_type > 2:
        error() # caling error function
        order_type= int(input("Enter 1 for delivery or 2 for pickup: "))
    #connected input for order type  
    if order_type == 1:
       delivery_address = input("Please enter your delivery address: ")
    else:
        delivery_address = ""
        
    # creating loop for order type and condition
    while order != 4:
        menu()#calling pizza type display function
        order = int(input('Enter your order here:'))#Get the order detail from user:

        #identify order & initial calculation, and conditions statments 
        if order == 1:
            cost_total +=plain
            show_order('plain pizza') #creat argument for later to display what user ordered
        elif order == 2:
            cost_total += pepperoni
            show_order('pepperoni pizza')#creat argument for later to display what user ordered
        elif order == 3:
            cost_total += veggie
            show_order('veggie pizza')#creat argument for later to display what user ordered
        elif order == 4:
            tip_amount = float(input('Please enter the amount of the tip: $'))# get tip amount from user
            while tip_amount <= 0: #tip amount condition
                error() # caling error function
                tip_amount = float(input('Please enter the amount of the tip: $'))
        else:
            error()# caling error function 

    check_out(cost_total, order_type, delivery_address,tip_amount)# create argument for later and checkout calculation
        
    print('\nThank you for using the CMSY-156 Pizza Shop. Please come again!') #Closing text

#error function
def error():
    print('Error: Please enter a valid value. Please try again! ')
    
# pizza options display function
def menu():
    print('\nWhat would you like to order today?') #inform user about code of pizza type and checkout
    print('\n1. Plain Pizza')
    print('2. Pepperoni Pizza')
    print('3. Veggie Pizza')
    print('4. Checkout')

#argument function and  display what user selected function
def show_order(pizza_kind):
    print(f'\nYou ordered a {pizza_kind}')

#checkout calculation and display function
def check_out(cost_total, order_type, delivery_address,tip_amount):

    tax = cost_total * sales_tax
        
    if order_type == 1:
        final_cost = cost_total + delivery_fee + tip_amount + tax
        print(f'Your total cost with tax, tip and delivery charge is: ${final_cost:.2f}')
        print(f'The pizza will be delivered to: {delivery_address}')
    elif order_type == 2:
        final_cost = cost_total + tip_amount + tax
        print(f'The total cost with tax and tip is: ${final_cost:.2f}')

# Run the program
main()