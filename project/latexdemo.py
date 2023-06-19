from manim import *

class latex(Scene):
    
    
    def construct(self):
        text_parameters = {
            "color" : RED,
            "opacity": 0.7,
        }
        
        title = Text("Text, Latex", **text_parameters)
       
        self.play(FadeIn(title)) 
        self.wait(3)
        
        self.play(FadeOut(title)) 
        
        groceries = Text("Cheese, Tomatoes, Bread, Yeast").set_color(RED)
        self.add(groceries)
        self.wait(2)
        self.remove(groceries)
        
        groceries2 = Text("""
            - Cheese
            - Lettuce
            - Tomatoes
                           
                           
            """)
        
        self.add(groceries2)
        
        self.wait(2)
        self.remove(groceries2)
        
        equation = MathTex(r"\begin{Bmatrix}1 & 2 & 3\\a & b & c\end{Bmatrix}")
        self.play(Write(equation))
        self.wait()
        
        textintex = MathTex(r"\text{This is Text in LaTex}").shift(DOWN * 3)
        self.add(textintex)
        self.wait()
        
        
        