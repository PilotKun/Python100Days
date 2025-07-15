import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

#*read the csv file convert the the input to lowercase when typed a state make the name appear in the coor respective of that state

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = [] 

#* My Code this is ok but it isn't perfect
# answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title

# if answer_state in data.state:
#     print("correct")
# else:
#     print("try again")

# print(data[data.state == answer_state])
# row = data[data.state == answer_state].iloc[0]
# x = row["x"]
# y = row["y"]

# writer = t.Turtle()
# writer.hideturtle()      #so it doesn't show an arrow
# writer.penup()           #prevent it from drawing a line
# writer.goto(x, y)        #move to the state’s coordinates
# writer.write(answer_state)  #write the state name on the map


# t.mainloop()


#* The correct code
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = t.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)