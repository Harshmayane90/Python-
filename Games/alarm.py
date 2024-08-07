z=input("Enter the day: ")
b=int(input("Enter the Minute: "))
a=int(input("Enter the Hour: "))
def day_fun():
        print()

while True:
       if z in['Monday',"Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]:
            break
       else:
            print("Inavalid input")
            break

while True:
     if a in range(0,25):
          print()
     else:
          print("Invalid input ")

     if b in range(00,61):
          print()
          break
     else:
          print("Invalid Input ") 
print(f"Alarm is set :{z}/{a}/{b}am")   
day_fun()