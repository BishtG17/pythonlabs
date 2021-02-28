while True:
	print("0 for exit")
	print("2 for concatenation")
	print("3 for maximum")
	print("4 for minimum")
	print("5 for length")
	print("5 for reverse")
	print("7 for uppercase")
	print("8 for lowercase")
	li=[]
	t2=(1,2,3,4)
	t1=(1,2,3,"rvce",5,6)
	choice=int(input("choose an option"))
	if choice==1:
		print("create a list")
		for i in range(0,1):
			li.append(input("enter the element"))
			t1=tuple(li)
			print(t4)
	elif choice==2:
		print("---------------------------------------------------------------------------")
		print("concatenation of the tuple is")
		print(t1+t2)
		print("---------------------------------------------------------------------------")
	elif choice==3:
                print("---------------------------------------------------------------------------")
                print("maximum of the tuple is")
                print(max(t2))
                print("---------------------------------------------------------------------------")
	elif choice==4:
		print("---------------------------------------------------------------------------")
		print("maximum of the tuple is")
		print(min(t2))
		print("---------------------------------------------------------------------------")
	elif choice==7:
		print("---------------------------------------------------------------------------")
		print("uppercase of the tuple is")
		print(t1.upper())
		print("---------------------------------------------------------------------------")

	else:
		print("invalid choice")
