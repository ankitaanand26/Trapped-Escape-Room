import images

room2doorOpen=False
space= "\n\n"
prev=""
phoneUnlocked=False
escaped=False

while True:
    
    print(images.room2_middle)
    print(space)
    
    direction=input("Enter: ").lower()
    
    if direction== "r":
        
        while True:

            print(images.room2_table)       
            print("""Choose an object:
            1- Vase
            2- Candle
            3- Phone
            """)
            tablech=input("Enter: ")

            if tablech=="1":
            
                print(images.room2_vase)
                print(space)
                direction= input("Enter:  ").lower()
                continue

            elif tablech=="2":

                
                print(images.room2_candle)
                print(space)
                direction= input("Enter:  ").lower()
                continue
            
            elif tablech=="3":
                

                if phoneUnlocked:

                    print(images.room2_phone_unlocked)
                    print(space)
                    direction= input("Enter:  ").lower()
                    continue
                
                else:

                    while True:

                        print(images.room2_phone_locked)
                        print(space)
                        
                        password = input("Enter: ")
                        
                        if password == "35":
                            
                            phoneUnlocked = True
                            print(images.room2_phone_unlocked)
                            direction= input("Enter:  ").lower()
                            break

                        elif password=='b':
                            break

                        else:

                            print(space)
                            print("\t\t\t\t\INCORRECT PASSWORD")
                            
            elif tablech=="b":
                break

            else:
                continue
            

    elif direction== "l":

        print(images.room2_wordpuz)
        print(space)

        direction= input("Enter:  ").lower()

    elif direction=="f":
        
        while True:
            if room2doorOpen:

                        print(images.room2_door_open)
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

                    print(images.room2_door_closed)
                    print(space)
                        
                    key = input("Enter: ").lower()
                        
                    if key == "happy":
                            
                        room2doorOpen = True
                        print(images.room2_door_open)
                        print(space)
                    
                        direction= input("Enter:  ").lower()

                        if direction== "f":
                            
                            escaped=True
                            print(images.escaped)
                            print(space)
                            break
                    
                        else:
                            break
                    
                    elif key == "b":
                        break

                    else:

                        print(space)
                        print("\t\t\t\tINCORRECT KEY")
                        
                break

        if escaped:
            break
        else:
            continue
