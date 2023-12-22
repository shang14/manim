from manim import *

class moreshapes(Scene):
    def construct(self):
        title = Text("Arc, Sector, Vector, DashedLine, Arrow")
        self.play(FadeIn(title))
        self.play(FadeOut(title))
        
        shape1 = Arc()
        self.add(shape1)