# atm machine 2
n=50000
def choice():
    print("-----------------Sbi Bank-----------------")
    print(1,"Cash Withdraw")
    print(2,"Deposit cash")
    print(3,"Change Pin")
    print(4,"Balance enquiry")
    print(5,"Exit")

def Cash_withdraw():
    cash=int(input("Enter the the amount to withdraw:"))
    print(f"Cash withdrawed:{cash}")
    avilable_balance=(n-cash)
    print(f"Avilable balance: {avilable_balance}")
def Deposit_cash():
    cash=int(input("Enter the amount to deposit: "))
    print(f"Deposited amount:{cash} ")
    avilable_balance=(n+cash)
    print(f"Avilable balance: {avilable_balance}")
def Balance_enquiry():
    print(f"Total Balance in account  is :{n}")
def exit():
    print("---------Exited-------- ")
def Change_pin():
    global pin1
    while True:
        user_pin = input("Enter Your Pin: ")
        if user_pin == pin1:
            while True:
                pin1 = input("Enter New Pin: ")
                pin2 = input("Confirm Pin: ")
                if pin1==pin2:
                    print("Pin Updated Sucessfull")
                    break
                else:
                    print("Password not matching")
            break
        else:
            print("Invalid Pin")
def display_fun():
    while True:
        choice()
        ch=int(input("Enter your choice:"))
        if ch==1:
            Cash_withdraw()
        elif ch==2:
            Deposit_cash()
        elif ch==3:
            Change_pin()
        elif ch==4:
            Balance_enquiry()
        elif ch==5:
            exit()
        else:
            ch==6 or ch==0
            print("-----Invalid choice-----")
            break
        print()
name = input("Enter Name: ")
balance = int(input("Set Balance: "))
while True:
    print()
    pin1 = input("Enter Pin: ")
    pin2 = input("Confirm Pin: ")
    if pin1==pin2:
        print("Pin Set Sucessfull")
        break
    else:
        print("Password not matching")
display_fun()