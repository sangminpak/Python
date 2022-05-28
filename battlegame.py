wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"


play = True
while play:
    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 170

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 10

    dragon_hp = 300
    dragon_damage = 50

    my_hp = 0
    my_damage = 0
    while play:
        print("1) Wizard\n2) Elf\n3) Human\n4) Orc")
        character = input("Choose your character(Enter X to exit the game): ")
        if character == "1" or character.lower() == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            play = True
            break
        elif character == "2" or character.lower() == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            play = True
            break
        elif character == "3" or character.lower() == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            play = True
            break
        elif character == "4" or character.lower() == "orc":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            play = True
            break
        elif character.lower() == "x":
            play = False
            break
        else:
            print("Unknown character.")

    if character.lower() != "x":
        print("You have chosen the character: ", character)
        print("Health: ", my_hp)
        print("Damage: ", my_damage)
        print("===================================")

    while play:
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now: ", dragon_hp, "\n")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break
        my_hp = my_hp - dragon_damage
        print("The Dragon damaged the", character, end="")
        print("!")
        print("The", character, end='')
        print("'s hitpoints are now:", my_hp, "\n")
        if my_hp <= 0:
            print("The", character, "has lost the battle.")
            break

    end = input("Would you like to play again? Y or N: ")
    if end.lower() == "y":
        play = True
    else:
        break

if character.lower() == "x":
    print("Goodbye.")
