from manim import *
import numpy as np 

class moreshapes(Scene):
    def construct(self):
        title = Text("Arc, Sector, Vector, DashedLine, Arrow")
        self.play(FadeIn(title))
        self.play(FadeOut(title))
        
        shape1 = Arc(start_angle= np.pi/2 + np.pi/3, angle=np.pi)
        self.add(shape1)
        self.wait(2)
        self.remove(shape1)
        
        shape2 = Sector(start_angle= np.pi/2 + np.pi/3, angle=np.pi)
        self.add(shape2)
        self.wait(2)
        self.remove(shape1)
        
        shape3 = Vector(direction=[3, 1, 0])
        shape4 = Vector(direction=[3, 2, 0], color=GREEN)
        shape5 = Vector(direction=[3, 3, 0], color = YELLOW)
        shape6 = Vector(direction=[3, 4, 0], color = RED)
        self.add(shape3)
        self.add(shape4)
        self.add(shape5)
        self.add(shape6)
        self.wait(2)
        