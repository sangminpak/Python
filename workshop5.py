import random


def setup():
    global tries
    global start
    global stop

    tries = int(input("Enter a number of tries: "))
    start = int(input("Enter the start number: "))
    stop = int(input("Enter the stop number: "))


def guess_random_number(tries, start, stop):
    target_num = random.randint(start, stop)
    while tries != 0:
        print("Number of  tries remaining:", tries)
        guess = int(input(f"Guess a number between {start} and {stop}: "))
        if guess == target_num:
            print("Success!")
            return
        elif start <= guess <= stop and guess < target_num:
            print("Guess higher!")
        elif start <= guess <= stop and guess > target_num:
            print("Guess lower!")
        else:
            print("Enter a valid number")
        tries -= 1
    print("Your program has failed to guess the number:", target_num)


def guess_random_num_linear(tries, start, stop):
    target_num = random.randint(start, stop)
    print("The number for the program to guess is:", target_num)
    for x in range(start, stop+1):
        if tries == 0:
            print("You have failed to guess the number.")
            return
        print("Number of tries left:", tries)
        print("The program is guessing...", x)
        tries -= 1
        if x == target_num:
            print("Success!")
            return


def guess_random_num_binary(tries, start, stop):
    target_num = random.randint(start, stop)
    lower_bound = start
    upper_bound = stop

    print("The number for the program to guess is:", target_num)

    while lower_bound <= upper_bound:

        if tries == 0:
            print("Your program has failed to guess the number.")
            return

        pivot = (lower_bound + upper_bound) // 2

        if pivot == target_num:
            print("Found it!", pivot)
            return pivot
        elif pivot > target_num:
            print("Guessing lower!")
            # target is in the left side because it's smaller than pivot; so upper bound adjusts so that it's one less than pivot.
            upper_bound = pivot - 1
        else:
            (print("Guessing higher!"))
            # target is in the right side, so the lower bound increases to pivot + 1
            lower_bound = pivot + 1
        tries -= 1
        # if the target value is not found, lower bound will be higher than upper bound and it exits the loop
    return -1


#guess_random_number(5, 0, 10)
#guess_random_num_linear(5, 0, 10)
# setup()
#guess_random_num_binary(tries, start, stop)

player_money = 10


while player_money != 0 or player_money > 50:
    while True:
        player_guess = input(
            "Do you think the program will guess the correct number? Y or N: ")
        if player_guess.lower() == "y" or player_guess.lower() == "n":
            break
        else:
            print("Enter valid answer.")

    while True:

        bet = int(input("How much do you want to bet? Choose between $1 - $10: "))
        if bet <= player_money:
            break
        if bet > player_money:
            print("You cannot bet more than you have.")

    return_val = guess_random_num_linear(5, 0, 10)
    if return_val == True:
        if player_guess.lower() == "y":
            player_money += bet
            bet *= 2
            print("You guessed correctly!")
            print("Your bet is now $" + str(bet))
            print("Your current money is: $" + str(player_money))

        else:
            print("You guessed incorrectly.")
            player_money -= bet
            print("Your current money is: $" + str(player_money))
    else:
        if player_guess.lower == "n":
            player_money += bet
            bet *= 2
            print("You guessed correctly!")
            print("Your bet is now $" + str(bet))
            print("Your current money is: $" + str(player_money))
        else:
            print("You guessed incorrectly.")
            player_money -= bet
            print("Your current money is: $" + str(player_money))

print("Game over.")
