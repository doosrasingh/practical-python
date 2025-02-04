# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_payments = 30 * 12
extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108
current_month = 0

while principal > 0:
    current_month += 1
    if (current_month >= extra_payment_start_month) and (current_month <= extra_payment_end_month):
        monthly_payment = payment + extra_payment
    else:
        monthly_payment = payment
    if (principal <= monthly_payment) : 
        monthly_payment = principal 
        principal = 0
    else:
        principal = principal * (1+rate/12) - monthly_payment
    total_paid = total_paid + monthly_payment
    #print(current_month, round(total_paid, 2), round(principal, 2))
    print(f'{current_month:4} {total_paid:10.2f} {principal:10.2f}')


print('Total paid', f'{total_paid:0.2f}')
print('Months', current_month)
