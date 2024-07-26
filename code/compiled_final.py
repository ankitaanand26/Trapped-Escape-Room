import images

room2doorOpen=False
space= "\n\n"
phoneUnlocked=False
escaped=False
room1,room2,room3= True, False, False
room3doorOpen = False
escaped = False
miniroom_dooropen = False
room1doorOpen=False
safeopen=False
key=False

print(images.prompt)
print(space)
input("Type anything to begin:")

#import only system from os
from os import system, name

#defining clear function
def clear():

    #for windows
    if name== 'nt':
        _=system('cls')


    #for mac and linux
    else:

        _= system('clear')


while True:
    #to check which level cleared by user
    if room1 and not room2 and not room3:
        clear()
        print(images.room1_middle)

    elif room2 and not room3:
        clear()
        print(images.room2_middle)

    elif room3:
        clear()
        print(images.room3_middle)

    print(space)
    direction=input("Enter: ").lower()
    #To go right
    if direction== "r":
        #Displaying right object of room 1
        if room1 and not room2 and not room3:
            
            clear()
            
            if safeopen:

                clear()
                print(images.room1_safe_open)
                print(space)
                direction= input("Enter:  ").lower()
                continue
                
            else:

                while True:

                    print(images.room1_safe_closed)
                    print(space)
                        
                    password = input("Enter: ")
                    #To make case-insensitive    
                    if password == "3N" or password== "3n":
                            
                        safeopen = True
                        room1doorOpen=True #Key given on opening safe
                        clear()
                        print(images.room1_safe_open)
                        print(space)
                        direction= input("Enter:  ").lower()
                        break

                    elif password=='b':
                        break

                    else:

                        clear()
                        print(space)
                        print("\t\t\t\tINCORRECT PASSWORD")

        #Displaying right object of room 2
        elif room2 and not room3:

            while True:

                clear()
                print(images.room2_table)       
                print("""Choose an object:
                1- Vase
                2- Candle
                3- Phone
                """)
                print(space)
                #Inputting object choice on table
                tablech=input("Enter: ") 

                if tablech=="1":
                    
                    clear()
                    print(images.room2_vase)
                    print(space)
                    direction= input("Enter:  ").lower()
                    continue

                elif tablech=="2":

                    clear()
                    print(images.room2_candle)
                    print(space)
                    direction= input("Enter:  ").lower()
                    continue
            
                elif tablech=="3":

                    clear()

                    if phoneUnlocked:

                        clear()
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
                            
                                clear()
                                phoneUnlocked = True
                                print(images.room2_phone_unlocked)
                                print(space)
                                direction= input("Enter:  ").lower()
                                break
                            #To go back to table view
                            elif password=='b':
                                break

                            else:

                                clear()
                                print(space)
                                print("\t\t\t\tINCORRECT PASSWORD")
                            
                elif tablech=="b":
                    break

                else:
                    continue
        #Displaying right object of room 3
        elif room3:

            while True:

                clear()
                print(images.room3_miniroom_door_open)
                print(space)
                direction=input("Enter: ").lower()

                if direction == "b":
                    break

                elif direction == "f":

                    clear()
                    print(images.room3_miniroom_maze)
                    print(space)
                    direction=input("Enter: ").lower()

                
            

            
    #To go left
    elif direction== "l":
        #Displaying left object of room 1
        if room1 and not room2 and not room3:

            clear()
            print(images.room1_matrix)
            print(space)
        #Displaying left object of room 2
        if room2 and not room3:

            clear()
            print(images.room2_wordpuz)
            print(space)
        #Displaying left object of room 3
        elif room3:

            clear()
            print(images.room3_left_synonym_wall)
            print(space)

        direction= input("Enter:  ").lower()


#To go front
    elif direction=="f":
        #Displaying front object of room 1
        if room1 and not room2 and not room3:

            if room1doorOpen:

                clear()
                print(images.room1_door_open)
                print(space)

                direction= input("Enter:  ").lower()

                if direction== "f":
                    room2=True

                else:
                    continue

            else:

                clear()
                print(images.room1_door_closed)
                print(space)

                direction= input("Enter:  ").lower()
        #Displaying front object of room 2
        elif room2 and not room3:
        
            while True:

                if room2doorOpen:

                            clear()
                            print(images.room2_door_open)
                            print(space)
                            direction= input("Enter:  ").lower()

                            if direction== "f":
                                room3=True
                                break

                            else:
                                continue
                
                else:

                    clear()

                    while True:

                        print(images.room2_door_closed)
                        print(space)
                        
                        key = input("Enter: ").lower()
                        #Inputting key for room 2 front door
                        if key == "happy":
                            
                            clear()
                            room2doorOpen = True
                            print(images.room2_door_open)
                            print(space)
                    
                            direction= input("Enter:  ").lower()

                            if direction== "f":
                            
                                room3=True
                                print(space)
                                break
                    
                            else:
                                break
                    
                        elif key == "b":
                            break

                        else:

                            clear()
                            print(space)
                            print("\t\t\t\tINCORRECT KEY")
                        
                    break
        #Displaying front object of room 3
        elif room3:

            while True:
                if room3doorOpen:

                            clear()
                            print(images.room3_front_door_open)
                            print(space)
                            direction= input("Enter:  ").lower()
                            
                            if direction== "f":
                                escaped=True
                                clear()
                                print(images.escaped)
                                input()
                                break

                            else:
                                continue
                
                else:

                    clear()

                    while True:

                        print(images.room3_front_door_closed)
                        print(space)
                        
                        key = input("Enter: ").lower()
                        #Inputting key for room 3 front door
                        if key == "shiny":
                            
                            clear()
                            room3doorOpen = True
                            print(images.room3_front_door_open)
                            print(space)
                    
                            direction= input("Enter:  ").lower()

                            if direction== "f":
                            
                                escaped=True
                                clear()
                                print(images.escaped)
                                print(space)
                                input()
                                break
                    
                            else:
                                break
                    
                        elif key == "b":
                            break

                        else:

                            clear()
                            print(space)
                            print("\t\t\t\tINCORRECT KEY")
                        
                    break


    #Checking image to display when b chosen
    elif direction=="b":

        if room1 and not room2 and not room3:
            clear()
            print(images.room1_middle)
            print(space)

        elif room2 and not room3:
            clear()
            print(images.room1_middle)
            print(space)
            room2=False
            
        elif room3:
            clear()
            print(images.room2_middle)
            print(space)
            room3= False


    if escaped:
        input()
        break
    else:
        continue
