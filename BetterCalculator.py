#calculator

class EquationSymbols():
    #Addition
    def add(n1,n2):
        return n1 + n2
    #Subtraction
    def sub(n1,n2):
        return n1 - n2
    #multiplication
    def mlt(n1,n2):
        return n1 * n2
    #division
    def div(n1,n2):
        return n1 / n2
    
    while True:
        #user input
        symbol = input("Enter choice (1, 2, 3, 4): ")

        #validiation check
        if symbol in ('1', '2', '3', '4'):
            try:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter one of the following numbers: (1, 2, 3, 4)")
                continue

            if symbol == '1':
                print(n1, "+", n2, "=", 
                    add(n1, n2))

            elif symbol == '2':
                print(n1, "-", n2, "=", 
                    sub(n1, n2))

            elif symbol == '3':
                print(n1, "*", n2, "=", 
                    mlt(n1, n2))

            elif symbol == '4':
                print(n1, "/", n2, "=", 
                    div(n1, n2))
            
            #asking to see if user whats to continue using
            newcalc = input("Would you like to do another calculation? (yes/no): ")
            if newcalc == "no":
            print()
            print()
            print()
            print()
            print()
            print("Thank you for using the samulator!")
            print()
            print()
            print()
            print()
            break
        else:
            print("Invalid Input")