from manim import *

class someShapes(Scene):
    def construct(self):
        title = Text("Square, Circle, Dot, Rectangle, Line, Ellipse, Triangle").scale(0.7)
        self.play(FadeIn(title))
        #self.wait(3)
        self.play(FadeOut(title))
        
        theShapes = []
        theShapes.append( Square().shift(RIGHT*4) )
        theShapes.append( Dot().shift(LEFT*4) )
        theShapes.append( Circle().shift(DOWN*2))
        theShapes.append( Rectangle().shift(UP*2))
        
        for i in theShapes:
            self.play(FadeIn(i))
        