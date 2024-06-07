import turtle
from turtle import Screen, Turtle
import pandas as pd
screen=Screen()
screen.title('US States game')
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
on_board=Turtle()
count=0
right_guesses=[]
states=pd.read_csv('50_states.csv')
names=states['state']
no_guess = states['state'].tolist()
while count!=50:
    answer=screen.textinput(title=f"Guess the State{count}/50", prompt="What's another State?")
    answer=answer.title()

    if answer in states['state'].values:
        count+=1
        on_board.penup()
        on_board.hideturtle()
        col=states[states['state']==answer]
        on_board.goto(x=col.get('x').values[0], y=col.get('y').values[0])
        #col.x or col.y
        on_board.write(answer)
        right_guesses.append(answer)
        no_guess.remove(answer)
    if answer.lower() == 'exit':
        states.to_csv('guess.csv')
        break
