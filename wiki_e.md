# Add to "Adding MObjects to Our Scene"

MObjects have a wide array of methods that can be used to manipulate its features.




# Displaying Text

Displaying text is pretty straightforward:

`
from manim import *

class MyScene(Scene):
    def construct(self):
        line1 = Text("You can use Manim")
        line2 = Text("to create animations like these")
        line3 = Text("Cool, right?")
        
        line2.next_to(line1, DOWN)
        
        self.play(Write(line1))
        self.wait(1)
        self.play(Write(line2))
        self.wait(1)
        self.play(FadeOut(line1), FadeOut(line2))
        self.wait(1)
        self.play(Write(line3))
`

Like the Circle object, we first create a Text object, then pass on the text that should be created. The Text object has additional 
parameters that can be passed on, like font, font size, color, and such. 
