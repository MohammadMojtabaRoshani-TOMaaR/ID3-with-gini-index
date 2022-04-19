import sys

def initial_program():
    try:
        n = len(sys.argv)
        if n < 2:
            print("ERROR> missing values, path to dataset CSV file is required")
    except Exception:
        print("Exception")


def printer(args):
    _many_dash_printer()

    for arg in args:
        print(arg)

def lowest(args):
    _many_dash_printer()

    sort_orders = sorted(args, key= lambda x: x['gini_index'], reverse= True)

    return sort_orders.pop()


def _many_dash_printer():
    print("__________________________________________________________________________________________")
