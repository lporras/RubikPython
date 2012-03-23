#!/usr/bin/env python
from base import *

def draw_axis(max_=1.0, delta=0.5, **keys):
    gray1 = color.gray(0.5)
    gray2 = color.gray(0.6)
    labels = ('x', 'y', 'z')
    f = frame()
    for j, i in enumerate(identity(3)):
        curve(frame=f, pos=[-max_*i, max_*i],  radius=0.02, color=gray1)
        cone( frame=f, pos=max_*i, axis=0.2*i, radius=0.04, color=gray1)
        label(frame=f, pos=(max_+0.3)*i,
              text=labels[j], height=20, color=gray1, font='serif',
              line=False, box=False)
        for k in arange(-max_+delta, max_, delta):
            sphere(frame=f, pos=k*i, radius=0.03, color=gray1)
    return f


if __name__ == '__main__':
    stereo(False)
    draw_axis()
    box(  pos=( 0.0, 1, 0), color=color.red, opacity=0.5)
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
