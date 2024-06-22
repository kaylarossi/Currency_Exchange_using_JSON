"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

"""
import a1

src = input('Enter source currency: ')
dst = input('Enter target currency: ')
amt = float(input('Enter original amount: '))

newMoney = a1.exchange(src,dst,amt)

print('You can exchange', amt, src, 'for', newMoney, dst,'.')
