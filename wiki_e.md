### Add to "Adding MObjects to Our Scene"

MObjects have a wide array of [methods](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#) that can be used to manipulate its features. 

Some methods which will probably be most likely used are:

`arrange`, which is used to sort MObjects next to each other.

`flip`, which flips an MObject about its center.

`move_to`, which moves the center of an MObject to the specified coordinates.

`next_to`, which moves an MObject next to another MObject.

`rotate`, which rotates an MObject about a specified point.

`scale`, which increases or decreases the MObject's size by a specified factor.


### Condensing Animation Code

If you want to create an animation that only requires using an MObject's base methods, and not any dedicated Animation class function,
then you can condense multiple `self.play()` lines into one using `animate`.

For example, the following two code blocks are identical in function.

```Python
from manim import *

class AnimateExample(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.play(circle.animate.shift(LEFT))
        self.play(circle.animate.scale(2))
        self.play(circle.animate.rotate(PI / 2))
        self.play(Uncreate(circle))
```

```Python
from manim import *

class AnimateCombinedExample(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.play(circle.animate.shift(LEFT).scale(2).rotate(PI / 2))
        self.play(Uncreate(circle))
```

Additionally, `Uncreate` can be used to animate destruction rather than a `FadeOut` transform. `Uncreate` is simply `Create`, but in reverse.


### Grouping Objects

MObjects can be grouped together in order to do things like animate dots on a graph moving together. 
Groups can be formed with `VGroup`, and any MObjects that are passed within that functions will be added to the group defined. 


```Python
from manim import *

class GroupExample(Scene):
    def construct(self):
        red_circle = Circle(color = RED)
        green_circle = Circle(color = GREEN)
        blue_circle = Circle(color = BLUE)
        
        red_circle.shift(LEFT)
        blue_circle.shift(RIGHT)
        
        group1 = VGroup(red_circle, green_circle)
        group2 = VGroup(green_circle, blue_circle)
        self.add(group1, group2)
        self.play(Create(red_circle))
        self.play(Create(green_circle))
        self.play(Create(blue_circle))
        self.play((group1 + group2).animate.shift(LEFT).scale(2))
        self.play(group2.animate.rotate(PI / 2))
        self.play(Uncreate(red_circle))
        self.play(Uncreate(green_circle))
        self.play(Uncreate(blue_circle))
```

In this example, three RGB circles are made with two groups formed from them. First they are created, then they all move left and grow by a factor of 2 because both groups were specified to move in the code. Then the green and blue circles are rotated 90 degrees because only `group2` was specified to rotate.

By utilizing groups, animating many MObjects will hopefully not be as daunting of a task.


### Displaying Text

Displaying text is pretty straightforward:

```Python
from manim import *

class TextExample(Scene):
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
```

Like the `Circle` object, we first create a `Text` object, then pass on the text that should be created. The `Text` object has additional 
parameters that can be passed on, like `font`, `font_size`, `color`, and such. 


### Displaying Mathematical Equations

Math equations and formulas go hand-in-hand in application with educational animations. However, it is incredibly difficult to read math equations written in 
normal text! This is where [LaTeX](https://www.latex-project.org/) comes in handy. LaTeX is a typesetting software system widely used in academia. It allows users to produce math equations that look good while still being intuitive. There are many tutorials on the internet regarding LaTeX if needed, whether
you are new or need a refresher.

<!---
comment: add student wiki about LaTeX here!
-->

After installing a LaTeX distribution like [PyLaTeX](https://pypi.org/project/PyLaTeX/), you will use a `Tex` object rather than a `Text` object.

Now you can create math equations and add them to your Manim animations!

```Python
equation = Text(r"$E(z,t) = \hat{x}cos(2\pi \times 10^{6}t - 7z + \frac{\pi}{2})$")
```

While LaTeX is capable of producing matrices and tables, Manim actually has built-in `Matrix` and `Table` MObjects, but if you prefer to use LaTeX,  `MathTable` is a specialized MObject for use with LaTex.
