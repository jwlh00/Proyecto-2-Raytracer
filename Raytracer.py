from re import I
from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *
import random


def seq(start, stop, step=1):
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    elif n == 1:
        return([start])
    else:
        return([])

width = 512
height = 512

# Materiales
whiteStar = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = OPAQUE)
greyStar = Material(diffuse = (0.5, 0.5, 0.5), spec = 16, ior = 1.5, matType = TRANSPARENT)
mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)
marble = Material(spec = 64, texture = Texture("whiteMarble.bmp"), matType= REFLECTIVE)
rtx = Raytracer(width, height)

rtx.envMap = Texture("witch.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-5,-3,-7), intensity = 0.5 ))
rtx.lights.append( PointLight(point = (-1,-1,0) ))


xList = seq(-12,-0.5,0.5)
yList = seq(-2,14,0.5)

for y in yList:
    for x in xList:
        rand = random.randint(1,10)
        if (rand > 6):
            rand2 = random.randint(1,10)
            if (rand2 == 1):
                rtx.scene.append( Disk(position = (x-0.3,y+0.5,-7), radius = 0.1, normal = (0,0,1), material = whiteStar ))
            elif (rand == 2):
                rtx.scene.append( Disk(position = (x-0.5,y+0.4,-7), radius = 0.1, normal = (0,0,1), material = whiteStar ))
            elif (rand == 3):
                rtx.scene.append( Disk(position = (x+0.2,y+0.3,-7), radius = 0.1, normal = (0,0,1), material = whiteStar ))
            elif (rand == 4):
                rtx.scene.append( Disk(position = (x+0.4,y+0.2,-7), radius = 0.1, normal = (0,0,1), material = whiteStar ))
            elif (rand == 5):
                rtx.scene.append( Disk(position = (x+0.2,y+0.1,-7), radius = 0.1, normal = (0,0,1), material = whiteStar ))
            elif (rand == 5):
                rtx.scene.append( Disk(position = (x+0.2,y,-7), radius = 0.1, normal = (0,0,1), material = whiteStar ))
            elif (rand == 6):
                rtx.scene.append( Disk(position = (x+0.2,y-0.5,-7), radius = 0.1, normal = (0,0,1), material = whiteStar ))
            elif (rand == 7):
                rtx.scene.append( Disk(position = (x+0.2,y-0.4,-7), radius = 0.1, normal = (0,0,1), material = whiteStar ))
            elif (rand == 8):
                rtx.scene.append( Disk(position = (x+0.4,y-0.3,-7), radius = 0.1, normal = (0,0,1), material = whiteStar ))
            elif (rand == 9):
                rtx.scene.append( Disk(position = (x-0.3,y-0.2,-7), radius = 0.1, normal = (0,0,1), material = whiteStar ))
            elif (rand == 10):
                rtx.scene.append( Disk(position = (x+0.1,y-0.1,-7), radius = 0.1, normal = (0,0,1), material = greyStar ))
            

rtx.scene.append( Disk(position = (-5.5,-4,-7), radius = 3, normal = (0,0,1), material = glass ))
rtx.scene.append( Disk(position = (9,7.5,-7), radius = 7, normal = (0,0,1), material = glass ))

rtx.scene.append( AABB(position = (5.5,-14,-10), size = (8,5,2), material = marble))

rtx.scene.append( Disk(position = (-3,-6,-5), radius = 2, normal = (1,0,0), material = mirror ))
rtx.scene.append( Disk(position = (8,-6,-5), radius = 2, normal = (1,0,0), material = mirror ))


rtx.glRender()

rtx.glFinish("output.bmp")
