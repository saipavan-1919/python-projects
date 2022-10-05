#ATM functionality\
import csv
from employee import *

def money_withdraw(emp):
    cash = int(input("enter amount = "))
    for i in range(0, 3):
        pin = input("plaease enter you pin = ")
        if pin == emp["PIN"]:
            if cash > int(emp["BALANCE"]):
                print("sorry, insufficient funds")
                break
            emp["BALANCE"] = str(int(emp["BALANCE"]) - cash)
            print("please wait while we are processing your request")
            print("please collect your cash")
            print("your current balance = ", emp["BALANCE"])
            re_opt = input("do you want to continue[y/n]")
            if re_opt == 'n':
                break
        else:
            if i == 2:
                print("sorry, exceeded retry limit, try again")
            else:
                print(f"Incorrect pin, please enter a valid pin.You have 3 tries.{i+1}/3")

                
def atm_transaction():
    global my_money
    print("choose your choice\n1)balance\n2)withdraw\n3)quit")
    opt=int(input("choice="))
    emp = employee_data()
    if emp=={}:
        print("sorry no user exist with your name please visit again")
        return 0
    if opt==1:
        print("your balance =",emp["BALANCE"])
    elif opt==2:
        money_withdraw(emp)
    elif opt==3:
        print("thanks for banking with us \n***visit us again***")


atm_transaction()
