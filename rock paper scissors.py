# 0 for rock
# 1 for paper
# 2 for scissors
# paper> rock, scissors>paper, rock>scissors
import random
print('0 for rock'+'\n'+'1 for paper'+'\n'+'2 for scissors')
user= int(input('enter your choice: '))
game=['Rock','Paper','Scissors']
selected_index=random.randint(0,2)
print("you chose",game[user])
print("computer chose",game[selected_index])
if user == selected_index :
    print("It's a tie")

else:
    if (user == 0 and selected_index == 2)or(user == 2 and selected_index == 0):
         print('Rock wins against scissors')
         if (user == 0):
            print('YOU WIN')
         else:
            print('YOU LOOSE')

    elif  user> selected_index :
        print(f"{game[user]} wins against {game[selected_index]}")
        print('YOU WIN')
    else:
         print(f"{game[selected_index]} wins against {game[user]}")
         print('YOU LOOSE')
