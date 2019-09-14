a=1
while a:
	a=int(input("Введите число: "))
	if a>1000:
		print("нашли и остановились", a)
		break
	else:
		print("не подходит", a)

