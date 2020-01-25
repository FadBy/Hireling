from math import *

def convert_side_in_angle(side):
    if side == "right":
        return 0
    elif side == "up":
        return 90
    elif side == "left":
        return 180
    elif side == "down":
        return 270
    elif side == "right-up":
        return 45
    elif side == "left-up":
        return 135
    elif side == "left-down":
        return 225
    elif side == "right-down":
        return 315


def set_change_coord(angle, speed):
    if angle % 360 == 0:
        xspeed = speed
        yspeed = 0
    elif angle % 360 == 90:
        xspeed = 0
        yspeed = -speed
    elif angle % 360 == 180:
        xspeed = -speed
        yspeed = 0
    elif angle % 360 == 270:
        xspeed = 0
        yspeed = speed
    else:
        xspeed = speed / sqrt(1 + abs(tan(angle * pi / 180)))
        yspeed = xspeed * abs(tan(angle * pi / 180))
        if 90 < angle % 360 < 270:
            xspeed = -xspeed
        if 0 < angle % 360 < 180:
            yspeed = -yspeed
    return [xspeed, yspeed]
