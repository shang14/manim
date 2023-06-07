from manim import *

class add(Scene):
    
    
    def construct(self):
        text_parameters = {
            "color" : RED,
            "opacity": 0.7,
        }
        
        title = Text("Add, Remove, Wait, and Play", **text_parameters)
        self.add(title)
        self.wait(3)
        self.remove(title)
        self.wait(2)
        self.play(FadeIn(title)) 
        self.wait()