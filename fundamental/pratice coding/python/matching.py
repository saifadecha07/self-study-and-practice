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

#capture pattern นำ service มาเเจกเเจงรายละเอียด 
service = 1000
match service :
    case 1 : print("ฝากเงิน")
    case 2 : print("ถอนเงิน")
    case None: print("Invalid input")
    case service : print(f"{service} ไม่อยู่ในบริการใน 1 2 None") #เอา service มาใช้ 

#guard filter 
#100 = สอบได้คะเเนนเต็ม 50-99ผ่าน     ****if+match
score = int(input("enter score(0-100)"))
print(f"{score}")
match score:
    case 100: 
        print("full")
    case score if 99>=score>=50: #เอา score มาใช้เเล้ว ใช้ IF statement 
        print("ผ่านเกณฑ์")
    case _:
        print("ไม่ผ่าน")

#OR pattern ใช้ | pipe กำหนด case หลายๆ เคสเชื่อมเคสด้วย OR operator 
data =input("enter ")   
match data:
    case "เด็กชาย" | "นาย":
        print("เพศชาย")
    case "เด็กหญิง" | "นาง" | "นางสาว":
        print("เพศหญิง")
    case _: 
        print("ไม่รู้")

#sequence pattern เกี่ยวกับลำดับ list tuple
data = []
match data:
    case []:
        print("empty")
    case [1,2]:
        print("2")

