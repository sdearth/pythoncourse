################### Scope ####################

enemies = 1

#convention for constants is all uppercase names
PI = 3.14159

def increase_enemies():
  #this would create a local variable 
  #enemies = 2
  #this would access the global scope enemies variable
#   global enemies
#   enemies += 1
    return enemies + 1
 

increase_enemies()
print(f"enemies outside function: {increase_enemies()}")

#There is no block scope in python
enemies = ["Skeletons", "zombies", "Alien"]
game_level = 3

def create_enemy():
    if game_level < 5:
        #this isn't a block scope
        new_enemy = enemies[0]
    print(new_enemy)