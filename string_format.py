width = int(input('Please enter width: '))

fruits = [
    ['Apples', 0.4],
    ['Pears', 0.5],
    ['Cantaloupes', 1.92],
    ['Dired Apricots (16 oz.)', 8],
    ['Prunes (4 lbs.)', 12]
]

price_width = 10
item_width = width - price_width

header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{0[0]:{}}}{{0[1]:>{}.2f}}'.format(item_width, price_width)

print('=' * width)

print(header_fmt.format('Item', 'Price'))

print('-' * width)

for fruit in fruits:
    print(fmt.format(fruit))

print('=' * width)