#!python3
"""
##### Task 5
create a dictionary for an inventory of items in a game.  
Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  
If they choose to drop item' remove that item from that invenory.  
If they choose 'show inventory' give them a list of the items that they have.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)

possible items:
food
water
rope
torch
sack
wood
iron
steel
ginger
garlic
fish
stone
wool

example:
>get food
>get water
>get water
>get iron
>get 3 wood
>inventory
You have:
 1 food
 2 water
 1 iron
 3 wood
 >
"""
inventory = {"food" : 0,"water" : 0,"rope" : 0,"torch" : 0,"sack" : 0,"wood" : 0,"iron" : 0,"steel" : 0,"ginger" : 0,"garlic" : 0,"fish" : 0,"stone" : 0,"wool" : 0}
while True:
    playerinput = input("Enter your command, type help for list of commands: ")
    playerinput = playerinput.split(" ")
    #print(playerinput)
    
    if playerinput[0] == "help":
        print("To play type the action, then you can type the amount or leave blank for 1\nThe items in the game are: food, water, rope, torch, sack, wood, iron, steel, ginger, garlic, fish, stone, wool\nThe actions in the game are: get = get an item, drop = drop an item, inventory (inv) = show inventory") 
    
    elif playerinput[0] == "inventory" or playerinput[0] == "inv":
        check = 0
        for i in inventory:
            if inventory[i] == 0:
                pass
            else:
                print(f"You have {inventory[i]} {i}")
                check = 1
        if check == 0:
            print("You have no items")
    elif playerinput[0] == "get":
        
        if playerinput[1].isdigit():
            try:
                for i in inventory:
                    if playerinput[2] == i:
                        #print(inventory[i])
                        inventory[i] = (inventory[i] + int(playerinput[1]))
            except Exception as e:
                print(f"Error: {e}")
        else:
            try:
                for i in inventory:
                    if playerinput[1] == i:
                        inventory[i] = (inventory[i] + 1)
            except Exception as e:
                print(f"Error: {e}")
    elif playerinput[0] == "drop":
        if playerinput[1].isdigit():
            try:
                for i in inventory:
                    if playerinput[2] == i:
                        #print(inventory[i])
                        inventory[i] = (inventory[i] - int(playerinput[1]))
                        if inventory[i] < 0:
                            inventory[i] = 0
            except Exception as e:
                print(f"Error: {e}")
        else:
            try:
                for i in inventory:
                    if playerinput[1] == i:
                        inventory[i] = (inventory[i] - 1)
                        if inventory[i] < 0:
                            inventory[i] = 0
            except Exception as e:
                print(f"Error: {e}")