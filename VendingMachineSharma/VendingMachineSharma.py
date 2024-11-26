def format_change(cents):
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    pennies = cents % 5
    
    print("Your change is:")
    print(f"{quarters} Quarters")
    print(f"{dimes} Dimes")
    print(f"{nickels} Nickels")
    print(f"{pennies} Pennies")

def vending_machine():
    print("*" * 40)
    print("Welcome to Vending Machine Bravo!")
    print("*" * 40)
    
    print("If you would like to make a selection,")
    print("please insert the appropriate currency into the machine.")
    
    print("\nPlease enter:")
    print("1.00 for $1 bills")
    print("5.00 for $5 bills")
    print(".01 for pennies")
    print(".05 for nickels")
    print(".10 for dimes")
    print(".25 for quarters")
    print("0 to cancel")
    
    total = 0
    while True:
        print("\n* At any point if you wish to cancel operation or go back to last menu,")
        print("please enter 0. Thank you!:")
        
        try:
            amount = float(input())
            if amount == 0:
                return
            
            valid_amounts = [0.01, 0.05, 0.10, 0.25, 1.00, 5.00]
            if amount in valid_amounts:
                total += amount
                print("\n" + "*" * 10 + f" Total money in machine is: {total:.2f} " + "*" * 10)
            else:
                print("Invalid amount. Please try again.")
                continue
                
            print("\nIf you would like to purchase:")
            print("Product A type '1', (Price = $1.00)")
            print("Product B type '2', (Price = $1.25)")
            print("Product C type '3', (Price = $1.50)")
            print("Product D type '4', (Price = $1.75)")
            print("Product E type '5', (Price = $2.00)")
            
            print("\nYour enter is:")
            choice = int(input())
            
            prices = {1: 1.00, 2: 1.25, 3: 1.50, 4: 1.75, 5: 2.00}
            if choice in prices:
                price = prices[choice]
                print("\n" + "*" * 10 + f" The item costs ${price:.2f} " + "*" * 10)
                
                if total >= price:
                    remaining = total - price
                    print("\n" + "*" * 10 + f" You have ${remaining:.2f} left in the machine " + "*" * 10)
                    
                    # Convert remaining amount to cents for change calculation
                    cents = int(remaining * 100)
                    format_change(cents)
                    return
                else:
                    print("Insufficient funds. Please add more money.")
            else:
                print("Invalid selection. Please try again.")
                
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    vending_machine()