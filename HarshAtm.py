import mysql.connector
import random
mydb=mysql.connector.connect(host='localhost',username='root',password='root',database="AtmMachine")
mycursor=mydb.cursor()
# mycursor.execute("Create Database AtmMachine")
# print("Database created")

create_transaction_history_table_query = """
CREATE TABLE IF NOT EXISTS transaction_history (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    transaction_type VARCHAR(255),
    amount DECIMAL(10, 2),
    transaction_date DATETIME
)
"""
mycursor.execute(create_transaction_history_table_query)

User_table="""CREATE TABLE IF NOT EXISTS user_accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE,
    account_no INT UNIQUE,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    user_pas VARCHAR(255),  # Added user password field
    balance DECIMAL(10, 2)
)
"""
mycursor.execute(User_table)

admin_table= """
CREATE TABLE IF NOT EXISTS admin_accounts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  admin_id INT,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  admin_pas VARCHAR(255)
)
"""
mycursor.execute(admin_table)

def generate_unique_id():
    return random.randint(0, 99)


def generate_unique_account_no():
    return random.randint(10000, 999999999)
def admin():
    admin_id = int(input("Enter an admin ID: "))
    admin_pas = input("Enter a Password: ")

    mycursor.execute("SELECT * FROM admin_accounts WHERE admin_id = %s AND admin_pas = %s", (admin_id, admin_pas))
    admin =mycursor.fetchone()

    if admin:
        print("Admin login successful")
        return admin
    else:
        print("Invalid admin ID or password")
        return None


def user():
    account_no = int(input("Enter an account number: "))
    user_pas = input("Enter a Password: ")

    mycursor.execute("SELECT * FROM user_accounts WHERE account_no = %s AND user_pas = %s", (account_no, user_pas))
    user = mycursor.fetchone()

    if user:
        print("User login successful")
        return user
    else:
        print("Invalid account number or password")
        return None


def create_admin_ac(admin):
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    admin_pas = input("Create Password: ")

    admin_id = generate_unique_id()

    insert_query = """
    INSERT INTO admin_accounts (admin_id, first_name, last_name, admin_pas)
    VALUES (%s, %s, %s, %s)
    """
    data = (admin_id, fname, lname, admin_pas)
    mycursor.execute(insert_query, data)

    mydb.commit()

    print(f"Admin Account Created with Admin ID: {admin_id}")


def create_user_ac(admin):
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    user_pas = input("Create Password: ")

    user_id = generate_unique_id()
    account_no = generate_unique_account_no()

    balance = float(input("Enter balance: "))

    insert_query = """
    INSERT INTO user_accounts (user_id, account_no, first_name, last_name, user_pas, balance)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    data = (user_id, account_no, fname, lname, user_pas, balance)
    mycursor.execute(insert_query, data)

    mydb.commit()

    print(f"User Account Created with User ID: {user_id} and Account No: {account_no}")


def update_user_detail(admin):
    print("Update User Details")
    user_id = int(input("Enter the User ID to update: "))

    mycursor.execute("SELECT * FROM user_accounts WHERE user_id = %s", (user_id,))
    user = mycursor.fetchone()

    if user is None:
        print("User not found.")
        return

    new_balance = float(input("Enter the new balance: "))

    update_query = "UPDATE user_accounts SET balance = %s WHERE user_id = %s"
    mycursor.execute(update_query, (new_balance, user_id))

    mydb.commit()

    print("User details updated")


def delete_user_details(admin):
    print("Delete User Details")
    user_id = int(input("Enter the User ID to delete: "))

    mycursor.execute("SELECT * FROM user_accounts WHERE user_id = %s", (user_id,))
    user = mycursor.fetchone()

    if user is None:
        print("User not found.")
        return

    delete_query = "DELETE FROM user_accounts WHERE user_id = %s"
    mycursor.execute(delete_query, (user_id,))

    mydb.commit()

    print("User account deleted")


def acc_list():
    print("User Account List")

    mycursor.execute("SELECT id, user_id, account_no, first_name, last_name, balance FROM user_accounts")
    accounts = mycursor.fetchall()

    table = PrettyTable()
    table.field_names = ["ID", "User ID", "Account No", "First Name", "Last Name", "Balance"]

    for account in accounts:
        table.add_row(account)

    print(table)


def transaction_history(user):
    print("Transaction History")

    try:
        user_id = user[1]
        mycursor.execute("SELECT * FROM transaction_history WHERE user_id = %s", (user_id,))
        transactions = mycursor.fetchall()

        if len(transactions) == 0:
            print("No transaction history available.")
        else:
            table =()
            table.field_names = ["Transaction ID", "User ID", "Transaction Type", "Amount", "Transaction Date","Current Balance"]

            current_balance = user[1]

            for transaction in transactions:
                transaction_id, user_id, transaction_type, amount, transaction_date = transaction
                if transaction_type == "Deposit":
                    current_balance += amount
                elif transaction_type == "Withdrawal":
                    current_balance -= amount
                table.add_row(
                    [transaction_id, user_id, transaction_type, amount, transaction_date, current_balance])

            print(table)
    except mysql.connector.Error as e:
        print(f"Error fetching transaction history: {e}")


def withdraw(user):
    userwithdraw = float(input("Enter an amount to withdraw: "))
    current_balance = user[6]

    if userwithdraw <= current_balance:
        new_balance = current_balance - userwithdraw
        update_balance(user[1], new_balance)

        # Insert a withdrawal record into transaction_history
        insert_transaction_record(user[1], "Withdrawal", userwithdraw)
        print("Balanc2e withdrawal successful")
    else:
        print("Insufficient Funds")


def deposit(user):
    userdeposit = float(input("Enter a deposit amount: "))
    current_balance = user[6]

    if userdeposit > 0:
        new_balance = current_balance + userdeposit
        update_balance(user[1], new_balance)

        # Insert a deposit record into transaction_history
        insert_transaction_record(user[1], "Deposit", userdeposit)
        print(f"Amount deposited successfully. New Balance: {new_balance:.2f}")


def insert_transaction_record(user_id, transaction_type, amount):
    try:
        insert_query = """
        INSERT INTO transaction_history (user_id, transaction_type, amount, transaction_date)
        VALUES (%s, %s, %s, NOW())
        """
        data = (user_id, transaction_type, amount)
        mycursor.execute(insert_query, data)
        mydb.commit()
    except mysql.connector.Error as e:
        print(f"Error inserting transaction record: {e}")


def update_balance(user_id, new_balance):
    try:
        # Update the balance in the database
        mycursor.execute("UPDATE user_accounts SET balance = %s WHERE user_id = %s", (new_balance, user_id))
        mydb.commit()
        print(f"Updating balance for user_id {user_id} to {new_balance:.2f}")
    except mysql.connector.Error as e:
        print(f"Error updating balance: {e}")


def check_balance(user):
    try:
        mycursor.execute("SELECT balance FROM user_accounts WHERE user_id = %s", (user[1],))
        result = mycursor.fetchone()

        if result is not None:
            current_balance = result[0]
            print(f"Your Balance: {current_balance:.2f}")
        else:
            print("User not found or balance data missing.")
    except mysql.connector.Error as e:
        print(f"Error fetching balance: {e}")


while True:
    print("Choose")
    print("1. Admin ")
    print("2. User ")
    print("3. Exit ")

    choice = int(input("Choice: "))

    if choice == 1:
        admin_data = admin()
        if admin_data:
            while True:
                print("Choose")
                print("1. Create a User Account")
                print("2. Create an Admin Account")
                print("3. Update User Details")
                print("4. Delete User Details")
                print("5. Show User Details")
                print("6. Exit")

                user_choice = int(input("Choice: "))

                if user_choice == 1:
                    create_user_ac(admin_data)
                elif user_choice == 2:
                    create_admin_ac(admin_data)
                elif user_choice == 3:
                    update_user_detail(admin_data)
                elif user_choice == 4:
                    delete_user_details(admin_data)
                elif user_choice == 5:
                    acc_list()
                elif user_choice == 6:
                    exit()
                else:
                    print("Invalid choice")
        else:
            print("Invalid admin ID or password")

    elif choice == 2:
        user_data = user()
        if user_data:
            while True:
                print("Choose")
                print("1. Withdraw Money")
                print("2. Deposit Money")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5. Exit")

                user_choice = int(input("Choice: "))

                if user_choice == 1:
                    withdraw(user_data)
                elif user_choice == 2:
                    deposit(user_data)
                elif user_choice == 3:
                    check_balance(user_data)
                elif user_choice == 4:
                    transaction_history(user_data)
                elif user_choice == 5:
                        exit()
                else:
                    print("Invalid choice")
    else:
        print("Invalid choice")
        exit()

mycursor.close()
mydb.close()