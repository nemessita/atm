# ATM PROQRAMI
# Proqram Sorushur :
# (1) Balansi yoxla (2) Kartdan Pul Cixar (3) Karta Medaxil et (4) Pini deyish (5) Cixish et
# Qeyd:
# Pin kodun databazada olub olmamasini yoxlayin , 
# yoxdursa error qaytarsin , varsa kodlar icra olunsun

import sqlite3

db = sqlite3.connect('bot.db')
sql = db.cursor()


# def create_database():
#     sql.execute("""CREATE TABLE IF NOT EXISTS users(
                
#                 id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                 pin INTEGER NOT NULL CHECK (pin >= 0),
#                 cash INTEGER NOT NULL CHECK (cash >= 0)
#                 )""")
# db.commit()
# db.close()

def register_user():
    pin = int(input('Pin : '))
    cash = int(input('Cash : '))

    sql.execute(f"SELECT * FROM users WHERE pin=? ", (pin,))
    if sql.fetchone():
        print("qeydiyyayin artiq var!")
    else:
        sql.execute(f"INSERT INTO users (pin,cash) VALUES({pin},{cash})")
        db.commit()
        print("qeseng!!")

def check_balance(pin):
    pin = int(input('Pin : '))

    sql.execute(f"SELECT * FROM users WHERE pin=? ", (pin,))
    print(sql.fetchone())
    result = sql.fetchone()
    if result:
        print(f"Balance for {pin}: {result[0]}")
    else:
        print("bele login yoxdur.")



def spend():
    try:
        pin = int(input('PIN: '))
        amount = int(input('amount: '))
    except ValueError:
        print("Yalnis.")
        return

    with sqlite3.connect('bot.db') as db:
        sql = db.cursor()
    sql.execute("SELECT cash FROM users WHERE pin=?", (pin,))
    result = sql.fetchone()

    if result:
        current_balance = result[0]
        if current_balance >= amount:
            new_balance = current_balance - amount
            sql.execute("UPDATE users SET cash=? WHERE pin=?", (new_balance, pin))
            db.commit()
            
            print(f"Withdrew {amount}. New balance for PIN {pin}: {new_balance}.")
        else:
            print("Yeterince pul yoxdur.")
    else:
        print("yalnis pin.")



    

def withdraw():
    try:
        pin = int(input('PIN: '))
        amount = int(input('amount: '))
    except ValueError:
        print("Yalnis.")
        return

    with sqlite3.connect('bot.db') as db:
        sql = db.cursor()
    sql.execute("SELECT cash FROM users WHERE pin=?", (pin,))
    result = sql.fetchone()

    if result:
        current_balance = result[0]
        
        new_balance = current_balance + amount
        sql.execute("UPDATE users SET cash=? WHERE pin=?", (new_balance, pin))
        db.commit()
            
        print(f"Withdrew {amount}. New balance for PIN {pin}: {new_balance}.")
        
    else:
        print("yalnis pin.")

def change_pin():
    pin = int(input('Pin : '))
    new_pin = int(input('New Pin : '))

    sql.execute(f"UPDATE users SET pin={new_pin} WHERE pin={pin}")
    db.commit()
    print(f"Pin changed to {new_pin}.")

def delete_user():

    pin = input("Enter username to delete: ")
    sql.execute("DELETE FROM users WHERE pin=?", (pin,))
    db.commit()
    print(f"User '{pin}' deleted.")

def main():
    # create_database()

    while True:
        choice = input("Select an option: (1) Qeydiyyatdan kecin (2) Balansi yoxla  (3) Kartdan Pul Cixar  (4) Karta Medaxil et (5) Pini deyish (6) Sil  (7) Cixish: ")
        
        if choice == "1":
            register_user()
        elif choice == "2":
            check_balance()
        elif choice == "3":
            spend()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            change_pin()
        elif choice == "6":
            delete_user()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("error_yeniden cehd ele.")

if __name__ == "__main__":
    main()
db.close()













