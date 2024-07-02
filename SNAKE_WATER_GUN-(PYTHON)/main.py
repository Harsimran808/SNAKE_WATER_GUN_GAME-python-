# Snake Water and Gun game

# Randomly computer choose between Snake, Water or Gun
import random
computer_choice=random.choice([1,2,3])

# number of rounds to play 
rounds=1
rounds_entered=int(input("Enter number of rounds :"))

# user points and computer points
user_points=0
computer_points=0

# conditions for winning and losing
while(rounds<=rounds_entered):

    # Taking input from the user 
    user_choice=int(input("Enter your choice :\n1. for Snake\n2. for Water\n3. for Gun\n "))
    game_dict={ 1: "Snake"  , 2:  "Water"  , 3 : "Gun" }


    # to store the value of key in variable i.e 1 stores snake , 2 stores water and 3 stores gun 
    you_choose=game_dict[user_choice]
    computer_choose=game_dict[computer_choice]

    # printing computer and your choice
    print(f"Computer choose {computer_choose} and you choose {you_choose}")

    if(computer_choice == user_choice):
        print("It's a draw")
        rounds+=1
        
    else:

        if(computer_choice == 1 and user_choice == 2):
            print("Snake's drink the water")
            print("You lose!\n")
            rounds+=1
            computer_points+=1


        elif(computer_choice == 1 and user_choice == 3):
            print("Gun shoots the snake")
            print("You won!\n")
            rounds+=1
            user_points+=1


        elif(computer_choice == 2 and user_choice == 1):
            print("Snake's drink the water")
            print("You won!\n")
            rounds+=1
            user_points+=1

        elif(computer_choice == 2 and user_choice == 3):
            print("Water drowns the gun")
            print("You lose!\n")
            rounds+=1
            computer_points+=1

        elif(computer_choice == 3 and user_choice == 1):
            print("Gun shoots the snake")
            print("You lose!\n")
            rounds+=1
            computer_points+=1

        elif(computer_choice == 3 and user_choice == 2):
            print("Water drowns the gun")
            print("You won!\n")
            rounds+=1
            user_points+=1

        else:
            print("Their is a problem")

# printing user and computer points out of rounds completed
print(f"\nYour score is {user_points} and computer score is {computer_points}")