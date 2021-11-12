# a121_catch_a_turtle.py
#-----import statements-----
import random as rand
import turtle as trtl
import turtle as score_writer
import turtle as counter
import leaderboard as lb
#-----game configuration----

score = 0
spot_color = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "silver"]
spot_size = [0.5, 0.75, 1, 1.5, 2, 2.5, 3]
bg_color = ["green", "blue", "purple"]
spot_shape = "circle"
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False



#-----initialize turtle-----
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")

score_writer.speed(0)
score_writer.penup()
score_writer.goto(-250, 250)
score_writer.hideturtle()

counter.speed()
counter.penup()
counter.goto(-250, 250)
counter.hideturtle()

spot = trtl.Turtle()
spot.speed(0)
spot.penup()
spot.shape("circle")
#-----game functions--------
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

def spot_clicked(x, y):
    update_score(x, y)
    change_position()
    colorsize()

def change_position():
    new_xpos = rand.randint(-350, 350)
    new_ypos = rand.randint(-300, 300)
    spot.goto(new_xpos, new_ypos)

def update_score(x, y):
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
def colorsize():
  spot.shapesize(rand.choice(spot_size))
  spot.color(rand.choice(spot_color)) 

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.bgcolor("indigo")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()

#------high scores-------------
# 32