import tkinter as tk
import time
from tkinter import font
import random
import math

VIEW_DISTANCE = 800     #Size of the viewable area
WORLD_SIZE = 3200       #Size of world
MOVE_SPEED = 20         #How far the player moves per step
STEP_COUNTER = 0
HAVE_PISTOL = False
HAVE_RIFLE = False
HAVE_MG = False
pistol_ammo = 0
rifle_ammo = 0
mg_ammo = 0

alive = True

def north_stationary():
    current_sprite = canvas.create_image(current_x, current_y, image = north_stationary_player, anchor = "center")
def east_stationary():
    current_sprite = canvas.create_image(current_x, current_y, image = east_stationary_player, anchor = "center")
def south_stationary():
    current_sprite = canvas.create_image(current_x, current_y, image = south_stationary_player, anchor = "center")
def west_stationary():
    current_sprite = canvas.create_image(current_x, current_y, image = west_stationary_player, anchor = "center")

def make_north_stationary_player():
    pattern = [
        "0000000000011100000000000",
        "0000000000111110000000000",
        "0000000001111111000000000",
        "0000000004111114000000000",
        "0000000000411140000000000",
        "0000000000044400000000000",
        "0000000000444440000000000",
        "0000000001444441000000000",
        "0000000001444441000000000",
        "0000000001444441000000000",
        "0000000001444441000000000",
        "0000000001444441000000000",
        "0000000001444441000000000",
        "0000000003444443000000000",
        "0000000003444443000000000",
        "0000000000444440000000000",
        "0000000000444440000000000",
        "0000000000444440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000004440444000000000"
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
def make_east_stationary_player():
    pattern = [
        "0000000001100000000000000",
        "0000000011440000000000000",
        "0000000111424000000000000",
        "0000000144444000000000000",
        "0000000044440000000000000",
        "0000000004400000000000000",
        "0000000044440000000000000",
        "0000000041140000000000000",
        "0000000041140000000000000",
        "0000000041140000000000000",
        "0000000041143300000000000",
        "0000000041143300000000000",
        "0000000044110000000000000",
        "0000000044411100000000000",
        "0000000044441100000000000",
        "0000000044440000000000000",
        "0000000044440000000000000",
        "0000000044440000000000000",
        "0000000004400000000000000",
        "0000000004400000000000000",
        "0000000004400000000000000",
        "0000000004400000000000000",
        "0000000004400000000000000",
        "0000000004440000000000000",
        "0000000004444000000000000"
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
def make_south_stationary_player():
    pattern = [
        "0000000000011100000000000",
        "0000000000144410000000000",
        "0000000001424241000000000",
        "0000000004444444000000000",
        "0000000000411140000000000",
        "0000000000044400000000000",
        "0000000000444440000000000",
        "0000000003444443000000000",
        "0000000003444443000000000",
        "0000000003444443000000000",
        "0000000003444443000000000",
        "0000000003444443000000000",
        "0000000003444443000000000",
        "0000000001444441000000000",
        "0000000001444441000000000",
        "0000000000444440000000000",
        "0000000000444440000000000",
        "0000000000444440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000004440444000000000"
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
def make_west_stationary_player():
    pattern = [
        "0000000000000011000000000",
        "0000000000000441100000000",
        "0000000000004241110000000",
        "0000000000004444410000000",
        "0000000000000444400000000",
        "0000000000000044000000000",
        "0000000000000444400000000",
        "0000000000000411400000000",
        "0000000000000411400000000",
        "0000000000000411400000000",
        "0000000000033411400000000",
        "0000000000033411400000000",
        "0000000000000114400000000",
        "0000000000011144400000000",
        "0000000000011444400000000",
        "0000000000000444400000000",
        "0000000000000444400000000",
        "0000000000000444400000000",
        "0000000000000044000000000",
        "0000000000000044000000000",
        "0000000000000044000000000",
        "0000000000000044000000000",
        "0000000000000044000000000",
        "0000000000000444000000000",
        "0000000000004444000000000"
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

def make_north_stationary_pistol():
    pattern = [
        "0000000000011100000000000",
        "0000000000111110000000000",
        "0000000001111111000000000",
        "0000000004111114000000000",
        "0000000000411140000000000",
        "0000000000044400000000000",
        "0000000000444440000000000",
        "0000000001444441000000000",
        "0000000001444441000000000",
        "0000000001444441000000000",
        "0000000001444441000000000",
        "0000000001444441600000000",
        "0000000001444441000000000",
        "0000000003444443000000000",
        "0000000003444443000000000",
        "0000000000444440000000000",
        "0000000000444440000000000",
        "0000000000444440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000004440444000000000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#efefef", (x,y))
            elif pattern[y][x] == "6":
                img.put("#434343", (x,y))
            elif pattern[y][x] == "3":
                img.put("#d9d9d9", (x,y))
            elif pattern[y][x] == "4":
                img.put("#b7b7b7", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
def make_east_stationary_pistol():
    pattern = [
        "0000000001100000000000000",
        "0000000011440000000000000",
        "0000000111424000000000000",
        "0000000144444000000000000",
        "0000000044440000000000000",
        "0000000004400000000000000",
        "0000000044440000000000000",
        "0000000041140000000000000",
        "0000000041140000000000000",
        "0000000041140000000000000",
        "0000000041143300000000000",
        "0000000041143300000000000",
        "0000000044110555500000000",
        "0000000044411150000000000",
        "0000000044441100000000000",
        "0000000044440000000000000",
        "0000000044440000000000000",
        "0000000044440000000000000",
        "0000000004400000000000000",
        "0000000004400000000000000",
        "0000000004400000000000000",
        "0000000004400000000000000",
        "0000000004400000000000000",
        "0000000004440000000000000",
        "0000000004444000000000000"
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
                img.put("#666666", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
def make_south_stationary_pistol():
    pattern = [
        "0000000000011100000000000",
        "0000000000144410000000000",
        "0000000001424241000000000",
        "0000000004444444000000000",
        "0000000000411140000000000",
        "0000000000044400000000000",
        "0000000000444440000000000",
        "0000000003444443000000000",
        "0000000003444443000000000",
        "0000000003444443000000000",
        "0000000005444443000000000",
        "0000000050544443000000000",
        "0000000005444443000000000",
        "0000000006444441000000000",
        "0000000001444441000000000",
        "0000000000444440000000000",
        "0000000000444440000000000",
        "0000000000444440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000000440440000000000",
        "0000000004440444000000000"
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
                img.put("#666666", (x,y))
            elif pattern[y][x] == "6":
                img.put("#434343", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
def make_west_stationary_pistol():
    pattern = [
        "0000000000000011000000000",
        "0000000000000441100000000",
        "0000000000004241110000000",
        "0000000000004444410000000",
        "0000000000000444400000000",
        "0000000000000044000000000",
        "0000000000000444400000000",
        "0000000000000411400000000",
        "0000000000000411400000000",
        "0000000000000411400000000",
        "0000000000033411400000000",
        "0000000000033411400000000",
        "0000000055550114400000000",
        "0000000000511144400000000",
        "0000000000011444400000000",
        "0000000000000444400000000",
        "0000000000000444400000000",
        "0000000000000444400000000",
        "0000000000000044000000000",
        "0000000000000044000000000",
        "0000000000000044000000000",
        "0000000000000044000000000",
        "0000000000000044000000000",
        "0000000000000444000000000",
        "0000000000004444000000000"
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
                img.put("#666666", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
def make_north_stationary_rifle():
    pattern = [

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
def make_east_stationary_rifle():
    pattern = [

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
def make_south_stationary_rifle():
    pattern = [

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
def make_west_stationary_rifle():
    pattern = [

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
def make_north_stationary_MG():
    pattern = [

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
def make_east_stationary_MG():
    pattern = [

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
def make_south_stationary_MG():
    pattern = [

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
def make_west_stationary_MG():
    pattern = [

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

def north_moving_player_pistol_1():
def north_moving_player_pistol_2():
def east_moving_player_pistol_1():
def east_moving_player_pistol_2():
def south_moving_player_pistol_1():
def south_moving_player_pistol_2():
def west_moving_player_pistol_1():
def west_moving_player_pistol_2():

def north_moving_player_rifle_1():
def north_moving_player_rifle_2():
def east_moving_player_rifle_1():
def east_moving_player_rifle_2():
def south_moving_player_rifle_1():
def south_moving_player_rifle_2():
def west_moving_player_rifle_1():
def west_moving_player_rifle_2():

def north_moving_player_MG_1():
def north_moving_player_MG_2():
def east_moving_player_MG_1():
def east_moving_player_MG_2():
def south_moving_player_MG_1():
def south_moving_player_MG_2():
def west_moving_player_MG_1():
def west_moving_player_MG_2():

def make_west_stationary_trex():
def make_west_stationary_raptor():
def make_west_stationary_trike():
def make_west_stationary_stego():

def make_east_stationary_trex():
def make_east_stationary_raptor():
def make_east_stationary_trike():
def make_east_stationary_stego():

def make_west_moving_trex_1():
def make_west_moving_raptor_1():
def make_west_moving_trike_1():
def make_west_moving_stego_1():
def make_east_moving_trex_1():
def make_east_moving_raptor_1():
def make_east_moving_trike_1():
def make_east_moving_stego_1():

def make_west_moving_trex_2():
def make_west_moving_raptor_2():
def make_west_moving_trike_2():
def make_west_moving_stego_2():
def make_east_moving_trex_2():
def make_east_moving_raptor_2():
def make_east_moving_trike_2():
def make_east_moving_stego_2():

def make_helicopter():

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

def move_viewport():
    global current_sprite
    #center of player
    x1, y1, x2, y2 = canvas.bbox(current_sprite)
    current_sprite_center_x = (x1 + x2) / 2
    current_sprite_center_y = (y1 + y2) / 2

    #frame must have world in view
    max_offset = WORLD_SIZE - VIEW_DISTANCE
    left = min(max(current_sprite_center_x - VIEW_DISTANCE / 2, 0), max_offset)
    top = min(max(current_sprite_center_y - VIEW_DISTANCE / 2, 0), max_offset)

    #actually moves the frame
    canvas.xview_moveto(left / WORLD_SIZE)
    canvas.yview_moveto(top / WORLD_SIZE)

#Executes the set up
canvas.pack()

#Optional line drawing to show movement can be inserted HERE:
for line in range(0, WORLD_SIZE + 1, 250):
    canvas.create_line(line, 0, line, WORLD_SIZE, fill = "#0D4F00")
    canvas.create_line(0, line, WORLD_SIZE, line, fill = "#0D4F00")

#Creates the world border
#canvas.create_rectangle(5, 5, WORLD_SIZE - 5, WORLD_SIZE - 5, outline = "#0BA5F8", width = 5)
spawn_x = VIEW_DISTANCE // 2    #Starts player in center of map
spawn_y = VIEW_DISTANCE // 2    #Starts player in center of map


north_stationary_player = make_north_stationary_player()
east_stationary_player = make_east_stationary_player()
south_stationary_player = make_south_stationary_player()
west_stationary_player = make_west_stationary_player()

east_move_1_img= make_east_moving_player_1()
east_move_2_img= make_east_moving_player_2()
north_move_1_img = make_north_moving_player_1()
north_move_2_img = make_north_moving_player_2()
south_move_1_img = make_south_moving_player_1()
south_move_2_img = make_south_moving_player_2()
west_move_1_img = make_west_moving_player_1()
west_move_2_img = make_west_moving_player_2()

north_stationary_player_img = make_north_stationary_player()
east_stationary_player_img = make_east_stationary_player()
south_stationary_player_img = make_south_stationary_player()
west_stationary_player_img = make_west_stationary_player()
north_stationary_pistol_img = make_north_stationary_pistol()
east_stationary_pistol_img = make_east_stationary_pistol()
south_stationary_pistol_img = make_south_stationary_pistol()
west_stationary_pistol_img = make_west_stationary_pistol()
north_stationary_rifle_img = make_north_stationary_rifle()
east_stationary_rifle_img = make_east_stationary_rifle()
south_stationary_rifle_img = make_south_stationary_rifle()
west_stationary_rifle_img = make_west_stationary_rifle()
north_stationary_MG_img = make_north_stationary_MG()
east_stationary_MG_img = make_east_stationary_MG()
south_stationary_MG_img = make_south_stationary_MG()
west_stationary_MG_img = make_west_stationary_MG()

north_moving_pistol_1_img = north_moving_player_pistol_1()
north_moving_pistol_2_img = north_moving_player_pistol_2()
east_moving_pistol_1_img = east_moving_player_pistol_1()
east_moving_pistol_2_img = east_moving_player_pistol_2()
south_moving_pistol_1_img = south_moving_player_pistol_1()
south_moving_pistol_2_img = south_moving_player_pistol_2()
west_moving_pistol_1_img = west_moving_player_pistol_1()
west_moving_pistol_2_img = west_moving_player_pistol_2()

north_moving_rifle_1_img = north_moving_player_rifle_1()
north_moving_rifle_2_img = north_moving_player_rifle_2()
east_moving_rifle_1_img = east_moving_player_rifle_1()
east_moving_rifle_2_img = east_moving_player_rifle_2()
south_moving_rifle_1_img = south_moving_player_rifle_1()
south_moving_rifle_2_img = south_moving_player_rifle_2()
west_moving_rifle_1_img = west_moving_player_rifle_1()
west_moving_rifle_2_img = west_moving_player_rifle_2()

north_moving_MG_1_img = north_moving_player_MG_1()
north_moving_MG_2_img = north_moving_player_MG_2()
east_moving_MG_1_img = east_moving_player_MG_1()
east_moving_MG_2_img = east_moving_player_MG_2()
south_moving_MG_1_img = south_moving_player_MG_1()
south_moving_MG_2_img = south_moving_player_MG_2()
west_moving_MG_1_img = west_moving_player_MG_1()
west_moving_MG_2_img = west_moving_player_MG_2()

west_stationary_trex_img = make_west_stationary_trex()
west_stationary_raptor_img = make_west_stationary_raptor()
west_stationary_trike_img = make_west_stationary_trike()
west_stationary_stego_img = make_west_stationary_stego()

east_stationary_trex_img = make_east_stationary_trex()
east_stationary_raptor_img = make_east_stationary_raptor()
east_stationary_trike_img = make_east_stationary_trike()
east_stationary_stego_img = make_east_stationary_stego()

west_moving_trex_1_img = make_west_moving_trex_1()
west_moving_raptor_1_img = make_west_moving_raptor_1()
west_moving_trike_1_img = make_west_moving_trike_1()
west_moving_stego_1_img = make_west_moving_stego_1()
east_moving_trex_1_img = make_east_moving_trex_1()
east_moving_raptor_1_img = make_east_moving_raptor_1()
east_moving_trike_1_img = make_east_moving_trike_1()
east_moving_stego_1_img = make_east_moving_stego_1()

west_moving_trex_2_img = make_west_moving_trex_2()
west_moving_raptor_2_img = make_west_moving_raptor_2()
west_moving_trike_2_img = make_west_moving_trike_2()
west_moving_stego_2_img = make_west_moving_stego_2()
east_moving_trex_2_img = make_east_moving_trex_2()
east_moving_raptor_2_img = make_east_moving_raptor_2()
east_moving_trike_2_img = make_east_moving_trike_2()
east_moving_stego_2_img = make_east_moving_stego_2()

helicopter_img = make_helicopter()


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
    if HAVE_MG == False and HAVE_PISTOL == False and HAVE_RIFLE == False:
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





    west_stationary()
    move_viewport()
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
    move_viewport()
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
    move_viewport()
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
    move_viewport()

root.bind("a", move_left)
root.bind("d", move_right)
root.bind("w", move_up)
root.bind("s", move_down)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

#def random_spawn_weapon():
#def random_spawn_ammo():
#def random_spawn_peaceful():
#def random_spawn_predator():





move_viewport()
canvas.focus_set()

root.mainloop()