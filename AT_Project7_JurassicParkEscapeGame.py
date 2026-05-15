import tkinter as tk
import time
from tkinter import font
import random
import math

VIEW_DISTANCE = 400     #Size of the viewable area
WORLD_SIZE = 1600       #Size of world
MOVE_SPEED = 20         #How far the player moves per step
STEP_COUNTER = 0

alive = True

def make_east_moving_player_1():
    pattern = [
        "0000000001100000000",
        "0000000011440000000",
        "0000000111424000000",
        "0000000144444000000",
        "0000000044440000000",
        "0000000004400000000",
        "0000000044440000000",
        "0000000041140000000",
        "0000000011140000000",
        "0000000111440000000",
        "0000001114440330000",
        "0000011044443330000",
        "0000011144443300000",
        "0000001114440000000",
        "0000000111440000000",
        "0000000011440000000",
        "0000000044440000000",
        "0000000044440000000",
        "0000000444044000000",
        "0000004440044400000",
        "0000044400004440000",
        "0000444000000440000",
        "0004440000000440000",
        "0004400000000440000",
        "0004400000000444000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#efefef", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#d9d9d9", (x,y))
            elif pattern[y][x] == "4":
                img.put("#b7b7b7", (x,y))
            else:
                pass
            
    return img
            
def make_east_moving_player_2():
    pattern = [
        "0000000001100000000",
        "0000000011440000000",
        "0000000111424000000",
        "0000000144444000000",
        "0000000044440000000",
        "0000000004400000000",
        "0000000044440000000",
        "0000000041140000000",
        "0000000041140000000",
        "0000000341110000000",
        "0000003344110000000",
        "0000033044110000000",
        "0000033344111011000",
        "0000003344411111000",
        "0000000344441100000",
        "0000000044440000000",
        "0000000044440000000",
        "0000000044440000000",
        "0000000444044000000",
        "0000004440044400000",
        "0000044400004440000",
        "0000444000000440000",
        "0004440000000440000",
        "0004400000000440000",
        "0004400000000444000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#efefef", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#d9d9d9", (x,y))
            elif pattern[y][x] == "4":
                img.put("#b7b7b7", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
            
def make_west_moving_player_1():
    pattern = [
        "0000000011000000000",
        "0000000441100000000",
        "0000004241110000000",
        "0000004444410000000",
        "0000000444400000000",
        "0000000044000000000",
        "0000000444400000000",
        "0000000411400000000",
        "0000000411100000000",
        "0000000441110000000",
        "0000330444111000000",
        "0000333444401100000",
        "0000033444411100000",
        "0000000444111000000",
        "0000000441110000000",
        "0000000441100000000",
        "0000000444400000000",
        "0000000444400000000",
        "0000004404440000000",
        "0000044400444000000",
        "0000444000044400000",
        "0000440000004440000",
        "0000440000000444000",
        "0000440000000044000",
        "0004440000000044000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#efefef", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#d9d9d9", (x,y))
            elif pattern[y][x] == "4":
                img.put("#b7b7b7", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
            
def make_west_moving_player_2():
    pattern = [
        "0000000011000000000",
        "0000000441100000000",
        "0000004241110000000",
        "0000004444410000000",
        "0000000444400000000",
        "0000000044000000000",
        "0000000444400000000",
        "0000000411400000000",
        "0000000411400000000",
        "0000000111430000000",
        "0000000114433000000",
        "0000000114403300000",
        "0001101114433300000",
        "0001111144433000000",
        "0000011444430000000",
        "0000000444400000000",
        "0000000444400000000",
        "0000000444400000000",
        "0000004404440000000",
        "0000044400444000000",
        "0000444000044400000",
        "0000440000004440000",
        "0000440000000444000",
        "0000440000000044000",
        "0004440000000044000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#efefef", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#d9d9d9", (x,y))
            elif pattern[y][x] == "4":
                img.put("#b7b7b7", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
            
def make_south_moving_player_1():
    pattern = [
        "0000011100000",
        "0000144410000",
        "0001424241000",
        "0004444444000",
        "0000411140000",
        "0000044400000",
        "0000444440000",
        "0004444443000",
        "0005444443000",
        "0005444443000",
        "0005444443000",
        "0004444441000",
        "0004444441000",
        "0003444441000",
        "0003444410000",
        "0000444440000",
        "0000444440000",
        "0000444440000",
        "0000330440000",
        "0000330440000",
        "0000330550000",
        "0000440550000",
        "0000550550000",
        "0000550550000",
        "0005550555000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#efefef", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#d9d9d9", (x,y))
            elif pattern[y][x] == "4":
                img.put("#b7b7b7", (x,y))
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
            
def make_south_moving_player_2():
    pattern = [
        "0000011100000",
        "0000144410000",
        "0001424241000",
        "0004444444000",
        "0000411140000",
        "0000044400000",
        "0000444440000",
        "0003444444000",
        "0003444445000",
        "0003444445000",
        "0003444445000",
        "0001444444000",
        "0001444444000",
        "0001444443000",
        "0000144443000",
        "0000444440000",
        "0000444440000",
        "0000444440000",
        "0000440330000",
        "0000440330000",
        "0000550330000",
        "0000550440000",
        "0000550550000",
        "0000550550000",
        "0005550555000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#efefef", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#d9d9d9", (x,y))
            elif pattern[y][x] == "4":
                img.put("#b7b7b7", (x,y))
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
            
def make_north_moving_player_1():
    pattern = [
        "0000011100000",
        "0000111110000",
        "0001111111000",
        "0004111114000",
        "0000411140000",
        "0000044400000",
        "0000444440000",
        "0003444443000",
        "0003444441000",
        "0004444441000",
        "0004444441000",
        "0004444441000",
        "0005444443000",
        "0005444443000",
        "0005444443000",
        "0000444440000",
        "0000444440000",
        "0000444440000",
        "0000440440000",
        "0000330440000",
        "0000330550000",
        "0000330550000",
        "0000110550000",
        "0000110550000",
        "0001110555000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#efefef", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#d9d9d9", (x,y))
            elif pattern[y][x] == "4":
                img.put("#b7b7b7", (x,y))
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
    
            
    return img
            
def make_north_moving_player_2():
    pattern = [
        "0000011100000",
        "0000111110000",
        "0001111111000",
        "0004111114000",
        "0000411140000",
        "0000044400000",
        "0000444440000",
        "0003444443000",
        "0001444443000",
        "0001444444000",
        "0001444444000",
        "0001444444000",
        "0003444445000",
        "0003444445000",
        "0003444445000",
        "0000444440000",
        "0000444440000",
        "0000444440000",
        "0000440440000",
        "0000440330000",
        "0000550330000",
        "0000550330000",
        "0000550110000",
        "0000550110000",
        "0005550111000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#efefef", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#d9d9d9", (x,y))
            elif pattern[y][x] == "4":
                img.put("#b7b7b7", (x,y))
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
            

#Declare the root and name it
root = tk.Tk()
root.title("Escape from Jurassic Park!")

#Setting up the canvas w/ scrolling capabilities and a blue border
canvas = tk.Canvas(
    root,
    width = VIEW_DISTANCE,
    height = VIEW_DISTANCE,
    bg = "#03AE00",
    scrollregion=(0, 0, WORLD_SIZE, WORLD_SIZE),
    #highlightthickness = 5,
    #highlightbackground = "#0BA5F8"
)

#Executes the set up
canvas.pack()

#Optional line drawing to show movement can be inserted HERE:

#Creates the world border
#canvas.create_rectangle(5, 5, WORLD_SIZE - 5, WORLD_SIZE - 5, outline = "#0BA5F8", width = 5)
spawn_x = VIEW_DISTANCE // 2    #Starts player in center of map
spawn_y = VIEW_DISTANCE // 2    #Starts player in center of map




east_move_1_img= make_east_moving_player_1()
east_move_2_img= make_east_moving_player_2()
north_move_1_img = make_north_moving_player_1()
north_move_2_img = make_north_moving_player_2()
south_move_1_img = make_south_moving_player_1()
south_move_2_img = make_south_moving_player_2()
west_move_1_img = make_west_moving_player_1()
west_move_2_img = make_west_moving_player_2()

current_x = 300
current_y = 300

current_sprite_img = "south_move_1_img"

current_sprite_list = []

current_sprite = canvas.create_image(current_x, current_y, image = south_move_1_img, anchor = "center")
current_sprite_list.append(current_sprite)

def move_left(event):
    global current_sprite_img, current_x, current_sprite, current_sprite_list, STEP_COUNTER
    STEP_COUNTER+=1

    px1, py1, px2, py2 = canvas.bbox(current_sprite)
    
    counter = 0
    if len(current_sprite_list)>0:
        for i in range(len(current_sprite_list)):
            canvas.delete(current_sprite) 
    if STEP_COUNTER %2 == 0:
        current_sprite = canvas.create_image(current_x, current_y, image = west_move_2_img, anchor = "center")
    else:
        current_sprite = canvas.create_image(current_x, current_y, image = west_move_1_img, anchor = "center")
    current_sprite_list.append(current_sprite)
    if px1 <= 30:
        pass
    else:
        current_x -= MOVE_SPEED
        canvas.move(current_sprite, -MOVE_SPEED, 0) 
def move_right(event):
    global current_sprite_img, current_x, current_sprite, current_sprite_list, STEP_COUNTER
    STEP_COUNTER+=1

    px1, py1, px2, py2 = canvas.bbox(current_sprite)
    
    counter = 0
    if len(current_sprite_list)>0:
        for i in range(len(current_sprite_list)):
            canvas.delete(current_sprite) 
    if STEP_COUNTER %2 == 0:
        current_sprite = canvas.create_image(current_x, current_y, image = east_move_2_img, anchor = "center")
    else:
        current_sprite = canvas.create_image(current_x, current_y, image = east_move_1_img, anchor = "center")
    current_sprite_list.append(current_sprite)
    if px1 >= WORLD_SIZE-30:
        pass
    else:
        current_x += MOVE_SPEED
        canvas.move(current_sprite, MOVE_SPEED, 0)
def move_up(event):
    global current_sprite_img, current_y, current_sprite, current_sprite_list, STEP_COUNTER
    STEP_COUNTER+=1
    
    px1, py1, px2, py2 = canvas.bbox(current_sprite)
    
    counter = 0
    if len(current_sprite_list)>0:
        for i in range(len(current_sprite_list)):
            canvas.delete(current_sprite) 
    if STEP_COUNTER %2 == 0:
        current_sprite = canvas.create_image(current_x, current_y, image = north_move_2_img, anchor = "center")
    else:
        current_sprite = canvas.create_image(current_x, current_y, image = north_move_1_img, anchor = "center")
    current_sprite_list.append(current_sprite)
    if py1 <= 30:
        pass
    else:
        current_y -= MOVE_SPEED
        canvas.move(current_sprite, 0, -MOVE_SPEED) 
def move_down(event):
    global current_sprite_img, current_y, current_sprite, current_sprite_list, STEP_COUNTER
    STEP_COUNTER+=1
    
    px1, py1, px2, py2 = canvas.bbox(current_sprite)
    
    counter = 0
    if len(current_sprite_list)>0:
        for i in range(len(current_sprite_list)):
            canvas.delete(current_sprite) 
    if STEP_COUNTER %2 == 0:
        current_sprite = canvas.create_image(current_x, current_y, image = south_move_2_img, anchor = "center")
    else:
        current_sprite = canvas.create_image(current_x, current_y, image = south_move_1_img, anchor = "center")
    current_sprite_list.append(current_sprite)
    if py2 >= WORLD_SIZE-30:
        pass
    else:
        current_y += MOVE_SPEED
        canvas.move(current_sprite, 0, MOVE_SPEED)

root.bind("a", move_left)
root.bind("d", move_right)
root.bind("w", move_up)
root.bind("s", move_down)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

root.mainloop()