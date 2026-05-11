import tkinter as tk
import time
from tkinter import font
import random
import math

VIEW_DISTANCE = 400     #Size of the viewable area
WORLD_SIZE = 1600       #Size of world
MOVE_SPEED = 20         #How far the player moves per step

alive = True

def make_east_moving_player_1(spawn_x, spawn_y):
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
            
def make_east_moving_player_2(spawn_x, spawn_y):
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
                img.put("#000000", (x,y))
            
    return img
            
def make_north_moving_player_1(spawn_x, spawn_y):
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
                img.put("#000000", (x,y))
            
    return img
            
def make_north_moving_player_2(spawn_x, spawn_y):
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
                img.put("#000000", (x,y))
            
    return img
            
def make_south_moving_player_1(spawn_x, spawn_y):
    pattern = [

    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("", (x,y))
            elif pattern[y][x] == "2":
                img.put("", (x,y))
            elif pattern[y][x] == "3":
                img.put("", (x,y))
            elif pattern[y][x] == "4":
                img.put("", (x,y))
            elif pattern[y][x] == "5":
                img.put("", (x,y))
            elif pattern[y][x] == "6":
                img.put("", (x,y))
            elif pattern[y][x] == "7":
                img.put("", (x,y))
            elif pattern[y][x] == "8":
                img.put("", (x,y))
            elif pattern[y][x] == "9":
                img.put("", (x,y))
            else:
                img.put("#000000", (x,y))
            
    return img
            
def make_south_moving_player_2(spawn_x, spawn_y):
    pattern = [

    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("", (x,y))
            elif pattern[y][x] == "2":
                img.put("", (x,y))
            elif pattern[y][x] == "3":
                img.put("", (x,y))
            elif pattern[y][x] == "4":
                img.put("", (x,y))
            elif pattern[y][x] == "5":
                img.put("", (x,y))
            elif pattern[y][x] == "6":
                img.put("", (x,y))
            elif pattern[y][x] == "7":
                img.put("", (x,y))
            elif pattern[y][x] == "8":
                img.put("", (x,y))
            elif pattern[y][x] == "9":
                img.put("", (x,y))
            else:
                img.put("#000000", (x,y))
            
    return img
            
def make_west_moving_player_1(spawn_x, spawn_y):
    pattern = [

    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("", (x,y))
            elif pattern[y][x] == "2":
                img.put("", (x,y))
            elif pattern[y][x] == "3":
                img.put("", (x,y))
            elif pattern[y][x] == "4":
                img.put("", (x,y))
            elif pattern[y][x] == "5":
                img.put("", (x,y))
            elif pattern[y][x] == "6":
                img.put("", (x,y))
            elif pattern[y][x] == "7":
                img.put("", (x,y))
            elif pattern[y][x] == "8":
                img.put("", (x,y))
            elif pattern[y][x] == "9":
                img.put("", (x,y))
            else:
                img.put("#000000", (x,y))
            
    return img
            
def make_west_moving_player_2(spawn_x, spawn_y):
    pattern = [

    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("", (x,y))
            elif pattern[y][x] == "2":
                img.put("", (x,y))
            elif pattern[y][x] == "3":
                img.put("", (x,y))
            elif pattern[y][x] == "4":
                img.put("", (x,y))
            elif pattern[y][x] == "5":
                img.put("", (x,y))
            elif pattern[y][x] == "6":
                img.put("", (x,y))
            elif pattern[y][x] == "7":
                img.put("", (x,y))
            elif pattern[y][x] == "8":
                img.put("", (x,y))
            elif pattern[y][x] == "9":
                img.put("", (x,y))
            else:
                img.put("#000000", (x,y))
            
    return img
            

def make_world():
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
        highlightthickness = 5,
        highlightbackground = "#0BA5F8"
    )
    #Executes the set up
    canvas.pack()

    #Optional line drawing to show movement can be inserted HERE:

    #Creates the world border
    canvas.create_rectangle(5, 5, WORLD_SIZE - 5, WORLD_SIZE - 5, outline = "#0BA5F8", width = 5)

    spawn_x = VIEW_DISTANCE // 2    #Starts player in center of map
    spawn_y = VIEW_DISTANCE // 2    #Starts player in center of map
