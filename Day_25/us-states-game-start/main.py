import turtle,pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
score = 0
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# print(data_coordinates)
while len(guessed_states) != 50:
    
    answer = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state", prompt="Try another guess")
    answer = answer.title()

    if answer == "Exit" :
        break
    if answer in all_states:
        #Create a new turtle
        guessed_states.append(answer)
        state_data = data[data.state == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x),int(state_data.y))  
        t.write(answer)
 
#Save the missing states to a csv file
missed_states = []

#I have all states list , I have guessed states list
for state in all_states:
    if state in guessed_states:
        continue
    else:
        missed_states.append(state)


#COnvert the list to csv file
state_dictionary = pandas.DataFrame(missed_states)

state_dictionary.to_csv("missed_states.csv",index=False)

