import tkinter as tk
import time
from tkinter import font
import random
import math

VIEW_DISTANCE = 800     #Size of the viewable area
WORLD_SIZE = 5000       #Size of world
MOVE_SPEED = 20         #How far the player moves per step
STEP_COUNTER = 0
HAVE_PISTOL = False
HAVE_RIFLE = False
HAVE_MG = True
WIN = False
pistol_ammo = 0
rifle_ammo = 0
mg_ammo = 100
current_mg_bullets = []
current_rifle_bullets = []
current_pistol_bullets = []
rex = []
raptors = []
trikes = []
stegos = []

alive = True

'''
def north_stationary():
    current_sprite = canvas.create_image(current_x, current_y, image = north_stationary_player, anchor = "center")
def east_stationary():
    current_sprite = canvas.create_image(current_x, current_y, image = east_stationary_player, anchor = "center")
def south_stationary():
    current_sprite = canvas.create_image(current_x, current_y, image = south_stationary_player, anchor = "center")
def west_stationary(prev_sprite):
    canvas.delete(prev_sprite)
    current_sprite = canvas.create_image(current_x, current_y, image = west_stationary_player, anchor = "center")
'''
    
def make_north_stationary_player():
    pattern = [
        "0000011100000",
        "0000111110000",
        "0001111111000",
        "0004111114000",
        "0000411140000",
        "0000044400000",
        "0000444440000",
        "0001444441000",
        "0001444441000",
        "0001444441000",
        "0001444441000",
        "0001444441000",
        "0001444441000",
        "0003444443000",
        "0003444443000",
        "0000444440000",
        "0000444440000",
        "0000444440000",
        "0000440440000",
        "0000440440000",
        "0000440440000",
        "0000440440000",
        "0000440440000",
        "0000440440000",
        "0004440444000"
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
        "0000011000000",
        "0000114400000",
        "0001114240000",
        "0001444440000",
        "0000444400000",
        "0000044000000",
        "0000444400000",
        "0000411400000",
        "0000411400000",
        "0000411400000",
        "0000411433000",
        "0000411433000",
        "0000441100000",
        "0000444111000",
        "0000444411000",
        "0000444400000",
        "0000444400000",
        "0000444400000",
        "0000044000000",
        "0000044000000",
        "0000044000000",
        "0000044000000",
        "0000044000000",
        "0000044400000",
        "0000044440000"
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
        "0000011100000",
        "0000144410000",
        "0001424241000",
        "0004444444000",
        "0000411140000",
        "0000044400000",
        "0000444440000",
        "0003444443000",
        "0003444443000",
        "0003444443000",
        "0003444443000",
        "0003444443000",
        "0003444443000",
        "0001444441000",
        "0001444441000",
        "0000444440000",
        "0000444440000",
        "0000444440000",
        "0000440440000",
        "0000440440000",
        "0000440440000",
        "0000440440000",
        "0000440440000",
        "0000440440000",
        "0004440444000"
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
        "0000001100000",
        "0000044110000",
        "0000424111000",
        "0000444441000",
        "0000044440000",
        "0000004400000",
        "0000044440000",
        "0000041140000",
        "0000041140000",
        "0000041140000",
        "0003341140000",
        "0003341140000",
        "0000011440000",
        "0001114440000",
        "0001144440000",
        "0000044440000",
        "0000044440000",
        "0000044440000",
        "0000004400000",
        "0000004400000",
        "0000004400000",
        "0000004400000",
        "0000004400000",
        "0000044400000",
        "0000444400000"
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
        "00000111000000",
        "00001111100000",
        "00011111110000",
        "00041111140000",
        "00004111400000",
        "00000444000000",
        "00004444400000",
        "00014444410000",
        "00014444410000",
        "00014444410000",
        "00014444410000",
        "00014444416000",
        "00014444410000",
        "00034444430000",
        "00034444430000",
        "00004444400000",
        "00004444400000",
        "00004444400000",
        "00004404400000",
        "00004404400000",
        "00004404400000",
        "00004404400000",
        "00004404400000",
        "00004404400000",
        "00044404440000"
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
        "0000011000000000",
        "0000114400000000",
        "0001114240000000",
        "0001444440000000",
        "0000444400000000",
        "0000044000000000",
        "0000444400000000",
        "0000411400000000",
        "0000411400000000",
        "0000411400000000",
        "0000411433000000",
        "0000411433000000",
        "0000441105555000",
        "0000444111500000",
        "0000444411000000",
        "0000444400000000",
        "0000444400000000",
        "0000444400000000",
        "0000044000000000",
        "0000044000000000",
        "0000044000000000",
        "0000044000000000",
        "0000044000000000",
        "0000044400000000",
        "0000044440000000"
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
        "00000011100000",
        "00000144410000",
        "00001424241000",
        "00004444444000",
        "00000411140000",
        "00000044400000",
        "00000444440000",
        "00003444443000",
        "00003444443000",
        "00003444443000",
        "00005444443000",
        "00050544443000",
        "00005444443000",
        "00006444441000",
        "00001444441000",
        "00000444440000",
        "00000444440000",
        "00000444440000",
        "00000440440000",
        "00000440440000",
        "00000440440000",
        "00000440440000",
        "00000440440000",
        "00000440440000",
        "00004440444000"
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
        "0000000001100000",
        "0000000044110000",
        "0000000424111000",
        "0000000444441000",
        "0000000044440000",
        "0000000004400000",
        "0000000044440000",
        "0000000041140000",
        "0000000041140000",
        "0000000041140000",
        "0000003341140000",
        "0000003341140000",
        "0005555011440000",
        "0000051114440000",
        "0000001144440000",
        "0000000044440000",
        "0000000044440000",
        "0000000044440000",
        "0000000004400000",
        "0000000004400000",
        "0000000004400000",
        "0000000004400000",
        "0000000004400000",
        "0000000044400000",
        "0000000444400000"
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
        "000001110000000",
        "000011111000000",
        "000111111100000",
        "000411111400000",
        "000041114000000",
        "000004440000000",
        "000044444000000",
        "000144444100000",
        "000144444110000",
        "000144444511000",
        "000144444511000",
        "000144444110000",
        "000144444130000",
        "000344444500000",
        "000344444500000",
        "000044444500000",
        "000044444500000",
        "000044444500000",
        "000044044500000",
        "000044044000000",
        "000044044000000",
        "000044044000000",
        "000044044000000",
        "000044044000000",
        "000444044400000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#efefef", (x,y))
            elif pattern[y][x] == "6":
                img.put("#cccccc", (x,y))
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
def make_east_stationary_rifle():
    pattern = [
        "000001100000000000000",
        "000011440000000000000",
        "000111424000000000000",
        "000144444000000000000",
        "000044440000000000000",
        "000004400000000000000",
        "000044440000000000000",
        "000041140000000000000",
        "000041150000000000000",
        "000041155000600000000",
        "000041155506660000000",
        "000041143555666000000",
        "000044110555567600000",
        "000044411505556000000",
        "000044445000550000000",
        "000044440000055000000",
        "000044440000005500000",
        "000044440000050550000",
        "000004400000500055000",
        "000004400000000000000",
        "000004400000000000000",
        "000004400000000000000",
        "000004400000000000000",
        "000004440000000000000",
        "000004444000000000000"
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
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "7":
                img.put("#c0feff", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
def make_south_stationary_rifle():
    pattern = [
        "000000011100000",
        "000000144410000",
        "000001424241000",
        "000004444444000",
        "000000411140000",
        "000000044400000",
        "000000444440000",
        "000003444443000",
        "000035444443000",
        "000331444443000",
        "000311144443000",
        "000011144443000",
        "000017144443000",
        "000001444441000",
        "000005444441000",
        "000005444440000",
        "000005444440000",
        "000005444440000",
        "000005440440000",
        "000000440440000",
        "000000440440000",
        "000000440440000",
        "000000440440000",
        "000000440440000",
        "000004440444000"
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
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "7":
                img.put("#c0feff", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
def make_west_stationary_rifle():
    pattern = [
        "000000000000001100000",
        "000000000000044110000",
        "000000000000424111000",
        "000000000000444441000",
        "000000000000044440000",
        "000000000000004400000",
        "000000000000044440000",
        "000000000000041140000",
        "000000000000051140000",
        "000000003000551140000",
        "000000033305551140000",
        "000000333555341140000",
        "000003735555011440000",
        "000000355505114440000",
        "000000055000544440000",
        "000000550000044440000",
        "000005500000044440000",
        "000055050000044440000",
        "000550005000004400000",
        "000000000000004400000",
        "000000000000004400000",
        "000000000000004400000",
        "000000000000004400000",
        "000000000000044400000",
        "000000000000444400000"
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
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "7":
                img.put("#c0feff", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img

def make_north_stationary_MG():
    pattern = [
        "000000000011100000",
        "000000000111110000",
        "000000001111111000",
        "000000004111114000",
        "000000000411140000",
        "000000000044400000",
        "000000000444440000",
        "000000001444441000",
        "000000001444441000",
        "000000001444441000",
        "000000001444441000",
        "000000000444441000",
        "000000000444441000",
        "000000055444443000",
        "000555555444443000",
        "000555555444445000",
        "000000000444440000",
        "000000000444440000",
        "000000000446440000",
        "000000000447440000",
        "000000000446440000",
        "000000000447440000",
        "000000000446440000",
        "000000000440440000",
        "000000004440444000"
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
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "7":
                img.put("#bf9000", (x,y))
            elif pattern[y][x] == "8":
                img.put("#ffa96b", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
def make_east_stationary_MG():
    pattern = [
        "000001100000000000000",
        "000011440000000000000",
        "000111424000000000000",
        "000144444000000000000",
        "000044440000000000000",
        "000004400000000000000",
        "000044440000000000000",
        "000041140000000000000",
        "000041140000000000000",
        "000041140000000000000",
        "000041140000000000000",
        "000041143300000000000",
        "000041143500000000000",
        "000041140555550000000",
        "000044155566555555000",
        "000044545578555555000",
        "000044555066800000000",
        "000044440078600000000",
        "000004400066800000000",
        "000004400078600000000",
        "000004400066800000000",
        "000004400078600000000",
        "000004400066800000000",
        "000004440000000000000",
        "000004444000000000000"
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
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "7":
                img.put("#bf9000", (x,y))
            elif pattern[y][x] == "8":
                img.put("#ffa96b", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
def make_south_stationary_MG():
    pattern = [
        "000001110000000000",
        "000014441000000000",
        "000142424100000000",
        "000444444400000000",
        "000041114000000000",
        "000004440000000000",
        "000044444000000000",
        "000344444300000000",
        "000344444300000000",
        "000344444300000000",
        "000344443300000000",
        "000344133000000000",
        "000345114000000000",
        "000155555550000000",
        "000545555555555000",
        "000554655555555000",
        "000044764000000000",
        "000044684000000000",
        "000044764000000000",
        "000044684000000000",
        "000044764000000000",
        "000044684000000000",
        "000044764000000000",
        "000044084000000000",
        "000444044400000000",
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
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "7":
                img.put("#bf9000", (x,y))
            elif pattern[y][x] == "8":
                img.put("#ffa96b", (x,y))
            else:
                pass
                #img.put("#000000", (x,y))
            
    return img
def make_west_stationary_MG():
    pattern = [
        "000000000000001100000",
        "000000000000044110000",
        "000000000000424111000",
        "000000000000444441000",
        "000000000000044440000",
        "000000000000004400000",
        "000000000000044440000",
        "000000000000041140000",
        "000000000000041140000",
        "000000000000041140000",
        "000000000000041140000",
        "000000000003341140000",
        "000000000005341140000",
        "000000055555041140000",
        "000555555875551440000",
        "000555555665545440000",
        "000000006870555440000",
        "000000008660044440000",
        "000000006870004400000",
        "000000008660004400000",
        "000000006870004400000",
        "000000008660004400000",
        "000000006870004400000",
        "000000000000044400000",
        "000000000000444400000",
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
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "7":
                img.put("#bf9000", (x,y))
            elif pattern[y][x] == "8":
                img.put("#ffa96b", (x,y))
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
        "0000444446000",
        "0000444446000",
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            
            else:
                pass
            
    return img
def north_moving_player_pistol_2():
    pattern = [
        "000001110000000",
        "000011111000000",
        "000111111100000",
        "000411111400000",
        "000041114000000",
        "000004440000000",
        "000044444000000",
        "000344444300000",
        "000144444300000",
        "000144444400000",
        "000144444400000",
        "000144444400000",
        "000344444507000",
        "000344444570000",
        "000344444600000",
        "000044444000000",
        "000044444000000",
        "000044444000000",
        "000044044000000",
        "000044033000000",
        "000055033000000",
        "000055033000000",
        "000055011000000",
        "000055011000000",
        "000555011100000"
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            
            else:
                pass
            
    return img
def east_moving_player_pistol_2():
    pattern = [
        "0000000001100000000000",
        "0000000011440000000000",
        "0000000111424000000000",
        "0000000144444000000000",
        "0000000044440000000000",
        "0000000004400000000000",
        "0000000044440000000000",
        "0000000041140000000000",
        "0000000041140000000000",
        "0000000341110000000000",
        "0000003344110000000000",
        "0000033044110006666000",
        "0000033344111011600000",
        "0000003344411111000000",
        "0000000344441100000000",
        "0000000044440000000000",
        "0000000044440000000000",
        "0000000044440000000000",
        "0000000444044000000000",
        "0000004440044400000000",
        "0000044400004440000000",
        "0000444000000440000000",
        "0004440000000440000000",
        "0004400000000440000000",
        "0004400000000444000000"
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            
            else:
                pass
            
    return img
def east_moving_player_pistol_1():
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
        "0000000011640000000",
        "0000000046640000000",
        "0000000044640000000",
        "0000000444644000000",
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            
            else:
                pass
            
    return img
def south_moving_player_pistol_1():
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
        "0005444441000",
        "0005444441000",
        "0007444441000",
        "0006444410000",
        "0006444440000",
        "0006444440000",
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            
            else:
                pass
            
    return img
def south_moving_player_pistol_2():
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
        "0001444445000",
        "0006444444000",
        "0006444444000",
        "0007444443000",
        "0001444443000",
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            
            else:
                pass
            
    return img
def west_moving_player_pistol_1():
    pattern = [
        "000000000011000000000",
        "000000000441100000000",
        "000000004241110000000",
        "000000004444410000000",
        "000000000444400000000",
        "000000000044000000000",
        "000000000444400000000",
        "000000000411400000000",
        "000000000411100000000",
        "000666600441110000000",
        "000006330444111000000",
        "000000333444401100000",
        "000000033444411100000",
        "000000000444111000000",
        "000000000441110000000",
        "000000000441100000000",
        "000000000444400000000",
        "000000000444400000000",
        "000000004404440000000",
        "000000044400444000000",
        "000000444000044400000",
        "000000440000004440000",
        "000000440000000444000",
        "000000440000000044000",
        "000004440000000044000"
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            
            else:
                pass
            
    return img
def west_moving_player_pistol_2():
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
        "0000004464440000000",
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            else:
                pass
            
    return img

def north_moving_player_rifle_1():
    pattern = [
        "00000111000000",
        "00001111100000",
        "00011111110000",
        "00041111140000",
        "00004111400000",
        "00000444000000",
        "00004444400000",
        "00034444430000",
        "00034444410000",
        "00044444410000",
        "00044444410000",
        "00044444410000",
        "00054444430000",
        "00054444438000",
        "00054444460000",
        "00004444470000",
        "00004444470000",
        "00004444470000",
        "00004404460000",
        "00003304470000",
        "00003305570000",
        "00003305500000",
        "00001105500000",
        "00001105500000",
        "00011105550000"
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "9":
                img.put("#c0feff", (x,y))
            else:
                pass
            
    return img
def north_moving_player_rifle_2():
    pattern = [
        "00000111000000",
        "00001111100000",
        "00011111110000",
        "00041111140000",
        "00004111400000",
        "00000444000000",
        "00004444400000",
        "00034444430000",
        "00014444430000",
        "00014444440000",
        "00014444440000",
        "00014444440000",
        "00034444458000",
        "00034444450000",
        "00044444460000",
        "00004444470000",
        "00004444470000",
        "00004444460000",
        "00004404470000",
        "00004403300000",
        "00005503300000",
        "00005503300000",
        "00005501100000",
        "00005501100000",
        "00055501110000"
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "9":
                img.put("#c0feff", (x,y))
            else:
                pass
            
    return img
def east_moving_player_rifle_1():
    pattern = [
        "000000000110000000000",
        "000000001144000000000",
        "000000011142400000000",
        "000000014444400000000",
        "000000004444000000000",
        "000000000440000000000",
        "000000004444000000000",
        "000000004114000000000",
        "000000001114000000000",
        "000000011174000000000",
        "000000111774800000000",
        "000001107778880000000",
        "000001114477888000000",
        "000000111777786800000",
        "000000011147778000000",
        "000000001144770000000",
        "000000004444077000000",
        "000000004444007700000",
        "000000044404470770000",
        "000000444004740077000",
        "000004440000444000000",
        "000044400000044000000",
        "000444000000044000000",
        "000440000000044000000",
        "000440000000044400000"
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "9":
                img.put("#c0feff", (x,y))
            else:
                pass
            
    return img
def east_moving_player_rifle_2():
    pattern = [
        "0000000001100000000000000",
        "0000000011440000000000000",
        "0000000111424000000000000",
        "0000000144444000000000000",
        "0000000044440000000000000",
        "0000000004400000000000000",
        "0000000044440000000000000",
        "0000000041170000000000000",
        "0000000041177000800000000",
        "0000000341177708880000000",
        "0000003344110777888000000",
        "0000033044110077786800000",
        "0000033344111007778000000",
        "0000003344411170770000000",
        "0000000344441100077000000",
        "0000000044440000007700000",
        "0000000044440000070770000",
        "0000000044440000700077000",
        "0000000444044400000000000",
        "0000004440044400000000000",
        "0000044400004440000000000",
        "0000444000000440000000000",
        "0004440000000440000000000",
        "0004400000000440000000000",
        "0004400000000444000000000"
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "9":
                img.put("#c0feff", (x,y))
            else:
                pass
            
    return img
def south_moving_player_rifle_1():
    pattern = [
        "0000011100000",
        "0000144410000",
        "0001424241000",
        "0004444444000",
        "0000411140000",
        "0000044400000",
        "0000444440000",
        "0004444443000",
        "0005744443000",
        "0005744443000",
        "0005644443000",
        "0005644441000",
        "0005844441000",
        "0006844441000",
        "0005844410000",
        "0000844440000",
        "0000644440000",
        "0000644440000",
        "0007630440000",
        "0000630440000",
        "0000630550000",
        "0000640550000",
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "9":
                img.put("#c0feff", (x,y))
            else:
                pass
            
    return img
def south_moving_player_rifle_2():
    pattern = [
        "0000011100000",
        "0000144410000",
        "0001424241000",
        "0004444444000",
        "0000411140000",
        "0000044400000",
        "0000444440000",
        "0003444444000",
        "0003744444000",
        "0003644445000",
        "0001844445000",
        "0001844445000",
        "0008984445000",
        "0007844445000",
        "0000644445000",
        "0000644440000",
        "0007644440000",
        "0000644440000",
        "0000630440000",
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "9":
                img.put("#c0feff", (x,y))
            else:
                pass
            
    return img
def west_moving_player_rifle_1():
    pattern = [
        "0000000000011000000000",
        "0000000000441100000000",
        "0000000004241110000000",
        "0000000004444410000000",
        "0000000000444400000000",
        "0000000000044000000000",
        "0000008000444400000000",
        "0000088807411400000000",
        "0000888777411100000000",
        "0008687770441110000000",
        "0000877707444111000000",
        "0000077003444401100000",
        "0000770000444411100000",
        "0007700000444111000000",
        "0077070000441110000000",
        "0770007000441100000000",
        "0000000000444400000000",
        "0000000000444400000000",
        "0000000004404440000000",
        "0000000044400444000000",
        "0000000444000044400000",
        "0000000440000004440000",
        "0000000440000000444000",
        "0000000440000000044000",
        "0000004440000000044000"
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "9":
                img.put("#c0feff", (x,y))
            else:
                pass
            
    return img
def west_moving_player_rifle_2():
    pattern = [
        "00000000000011000000000",
        "00000000000441100000000",
        "00000000004241110000000",
        "00000000004444410000000",
        "00000000000444400000000",
        "00000000000044000000000",
        "00000000000444400000000",
        "00000000000411400000000",
        "00000000800411400000000",
        "00000008880111430000000",
        "00000088877114433000000",
        "00000868777114403300000",
        "00000081171114433300000",
        "00000001111144433000000",
        "00000077011444430000000",
        "00000770000444400000000",
        "00007707000444400000000",
        "00077000700444400000000",
        "00000000004404440000000",
        "00000000044400444000000",
        "00000000444000044400000",
        "00000000440000004440000",
        "00000000440000000444000",
        "00000000440000000044000",
        "00000004440000000044000"
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "9":
                img.put("#c0feff", (x,y))
            else:
                pass
            
    return img

def north_moving_player_MG_1():
    pattern = [
        "000000000011100000",
        "000000000111110000",
        "000000001111111000",
        "000000004111114000",
        "000000000411140000",
        "000000000044400000",
        "000000000444440000",
        "000000003444443000",
        "000000003444441000",
        "000000004444441000",
        "000000004444441000",
        "000000004444441000",
        "000000005444443000",
        "000000077444443000",
        "000777777444443000",
        "000777777444447000",
        "000000000444440000",
        "000000000444440000",
        "000000000440440000",
        "000000000330440000",
        "000000000330550000",
        "000000000330550000",
        "000000000110550000",
        "000000000110550000",
        "000000001110555000"
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            else:
                pass
            
    return img
def north_moving_player_MG_2():
    pattern = [
        "000000000011100000",
        "000000000111110000",
        "000000001111111000",
        "000000004111114000",
        "000000000411140000",
        "000000000044400000",
        "000000000444440000",
        "000000003444443000",
        "000000003444441000",
        "000000004444441000",
        "000000004444441000",
        "000000004444441000",
        "000000005444443000",
        "000000077444443000",
        "000777777444443000",
        "000777777444447000",
        "000000000444440000",
        "000000000444440000",
        "000000000440440000",
        "000000000440330000",
        "000000000550330000",
        "000000000550330000",
        "000000000550110000",
        "000000000550110000",
        "000000005550111000"
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
            elif pattern[y][x] == "6":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "7":
                img.put("#434343", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            else:
                pass
            
    return img
def east_moving_player_MG_1():
    pattern = [
        "0000000001100000000000000",
        "0000000011440000000000000",
        "0000000111424000000000000",
        "0000000144444000000000000",
        "0000000044440000000000000",
        "0000000004400000000000000",
        "0000000044440000000000000",
        "0000000041140000000000000",
        "0000000011140000000000000",
        "0000000111440000000000000",
        "0000001114440000000000000",
        "0000011044443300000000000",
        "0000011144443700000000000",
        "0000001114440777770000000",
        "0000000111777788777777000",
        "0000000017477765777777000",
        "0000000047770088500000000",
        "0000000044440065800000000",
        "0000000444044088500000000",
        "0000004440044465800000000",
        "0000044400004448500000000",
        "0000444000000445800000000",
        "0004440000000448500000000",
        "0004400000000440000000000",
        "0004400000000444000000000"
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
                img.put("#ffa96b", (x,y))
            elif pattern[y][x] == "6":
                img.put("#bf9000", (x,y))
            elif pattern[y][x] == "7":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            else:
                pass
            
    return img
def east_moving_player_MG_2():
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
        "0000000011440000000000000",
        "0000000011440033000000000",
        "0000000011443337000000000",
        "0000000011143307777700000",
        "0000000041117777887777770",
        "0000000044170777657777770",
        "0000000044477700885000000",
        "0000000044440000658000000",
        "0000000044440000885000000",
        "0000000444044000658000000",
        "0000004440044400885000000",
        "0000044400004440658000000",
        "0000444000000440885000000",
        "0004440000000440000000000",
        "0004400000000440000000000",
        "0004400000000444000000000"
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
                img.put("#ffa96b", (x,y))
            elif pattern[y][x] == "6":
                img.put("#bf9000", (x,y))
            elif pattern[y][x] == "7":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            else:
                pass
            
    return img
def south_moving_player_MG_1():
    pattern = [
        "000001110000000000",
        "000014441000000000",
        "000142424100000000",
        "000444444400000000",
        "000041114000000000",
        "000004440000000000",
        "000044444000000000",
        "000344444300000000",
        "000944444300000000",
        "000944444300000000",
        "000944443300000000",
        "000444133000000000",
        "000445114000000000",
        "000355555550000000",
        "000545555555555000",
        "000554655555555000",
        "000044764000000000",
        "000044684000000000",
        "000033764000000000",
        "000033684000000000",
        "000033769000000000",
        "000044689000000000",
        "000099769000000000",
        "000099089000000000",
        "000999099900000000"
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
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "7":
                img.put("#bf9000", (x,y))
            elif pattern[y][x] == "8":
                img.put("#ffa96b", (x,y))
            elif pattern[y][x] == "9":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def south_moving_player_MG_2():
    pattern = [
        "0000011100000000000",
        "0000144410000000000",
        "0001424241000000000",
        "0004444444000000000",
        "0000411140000000000",
        "0000044400000000000",
        "0000444440000000000",
        "0003444444000000000",
        "0003444449000000000",
        "0003444449000000000",
        "0003444499000000000",
        "0001444130000000000",
        "0001445110000000000",
        "0000155555550000000",
        "0000545555555555000",
        "0000554655555555000",
        "0000447640000000000",
        "0000446840000000000",
        "0000447630000000000",
        "0000446830000000000",
        "0000997630000000000",
        "0000996840000000000",
        "0000997690000000000",
        "0000990890000000000",
        "0009990999000000000"
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
                img.put("#cccccc", (x,y))
            elif pattern[y][x] == "7":
                img.put("#bf9000", (x,y))
            elif pattern[y][x] == "8":
                img.put("#ffa96b", (x,y))
            elif pattern[y][x] == "9":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def west_moving_player_MG_2():
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
        "0000000000000441100000000",
        "0000000003300441100000000",
        "0000000007333441100000000",
        "0000077777033411100000000",
        "0777777887777111400000000",
        "0777777567770714400000000",
        "0000005880077744400000000",
        "0000008560000444400000000",
        "0000005880000444400000000",
        "0000008560004404440000000",
        "0000005880044400444000000",
        "0000008560444000044400000",
        "0000005880440000004440000",
        "0000000000440000000444000",
        "0000000000440000000044000",
        "0000000004440000000044000"
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
                img.put("#ffa96b", (x,y))
            elif pattern[y][x] == "6":
                img.put("#bf9000", (x,y))
            elif pattern[y][x] == "7":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            else:
                pass
            
    return img
def west_moving_player_MG_1():
    pattern = [
        "0000000000000011000000000",
        "0000000000000441100000000",
        "0000000000004241110000000",
        "0000000000004444410000000",
        "0000000000000444400000000",
        "0000000000000044000000000",
        "0000000000000444400000000",
        "0000000000000411400000000",
        "0000000000000411100000000",
        "0000000000000441110000000",
        "0000000000000444111000000",
        "0000000000033444401100000",
        "0000000000073444411100000",
        "0000000777770444111000000",
        "0007777778877771110000000",
        "0007777775677747100000000",
        "0000000058800777400000000",
        "0000000085600444400000000",
        "0000000058804404440000000",
        "0000000085644400444000000",
        "0000000058444000044400000",
        "0000000085440000004440000",
        "0000000058440000000444000",
        "0000000000440000000044000",
        "0000000004440000000044000"
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
                img.put("#ffa96b", (x,y))
            elif pattern[y][x] == "6":
                img.put("#bf9000", (x,y))
            elif pattern[y][x] == "7":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "8":
                img.put("#cccccc", (x,y))
            else:
                pass
            
    return img

'''
def make_west_stationary_trex():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_west_stationary_raptor():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_west_stationary_trike():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_west_stationary_stego():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_east_stationary_trex():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_east_stationary_raptor():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_east_stationary_trike():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_east_stationary_stego():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_west_moving_trex_1():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_west_moving_raptor_1():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_west_moving_trike_1():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_west_moving_stego_1():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_east_moving_trex_1():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_east_moving_raptor_1():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_east_moving_trike_1():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_east_moving_stego_1():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_west_moving_trex_2():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_west_moving_raptor_2():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_west_moving_trike_2():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_west_moving_stego_2():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_east_moving_trex_2():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_east_moving_raptor_2():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_east_moving_trike_2():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
def make_east_moving_stego_2():
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
            elif pattern[y][x] == "5":
                img.put("#999999", (x,y))
            else:
                pass
            
    return img
'''
def make_helicopter():
    pattern = [
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
        "555555555555555555555555555555",
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

def vert_bullet():
    pattern = [
        "1",
        "1"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern [y][x] == "1":
                img.put("#ffa96b", (x, y))
    return img
def hori_bullet():
    pattern = [
        "11"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern [y][x] == "1":
                img.put("#ffa96b", (x, y))
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

#line drawing to show movement
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

'''
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
'''

helicopter_img = make_helicopter()

north_bullet_img = vert_bullet()
east_bullet_img = hori_bullet()
south_bullet_img = vert_bullet()
west_bullet_img = hori_bullet()

'''
def win_blink():
    global restart_text, flashID
    counter = 0
    current_color = canvas.itemcget("PLAY AGAIN", "fill")
    if current_color == "#03AE00":
        canvas.itemconfig("PLAY AGAIN", fill = "#5F0505")   
    elif current_color == "#5F0505":
        canvas.itemconfig("PLAY AGAIN", fill = "#03AE00")
    flashID = root.after(900, win_blink)
'''
    
def start():
    global current_sprite, current_sprite_img, helicopter_sprite, current_sprite_list, current_x, current_y

    #Create the player
    current_x = 300
    current_y = 300

    current_sprite_img = "south_move_1_img"

    current_sprite_list = []

    current_sprite = canvas.create_image(current_x, current_y, image = south_move_1_img, anchor = "center")
    current_sprite_list.append(current_sprite)
    helicopter_sprite = canvas.create_image(100, 100, image = helicopter_img, anchor = "center")


def restart(event):
    global alive, current_mg_bullets, current_rifle_bullets, current_pistol_bullets, rex, raptors, trikes, stegos
    canvas.delete("all")

    alive = True

    #if flashID is not None:
    #    root.after_cancel(flashID)
    #    flashID = None

    current_mg_bullets = []
    current_rifle_bullets = []
    current_pistol_bullets = []
    rex = []
    raptors = []
    trikes = []
    stegos = []
    start()

root.bind("r", restart)


def win():
    canvas.delete("all")
    canvas.create_text(VIEW_DISTANCE//2, VIEW_DISTANCE//2, text = "YOU WIN!", fill = "#5F0505", font = ("Terminal", 36))
    play_again_text = canvas.create_text(VIEW_DISTANCE//2, VIEW_DISTANCE//1.5, text = "PLAY AGAIN", fill = "#5F0505", tags = "restart_button", font = ("Terminal", 24))
    #win_blink()
    canvas.tag_bind("restart_button", "<Button-1>", restart)
    return

'''
current_x = 300
current_y = 300

current_sprite_img = "south_move_1_img"

current_sprite_list = []

current_sprite = canvas.create_image(current_x, current_y, image = south_move_1_img, anchor = "center")
current_sprite_list.append(current_sprite)
helicopter_sprite = canvas.create_image(100, 100, image = helicopter_img, anchor = "center")
'''

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
    elif HAVE_MG == False and HAVE_PISTOL == False and HAVE_RIFLE == True:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = west_moving_rifle_1_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = west_moving_rifle_2_img, anchor = "center")
        current_sprite_list.append(current_sprite)
        if px1 <= 30:
            pass
        else:
            current_x -= MOVE_SPEED
            canvas.move(current_sprite, -MOVE_SPEED, 0)
    elif HAVE_MG == False and HAVE_PISTOL == True and HAVE_RIFLE == False:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = west_moving_pistol_1_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = west_moving_pistol_2_img, anchor = "center")
        current_sprite_list.append(current_sprite)
        if px1 <= 30:
            pass
        else:
            current_x -= MOVE_SPEED
            canvas.move(current_sprite, -MOVE_SPEED, 0)
    elif HAVE_MG == True and HAVE_PISTOL == False and HAVE_RIFLE == False:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = west_moving_MG_1_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = west_moving_MG_2_img, anchor = "center")
        current_sprite_list.append(current_sprite)
        if px1 <= 30:
            pass
        else:
            current_x -= MOVE_SPEED
            canvas.move(current_sprite, -MOVE_SPEED, 0)

    #west_stationary(current_sprite)
    move_viewport()
def move_right(event):
    global current_sprite_img, current_x, current_sprite, current_sprite_list, STEP_COUNTER
    STEP_COUNTER+=1

    px1, py1, px2, py2 = canvas.bbox(current_sprite)
    if HAVE_MG == False and HAVE_PISTOL == False and HAVE_RIFLE == False:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = east_move_2_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = east_move_1_img, anchor = "center")
        current_sprite_list.append(current_sprite)
        if px2 >= WORLD_SIZE - 30:
            pass
        else:
            current_x += MOVE_SPEED
            canvas.move(current_sprite, MOVE_SPEED, 0)
    elif HAVE_MG == False and HAVE_PISTOL == False and HAVE_RIFLE == True:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = east_moving_rifle_1_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = east_moving_rifle_2_img, anchor = "center")
        current_sprite_list.append(current_sprite)
        if px2 >= WORLD_SIZE - 30:
            pass
        else:
            current_x += MOVE_SPEED
            canvas.move(current_sprite, MOVE_SPEED, 0)
    elif HAVE_MG == False and HAVE_PISTOL == True and HAVE_RIFLE == False:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = east_moving_pistol_1_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = east_moving_pistol_2_img, anchor = "center")
        current_sprite_list.append(current_sprite)
        if px2 >= WORLD_SIZE - 30:
            pass
        else:
            current_x += MOVE_SPEED
            canvas.move(current_sprite, MOVE_SPEED, 0)
    elif HAVE_MG == True and HAVE_PISTOL == False and HAVE_RIFLE == False:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = east_moving_MG_1_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = east_moving_MG_2_img, anchor = "center")
        current_sprite_list.append(current_sprite)
        if px2 >= WORLD_SIZE - 30:
            pass
        else:
            current_x += MOVE_SPEED
            canvas.move(current_sprite, MOVE_SPEED, 0)

    move_viewport()
def move_up(event):
    global current_sprite_img, current_y, current_sprite, current_sprite_list, STEP_COUNTER
    STEP_COUNTER+=1
    
    px1, py1, px2, py2 = canvas.bbox(current_sprite)
    
    if HAVE_MG == False and HAVE_PISTOL == False and HAVE_RIFLE == False:
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
    elif HAVE_MG == False and HAVE_PISTOL == False and HAVE_RIFLE == True:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = north_moving_rifle_1_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = north_moving_rifle_2_img, anchor = "center")
        current_sprite_list.append(current_sprite)
        if py1 <= 30:
            pass
        else:
            current_y -= MOVE_SPEED
            canvas.move(current_sprite, 0, -MOVE_SPEED)
    elif HAVE_MG == False and HAVE_PISTOL == True and HAVE_RIFLE == False:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = north_moving_pistol_1_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = north_moving_pistol_2_img, anchor = "center")
        current_sprite_list.append(current_sprite)
        if py1 <= 30:
            pass
        else:
            current_y -= MOVE_SPEED
            canvas.move(current_sprite, 0, -MOVE_SPEED)
    elif HAVE_MG == True and HAVE_PISTOL == False and HAVE_RIFLE == False:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = north_moving_MG_1_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = north_moving_MG_2_img, anchor = "center")
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
    
    if HAVE_MG == False and HAVE_PISTOL == False and HAVE_RIFLE == False:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = south_move_2_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = south_move_1_img, anchor = "center")
        current_sprite_list.append(current_sprite)
        if py2 >= WORLD_SIZE - 30:
            pass
        else:
            current_y += MOVE_SPEED
            canvas.move(current_sprite, 0, MOVE_SPEED)
    elif HAVE_MG == False and HAVE_PISTOL == False and HAVE_RIFLE == True:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = south_moving_rifle_1_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = south_moving_rifle_2_img, anchor = "center")
        current_sprite_list.append(current_sprite)
        if py2 >= WORLD_SIZE - 30:
            pass
        else:
            current_y += MOVE_SPEED
            canvas.move(current_sprite, 0, MOVE_SPEED)
    elif HAVE_MG == False and HAVE_PISTOL == True and HAVE_RIFLE == False:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = south_moving_pistol_1_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = south_moving_pistol_2_img, anchor = "center")
        current_sprite_list.append(current_sprite)
        if py2 >= WORLD_SIZE - 30:
            pass
        else:
            current_y += MOVE_SPEED
            canvas.move(current_sprite, 0, MOVE_SPEED)
    elif HAVE_MG == True and HAVE_PISTOL == False and HAVE_RIFLE == False:
        if len(current_sprite_list)>0:
            for i in range(len(current_sprite_list)):
                canvas.delete(current_sprite) 
        if STEP_COUNTER %2 == 0:
            current_sprite = canvas.create_image(current_x, current_y, image = south_moving_MG_1_img, anchor = "center")
        else:
            current_sprite = canvas.create_image(current_x, current_y, image = south_moving_MG_2_img, anchor = "center")
        current_sprite_list.append(current_sprite)
        if py2 >= WORLD_SIZE - 30:
            pass
        else:
            current_y += MOVE_SPEED
            canvas.move(current_sprite, 0, MOVE_SPEED)

    move_viewport()

def shoot_MG():
    #anywhere below that you see "pyimage...", it is just how the computer is reading the current sprite's image
    global mg_ammo, current_sprite_img, HAVE_MG, current_sprite
    current_sprite_img = canvas.itemcget(current_sprite, "image")
    print(current_sprite_img)
    if HAVE_MG == True:
        if len(current_mg_bullets) > 100:
            return
        px1, py1, px2, py2 = canvas.bbox(current_sprite)
        if current_sprite_img == "pyimage45" or current_sprite_img == "pyimage46":
            b = canvas.create_image((px1+px2)//2, py1, image = north_bullet_img, anchor = "n")
            current_mg_bullets.append(b)
            mg_ammo -= 1
        elif current_sprite_img == "pyimage47" or current_sprite_img == "pyimage48":
            b = canvas.create_image(px2, ((py1+py2)//2)+2, image = east_bullet_img, anchor = "e")
            current_mg_bullets.append(b)
            mg_ammo -= 1
        elif current_sprite_img == "pyimage49" or current_sprite_img == "pyimage50":
            b = canvas.create_image((px1+px2)//2, py2, image = south_bullet_img, anchor = "s")
            current_mg_bullets.append(b)
            mg_ammo -= 1
        elif current_sprite_img == "pyimage51" or current_sprite_img == "pyimage52":
            b = canvas.create_image(px1, (py1+py2)//2, image = west_bullet_img, anchor = "w")
            current_mg_bullets.append(b)
            mg_ammo -= 1
        else:
            pass
        
    else:
        pass
    print(mg_ammo)
def shoot_pistol():
    global pistol_ammo, current_sprite_img, HAVE_PISTOL
    if HAVE_MG == True:
        if len(current_mg_bullets) > 25:
            return
        pistol_ammo -= 1
    else:
        pass
def shoot_rifle():
    global rifle_ammo, current_sprite_img, HAVE_RIFLE
    if HAVE_RIFLE == True:
        if len(current_rifle_bullets) > 10:
            return
        rifle_ammo -= 1
    else:
        pass

def action(event):
    global current_sprite, helicopter_sprite, WIN
    px1, py1, px2, py2 = canvas.bbox(current_sprite)
    hx1, hy1, hx2, hy2 = canvas.bbox(helicopter_sprite)

    win_case =  px1 > hx1 and px2 < hx2 and py1 > hy1 and py2 < hy2
    if win_case == True:
        win()
    elif HAVE_MG and mg_ammo > 0:
        shoot_MG()
    elif HAVE_PISTOL and pistol_ammo > 0:
        shoot_pistol()
    elif HAVE_RIFLE and rifle_ammo > 0:
        shoot_rifle()
    #else:
    #    pass


root.bind("a", move_left)
root.bind("d", move_right)
root.bind("w", move_up)
root.bind("s", move_down)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

root.bind("<space>", action)

#def random_spawn_weapon():
#def random_spawn_ammo():
#def random_spawn_peaceful():
#def random_spawn_predator():



start()

move_viewport()
canvas.focus_set()

root.mainloop()