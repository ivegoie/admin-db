# ADMIN PROGRAM

This is a simple admin program that allows you to manage users in a SQLite database.

## Prerequisites

- Python 3.x
- SQLite3

## Installation and Setup

1. Clone this repository or download the code.

2. Open a terminal and navigate to the project directory.

3. Run the following command to install the required dependencies:

   ```
   pip install sqlite3
   ```

4. Start the program by running the following command:
   ```
   python main.py
   ```

## Usage

The program provides the following menu options:

1. **Dodaj korisnika (Add User)**: Allows you to add a new user to the database. You will be prompted to enter the user's name, email, and password.

2. **Ispisi sve korisnike (Show All Users)**: Prints all the users in the database.

3. **Ukloni korisnika (Delete User)**: Allows you to remove a user from the database. You will be prompted to enter the ID of the user you want to delete.

4. **Izlaz (Exit)**: Exits the program.

## Database

The program uses a SQLite database named "TCP.db". The database file will be created automatically if it doesn't exist. The "Users" table stores the user information, including their ID, name, email, and password.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
