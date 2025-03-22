lst = []

def display_options():
    print("1. Push into the stack.")
    print("2. Pop from the stack.")
    print("3. Display Stack items.")


def push():
    val = int(input("Please enter a value to push: "))
    lst.append(val)

def pop():
    popped = lst.pop()
    print(f"{popped} is poped from the stack.")

def display():
    if(len(lst)>0):
        for i in range(len(lst)):
            print(str(lst[i]) + "\t",end=" ")

def main():
   
    while True:
        print("\n")
        print("******** Select one of the options***********")
        display_options()
        choice = int(input("Please choose an option: "))
        if(choice == 1):
            push()
        elif(choice == 2):
            pop()
        elif(choice == 3):
            display()
        else:
            print("Invalid Choice")

main()       
