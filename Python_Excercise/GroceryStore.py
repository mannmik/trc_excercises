'''
    Author: 
        Michael Mann

    Description:
        Implementation of TRC Python Excercise to write a cash register program for a list of grocery items presented in a string
        and identified by letters i.e. 'ABCD'
'''

import json

class GroceryStore:

    def __init__(self):
        self.grocery_items = {}

    '''
    Description: 
        Reads grocery items from 'grocery_items.json' located in the same directory
        and stores in the grocery_items member var
    '''
    def fetch_grocery_items(self):
        inventory = {}

        with open('grocery_items.json') as item:
            inventory = json.load(item)
        
        self.grocery_items = inventory

    '''
    Description:
        Assumes a valid item list string will be passed in. i.e. 'ABCD'
        rings up each item individually
        gets the total of the item list passed in
        prints receipt each item, quantity of each item, and total of the item list passsed in
    '''
    def checkout(self, item_list):

        customer_total  = 0                                         # initial total of the cart is 0

        scanned_items   = self.scan_items(item_list)                # scan the each item to get the quantity

        customer_total  = self.calculate_total(scanned_items)       # calculates the overall total of all of these items

        self.print_receipt(scanned_items, customer_total)           # prints a receipt of  each item and the overall total


    '''
        Description:
            Calculates the quantity of each item in the item list
    '''
    def scan_items(self, item_list):

        scanned_items = {}

        for item in item_list:                                                                     # loop through each item id in the string of items i.e 'ABCD'
            if item in scanned_items:                                                              # if this item was already scanned 
                scanned_items[item]['quantity'] += 1                                               # increase the quantity by 1

            else:    
                qty = 1                                                                            # we are adding a quantity of 1
                                                                         
                scanned_items[item] = {                                                            # this item hasn't been scanned yet so add it to our cart dict                                                       
                'quantity': qty
                }

        return scanned_items


    '''
        Description:
            gets the subtotal of a grocery item using the number of items scanned at the register
            returns the quantity of items * cost, or the discounted price
    '''
    def calculate_item_subtotal(self, quantity, item):
        # check if this is a discount
        discountedValue = self.check_volume_discount(quantity, item)

        if discountedValue:
            return discountedValue

        return quantity * self.grocery_items[item]['cost']
    

    '''
        Description:
            Assumes all Volume Discounts will be formatted to match '{volume} for {discounted price}' i.e. '4 for $3'
            Checks if there is an existing volume discount for the specified item
            If the quantity matches the volume discount quantity return discount else return none
    '''
    def check_volume_discount(self, quantity, item):

        if self.grocery_items[item]['volume_discount']:                         # check that this item has an existing discount
            discount = self.grocery_items[item]['volume_discount']

            discount = discount.replace('$', '')                                # remove the $                          
            
            
            discount = discount.split(' ')                                      # parse by spaces

            # compare the quantity to the first value (volume) in the parsed array. 
            # we assume this is the format of the discount string
            if quantity == int(discount[0]):                               
                return float(discount[2])                                       # return the discount price which is assumed to be the third item of our parsed string                                    

        return None                                                             # no matching discount return none


    '''
        Description:
            Calculates the total of all items in our item list string by adding the subtotals
    '''
    def calculate_total(self, cart):
        total = 0
        
        for item in cart:
            total += self.calculate_item_subtotal(cart[item]['quantity'], item)
        
        return total
    
    '''
        Description:
            Prints the list of items, their quantites, and the total price
    '''
    def print_receipt(self, receipt_items, total):

        for item in receipt_items:

            print('{} {}').format(receipt_items[item]['quantity'], self.grocery_items[item]['item'])
        
        print('\nTotal: ${:.2f}\n'.format(total))                 # print to 2 decimal places to demonstrate currency

