from manim import *
import numpy as np

class twodgraphs(Scene):
    
    def construct(self):
        title = Text("Axes, NumberPlane, Complex Plane")
        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeOut(title))
        
        a1 = Axes()
        a1.add_coordinates()
        self.play(FadeIn(a1))
        self.wait(2)
        self.play(FadeOut(a1))
        