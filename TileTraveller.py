#We start by making 2 variables one that keeps track of how high the user is and another that keeps track of how much to the sides he goes
#Lets call them H and W and start them both at 1
#We use a while loop so the game continues to run until he hits tile W3 and H1
#At any point if his W is 1 he can only travel east, if its 3 he can only travel west and if it is 2 he can travel both ways
#If his H is 1 he can only travel north and if it is 3 he can only travel south, if it is 2 he can travel both ways
#Make sure the users input always get interpreted as a lowercase letter
#Lets make a function to control his movements
#We make restrictions for the middle boxes and the directions he cannot go
#We end the game when he hits W3 H1

h=1
w=1



north = "(N)orth"
south = "(S)outh"
east = "(E)ast"
west = "(W)est"

user_question = "You can travel:{}{}{}{}".format(north, east, west, south)

error = False
print(user_question)
player_move=input("Direction: ").lower()



def error(str):
    if h >= 3 and str == "n":
        error = True
    elif h <= 1 and str == "s":
        error = True
    elif w >= 3 and str == "e":
        error = True
    elif w <= 1 and str == "w":
        error = True
    else:
        error = False
    return(error)


def movement(str):
    h=1
    w=1
    if player_move == "n":
        h += 1
    elif player_move == "s":
        h -= 1
    elif player_move == "e":
        w += 1
    elif player_move == "w":
        w -= 1




while (h == 1 or h == 2) and (w == 1 or w ==2):
    error = error(player_move)
    if error:
        print("Not a valid direction!")
    elif not error:
        movement(player_move)
    print(user_question)
    player_move = input("Direction: ").lower()



