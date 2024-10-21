# Kareem's Cosmetic Store Inventory System
An Object-Oriented Programming (OOP)-based inventory management system for Kareem's Cosmetic Store, built in Python.

## Project Overview
This project provides an inventory management system for Kareem's Cosmetic Store. It allows store managers to:

Track, update, and manage cosmetic products.
Generate reports on stock levels and expiration dates.
Persist inventory data using a JSON file.
The system is built using Python and applies OOP principles to encapsulate different functionalities across several classes.

# Features
Add, update, and remove items in the inventory.
Generate reports for:
## Low stock: 
Identifies items below a specified stock threshold.
## Expired items:
Lists items past their expiration date.
Data persistence through a JSON file for saving and loading inventory data.
Role-based user management with permissions for admin and manager roles.
# Project Structure
bash
Copy code

## Installation and Usage
Clone the Repository
bash
Copy code
cd kareems-cosmetic-store-inventory
Running the System
Make sure you have Python 3.x installed on your machine. To run the inventory management system:

## bash
Copy code
python src/main.py
Usage Instructions
Adding an Item
To add an item to the inventory, use the Item and Inventory classes. Here's an example:

## Generating Reports
To generate a low-stock report:

## python
Copy code
from report import Report

report = Report(inventory)
low_stock_report = report.low_stock_report(threshold=5)
print(low_stock_report)
## Saving and Loading Data
Data is automatically saved to and loaded from a JSON file. You can use the FileHandler class to manually save or load data:

python
Copy code
from filehandler import FileHandler

file_handler = FileHandler('inventory_data.json')
file_handler.save_inventory(inventory)  # Save the inventory to a file
inventory.items = file_handler.load_inventory()  # Load data from a file
## Requirements
Python 3.x
No additional external libraries are required for this project.
 ##  Future Improvements
Database Integration: Migrate from JSON-based persistence to an SQLite or PostgreSQL database for better scalability and data management.
GUI: Develop a graphical user interface (GUI) to make the system more user-friendly.
Extended User Roles: Introduce additional user roles with more granular permissions (e.g., cashier, supervisor).
UML Class Diagram: 
