#literal pattern
service = None
match service :
    case 1 : print("ฝากเงิน")
    case 2 : print("ถอนเงิน")
    case None: print("Invalid input")

#wildcard pattern ไม่ตรงกับเคสไหนเลย
service = 1000
match service :
    case 1 : print("ฝากเงิน")
    case 2 : print("ถอนเงิน")
    case None: print("Invalid input")
    case _: print("default") #defualt case 

