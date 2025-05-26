# Author: Avi Sharma
# Assignment: PA4
# File: social_net.py
# Due Date: 11/27
#
# Program Description: school social network simulation using names and lexicographic distance
# Honor Code: I pledge on my honor that I have neither given nor received unauthorized aid

def main():
    while True:
        try:
            total_people = int(input("What is the total number of friends in the network: "))
            if total_people > 0:
                break
            else:
                print("You need to have at least one friend in the network. Please enter again:")
        except ValueError:
            print("That is an incorrect input! Please enter an integer.")

    names = []
    for i in range(total_people):
        name = input(f"Enter name {i + 1}: ")
        names.append(name)

    array_of_friends = [[0] * total_people for _ in range(total_people)]

    for i in range(total_people):
        for j in range(total_people):
            if i != j and abs(ord(names[i][0]) - ord(names[j][0])) <= 12:
                array_of_friends[i][j] = 1

    # Print the header
    print("\n\t" + "\t".join(names))
    for i in range(total_people):
        row = [str(array_of_friends[i][j]) for j in range(total_people)]
        print(f"{names[i]}\t" + "\t".join(row))

    # Total friends
    print("\nTotal Friends Count:")
    for i in range(total_people):
        total_friends = sum(array_of_friends[i])
        print(f"{names[i]}\t{total_friends}")

if __name__ == "__main__":
    main()
