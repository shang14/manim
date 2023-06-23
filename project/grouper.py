from manim import *

class grouper(Scene):
    
    
    def construct(self):
        text_parameters = {
            "color" : RED,
            "opacity": 0.7,
        }
        
        title = Text("Grouping MObject", **text_parameters)
       
        self.play(FadeIn(title)) 
        self.wait(3)
        
        self.play(FadeOut(title)) 
        
        
        
    