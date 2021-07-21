from stock import items 
import Now
from Now import curt
import sys

itm = []
prc = []
qty = []
atm = []
amt = 0


print('{0:^60}'.format('='*33))
print('{0:^60}'.format('welcome to item check counter').upper())
print('{0:^60}'.format('='*33))
print(' !. Note: If no items are left for input, Enter \'done\'\n\n')


while True:
    buy = input('Item bought :').lower()

    if buy == 'done':
        break
    elif buy not in items.keys():
    	raise KeyError('Item not found')
	    
    itm.append(buy)
    price = items[buy]
    prc.append(price)
    
    try:
    	quant = int(input('Quantity of {0}: '.format(buy)))
    except:
    	raise ValueError('Enter a number')

    qty.append(quant)
    atm.append(quant * price)
    amt += amt + (quant * price)
		
print('\nThe bill is {0}'.format(amt))
paid = float(input('How much was paid: '))
bal = paid - amt
print('\nBalance is: {}'.format(bal))
		
#output summary to Screen
print('\n\n\n\n\n')
Now.timestamp()
print('\n')
print("{0:^60}".format('SUMMARY'))
print('_'*60)
print("{0:<15}{1:<15}{2:>15}{3:>15}".format('Items', 'Price', 'Quantity', 'Amount'))
print('_'*60)
		
for x in range(len(itm)):
    print("{0:<15}{1:<15}{2:>15}{3:>15}".format(itm[x], prc[x], qty[x], atm[x]))
		
print('{0:>60}'.format('_'*60))
print('{0:>45}{1:>15}'.format('Total Amount', amt))
print('{0:>60}'.format('_'*60))
print('\nPaid: {0}\nBalance: {1}'.format(paid, bal))
		
		
#writing summary to file
sys.stdout = open("item_log_" + curt + ".txt", "w")
Now.timestamp()
print('\n')
print("{0:^60}".format('SUMMARY'))
print('_'*60)
print("{0:<15}{1:<15}{2:>15}{3:>15}".format('Items', 'Price', 'Quantity', 'Amount'))
print('_'*60)
				
for x in range(len(itm)):
    print("{0:<15}{1:<15}{2:>15}{3:>15}".format(itm[x], prc[x], qty[x], atm[x]))
		
print('{0:>60}'.format('_'*60))
print('{0:>45}{1:>15}'.format('Total Amount', amt))
print('{0:>60}'.format('_'*60))
print('\nPaid: {0}\nBalance: {1}'.format(paid, bal))
sys.stdout.close()

		
if __name__ == '__item_check__':
	item_check()