products = []
product = ''
while product  != 'q' :
    product = input("你要買啥？ ")
    if product == "q" :
        break
    price = float(input("價格是？ "))
    amount = float(input("數量是? "))
    total = str(price * amount)
    products.append([product,total])

with open("product.csv","w") as f :
    f.write('產品,價格\n')
    for p in products :
        f.write("%s\n" %p)
print(products)