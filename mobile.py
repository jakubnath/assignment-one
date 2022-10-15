import random
mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here


users = mobile_data.get('data')

rate = int(mobile_data.get('exchnage_rate'))

i = 0

for user in users:
    brand = users[i].get('name')
    price = users[i].get('price')
    only_price = "".join([c for c in price if c.isdigit()])
    country = users[i].get('made')
    bdt_price = int(only_price) * rate

    template = [
        f'{brand} is made in {country}. The price is {price} which is almost equal to {bdt_price} BDT',
        f'The price of {brand} is {price}. {brand} is made in {country}. Which is almost equal to {bdt_price} BDT',
        f'{brand} is most popular in {country}. The price is {price} which is almost equal to {bdt_price} BDT',
        f'I like {brand} which is made in {country}. The price is {price} which is almost equal to {bdt_price} BDT',
    ]
print(random.choice(template))

# template done



