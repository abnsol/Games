import random
import sys
chosen_numbers = random.sample(range(1, 10), 3)
def crack():
    count_positions=0
    count_numbers=0
    player=input("Input your code: ")
    player_list=[]
    for j in player:
        player_list.append(int(j))
    if len(player)!=3:
        print("Input 3 numbers")
        crack()
    for i in player_list:
        if i in chosen_numbers:
            count_numbers+=1
            if player_list.index(i)==chosen_numbers.index(i):
                count_positions+=1
    if count_numbers==len(player_list) and count_positions==len(player_list):
        print(f"Genius!🎉 you've cracked the code")
        sys.exit()
    elif count_numbers<len(player_list) or count_positions<len(player_list):
        print(f"{count_numbers} numbers and {count_positions} positions are correct. Try again!")
        crack()

print(crack())
