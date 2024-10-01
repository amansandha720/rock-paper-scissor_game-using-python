from tkinter import *
from PIL import Image,ImageTk
from random import randint

root = Tk()
root.title('Rock Paper Scissor')
root.configure(background='green')

rock_img = ImageTk.PhotoImage(Image.open('stone.png'))
paper_img = ImageTk.PhotoImage(Image.open('paper.png'))
scissor_img = ImageTk.PhotoImage(Image.open('scissor.png'))
rock_img_comp = ImageTk.PhotoImage(Image.open('stone.png'))
paper_img_comp = ImageTk.PhotoImage(Image.open('paper.png'))
scissor_img_comp = ImageTk.PhotoImage(Image.open('scissor.png'))

#Insert pictures

user_label = Label(root,image=rock_img,bg='green')
comp_label = Label(root,image=rock_img_comp,bg='green')
comp_label.grid(row=1 ,column=0)
user_label.grid(row=1 , column=4)

#Indicator

user_indicator = Label(root,font=50,text='USER',bg='green')
comp_indicator = Label(root,font=50,text='COMPUTER',bg='green')
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#message

msg = Label(root,font=50,bg='green',fg='white')
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg['text']=x

#update user score

def updateUserScore():
    score = int(player_score['text'])
    score += 1
    player_score['text'] = str(score)

#update user score
def updateCompScore():
    score = int(computer_score['text'])
    score += 1
    computer_score['text'] = str(score)

#check winner

def checkWinner(player,computer):
    if player == computer:
        updateMessage('Its a tie!!')
    elif player == 'rock':
        if computer == 'paper':
            updateMessage('You loose')
            updateCompScore()
        else:
            updateMessage('You Win')
            updateUserScore()
    elif player == 'paper':
        if computer == 'scissor':
            updateMessage('You loose')
            updateCompScore()
        else:
            updateMessage('You Win')
            updateUserScore()
    elif player == 'scissor':
        if computer == 'rock':
            updateMessage('You loose')
            updateCompScore()
        else:
            updateMessage('You Win')
            updateUserScore()
    else:
        pass
    
    
#update choices
choices=['rock','paper','scissor']
def updateChoice(x):
    #for computer
    compChoice = choices[randint(0,2)]
    if compChoice == 'rock':
        comp_label.configure(image=rock_img_comp)
    elif compChoice == 'paper':
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    
    
    #for user
    if x=='rock':
        user_label.configure(image=rock_img)
    elif x=='paper':
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWinner(x,compChoice)

#score

player_score = Label(root,text=0,font=100,bg='green',fg='white')
computer_score = Label(root,text=0,font=100,bg='green',fg='white')
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

#buttons

rock = Button(root,width=20,height=2,text='Rock',bg='blue',fg='black',command=lambda:updateChoice('rock'),font=('times new roman',14)).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text='Paper',bg='#FF3E4D',fg='black',command=lambda:updateChoice('paper'),font=('times new roman',14)).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text='Scissor',bg='yellow',fg='black',command=lambda:updateChoice('scissor'),font=('times new roman',14)).grid(row=2,column=3)



root.mainloop()