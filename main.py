import os
import sqlite3
from getpass import getpass
from time import sleep

menu = [
    "Dodaj korisnika",
    "Ispisi sve korisnike",
    "Ukloni korisnika",
    "Izlaz",
]


def main_menu(subtitle="", title="ADMIN PROGRAM", tag="#", tag_size=60):
    clear_terminal()
    print(f"{tag * tag_size}\n")
    print(f"{title.center(tag_size)}\n")
    print(f"{tag * tag_size}\n")
    print(f"{subtitle.upper()}:\n")

    if subtitle == "Glavni Izbornik":
        for number, item in enumerate(menu):
            print(f"{number+1}. {item}")


def main():
    database = DB("TCP.db")
    columns = [
        "id INTEGER PRIMARY KEY",
        "name TEXT NOT NULL",
        "email TEXT NOT NULL UNIQUE",
        "password TEXT NOT NULL",
    ]
    database.create_table(columns, "Users")

    main_menu(subtitle="Glavni Izbornik")

    while True:
        user_choice = input(">> ")
        match user_choice:
            case "1":
                add_user(database)
            case "2":
                show_all_users(database)
            case "3":
                delete_user(database)
            case "4":
                break
            case _:
                print("Neispravan unos 🙁 Molimo Vas ponovite.")


class DB:
    def __init__(self, db_name):
        self.s_connect = sqlite3.connect(db_name)
        self.cursor = self.s_connect.cursor()

    def create_table(self, columns, table_name):
        query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
            {', '.join(columns)}
            )"""
        self.cursor.execute(query)
        self.s_connect.commit()

    def create_user(self, data):
        placeholders = ", ".join(["?"] * len(data))
        query = f"""INSERT INTO Users (name, email, password) VALUES (
            {placeholders}
            )"""
        self.cursor.execute(query, data)
        self.s_connect.commit()

    def show_all_users(self):
        query = f"""
        SELECT * FROM Users
        """

        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        for user in rows:
            id = str(user[0])
            name = str(user[1])
            email = str(user[2])

            print(f"{id}. \t{name}\t {email} ")

    def delete_user(self, user_id):
        query = f"DELETE FROM Users WHERE id = ?"
        self.cursor.execute(query, (user_id,))
        self.s_connect.commit()

    def close_db_connection(self):
        self.cursor.close()
        self.s_connect.close()


def add_user(database):
    main_menu("Dodaj Korisnika:")

    full_name = input("Ime i Prezime: ")
    email = input("Email: ")
    password = getpass()

    user_data = (full_name, email, password)

    database.create_user(user_data)

    print(f"Korisnik {full_name} je uspjesno unesen 😁.")

    input("Pritisnite bilo koju tipku za nastavak ... ")

    database.close_db_connection()
    main()


def show_all_users(database):
    main_menu("Ispis svih korisnika:")

    print(database.show_all_users())

    input("\nPritisnite bilo koju tipku za nastavak ... ")

    database.close_db_connection()
    main()


def delete_user(database):
    main_menu("Ukloni korisnika:")
    database.show_all_users()

    user_id = int(input("Unesite ID od korisnika: "))
    confirm = input("Dali ste sigurni da zelite ukloniti korisnika? Y/N ").upper()

    while True:
        if confirm == "Y":
            database.delete_user(user_id)
            input(
                "Korisnik je uklonjen. Pritisnite bilo koju tipku za povratak u glavni izbornik ... "
            )
            database.close_db_connection()
            main()
        else:
            print("Pogresan unos ID-a, pokusajte ponovno")


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


main()
