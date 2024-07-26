import images

room1doorOpen=False
space= "\n\n"
prev=""
safeopen=False
key=False
escaped=False

while True:
    
    print(images.room1_middle)
    print(space)
    
    direction=input("Enter: ").lower()
    
    if direction== "r":
        if safeopen == False:
            print(images.room1_safe_closed)
            pw = input("Enter: ")
            print(space)

            if pw == "3N" or pw == "3n":
                safeopen= True
                key=True
                print(images.room1_safe_open)

            else:
                print("\t\t\t\tINCORRECT PASSWORD")
                print(space)
                pw = input("Enter:")


    elif direction== "l":

        print(images.room1_matrix)
        print(space)

        direction= input("Enter:  ").lower()

    elif direction=="f":
        
        while True:
            if room1doorOpen:

                        print(images.room1_door_open)
                        print(space)
                        direction= input("Enter:  ").lower()

                        if direction== "f":
                            escaped=True
                            print(images.escaped)
                            print(space)
                            break

                        else:
                            continue
                
            else:

                while True:

                    print(images.room1_door_closed)
                    print(space)
                        
                    key = input("Enter: ").lower()
                        
                    if key == True:
                            
                        room1doorOpen = True
                        print(images.room1_door_open)
                        print(space)
                    
                        direction= input("Enter:  ").lower()

                        if direction== "f":
                            
                            escaped=True
                            print(images.escaped)
                            print(space)
                            break
                    
                        else:
                            break
                        

        if escaped:
            break
        else:
            continue
