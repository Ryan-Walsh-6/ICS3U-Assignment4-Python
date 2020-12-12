#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: December 2020
# this program calculates the attendance the user

import constants


def main():
    # this program calculates the attendance the user

    # input
    classes_held = input("Enter the amount of classes held: ")
    print("\n", end="")
    classes_attended = input("Enter the amount of classes attended: ")
    print("\n", end="")

    # output & process
    try:
        classes_held_int = int(classes_held)
        classes_attended_int = int(classes_attended)

        if classes_attended_int >= 0 and classes_held_int > 0:
            attendance = (classes_attended_int / classes_held_int) * 100

            if attendance >= constants.PERCENT_ATTENDANCE:
                print("Your attendance for the year was {:,.2f}% so you"
                      " will be allowed to sit in the exam."
                      " Well done!".format(attendance))

            else:
                print("Your attendance for the year was {:,.2f}% so you will"
                      " not be allowed to sit in the exam."
                      " Good luck next time.".format(attendance))
        else:
            print("Classes Held were less than 1 or classes attended"
                  " was negative. Please try again")
    except Exception:
        print("Invalid entry. An amount of days was not entered."
              " Please try again")


if __name__ == "__main__":
    main()
