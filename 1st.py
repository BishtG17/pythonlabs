while True:
	print("0 for exit")
	print("1 for concatenation")
	print("2 for maximum")
	print("3 for upper")
	print("4 for lower")
	print("5 for length")
	print("6 for split")
	print("7 for repetation")
	print("8 for minimum")
	print("9 for slicing")
	print("10 for range slicing")
	choice= int(input("enter a string "))
	if choice == 0:
		exit()
	elif choice ==1:
		S1=(input("enter the string"))
		S2=(input("enter a string"))
		print(S1+S2)
	elif choice==2:
		S1=(input("enter a string "))
		print(max(S1))
	elif choice==3:
		S1=input("enter a string ")
		print(S1.upper())
	elif choice==4:
		S1=input("enter a string ")
		print(S1.lower())
	elif choice==5:
		S1=input("enter a string ")
		print(len(S1))
	elif choice==6:
		S1=input("enter a string")
		print(S1.split())
	elif choice==7:
                S1=input("enter a string")
                print(S1*2)
	elif choice==8:
                S1=input("enter a string ")
                print(min(S1))
	elif choice==9:
                S1=input("enter a string")
                print(S1[2])
	else:
		print("0")
	
