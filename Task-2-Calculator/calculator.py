def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b    

def divide(a,b):
    if b==0:
        return "Error: Division by zero not allowed"
    return a/b

def show_menu():
    print("\n===== Simple Calculator =====")    
    print("\n1.Add(+)")        
    print("2.Subtract(-)")   
    print("3.Multiply(*)")   
    print("4.Divide(/)")
    print("5.View History") 
    print("6.Exit") 

history=[]

operations={
    "1":"+",
    "2":"-",
    "3":"*",
    "4":"/"
}

while True:
    show_menu()
    choice=input("Enter your choice(1-6):")
    if choice=="6":
        print("Exiting Calculator...")
        break
    elif choice=="5":
        print("\n---Calculation History---")
        if not history:
            print("No calculation yet.")
        else:
            for h in history:
                print(h)
        continue                
    elif choice not in ["1","2","3","4"]:
        print("Invalid choice.Please try again.")
        continue
    try:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))  
    except:
        print("Invalid input.Please enter numeric values.")  
        continue
    if choice=="1":
        result=add(num1,num2)  
    elif choice=="2":
        result=subtract(num1,num2) 
    elif choice=="3":
        result=multiply(num1,num2) 
    elif choice=="4":
        result=divide(num1,num2)    

    if isinstance(result,str):
        print(result)
    else:
        output=f"{num1} {operations[choice]} {num2} = {result}"        
        print("\nResult:",output)
        history.append(output)
                        