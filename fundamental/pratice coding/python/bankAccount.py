balance = 0.0
def display():
    print(balance)
def deposit(value):
    global balance
    if value<0:
        print("invalid")
        return
    balance += value
def withdraw(value):
    global balance
    if(value<=0) or value>balance:
        print("invalid")
        return
    balance -= value

display()
deposit(500)
withdraw(100)
display()

def main():
    global balance
    withdraw(5000000)
    display()
main()
