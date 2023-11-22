

#Import Easygui function so gui can be created 2
#import easygui
from tkinter import *


Grand_Final_MIN = 8
Grand_Final_MAX = 21
Trivia_Grand_Final = 10
MAX_QUESTION_ATTEMPTS = 2

#Ask the user's NRL Team - String Variable
title = "Welcome to the NRL Trivia"
msg = "What is your NRL Team?"
NRL_Team = ""

#Ask the user how many Grand Finals they've won - Numeric Variable
while   NRL_Team == "":
        NRL_Team = easygui.enterbox(msg, title, "")

title = "Welcome to the NRL Start Trivia"
msg = "How many Grand Finals has your team won?"

#Check the Grand Final criteria for playing the Trivia. Also checks if the player has entered an integer within a valid Grand Final range. The loop repeats until a valid integer is entered. - Iteration
Grand_Final = easygui.integerbox(msg, title, "")
while Grand_Final < Grand_Final_MIN or Grand_Final > Grand_Final_MAX:
        msg = "Please enter a valid amount of Grand Finals from " + str (Grand_Final_MIN) + " to " + \
        str(Grand_Final_MAX) + " Grand Finals."
        Grand_Final = easygui.integerbox(msg, title, "")

#Checks whether the player falls within the Trivia Grand Final range
continue_game = "Continue"
if Grand_Final >= Trivia_Grand_Final:
        print (Grand_Final)
        msg = "This Trivia is intended for Teams with 8 to 21 Grand Final Championships."
        choices = ["Continue", "Quit"]
        continue_game = easygui.buttonbox(msg, title, choices=choices)
        print (continue_game)

#This is the gate to check whether the quiz should continue because either the user has earlier indicated they are under the Trivia Grand Final, or they want to continue even though they are older.
if continue_game == "Continue":
        title = "Welcome to the NRL Trivia"
        msg = "Hey " + NRL_Team + "! Just before we start, the only rule is that you are not allowed to search up the answers. If you do not know the answer, just take a guess or try really hard to remember it. Anyways, enjoy the Trivia and may the best team win."
        ok_button = "Start"
        easygui.msgbox(msg, title, ok_button)


#Setup questions and answers for players - Data stored in List
questions_a = ["Who won the 2010 Grand Final?\n\nA: Storms\nB: Sydney Roosters\nC: Cowboys\nD:ST George Illawarra Dragons\n","How many teams are there in the NRL?\n\nA: 15\nB: 14\nC: 16\nD: 17\n","Who is the current hooker that plays for the Rabbitohs?\n\nA: Harry Grant\nB: Damien Cook\nC: Api Koroisau\nD: Brandon Smith\n","Which person has played for 3 different teams?\n\nA: Josh Addo - Carr\nB:James Tedesco\nC: Brian To'o\nD: Latrell Mitchel\n","Who is the Coach for the Parramatta Eels?\n\nA: Wayne Barrett\nB: Brad Arthur\nC: Ricky Stuart\nD: Anthony Griffin\n","How many points is a try worth?\n\nA: 5\nB: 6\nC: 4\nD: 7\n","How many meters on a full NRL field?\n\nA: 110\nB: 10\nC: 100\nD: 1000\n","What happens if someone drops the ball?\n\nA: Drop Kick\nB: Foward Pass\nC: Knock On\nD: Double Dribble\n","Who has scored the most points in one game?\n\nA: Trent Robbinson\nB: Dave Brown\nC: Nathan Cleary\nD: Josh Papali'i\n","Which is the best NRL team?\n\nA: Rabbitohs\nB: Rabbitohs\nC:Rabbitohs\nD: All of the above\n"]

#Setup answers to the multiple questions - Data stored in List
answers_a=["D","C","B","A","B","C","C","C","B","A"]

#Set Question score to zero to start the Program with no score - Data stored in List
q_score=0

#Question 1 - Selection
player_trivia = easygui.buttonbox(questions_a[0],"Questions 1",choices= ["A","B","C","D"])
if player_trivia == answers_a[0]:
        easygui.msgbox("WOW, " + NRL_Team + "! " + " Good Job!")
        q_score = q_score + 1
else:
        q_response = easygui.msgbox("WOW, " + NRL_Team + " ! Guess your not winning this year.\nThe correct answer is " + answers_a[0])

#Question 2 - Selection
player_trivia = easygui.buttonbox(questions_a[1],"Questions 2",choices= ["A","B","C","D"])
if player_trivia == answers_a[1]:
        easygui.msgbox("Fantastic, " + NRL_Team + "! " + " Doing Great!")
        q_score = q_score + 1
else:
        q_response = easygui.msgbox("ERR ERRRRRRRR, " + NRL_Team + "!Wrong one.\nThe correct answer is " + answers_a[1])

#Question 3 - Selection
player_trivia = easygui.buttonbox(questions_a[2],"Questions 3",choices= ["A","B","C","D"])
if player_trivia == answers_a[2]:
        easygui.msgbox("Amazing, " + NRL_Team + "! " + " Keep it up!")
        q_score = q_score + 1
else:
        q_response = easygui.msgbox("Nope, " + NRL_Team + "! Wrong again.\nThe correct answer is " + answers_a[2])

#Question 4 - Selection
player_trivia = easygui.buttonbox(questions_a[3],"Questions 4",choices= ["A","B","C","D"])
if player_trivia == answers_a[3]:
        easygui.msgbox("Outstanding, " + NRL_Team + "! " + " You're on a roll")
        q_score = q_score + 1
else:
        q_response = easygui.msgbox("Really?, " + NRL_Team + "! That one was easy.\nThe correct answer is " + answers_a[3])

#Question 5 - Selection
player_trivia = easygui.buttonbox(questions_a[4],"Questions 5",choices= ["A","B","C","D"])
if player_trivia == answers_a[4]:
        easygui.msgbox("Impossible, " + NRL_Team + "! " + " Let's see if you make it to the finals")
        q_score = q_score + 1
else:
        q_response = easygui.msgbox("Come on, " + NRL_Team + "! Unlucky.\nThe correct answer is " + answers_a[4])

#Question 6 - Selection
player_trivia = easygui.buttonbox(questions_a[5],"Questions 6",choices= ["A","B","C","D"])
if player_trivia == answers_a[5]:
        easygui.msgbox("That's Crazy, " + NRL_Team + "! " + " Almost there")
        q_score = q_score + 1
else:
        q_response = easygui.msgbox("Wrong, " + NRL_Team + "! Guess you had a bad game.\nThe correct answer is " + answers_a[5])

#Question 7 - Selection
player_trivia = easygui.buttonbox(questions_a[6],"Questions 7",choices= ["A","B","C","D"])
if player_trivia == answers_a[6]:
        easygui.msgbox("ALL RIGHT, " + NRL_Team + "! " + " That was a fluke")
        q_score = q_score + 1
else:
        q_response = easygui.msgbox("NO WAY, " + NRL_Team + "! Are you serious.\nThe correct answer is " + answers_a[6])

#Question 8 - Selection
player_trivia = easygui.buttonbox(questions_a[7],"Questions 8",choices= ["A","B","C","D"])
if player_trivia == answers_a[7]:
        easygui.msgbox("Let's go, " + NRL_Team + "! " + " 2 more to go")
        q_score = q_score + 1
else:
        q_response = easygui.msgbox("Come on now, " + NRL_Team + "! NO NO NO.\nThe correct answer is " + answers_a[7])

#Question 9 - Selection
player_trivia = easygui.buttonbox(questions_a[8],"Questions 9",choices= ["A","B","C","D"])
if player_trivia == answers_a[8]:
        easygui.msgbox("OK, " + NRL_Team + "! " + " That one was easy")
        q_score = q_score + 1
else:
        q_response = easygui.msgbox("WOW, " + NRL_Team + "! Guess your not winning this year.\nThe correct answer is " + answers_a[8])

#Question 10 - Selection
player_trivia = easygui.buttonbox(questions_a[9],"Questions",choices=["A","B","C","D"])
if player_trivia == answers_a[9]:
        easygui.msgbox("Perfect pick, " + NRL_Team + "! " + " I always knew you were a Rabbitohs fan")
        q_score = q_score + 1
else:
        q_response = easygui.msgbox("Perfect pick, " + NRL_Team + "! I always knew you were a Rabbitohs fan.")

#Tell the user the amount of Grand Finals they have won out of 10
easygui.msgbox(str(NRL_Team) + ",you have won " + str(q_score)
+ " Grand Finals.\nYour score: " + str(q_score) + "/10","NRL Trivia")

#Displays message when player opts to quit the game or when all questions have been
answered
title = "NRL Trivia"
msg = "Have a great rest of your season!"
button = "Close"
easygui.msgbox(msg, title, button)
