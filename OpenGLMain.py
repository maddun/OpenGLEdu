# -*- coding: utf-8 -*-
__author__ = 'comp124'

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

rot = 0.0

def InitGl (Width, Height):
    """OpenGL initialization
    """
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth (1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)

def ResizeGlScene(Width, Height):
    """ Window Resize
    """
    if Height == 0:
        Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGlScene():
    """ Draw Scene
    """
    global rot
    rot = ((rot + 1)%360)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0,0.0,-10.0)
    glRotatef(rot/10.0,1.0,0.0,0.0)
    glRotatef(rot/10.0,0.0,1.0,0.0)
    glRotatef(rot/15.0,0.0,0.0,1.0)
    glColor4f(0.0,0.7,0.1,1)
    glutSolidCube(3)
    glutSwapBuffers()

def KeyPressed(*args):
    if args[0]=="\033": sys.exit()

def __main__():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(400, 300)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("OpenGL demo")
    glutDisplayFunc(DrawGlScene)
    glutIdleFunc(DrawGlScene)
    glutReshapeFunc(ResizeGlScene)
    glutKeyboardFunc(KeyPressed)
    InitGl(400, 300)
    glutMainLoop()

__main__()