import images
room3dooropen = False
escaped = False
miniroom_dooropen = False
newln = "\n\n"

while True:

    print(images.room3_middle)
    print(newln)

    direction=input("Enter: ").lower()

    if direction == "l":

        print(images.room3_left_synonym_wall)
        print(newln)

        direction=input("Enter: ").lower()

    elif direction == "r":

        while True:

            print(images.room3_miniroom_door_open)
            print(newln)
            direction=input("Enter: ").lower()

            if direction == "b":
                
                print(images.room3_middle)
                direction=input("Enter: ").lower()
                break

            elif direction == "f":

                print(images.room3_miniroom_maze)
                print(newln)
                direction=input("Enter: ").lower()
        break

    elif direction == "f":

        while True:
            if room3dooropen == False:

                print(images.room3_front_door_closed)
                print(newln)
                key = input("Enter key: ").lower()

                if key == "shiny":

                    room3dooropen = True
                    print(images.room3_front_door_open)
                    print(newln)
                    print(images.escaped)
                    print(newln)
                    break

                elif key == "b":

                    break
                
                else:

                    print(newln)
                    print("INCORRECT KEY")

            elif room3dooropen == True:

                print(images.room3_front_door_open)
                print(newln)
                print(images.escaped)
                print(newln)
                break
    
    if escaped:
        break
    else:
        continue



            


        
