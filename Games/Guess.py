
lst=['harsh','python','Gta-5','sumago','vivo']
 

print("--------Hint for guessing game-----------")
print(1,"your name")
print(2,"Your programing language")
print(3,"your favoritr game")
print(4,"your institue")
print(5,"Your mobile")

def guess():
    
    ch=int(input("Enter your choice: "))
    while True:
        if ch==0:
            1
        elif ch==2:
            2
        elif ch==3:
            3
        elif ch==4:
            4
        break

def choice_1():
    guess()
    n=input("Enter the word: ")
    

    if n==lst[0]:
        print(f"Enter word is correct: {lst[0]}")
    elif n==lst[1]:
        print(f"Entered word is correct: {lst[1]}")
    elif n==lst[2]:
        print(f"Enterd word is correct :{lst[2]}")
    elif n==lst[3]:
        print(f"Entered word is correct: {lst[3]}")
    elif n==lst[4]:
        print(f"ented word is correct : {lst[4]}")
    else:
        print("Enterd word is Incorrect")
            
choice_1()
