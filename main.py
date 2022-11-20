# Below code will give us the co-ordinates of the image where we click
# But we already have the states name with their co-ordinates in the csv file so
# we don't need to find it again
import turtle
import pandas as pd
from time import sleep
import time

screen = turtle.Screen()

#screen.bgcolor("black")
screen.title("Campeche Cities Game")
screen.bgpic("mexico.gif")
screen.tracer(0)

# read the data
data= pd.read_csv("datos1.csv")
cities= data.cities.to_list()
score=0
checking=[]

while score<12:

    answer_city= screen.textinput(title=f"{score}/12 Guess the city", prompt="What's another city's name?").title()
    
    if answer_city=="Exit":
        missing_cities=[]
        for city in cities:
            if city not in checking:
                missing_cities.append(city)
        # missing_cities
        new_data= pd.DataFrame(missing_cities)
        new_data.to_csv("cities_to_learn.csv")
        break
    if answer_city in cities and answer_city not in checking:
        checking.append(answer_city)
        print(checking)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        city_data= data[data.cities==answer_city]
        
        t.goto(int(city_data.x), int(city_data.y))
        t.write(answer_city,align="center", font=("Arial", 8, "normal"))
        score+=1
    elif answer_city in checking:
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0, 200)
        t.color("red")
        t.write("Ya escribiste anteriormente esta ciudad!!",align="center", font=("Arial", 20, "normal"))
        sleep(2)
        t.clear()
    else:
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0,200)
        t.color("red")
        t.write("No es una ciudad de Campeche, intenta de nuevo",align="center", font=("Arial", 20, "normal"))
        sleep(1)
        t.clear()

    if score==12:
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0,200)
        t.color("green")
        t.write("Felicidades, ganaste!!",align="center", font=("Arial", 20, "normal"))
        sleep(1)
        t.clear()
 
