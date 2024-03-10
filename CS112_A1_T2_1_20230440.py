# File: CS112_A1_T2_1_20230440
# Purpose: 100 game, Who reaches 100 first is the winner
# Name: Nada Amin Fawzy Mohamed
# ID: 20230440


def game():
    count = 0
    while count < 101:
        # Check validation of player1's input
        while True:
            player1 = input("*Player1* Enter a number from 1 to 10: ")
            # If player1 enters a non integer input, it'll ask him to enter a valid option
            try:
                player1 = int(player1)
                # Make sure that player1 enters a number in the range
                if player1 > 10 or player1 < 1:
                    continue
                count += player1
                # Make sure that the total doesn't exceed 100
                if count > 100:
                    print("You exceeded 100, Please enter a valid number to reach 100")
                    count -= player1
                    continue
                break
            except ValueError:
                print("Enter a valid option please!\n")
        # Condition of the winning of player1
        if count == 100:
            print("You reached", count)
            print("***Player 1 is the winner!😍***")
            break
        print(f"The total = {count} \n======================")

        # Check validation of player2's input
        while True:
            player2 = input("*Player2* Enter a number from 1 to 10: ")
            # If player2 enters a non integer input, it'll ask him to enter a valid option
            try:
                player2 = int(player2)
                # Make sure that player2 enters a number in the range
                if player2 > 10 or player2 < 1:
                    continue
                count += player2
                # Make sure that the total doesn't exceed 100
                if count > 100:
                    print("You exceeded 100, Please enter a valid number to reach 100")
                    count -= player2
                    continue
                break
            except ValueError:
                print("Enter a valid option please!\n")
        # Condition of the winning of player2
        if count == 100:
            print("You reached", count)
            print("***Player 2 is the winner!😍***")
            break
        print(f"The total = {count} \n======================")


print("******** Welcome to the 100 game ********\n--------------------------------------------------------------------")
print("Each player will take turns by choosing a number from 1 to 10 and the numbers will be added to the total")
print("The player which make the total reach 100 first wins, so play until one is a winner!")
print("--------------------------------------------------------------------")
game()
# Ask the user if he wants to play again
while True:
    play_again = input("\nDo you want to play again (yes or no)? ").lower()
    if play_again == "yes":
        print()
        game()
    elif play_again == "no":
        input("\nClick enter to exist the game...")
        break
    else:
        continue
