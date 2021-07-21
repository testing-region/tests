from datetime import datetime

today = datetime.now()

def timestamp():
    now = today.strftime("%B %d, %Y   %H:%M:%S")
    print('{0:>60}'.format(now))
    

curt = today.strftime("%d-%m-%Y_%H:%M:%S")