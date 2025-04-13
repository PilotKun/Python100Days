
#*Scope

# enemies = 1

# def increase_enimes():
#     enemies = 2
#     print(f"enimes inside function: {enemies}")

# increase_enimes()
# print(f"enemies outside function: {enemies}")

#*Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

#*Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#         drink_potion()

# print(player_health)

#* There is no block scope

# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

#* Modifying Glbobal scope

# enemies = 1

# def increase_enemies():
#     # enemies += 1
#     print(f"enimes inside function: {enemies}")
#     return enemies +1

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#* Global Constants

# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@pilot_kun"

