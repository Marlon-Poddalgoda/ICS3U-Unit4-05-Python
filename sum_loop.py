#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This program calculates the sum of all positive integers
#       entered by a user using a loop


def main():
    # This function calculates the sum of all positive integers
    #       entered by a user using a loop

    print("This program calculates the sum of all positive integers"
          " entered by a user.")

    # loop counter variable
    total = 0

    # input
    how_many_num = input("Enter how many numbers you want to add up: ")
    print("")

    # process
    try:
        how_many_int = int(how_many_num)

        if how_many_int > 0:
            while how_many_int > 0:
                user_add = input("Enter a number to add: ")
                try:
                    # making sure numbers are entered as integers
                    user_add_int = int(user_add)

                    how_many_int = how_many_int - 1
                    # If statement to ignore negative numbers
                    if user_add_int < 0:
                        print("Negative numbers will not be added.")
                        continue
                    else:
                        total = total + user_add_int
                except Exception:
                    # output
                    print("That's not a number! Try again.")

            print("")
            print("The sum of all positive numbers is {}.".format(total))
        else:
            # output
            print("{} is not a positive integer!"
                  .format(how_many_int))
    except Exception:
        # output
        print("That's not a number! Try again.")
    finally:
        print("")
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
