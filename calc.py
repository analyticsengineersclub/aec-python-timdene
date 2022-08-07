import argparse

parser = argparse.ArgumentParser(description = "A simple CLI calc")

# Sub commands
subparsers = parser.add_subparsers(help = "sub-command help", dest = "command")

add = subparsers.add_parser("add", help = "add two integers")
add.add_argument("ints_to_sum", nargs = '+', type=int)

add = subparsers.add_parser("subtract", help = "subtract two integers")
add.add_argument("ints_to_subtract", nargs = '+', type=int)

add = subparsers.add_parser("multiply", help = "multiply two integers")
add.add_argument("ints_to_multiply", nargs = '+', type=int)

add = subparsers.add_parser("divide", help = "divide two integers")
add.add_argument("ints_to_divide", nargs = '+', type=int)


args = parser.parse_args()

if args.command == "add":
    our_sum = sum(args.ints_to_sum)

    print(f"the sum of values is: {our_sum}")

if args.command == "subtract":
    first_number = args.ints_to_subtract[0]
    args.ints_to_subtract.pop(0)
    for integer in args.ints_to_subtract:
       first_number -= integer
       our_difference = first_number

    print(f"the difference of values is: {our_difference}")

if args.command == "multiply":
    first_number = args.ints_to_multiply[0]
    args.ints_to_multiply.pop(0)
    for integer in args.ints_to_multiply:
       first_number *= integer
       our_product = first_number

    print(f"the product of values is: {our_product}")

if args.command == "divide":
    first_number = args.ints_to_divide[0]
    args.ints_to_divide.pop(0)

    if 0 in args.ints_to_divide:
        print("Cannot divide by zero")
    else:
        for integer in args.ints_to_divide:
            first_number /= integer
            our_quotient = first_number

    print(f"the quotient of values is: {our_quotient}")