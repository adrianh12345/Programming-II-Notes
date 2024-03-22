name = input("what is your name? ")
age = input("How old are you? ")
try:
    age = int(age)
    birth_year = 2023 - age
    print(name, ", you were born in ", birth_year, ".", sep="")
    number = input("give me a number to divide the age")
    number = int(number)
    print(age/number)
except ValueError:
    print("Invalid age. Please enter a number")
except ZeroDivisionError:
    print("you cannot divide by zero")
except:
    print("Some other error I did not forsee")
else:
    print("No exceptions were raised")
finally:
    print("thank you for playing")
