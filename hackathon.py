print("Enter the quantity of available items: ")
item1 = int(input("Enter the quantity of item 1: "))
item2 = int(input("Enter the quantity of item 2: "))
item3 = int(input("Enter the quantity of item 3: "))
item4 = int(input("Enter the quantity of item 4: "))
item5 = int(input("Enter the quantity of item 5: "))
item6 = int(input("Enter the quantity of item 6: "))



data={"Item1":item1,"Item2":item2 ,"Item3":item3 ,"Item4":item4,"Item5":item5,"Item6":item6}
print(data)
customers=int(input("Enter no of customer "))
while customers>0:
	print("Enter 1 if you wish to check if an item is available", "Enter 2 if you wish to buy some items", sep='\n')

	choice=int(input("Enter your choice: "))
	if choice==1:
		n=int(input("Enter the item  whose quantity you want to check: "))
		if n==1:
			print(item1,'available')
		if n==2:
			print(item2,'available')
		if n==3:
			print(item3,'available')
		if n==4:
			print(item4,'available')
		if n==5:
			print(item5,'available')
		if n==6:
			print(item6,'available')
		
	if choice==2:
	
		qnt=int(input("Enter the no of items you wish to purchase:"))
		for i in range(0,qnt):
			purchase='Item'+input("Enter the item you wish to buy: ")
			no=int(input("Enter the quantity of "+purchase+" you wish to buy"))
			
			data[purchase]-=no
			for i in ['Item1','Item2','Item3','Item4','Item5','Item6']:
				if data[i]<0:
					print(no," not available")
				
			print("You have bought "+str(no)+ " of "+purchase)
			

		print(data)
	customers-=1
