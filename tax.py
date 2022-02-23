def income_tax(income):
    if (income<0):
        print('Invalid income. It should be greater than 0')
    else:
        rate  = 30/100
        tax = format(income*rate,'.2f')
        print('Tax is {}'.format(tax))
    
income = int(input('Your Income: '))
income_tax(income)