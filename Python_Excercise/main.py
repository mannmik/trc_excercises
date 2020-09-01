from GroceryStore import GroceryStore

CART_ONE    = 'ABCD'                # first test checkout to demonstrate from the excercise
CART_TWO    = 'DCCBAABB'            # second test checkout to demonstrate from the excercise

store       = GroceryStore()        # a grocery store object to handle to functional components of the excercise

store.fetch_grocery_items()         # gather the grocery items listed in a json file
store.checkout(CART_ONE)            # check the first test cart out according to the specified string of items
store.checkout(CART_TWO)            # check the second test cart out according to the specified string of items
