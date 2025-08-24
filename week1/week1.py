from manim import *

config.background_color = WHITE

class Title(Scene):
    def construct(self):
        self.play(Write(Text("Week 1 - Number Theory", color=ManimColor('#3C1053'), font='Calibri')))
        self.wait(1)
        rectangle = Rectangle(width=8, height=1.5, color=ManimColor('#3C1053'))
        self.play(Create(rectangle))
        self.wait(1)

        logo = ImageMobject("../assets/logo.jpg")
        logo.scale(0.1)
        logo.to_corner(DR, buff=0.5)

        self.play(FadeIn(logo))
        self.wait(2)

class slide1(Scene):
    def construct(self):
        test = Text("Why were numbers invented?", color=ManimColor('#3C1053'), font='Calibri', weight=BOLD)
        self.play(FadeIn(test))
        self.wait(1)
        self.play(FadeOut(test))

        line1 = Text("When people started living in permanent", color=ManimColor('#3C1053'), font='Calibri', font_size=36).shift(UP)
        line2 = Text("settlements, they faced new questions ", color=ManimColor('#3C1053'), font='Calibri',
                     font_size=36).next_to(line1, DOWN)
        line2a = Text("that they couldn't answer before.", color=ManimColor('#3C1053'), font='Calibri', font_size=36).next_to(line2, DOWN)
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(line2a))

        self.play(FadeOut(line1, line2, line2a))

        line3 = Text("Agriculture:", color=ManimColor('#3C1053'), font='Calibri', font_size=36).shift(UP)
        line4 = Text("How many animals do we own?", color=ManimColor('#3C1053'), font='Calibri', font_size=36).next_to(line3, DOWN)
        line5 = Text("How much grain did we harvest?", color=ManimColor('#3C1053'), font='Calibri', font_size=36).next_to(line4, DOWN)

        self.play(Write(line3))
        self.play(Write(line4))
        self.play(Write(line5))

        self.play(FadeOut(line3, line4, line5))

        line6 = Text("Commerce & Trade:", color=ManimColor('#3C1053'), font='Calibri', font_size=36).shift(UP)
        line7 = Text("What is a fair price for these tools?", color=ManimColor('#3C1053'), font='Calibri', font_size=36).next_to(line6, DOWN)
        line8 = Text("How can we keep track of who owes what?", color=ManimColor('#3C1053'), font='Calibri', font_size=36).next_to(line7, DOWN)

        self.play(Write(line6))
        self.play(Write(line7))
        self.play(Write(line8))

        self.play(FadeOut(line6, line7, line8))

        line9 = Text("Governance & Society:", color=ManimColor('#3C1053'), font='Calibri', font_size=36).shift(UP)
        line10 = Text("How many people live in our village?", color=ManimColor('#3C1053'), font='Calibri', font_size=36).next_to(line9, DOWN)
        line11 = Text("How do we fairly tax everyone to build a new wall?", color=ManimColor('#3C1053'), font='Calibri', font_size=36).next_to(line10, DOWN)

        self.play(Write(line9))
        self.play(Write(line10))
        self.play(Write(line11))

        self.play(FadeOut(line10, line11, line9))

        line12 = Text("The Solution: To answer these questions, people invented", color=ManimColor('#3C1053'), font='Calibri', font_size=36).shift(UP)
        line13 = Text("numbering systems.They are, at their core, a tool created", color=ManimColor('#3C1053'), font='Calibri', font_size=36).next_to(line12, DOWN)
        line14 = Text("to manage the complexities of living and working together.", color=ManimColor('#3C1053'), font='Calibri', font_size=36).next_to(line13, DOWN)
        self.wait(1)

        self.play(Write(line12))
        self.play(Write(line13))
        self.play(Write(line14))

        self.play(FadeOut(line12, line13, line14))
