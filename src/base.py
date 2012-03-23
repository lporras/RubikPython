#!/usr/bin/env python
from visual import *
#center_light       = local_light(pos=( 0, 0, 0), color=color.blue)
top_left_light     = local_light(pos=(-5, 5, 5), color=color.gray(1.0))
bottom_right_light = local_light(pos=( 5,-5,-5), color=color.gray(0.8))
scene.title = 'Laboratorio Inteligencia'
scene.x = 200
scene.y =  50
scene.width  = 600
scene.height = 600
scene.autoscale = False
scene.background = color.white
scene.range   = ( 3.4, 3.4, 3.4)
scene.forward = (-2.5,-3.2,-4.0)
color.orange = (1, 0.4, 0)
color.green = (0, 10, 0)
color.blue = (0.2, 0.2, 0.9)
color.red = (1,0,0)
color.white = (0.9,0.9,0.9)


def stereo(fullscreen=True,
           scene=scene,
           stereodepth=0,
           dpi=105,
           ):
    scene.visible = False
    if fullscreen:
        method = 'crosseyed'
    else:
        method = 'passive'
        scene.width  = dpi / 2.54 * 6 * 2 # / inch * cm * 3D
        scene.height = 480
    scene.stereo = method
    scene.stereodepth = stereodepth
    scene.fullscreen = fullscreen
    scene.visible = True


if __name__ == '__main__':
    stereo(False)
    box(  pos=( 0.0, 1, 0), color=color.red, opacity=0.8)
    helix(pos=(-0.5,-1, 0), color=color.yellow)
    scene.mouse.getclick()
    scene.visible = False
    s = scene
    win_props = s.x, s.y
    stereo(True)
    scene.visible = True
    scene.mouse.getclick()
    scene.visible = False
    s.x, s.y = win_props
    stereo(False)
    scene.visible = True
