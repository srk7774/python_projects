# Dictionary as an Alternative to If-Else
price_list = {
'fish': 8,
'beef': 7,
'broccoli': 3,
}

def find_price(item):
    if item in price_list:
        return 'The price for {} is {}'.format(item, price_list[item])
    else:
        return 'The price for {} is not available'.format(item)


find_price('fish')
find_price('cauliflower')


def find_price(item):
    return 'The price for {} is {}'.format(item, price_list.get(
        item, 'not available'))

find_price('fish')

def operations(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y


operations('mul', 2, 8)

def operations(operator, x, y):
    return {
        'add': lambda: x+y,
        'sub': lambda: x-y,
        'mul': lambda: x*y,
        'div': lambda: x/y,
    }.get(operator, lambda: 'Not a valid operation')()

operations('mul', 2, 8)