import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="OnlineBankingDB"
)
mycursor = mydb.cursor()

def create_account(account_number, pin, full_name, user_type):
    sql = "INSERT INTO Users (AccountNumber, PIN, FullName, UserType) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql, (account_number, pin, full_name, user_type))
    mydb.commit()
    return "Account created successfully"

def close_account(account_number):
    sql = "DELETE FROM Users WHERE AccountNumber = %s"
    mycursor.execute(sql, (account_number,))
    mydb.commit()
    return "Account closed successfully"

def modify_account(account_number, new_pin, new_full_name):
    sql = "UPDATE Users SET PIN = %s, FullName = %s WHERE AccountNumber = %s"
    mycursor.execute(sql, (new_pin, new_full_name, account_number))
    mydb.commit()
    return "Account details updated successfully"

print(create_account(555555, 5678, 'New Customer', 'Customer'))  # Create a new customer account
print(close_account(555555))   # Close the newly created account
print(modify_account(987654, 1111, 'Modified Customer'))  # Modify account details for account number 987654
