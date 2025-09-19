#Serra Tak
#8: Strings


def main():
    #Get file name and ident. open file function
    filename = input("Enter the input file name: ")
    file = open_file(filename)

    #read all the lines from file and close after that
    lines = file.readlines()
    file.close()

    #init totals
    tot_sold = len(lines)
    pizza_tot = 0
    burger_tot =0
    subtot = 0.0

    #Process the line in the file
    for line in lines:
        item_name = line[:16].strip() # addres item characters
        revenue_str = line[16:].strip() #addres rev string 
        revenue = float(revenue_str) #convert the value(rev) to a float

        #count pizzas and burgers(caseInsen)
        if "pizza" in item_name.lower():
            pizza_tot += 1
        if "burger" in item_name.lower():
            burger_tot += 1

   #calculations
        subtot += revenue

    tax = subtot * 0.06
    grand_tot = subtot + tax

    lines.sort()#sort lines alphabetically

    
    #output report
    print("\nOutput Report:")
    print("--------------\n")
    print(f"The total number of items sold is: {tot_sold}")
    print(f"Total number of items with pizza is: {pizza_tot}")
    print(f"Total number of items with burger is: {burger_tot}\n")

    print("Food Item        Amount Sold")
    print("---------        -----------")


    #print each item with its revenue
    for line in lines:
        item_name = line[:16].strip()
        revenue = float(line[16:].strip())
        print(f"{item_name:<16} ${revenue:>5.2f}")

    #print, display financial summary
    print(f"\nThe sub total sold is: ${subtot:.2f}")
    print(f"The total tax is: ${tax:.2f}")
    print(f"\nThe grand total collected for the night is: ${grand_tot:.2f}\n")
    print("Program complete!")
            
#correct file condition function
def open_file(filename):
    while True:
        try:
            file = open(filename, "r")
            return file
        except FileNotFoundError:
            print(f'\nERROR -- There is an issue with file {filename}. Please reenter:')
            filename = input("\nEnter the input file name: ")


main() #run the program