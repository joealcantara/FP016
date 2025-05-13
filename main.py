from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world", font_size=144)
        self.add(text)

from manim_slides import Slide

class BasicExample(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        dot = Dot()

        self.play(GrowFromCenter(circle))
        self.next_slide()  # Waits user to press continue to go to the next slide

        self.next_slide(loop=True)  # Start loop
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.next_slide()  # This will start a new non-looping slide

        self.play(dot.animate.move_to(ORIGIN))


class test2(Slide):
    def construct(self):
        self.camera.background_color = WHITE
        text = Text("FP016 - Computer Science", 
                    font_size=44,
                    font="Mononoki Nerd Font Mono",
                    color = "PURPLE_E")
        next_text = Text("Next slide",
                    font_size=44,
                    font="Mononoki Nerd Font Mono",
                    color = "PURPLE_E")
        self.play(Write(text))
        self.next_slide()
        self.play(FadeOut(text))
        self.next_slide()
        self.play(Write(next_text))

