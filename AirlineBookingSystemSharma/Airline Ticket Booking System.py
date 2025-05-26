'''
Assignment: Airline Ticket

Name: Avi Sharma

File Created on February 28, 2025
'''

def has_more_economy_seat(seats):
    """
    Check if there are any available seats in the economy section (seats 6-10).
    """
    for i in range(5, 10):  # Economy seats range from index 5 to 9
        if seats[i] == False:
            return True
    return False

def has_more_first_class_seat(seats):
    """
    Check if there are any available seats in the first-class section (seats 1-5).
    """
    for i in range(0, 5):  # First-class seats range from index 0 to 4
        if seats[i] == False:
            return True
    return False

def assign_economy_seat(seats):
    """
    Assign the first available economy seat.
    """
    for i in range(5, 10):
        if seats[i] == False:
            seats[i] = True
            return i + 1  # Seat numbers are 1-based
    return -1  # No seats available

def assign_first_class_seat(seats):
    """
    Assign the first available first-class seat.
    """
    for i in range(0, 5):
        if seats[i] == False:
            seats[i] = True
            return i + 1
    return -1

def print_boarding_pass(seat_number):
    """
    Print a boarding pass with seat information.
    """
    if 1 <= seat_number <= 5:
        print("Seat Number:", seat_number, "- First-class section")
    elif 6 <= seat_number <= 10:
        print("Seat Number:", seat_number, "- Economy section")

def main():
    # Initialize seating chart (10 seats, all unoccupied)
    seats = [False] * 10
    
    while True:
        # Check if plane is completely full
        if not has_more_first_class_seat(seats) and not has_more_economy_seat(seats):
            print("This flight is fully booked.")
            print("Next flight leaves in 3 hours.")
            break
        
        # Display menu
        print("Please type 1 for First Class and 2 for Economy:", end=" ")
        choice = input().strip()

        if choice == "1":  # First Class
            if has_more_first_class_seat(seats):
                seat_number = assign_first_class_seat(seats)
                print_boarding_pass(seat_number)
            else:
                print("First-class seats are fully booked. Would you like an economy seat instead? (Y/N):", end=" ")
                response = input().strip().upper()
                
                if response == "Y":
                    if has_more_economy_seat(seats):
                        seat_number = assign_economy_seat(seats)
                        print_boarding_pass(seat_number)
                    else:
                        print("This flight is fully booked.")
                        print("Next flight leaves in 3 hours.")
                else:
                    print("Next flight leaves in 3 hours.")

        elif choice == "2":  # Economy
            if has_more_economy_seat(seats):
                seat_number = assign_economy_seat(seats)
                print_boarding_pass(seat_number)
            else:
                print("Economy seats are fully booked. Would you like a first-class seat instead? (Y/N):", end=" ")
                response = input().strip().upper()
                
                if response == "Y":
                    if has_more_first_class_seat(seats):
                        seat_number = assign_first_class_seat(seats)
                        print_boarding_pass(seat_number)
                    else:
                        print("This flight is fully booked.")
                        print("Next flight leaves in 3 hours.")
                else:
                    print("Next flight leaves in 3 hours.")

        else:
            print("Invalid input. Please enter 1 for First Class or 2 for Economy.")

if __name__ == "__main__":
    main()
