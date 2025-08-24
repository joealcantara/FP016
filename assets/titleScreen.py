from manim import *

config.background_color = WHITE

class Title(Scene):
    def construct(self):
        self.play(Write(Text("Week Number - Title", color=ManimColor('#3C1053'), font='Calibri')))
        self.wait(1)
        rectangle = Rectangle(width=8, height=1.5, color=ManimColor('#3C1053'))
        self.play(Create(rectangle))
        self.wait(1)

        logo = ImageMobject("logo.jpg")
        logo.scale(0.1)
        logo.to_corner(DR, buff=0.5)

        self.play(FadeIn(logo))
        self.wait(2)
