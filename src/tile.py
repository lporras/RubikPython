#!/usr/bin/env python
from __future__ import division, print_function
from base import *


class _normal:

    def _normal_init(self, pos, normal):
        self.normal = vector(normal
                             if normal != None else
                             pos)

    def _set_normal(self, normal):
        self._normal = rint(normal)
        self.axis    = 0.5*normal
    
    normal = property(
        lambda self: self._normal,
        _set_normal)


class Arrow(arrow, _normal):

    def __init__(self,
                 pos,
                 color=color.orange,
                 normal=None,
                 frame=None):
        super(Arrow, self).__init__(
            frame=frame,
            pos=pos,
            color=color,
            opacity=0.7,
            headwidth=0.8, headlength=0.05,
            shaftwidth=0.1)
        self._normal_init(pos, normal)


class Box(frame, _normal):

    def __init__(self,
                 pos,
                 color=color.blue,
                 normal=None,
                 frame=None,colorcontorno = color.gray(0.09)):
        super(Box, self).__init__(
            frame=frame,
            pos=pos,
            color=color)
        self._normal_init(pos, normal)
        
        box(
            frame=self,
            pos=self.world_to_frame(vector(pos)),
            color=colorcontorno, opacity=1,
            width=1, height=1, length=1)
        
        self._tile = box(
            frame=self,
            pos=self.world_to_frame(vector(pos)+vector(self.axis)),
            color=color, opacity=1,
            width=0.89, height=0.89, length=0.03, material = materials.plastic)

Tile = Box

if __name__ == '__main__':
    from utils import *
    stereo(False)
    #draw_axis()
    #props = dict(color=color.white, opacity=0.6)
    #box(  pos=(0,0,1))
    #Arrow(pos=(0,0,1))
    #box(  pos=(0,1,0))
    #Box(  pos=(0,1,0))
    #box(  pos=(1,0,0))
    Tile( pos=(1,0,0), color=color.green)
