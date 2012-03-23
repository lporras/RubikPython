#!/usr/bin/env python
from __future__ import division, print_function
from tile import *

front  = ( 0, 0, 1)
back   = ( 0, 0,-1)
top    = ( 0, 1, 0)
bottom = ( 0,-1, 0)
right  = ( 1, 0, 0)
left   = (-1, 0, 0)
face_properties = (
    ('f', front , color.orange),
    ('b', back  , color.red),
    ('u', top   , color.white),
    ('d', bottom, color.yellow),
    ('r', right , color.green),
    ('l', left  , color.blue),
    )
face_properties_jp = (
    ('f', front , color.orange),
    ('b', back  , color.red),
    ('u', top   , color.white),
    ('d', bottom, color.blue),
    ('r', right , color.green),
    ('l', left  , color.yellow),
    )
keys = ''.join(p[0] for p in face_properties)


def add_centers(self):
    self.centers = {}
    for k, p, c in face_properties:
        obj = Tile(frame=self, pos=p, color=c, colorcontorno = color.black)
        obj.key = k
        self.centers[k] = obj


if __name__ == '__main__':
    stereo(False)
    cube = frame()
    add_centers(cube)
    print(cube.centers)
