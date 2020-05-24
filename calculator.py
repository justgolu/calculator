def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b
   
print("\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division")   
while True:
    ch = (input("\nEnter Operation: "))

    if ch in ("1", "2", "3", "4"):

        num1 = float(input("Enter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))

        if(ch == "1"):
            print(num1, "+", num2, "=", add(num1,num2))

        elif(ch == "2"):
            print(num1, "-", num2, "=", substract(num1,num2))

        elif(ch == "3"):
            print(num1, "*", num2, "=", multiply(num1,num2))
    
        elif(ch == "4"):
            print(num1, "/", num2, "=", divide(num1,num2))
        break    
    
    else:
        print("Please provide a valid input !!")



