flag=0
x=0 
y=0
z=0
while not flag:
    command=input("> ").lower() # .lower() to make command in lower case.
    if command=="start":
        if x==1:
            print('already started')
            continue
        x +=1
        y=0
        print("Car Started...")
    elif command=="stop":
        if y==1:
            print("already stoped")
            continue
        y+=1
        x=0
        print("Car stoped...")
    elif command=="help":
        if z==1:
            print("you already get")
            continue
        z+=1
        print("""
start - to start the car
stop - to stop the car
quit - to quit
         """)
    elif command=="quit":
        break
    else:
         print("sorry i don't understand")
