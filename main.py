import pyautogui as pg
import time
#import numpy as np

# position
p_dino = (86, 647)
p_tree = (370, 278)
p_crow = (174, 650)
p_replay = (483, 236)
p_eye = (223, 250)

#colors
white = (247, 247, 247)
dead_eye = (216, 216, 216)

#dino action
def play():
    pg.moveTo(p_replay[0], p_replay[1])
    pg.click()
    pg.press('space')

def jump():
    pg.keyDown('space')
    time.sleep(0.00005)
    pg.keyUp('space')

def crouch():
    #crouch for a second
    pg.keyDown('down')
    time.sleep(1)
    pg.keyUp('down')

#check Obstcle
def issafe():
    if(pg.pixel(p_tree[0], p_tree[1]) == white):
        return True
    return False

def isdead():
    if(pg.pixel(p_eye[0], p_eye[1]) == dead_eye):
        return True
    else:
        return False

# restart the  game
def restartGame():
    pg.click(p_replay[0], p_replay[1])
    pg.press('space')

def main():
    #start the game
    play()                                    
    #pg.moveTo(195, 664)
    while(True):
        if(issafe()):
            if(isdead()):
                restartGame()
            else:
                continue
        else:
            jump()
main()