#!/usr/bin/env python
from __future__ import division, print_function
from contextlib import contextmanager
from centers import *

D90 = pi/2
front = vector(0, 0, 1)
poses = ((-1, 1, 1), ( 0, 1, 1), ( 1, 1, 1),
         (-1, 0, 1),             ( 1, 0, 1),
         (-1,-1, 1), ( 0,-1, 1), ( 1,-1, 1) )
frame_rate = 80
frames_per_rotate = 30

def set_rotation_time(sec):
    global frames_per_rotate
    frames_per_rotate = int(frame_rate * sec + 0.5)


def rotate_args(pos0, pos1):
    '''returns angle, axis'''
    pos0 = vector(pos0)
    pos1   = vector(pos1)
    if all(pos0 == pos1):
        axis = vector(0, 1, 0)
        angle = 0
    elif all(pos0 == -pos1):
        axis = vector(0, 1, 0)
        angle = 2*D90
    else:
        axis  = cross(pos0, pos1)
        angle = D90
    return angle, axis


def rotate_animate(frame, angle, axis):
    if angle == 0: return
    
    da = angle/frames_per_rotate
    for i in range(frames_per_rotate):
        rate(frame_rate)
        frame.rotate(angle=da, axis=axis)


def rotate(frame, angle, axis):
    frame.rotate(angle=angle, axis=axis)


@contextmanager
def as_front(self, center):
    angle, axis = rotate_args(center.pos, front)
    _rotate = (rotate_animate if self.animate else rotate)
    _rotate(self, angle, axis)
    yield
    #scene.mouse.getclick()
    _rotate(self, -angle, axis)


def add_edges(self):
    for center in tuple(self.centers.values()):
        with as_front(self, center):
            normal = rint(self.world_to_frame(front))
            for pos in poses:
                if self.animate: rate(8)
                obj = Tile(frame=self,
                           pos=rint(self.world_to_frame(pos)),
                           normal=normal,
                           color=center.color, colorcontorno = color.black)
                obj.key = center.key
        

if __name__ == '__main__':
    stereo(False)
    cube = frame(animate=True)
    set_rotation_time(0.5)
    add_centers(cube)

    #scene.mouse.getclick()
    add_edges(cube)
    #for obj in cube.objects: print(obj.pos, obj.axis)
