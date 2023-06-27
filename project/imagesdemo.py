from manim import *

class imagesdemo(Scene):
    def construct(self):
        title = Text("Images and SVGs")
        self.play(FadeIn(title))
        self.wait(3)
        self.play(FadeOut(title))
        
        blueOrange = ImageMobject("./images.jpeg")
        self.play(FadeIn(blueOrange))
        
        umbrella = SVGMobject("./svgs.svg")
        self.play(FadeIn(umbrella))
        
        self.wait()