#!/usr/bin/env python
# coding: utf-8

# In[131]:


def player_choice(user):
    while user[1] != "r" and user[1] != "p" and user[1] != "s":
        user[1] = input(f"Hey {user[0]}, are you ready?? 3...2...1...GO! ").lower()
    return user[1]


# In[116]:


def computer_turn():
    
    import random
    
    options = ["r", "p", "s"] 
    return random.choice(options)


# In[117]:


def winner(user,computer_choice):
    if user[1] == computer_choice:
        print ("Wow! That's a tie!")
    elif user[1] == "r":
        if computer_choice == "s":
            user[3] += 1
            print ("Yeah! You won!")
        else:
            print ("Oh no! You lost!")
    elif user[1] == "p":
        if computer_choice == "r":
            user[3] += 1
            print ("Yeah! You won!")
        else:
            print ("Oh no! You lost!")
    elif user[1] == "s":
        if computer_choice == "p":
            user[3] += 1
            print ("Yeah! You won!")
        else:
            print ("Oh no! You lost!")


# In[127]:


def play_again():
    continue_play = ""
    while continue_play != "n" and continue_play != "y":
        
        continue_play =  input("\nWanna play again? Y/N ").lower()
        
    if continue_play == 'n':
        print ("See you next time!")
        return False
    else:
        return True


# In[122]:


def recap(user):
    win_rate = (user[3]/user[2])*100
    round(win_rate, 2)
    print (f"\nThank you for playing. Here are your stats:\nYou played {user[2]} game(s) and won {user[3]} game(s)\nYou won {win_rate}% of the games")


# In[136]:


# Define user with a list:
# user[0]: name
# user[1]: player_choice
# user[2]: games played
# user[3]: games won
user = ["","",0,0]

#Obtain the player name
user[0] = input("Welcome to Rock, Paper, Scissor! What's your name? ")
print (f"\nOk {user[0]} let's play! Type 'r' for rock, 'p' for paper and 's' for scissor")

#Play until keep_play stays True
keep_play = True
while keep_play == True:
    #Player choose rock (r) or paper (p) or scissor(s)
    player_choice(user)
    #Computer randomly choose rock (r) or paper (p) or scissor(s)
    computer_choice = computer_turn()
    print (f"The computer plays {computer_choice}")
    #Define the winner
    winner(user,computer_choice)
    #Increase the played games
    user[2] += 1
    #Ask if play again (y) or stop playing (n)
    keep_play = play_again() 
    #Reset the user choice
    user[1] = ""
    
#Show a recap of played and won game    
recap(user)


# In[ ]:




