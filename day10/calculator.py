
def user_input(operator,n_1,n_2):

    if operator == "+":
        result_1 = calculator["+"](n_1, n_2)
        return result_1

    elif operator =="-":
        result_1 = calculator["-"](n_1, n_2)
        return result_1

    elif operator =="/":
        result_1 = calculator["/"](n_1, n_2)
        return result_1

    elif operator =="*":
        result_1 = calculator["*"](n_1, n_2)
        return result_1

    else:
        return "none"








def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2


calculator = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

keep_running = True


final_result = 0
while keep_running:

    number_1 = int(input("whats your first number\n"))
    print(
          "+\n"
          "-\n"
          "/\n"
          "*")
    user_operator = input("Choose operator:\n")
    number_2 = int(input("Whats your second number\n"))


    result = (user_input(user_operator,n_1=number_1, n_2=number_2))


    if result == "none":
        print("type valid operator, please try again")

        continue

    final_result = result
    print(final_result)

    user_exit = input("type yes if you want to exit or no\n").lower()


    if user_exit == "yes":
        keep_running = False
        break


    previous_number = input("type Y if you want to continue with previous number ").lower()
    if previous_number == "y":

        keep_running_2 = True

        while keep_running_2:

            number_1 = final_result
            print("+\n-\n/\n*")
            user_operator = input("Choose operator:\n")
            number_2 = int(input("Whats your second number\n"))

            result = user_input(user_operator, number_1, number_2)


            if result == "none":
                print("type valid operator, please try again")
                continue
            final_result = result
            print(final_result)

            user_exit = input("type yes if you want to exit or no\n").lower()
            if user_exit == "yes":
                keep_running = False
                break

            previous_number = input("type Y if you want to continue with previous number ").lower()
            if previous_number != "y":
                keep_running_2 = False








