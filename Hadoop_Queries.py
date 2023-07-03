#!/usr/bin/env python

import sys
import csv

# Query 1: Find the Lenovo products that get a rating of above 3, whose MRP is less than 60,000, and get a discount of 25%.
def query_1_mapper():
    for line in sys.stdin:
        record = line.strip().split(',')
        if record[1] == 'Lenovo' and float(record[3]) > 3 and float(record[4]) < 60000 and float(record[5]) == 25:
            print(record[0] + '\t' + line.strip())

def query_1_reducer():
    for line in sys.stdin:
        print(line.strip())

# Query 2: Find the products named Lenovo and HP and get more than a 20% discount.
def query_2_mapper():
    for line in sys.stdin:
        record = line.strip().split(',')
        if record[1] in ['Lenovo', 'HP'] and float(record[5]) > 20:
            print(record[0] + '\t' + line.strip())

def query_2_reducer():
    for line in sys.stdin:
        print(line.strip())

# Query 3: Laptops that receive negative statements.
def query_3_mapper():
    for line in sys.stdin:
        record = line.strip().split(',')
        if 'negative' in record[6].lower():
            print(record[0] + '\t' + line.strip())

def query_3_reducer():
    for line in sys.stdin:
        print(line.strip())

# Query 4: HP laptops get more than 2 stars with flat discounts.
def query_4_mapper():
    for line in sys.stdin:
        record = line.strip().split(',')
        if record[1] == 'HP' and float(record[2]) > 2 and float(record[5]) == 0:
            print(record[0] + '\t' + line.strip())

def query_4_reducer():
    for line in sys.stdin:
        print(line.strip())

# Query 5: Lenovo laptops with more than 3 stars, a current price of less than 50,000, and positive statements.
def query_5_mapper():
    for line in sys.stdin:
        record = line.strip().split(',')
        if record[1] == 'Lenovo' and float(record[2]) > 3 and float(record[3]) < 50000 and 'positive' in record[6].lower():
            print(record[0] + '\t' + line.strip())

def query_5_reducer():
    for line in sys.stdin:
        print(line.strip())

# Query 6: Find the product that gets stars above 4, a discount of more than 30%, and gives any additional discounts.
def query_6_mapper():
    for line in sys.stdin:
        record = line.strip().split(',')
        if float(record[2]) > 4 and float(record[4]) > 30 and float(record[5]) > 0:
            print(record[0] + '\t' + line.strip())

def query_6_reducer():
    for line in sys.stdin:
        print(line.strip())

# Query 7: Find the product names with no rating or stars.
def query_7_mapper():
    for line in sys.stdin:
        record = line.strip().split(',')
        if record[2] == '' or record[2] == '0':
            print(record[1] + '\t' + line.strip())

def query_7_reducer():
    for line in sys.stdin:
        print(line.strip())

# Query 8: List the product names that have a discount of more than 50%, offer any additional discounts, and receive a positive response.
def query_8_mapper():
    for line in sys.stdin:
        record = line.strip().split(',')
        if float(record[4]) > 50 and float(record[5]) > 0 and 'positive' in record[6].lower():
            print(record[1] + '\t' + line.strip())

def query_8_reducer():
    for line in sys.stdin:
        print(line.strip())

# Query 9: List down the names of those products that have negative reviews.
def query_9_mapper():
    for line in sys.stdin:
        record = line.strip().split(',')
        if 'negative' in record[6].lower():
            print(record[1])

def query_9_reducer():
    for line in sys.stdin:
        print(line.strip())

# Query 10: List down the names of the products whose current price is less than their MRP.
def query_10_mapper():
    for line in sys.stdin:
        record = line.strip().split(',')
        if float(record[3]) < float(record[4]):
            print(record[1])

def query_10_reducer():
    for line in sys.stdin:
        print(line.strip())

# Query 11: List out all the products from Flipkart having a price less than 30,000 and stars above 4.5.
def query_11_mapper():
    for line in sys.stdin:
        record = line.strip().split(',')
        if record[0] == 'Flipkart' and float(record[3]) < 30000 and float(record[2]) > 4.5:
            print(record[1])

def query_11_reducer():
    for line in sys.stdin:
        print(line.strip())

# Query 12: List out all the products that have no stars, no ratings, and no reviews.
def query_12_mapper():
    for line in sys.stdin:
        record = line.strip().split(',')
        if record[2] == '' and record[6] == '':
            print(record[1])

def query_12_reducer():
    for line in sys.stdin:
        print(line.strip())


# Driver code
if __name__ == '__main__':
    query = int(sys.argv[1])

    if query == 1:
        query_1_mapper()
    elif query == 2:
        query_2_mapper()
    elif query == 3:
        query_3_mapper()
    elif query == 4:
        query_4_mapper()
    elif query == 5:
        query_5_mapper()
    elif query == 6:
        query_6_mapper()
    elif query == 7:
        query_7_mapper()
    elif query == 8:
        query_8_mapper()
    elif query == 9:
        query_9_mapper()
    elif query == 10:
        query_10_mapper()
    elif query == 11:
        query_11_mapper()
    elif query == 12:
        query_12_mapper()
