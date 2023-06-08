from manim import *

class someShapes(Scene):
    def construct(self):
        title = Text("Square, Circle, Dot, Rectangle, Line, Ellipse, Triangle").scale(0.7)
        self.play(FadeIn(title))
        self.wait(3)
        self.play(FadeOut(title))
        
        
        theShapes = []
        theShapes.append( Square(fill_opacity=1).shift(RIGHT*4).set_color(GREEN) )
        theShapes.append( Dot().shift(LEFT*4) )
        theShapes.append( Circle(fill_opacity=1).shift(DOWN*2).set_color(BLUE))
        theShapes.append( Rectangle(width=0.2, height=0.5, fill_opacity=0.5).shift(UP*2).set_color(ORANGE))
        
        for i in theShapes:
            self.play(FadeIn(i))
        
        self.wait(3)    
        self.play(FadeOut(Group(*self.mobjects)))
        
        
        theShapes2 = []
        theShapes2.append( Line([-1, -1, 0], [2, 3, 0]) )
        theShapes2.append( Ellipse(width=0.5, height=1, arc_center=[-1, 0, 0], fill_opacity=0.7).shift(DOWN*2).set_color(GREEN) )
        theShapes2.append( Triangle( fill_opacity=0.8 ).shift(UP*2).set_color(GREY).scale(0.8) )
        
        for i in theShapes2:
            self.play(FadeIn(i))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))