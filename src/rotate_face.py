#!/usr/bin/env python
from __future__ import division, print_function
from edges import *

hand = frame()


def rotate_face(self, center, clockwise=False):
    angle, axis = rotate_args(front, center.pos)
    hand.rotate(angle=angle, axis=axis)
    front_poses = tuple(tuple(rint(hand.frame_to_world(pos)))
                        for pos in poses+(front,))
    pieces = [obj
              for obj in self.objects
              if tuple(rint(obj.pos)) in front_poses]
    for obj in pieces:
        obj.pos    = hand.world_to_frame(obj.pos)
        obj.normal = hand.world_to_frame(obj.normal)
        obj.frame  = hand

    (rotate_animate if self.animate else rotate)(
        hand, (-D90 if clockwise else D90), hand.frame_to_world(front))

    for obj in pieces:
        obj.pos    = hand.frame_to_world(obj.pos)
        obj.normal = hand.frame_to_world(obj.normal)
        obj.pos    = rint(self.world_to_frame(obj.pos))
        obj.normal = rint(self.world_to_frame(obj.normal))
        obj.frame  = self
    hand.rotate(angle=-angle, axis=axis)


if __name__ == '__main__':
    stereo(False)
    cube = frame(animate=False)
    add_centers(cube)
    add_edges(cube)
    cube.animate = True
    for key in keys:
        scene.mouse.getclick()
        rotate_face(cube, cube.centers[key], False)
    for key in keys:
        scene.mouse.getclick()
        rotate_face(cube, cube.centers[key], True)
