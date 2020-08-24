num_1: int = int(input('skriv in ett tal '))
num_2: int = int(input('skriv in ett till tal '))

print(f'första numret ' + str(num_1))
print(f'andra numret ' + str(num_2))

print('addition ' + str(num_1 + num_2))

print('produkten av talen ' + str(num_1 * num_2))

höjden = float(input('mata in höjden på triangeln '))
basen = float(input('mata in basen på triangeln '))

area = basen * höjden / 2

print('triangelns area är:' + str(area))

price = float(input('mata in ordinarie pris '))

discount_price = price * 0.85

print('rea pris: ' + str(discount_price))

price2 = float(input('mata in ordinarie pris '))
discount = float(input('mata in rabatt procent '))

discount = (100 - discount) / 100
discount_price = price2 * discount

print('rea pris: ' + str(discount_price))

volume = float(input('mata in tankad mängd'))
liter_price = float(input('mata in liter pris'))

total_price = volume * liter_price

print(f'Kvitto')
print(f'tankad mängd i liter {volume}')
print(f'pris per liter {liter_price}')
print(f'betalt i euro + {total_price}')
print(' tack för besöket')
print('  välkommen åter!')
