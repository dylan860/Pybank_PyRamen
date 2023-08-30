# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
import pandas
import prettytable
from pathlib import Path
from prettytable import PrettyTable

pt = PrettyTable()

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('')
sales_filepath = Path('')


csv_menu_data = ""
csv_sales_data = ""

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []
report = {}
inv_report = {}
item_details = {}

# @TODO: Read in the menu data into the menu list

menu_filepath = Path("./PyRamen/Resources/menu_data.csv")
sales_filepath = Path("./PyRamen/Resources/sales_data.csv")

# print(f"the menu data is in {menu_filepath}")
# print(f"the sales data is in {sales_filepath}")

print(menu_filepath)
lst = []

# @TODO: Read in the sales data into the sales list


for line in csv_menu_data:
        lst = []
        lst.append(line[0])     # item
        lst.append(line[1])     # category
        lst.append(line[2])     # description
        lst.append(line[3])     # price        
        lst.append(line[4])     # cost


# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
inv_report[line[0]] = {"01-count" : 0, "02-revenue" : 0, "03-cogs" : 0, "04-profit" : 0}



    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit








    # @TODO: For every row in our sales data, loop over the menu records to determine a match


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables




        # @TODO: Calculate profit of each item in the menu data


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item


            # @TODO: Print out matching menu data






            # @TODO: Cumulatively add up the metrics for each item key





        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data




# @TODO: Write out report to a text file (won't appear on the command line output)
