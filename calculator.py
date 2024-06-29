import os
def add(number1,number2):
    return(number1+number2)
def subtract(number1,number2):
    return(number1-number2)
def product(number1,number2):
    return(number1*number2)
def division(number1,number2):
    return(number1/number2)

operations_dict={
"+": add,
"-": subtract,
"*": product,
"/": division
}
def cal():
    number1=float(input("enter first number:"))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("enter any operation symbol :")
        if op_symbol=='+'or op_symbol=='-'or op_symbol=='*'or op_symbol=='/':
             number2=float(input("enter next number:"))
             fun=operations_dict[op_symbol]
             output=fun(number1,number2)
             print(f"Result = {number1} {op_symbol} {number2} = {output}")

             should_continue=input("enter 'y' for continue further calculation with {output} or n for starting new calculation\n 'o' to exit :")

             if should_continue=='y':
                  number1=output
                  print("first number =",number1)
                  continue_flag=True
             elif should_continue=='n':
                   continue_flag=False
                   os.system('cls')
                   cal()
             else:
                    continue_flag=False
                    print("\nEXIT")

        else:
             print("invalid symbol")
             print("again")
             continue_flag= True

print("-------------CALCULATOR--------------")
cal()

