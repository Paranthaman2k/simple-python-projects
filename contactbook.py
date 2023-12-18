import csv
import json
import sqlite3
import tkinter as tk


# Initialize an empty contact book (dictionary)
contact_book = {}

# Function to add a new contact
def add_contact(name, details):
    contact_book[name] = details
    print(f"Contact {name} added successfully.")

# Function to delete a contact
def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found in the contact book.")

# Function to search for a contact
def search_contact(name):
    if name in contact_book:
        print(f"Contact: {name}")
        details = contact_book[name]
        for key, value in details.items():
            print(f"{key}: {value}")
    else:
        print(f"Contact {name} not found in the contact book.")

# Function to display all contacts
def display_contacts():
    print("Contacts in the contact book:")
    for name, details in contact_book.items():
        print(f"Contact: {name}")
        for key, value in details.items():
            print(f"{key}: {value}")
        print("")

# Main menu
while True:
    print("\nContact Book Menu:")
    print("1. Add a contact")
    print("2. Delete a contact")
    print("3. Search for a contact")
    print("4. Display all contacts")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name of the contact: ")
        details = {}
        details["Phone"] = input("Enter phone number: ")
        details["Email"] = input("Enter email address: ")
        add_contact(name, details)
    elif choice == "2":
        name = input("Enter the name of the contact to delete: ")
        delete_contact(name)
    elif choice == "3":
        name = input("Enter the name of the contact to search: ")
        search_contact(name)
    elif choice == "4":
        display_contacts()
    elif choice == "5":
        print("Exiting contact book.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-5).")
