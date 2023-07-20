basket=["baloons","chocolates",2.5,1]
print(basket)
basket.append("butter")
print(basket)
basket[0]="tea powder"
print(basket)
for loop in basket:
    print(loop)
basket.remove(2.5)
print(basket)
basket.pop(0)
print(basket)