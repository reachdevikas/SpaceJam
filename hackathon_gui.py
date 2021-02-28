from tkinter import  *
root=Tk()
root.title("ABC STORE")

item1=51
item2=50
item3=26
item4=30
item5=88
item6=5

l1=Label(root,text = 'Item1: '+str(item1))
l2=Label(root,text = 'Item2: '+str(item2))
l3=Label(root,text = 'Item3: '+str(item3))
l4=Label(root,text = 'Item4: '+str(item4))
l5=Label(root,text = 'Item5: '+str(item5))
l6=Label(root,text = 'Item6: '+str(item6)) 

l=Label(root, text = "Welcome!!")

l1.grid(row=1,column=0,columnspan=2)
l2.grid(row=2,column=0,columnspan=2)
l3.grid(row=3,column=0,columnspan=2)
l4.grid(row=4,column=0,columnspan=2)
l5.grid(row=5,column=0,columnspan=2)
l6.grid(row=6,column=0,columnspan=2)

l.grid(row=0,column=0,columnspan=2)



def onclick(n):
	root2=Tk()
	e = Entry(root2, width = 50)
	e.grid(row=0,column=0)
	e.insert(0, "Enter quantity ") 
	 
	
	def func():
		global item2
		global item1
		global item3
		global item4
		global item5
		global item6
		

		
		if n==1:
			lab=Label(root2, text="You have bought "+e.get()+" of Item1")
			lab.grid(row=1,column=0)
			
			item1=item1-int(e.get())
			
			
			l1=Label(root2,text = 'Item1: '+str(item1))
			l2=Label(root2,text = 'Item2: '+str(item2))
			l3=Label(root2,text = 'Item3: '+str(item3))
			l4=Label(root2,text = 'Item4: '+str(item4))
			l5=Label(root2,text = 'Item5: '+str(item5))
			l6=Label(root2,text = 'Item6: '+str(item6)) 


			l1.grid(row=2,column=0,columnspan=2)
			l2.grid(row=3,column=0,columnspan=2)
			l3.grid(row=4,column=0,columnspan=2)
			l4.grid(row=5,column=0,columnspan=2)
			l5.grid(row=6,column=0,columnspan=2)
			l6.grid(row=7,column=0,columnspan=2)
		if n==2:
			lab=Label(root2, text="You have bought "+e.get()+" of Item2")
			lab.grid(row=1,column=0)
			
			item2=item2-int(e.get())

			l1=Label(root2,text = 'Item1: '+str(item1))
			l2=Label(root2,text = 'Item2: '+str(item2))
			l3=Label(root2,text = 'Item3: '+str(item3))
			l4=Label(root2,text = 'Item4: '+str(item4))
			l5=Label(root2,text = 'Item5: '+str(item5))
			l6=Label(root2,text = 'Item6: '+str(item6)) 


			l1.grid(row=2,column=0,columnspan=2)
			l2.grid(row=3,column=0,columnspan=2)
			l3.grid(row=4,column=0,columnspan=2)
			l4.grid(row=5,column=0,columnspan=2)
			l5.grid(row=6,column=0,columnspan=2)
			l6.grid(row=7,column=0,columnspan=2)
		if n==3:
			lab=Label(root2, text="You have bought "+e.get()+" of Item3")
			lab.grid(row=1,column=0)
			
			item3=item3-int(e.get())

			l1=Label(root2,text = 'Item1: '+str(item1))
			l2=Label(root2,text = 'Item2: '+str(item2))
			l3=Label(root2,text = 'Item3: '+str(item3))
			l4=Label(root2,text = 'Item4: '+str(item4))
			l5=Label(root2,text = 'Item5: '+str(item5))
			l6=Label(root2,text = 'Item6: '+str(item6)) 


			l1.grid(row=2,column=0,columnspan=2)
			l2.grid(row=3,column=0,columnspan=2)
			l3.grid(row=4,column=0,columnspan=2)
			l4.grid(row=5,column=0,columnspan=2)
			l5.grid(row=6,column=0,columnspan=2)
			l6.grid(row=7,column=0,columnspan=2)

		if n==4:
			lab=Label(root2, text="You have bought "+e.get()+" of Item4")
			lab.grid(row=1,column=0)
			
			item4=item4-int(e.get())


			l1=Label(root2,text = 'Item1: '+str(item1))
			l2=Label(root2,text = 'Item2: '+str(item2))
			l3=Label(root2,text = 'Item3: '+str(item3))
			l4=Label(root2,text = 'Item4: '+str(item4))
			l5=Label(root2,text = 'Item5: '+str(item5))
			l6=Label(root2,text = 'Item6: '+str(item6)) 


			l1.grid(row=2,column=0,columnspan=2)
			l2.grid(row=3,column=0,columnspan=2)
			l3.grid(row=4,column=0,columnspan=2)
			l4.grid(row=5,column=0,columnspan=2)
			l5.grid(row=6,column=0,columnspan=2)
			l6.grid(row=7,column=0,columnspan=2)

		if n==5:
			lab=Label(root2, text="You have bought "+e.get()+" of Item5")
			lab.grid(row=1,column=0)
			
			item5=item5-int(e.get())


			l1=Label(root2,text = 'Item1: '+str(item1))
			l2=Label(root2,text = 'Item2: '+str(item2))
			l3=Label(root2,text = 'Item3: '+str(item3))
			l4=Label(root2,text = 'Item4: '+str(item4))
			l5=Label(root2,text = 'Item5: '+str(item5))
			l6=Label(root2,text = 'Item6: '+str(item6)) 


			l1.grid(row=2,column=0,columnspan=2)
			l2.grid(row=3,column=0,columnspan=2)
			l3.grid(row=4,column=0,columnspan=2)
			l4.grid(row=5,column=0,columnspan=2)
			l5.grid(row=6,column=0,columnspan=2)
			l6.grid(row=7,column=0,columnspan=2)

		if n==6:
			lab=Label(root2, text="You have bought "+e.get()+" of Item6")
			lab.grid(row=1,column=0)
			
			item6=item6-int(e.get())


			l1=Label(root2,text = 'Item1: '+str(item1))
			l2=Label(root2,text = 'Item2: '+str(item2))
			l3=Label(root2,text = 'Item3: '+str(item3))
			l4=Label(root2,text = 'Item4: '+str(item4))
			l5=Label(root2,text = 'Item5: '+str(item5))
			l6=Label(root2,text = 'Item6: '+str(item6)) 


			l1.grid(row=2,column=0,columnspan=2)
			l2.grid(row=3,column=0,columnspan=2)
			l3.grid(row=4,column=0,columnspan=2)
			l4.grid(row=5,column=0,columnspan=2)
			l5.grid(row=6,column=0,columnspan=2)
			l6.grid(row=7,column=0,columnspan=2)

	b=Button(root2,text="Enter",command=func)
	b.grid(row=1,column=0)


	root2.mainloop()

button1=Button(root, text="Item1" ,command= lambda : onclick(1), padx=50,pady=30)
button2=Button(root, text="Item2" ,command= lambda : onclick(2), padx=50,pady=30)
button3=Button(root, text="Item3" ,command= lambda : onclick(3), padx=50,pady=30)
button4=Button(root, text="Item4" ,command= lambda : onclick(4), padx=50,pady=30)
button5=Button(root, text="Item5" ,command= lambda : onclick(4), padx=50,pady=30)
button6=Button(root, text="Item6" ,command= lambda : onclick(4), padx=50,pady=30)



button1.grid(row=7, column=0)
button2.grid(row=7, column=1)
button3.grid(row=8, column=0)
button4.grid(row=8, column=1)
button5.grid(row=9, column=0)
button6.grid(row=9, column=1)

root.mainloop()
