from operations import start_addition_operation, start_division_operation, start_multiplication_operation, start_subtraction_operation


def main():
    print("Calculator is up and running")
    input("Press \"enter\" to continue")

    should_continue = True

    while should_continue:
        print("Please select from the following options:")
        raw_input = input("1) Add\n2) Subtract\n3) Multiply\n4) Divide\nOr type\"exit\" to close the program >> ")

        if raw_input == "1":
            start_addition_operation()
        elif raw_input == "2":
            start_subtraction_operation()
        elif raw_input == "3":
            start_multiplication_operation()
        elif raw_input == "4":
            start_division_operation()
        elif raw_input == "exit":
            print("Shutting down...")
            should_continue = False
        else:
            input("You did not enter a valid selection. Press \"enter\" to try again.")

# This "def main, if name main" pattern only runs the program if it's being run as a script, not if it's imported
# - This tells a reader of the code that it was intended to be run as a script
if __name__ == "__main__":
    main()
