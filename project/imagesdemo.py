from manim import *

class imagesdemo(Scene):
    def construct(self):
        title = Text("Images and SVGs")
        self.play(FadeIn(title))
        self.wait(3)
        self.play(FadeOut(title))