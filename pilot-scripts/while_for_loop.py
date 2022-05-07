number = 9
player_opinion = input("Do you wish to play? (Y/n): ")

while player_opinion != "n":
    player_guess = int(input("Enter a number: "))
    if player_guess == number:
        print("You guessed it right")
    elif abs(player_guess - number) == 1:
        print("You missed it by 1")
    else:
        print("You guessed it wrong")

    player_opinion = input("Do you wish to play? (Y/n): ")

# The same can be executed as below
# while True:

another_number = 7
while True:
    second_game_check = input("Do you wish to guess another number? (Y/n): ")
    if second_game_check == "n":
        break
    player_guess = int(input("Enter a number: "))
    if player_guess == another_number:
        print("You guessed it right")
    elif abs(player_guess - another_number) == 1:
        print("You missed it by 1")
    else:
        print("You guessed it wrong")

movies_seen = {"up", "red", "conair", "matrix", "independence"}
for movie in movies_seen:
    print(movie)

# We can also use range ust to iterate for a certain number of times
for i in range(10):
    print(i)