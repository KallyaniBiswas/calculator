print("Welcome to Smart Utility Function Toolkit")


# calculator functions

def add(*a):
    return sum(a)

# print(add(2,3,4,5))

def sub(a,*b):
    return a - sum(b)
# print(sub(8,2,3))

import math
def multi(*a):
    return math.prod(a)
# print(multi(2,3,4,5))

def devi(a,*b):
    import math
    if b == 0:
          return "not defined"
    return a/(math.prod(b))
# print(devi(20,2,5))

# user input

def get_number():
      a = input("enter number(space between two numbers): ").split()
      numbers = list(map(int,a))
      return numbers
# x = (get_number())
# print(x)



# main logic

def calculator():
      while True:

        #  user input menu
        print("Calculator option")
        print("1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n" \
        "5. Exit\n")

        choice = int(input("Enter your choice: "))

            
        if choice == 5:
                print("Exit")
                break
            
        if choice in [1,2,3,4]:
            num = tuple(get_number())
            print("num",num)
                

            if choice == 1:
                        print("Add: ",add(*num))
            elif choice == 2:
                        print("Subtration: ",sub(num[0],*num[1:]))
            elif choice == 3:
                        print("multiplication: ", multi(*num))

            elif choice == 4:
                        print("Divide: ",devi(num[0],*num[1:]))
        else:
                  print("invalid choice")
calculator()
