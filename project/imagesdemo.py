from manim import *
import itertools as it

class imagesdemo(Scene):
    def construct(self):
        title = Text("Images and SVGs")
        self.play(FadeIn(title))
        self.wait(3)
        self.play(FadeOut(title))
        
        blueOrange = ImageMobject("./images.jpeg")
        self.play(FadeIn(blueOrange))
        self.play(FadeOut(blueOrange))
        
        umbrella = SVGMobject("./svgs.svg")
        #self.play(FadeIn(umbrella))
        
        colors = it.cycle([BLACK, ORANGE])
        print("Processing SVG...")
        i = 0
        svgLayers = []
        for layer in umbrella:
            print("Current Layer: ", i)
            color = next(colors)
            svgLayers.append(layer.set_color(color).scale(3))
            
            i += 1
        print("Finished Processing SVG!")
        
        
        self.wait()