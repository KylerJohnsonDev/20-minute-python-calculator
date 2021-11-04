from utils import get_num_list_from_raw_input

def start_addition_operation():
    print("Enter the numbers you would like to add, spearated by a comma.")
    raw_input = input(">> ")
    num_list = get_num_list_from_raw_input(raw_input)
    sum = add_numbers(num_list)
    print(f"Sum: {sum}")
    input()


def add_numbers(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

def start_subtraction_operation():
    print("Enter the numbers you would like to subtract in order, separated by a comma.")
    raw_input = input(">> ")
    num_list = get_num_list_from_raw_input(raw_input)
    difference = subtract_numbers(num_list)
    print(f"Difference: {difference}")
    input()

def subtract_numbers(numbers):
    difference = None
    for num in numbers:
        if difference is None:
            difference = num
        else:
            difference = difference - num
    return difference

def start_multiplication_operation():
    print("Enter the numbers you would like to multiply, separated by a comma.")
    raw_input = input(">> ")
    num_list = get_num_list_from_raw_input(raw_input)
    product = multiply_numbers(num_list)
    print(f"Product: {product}")
    input()

def multiply_numbers(numbers):
    product = None
    for num in numbers:
        if product is None:
            product = num
        else:
            product = product * num
    return product

def start_division_operation():
    print("Enter the numbers you would like to divide in order, separated by a comma.")
    raw_input = input(">> ")
    num_list = get_num_list_from_raw_input(raw_input)
    quotient = divide_numbers(num_list)
    print(f"Quotient: {quotient}")
    input()

def divide_numbers(numbers):
    quotient = None
    for num in numbers:
        if quotient is None:
            quotient = num
        elif num == 0:
            print("Error: cannot divide by 0.")
            return
        else:
            quotient = quotient / num
    return quotient