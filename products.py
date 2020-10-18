products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	pn = []
	pn.append(name)
	pn.append(price)
	#7~9行化簡為 pn = [name, price]
	products.append(pn)
	#再化簡 products.append([name, price])
print(products)