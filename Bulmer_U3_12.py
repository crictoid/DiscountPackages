# Mark Bulmer - CIS 115 - 6-16-2021

price=99
quantity=int( input('# of packages purchased: '))

if quantity < 10:
    discount=0
elif quantity < 20:
    discount=.1
elif quantity < 50:
    discount=.2
elif quantity < 100:
    discount=.3
else:
    discount=.4

subtotal=price*quantity
discount_total=discount*subtotal
total=subtotal-discount_total

print("Discount: $", discount_total)
print("Total after discount: $", total)
