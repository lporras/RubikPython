#!/usr/bin/env python
from __future__ import division, print_function
from contextlib import contextmanager
from random import choice, randint
from rotate_face import *
from aestrella import Aestrella

@contextmanager
def save_animate(self, sw):
    animate = self.animate
    self.animate = sw
    yield
    self.animate = animate


def get_center(self, key):
    k = key.lower()
    clockwise = k != key
    center = self.centers.get(k, None)
    return center, clockwise


def undo(self, history):
    if not history:
        return
    key = history.pop(-1)
    key = (key.lower()
          if key.isupper() else
         key.upper())
    center, clockwise = get_center(self, key)
    rotate_face(self, center, clockwise)
    
def undo_solve(self, history):
    if not history:
        return
    key = history.pop(-1)
    center, clockwise = get_center(self, key)
    rotate_face(self, center, clockwise)


def undo_all(self, history):
    while history:
        undo(self, history)


def solve(self, animate=False):
    
    mensaje = '''Solucionando...'''
    mensaje2 = '''Solucionado'''
    legenda = label(pos=(2.5,1,2),
                   text=mensaje,
                   color=color.white,
                   height=12,
                   line=True, box=True,
                   visible=True,
                   )
    estrellita = Aestrella()
    cadena = ''.join(self.history)+''.join(self.script)
    cadena = cadena.strip()
    a = estrellita.start(cadena)
    a = a.strip()

    print('Secuencia Desorden: '+''.join(self.history)+''.join(self.script))
    print('Solucion: '+a)
    a = a[::-1]
    self.history = []
    self.script = []
    legenda.text = mensaje2

    for h in a:
        self.history.append(h)
    
    with save_animate(self, animate):
        
        while self.history:
            undo_solve(self, self.history)
    legenda.visible = False
            


def rotate_face_by(self, key, history):
    center, clockwise = get_center(self, key)
    if center:
        rotate_face(self, center, clockwise)
        history.append(key)
        #print('movimiento '+key)
    return center


def do_script(self, script):
    set_rotation_time(0.3)
    for key in script:
        rotate_face_by(self, key, self.script)

def randomize(self, N):
    undo_all(self, self.script)
    undo_all(self, self.history)
    script = random_script(N or randint(1,6))
    
    with save_animate(self, True):
        do_script(self, script)
    print(''.join(self.script))


Legend = '''Presione 0 para Aleatorio, sS:Solucionar, zZ:Deshacer, ?:Ayuda
f|b|u|d|r|l: Rotar Anti-Horario, F|B|U|D|R|L: Rotar Horario'''



def main(script):
    #stereo(True)
    legend = label(pos=(-1,2.5,-2),
                   text=Legend,
                   color=color.white,
                   height=12,
                   line=True, box=True,
                   visible=True,
                   )
    cube = frame(animate=False,
                 history=[],
                 script=[])
    add_centers(cube)
    add_edges(cube)
    cube.animate = True
    do_script(cube, script)
    while True:
        key = scene.kb.getkey()
        if key == '?':
            legend.visible = not legend.visible
        elif key == 'S':
            solve(cube)
        elif key == 's':
            solve(cube, True)
        elif key == 'z':
            undo(cube, cube.history)
        elif key == 'Z':
            undo_all(cube, cube.history)
        elif key.isdigit():
            randomize(cube, int(key))
        else:
            rotate_face_by(cube, key, cube.history)


def random_script(N=10):
    script = ""
    ch = last = ""
    ctr = 1
    KEYS = keys.upper()
    for i in range(N):
        ch = choice(KEYS)
        if ch == last:
            ctr += 1
        if 3 < ctr:
            while ch == last:
                ch = choice(KEYS)
            last = ch
            ctr = 1
        script = script + ch
    
    return script

if __name__ == '__main__':
    import sys
    N = (int(sys.argv[1])
         if 1 < len(sys.argv) else
         0)
    script = random_script(N)
    main(script)
