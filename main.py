from manim.constants import Vector3D
from manim_slides import Slide
from manim_slides.slide import MANIM, MANIMGL

from manim import *
import numpy as np


class PartialInt(Slide):
    def construct(self):
        integral_sum = MathTex(r"{\int", r"{e^x}", r"+", r"{", r"{\sin x}", r"\mathrm{d}x}", tex_to_color_map={r"e^x": BLUE, r"\sin x": RED})
        integral_product = MathTex(r"\int e^x \cdot {\sin x} \mathrm{d}x", tex_to_color_map={r"e^x": BLUE, r"\sin x": RED})

        integral_sum.move_to(UP * 1 + LEFT * 1.5)
        integral_product.next_to(integral_sum, RIGHT, buff = 2)

        self.play(Write(integral_sum), Write(integral_product))
        self.next_slide()

        integral_sum_copy = integral_sum.copy().move_to(DOWN * 0.5 + LEFT * 1.5)
        self.play(TransformMatchingTex(integral_sum.copy(), integral_sum_copy))
        self.next_slide()

        split_integrals = MathTex(r"{\int", r"{e^x}", r"\mathrm{d}x}", r"+", r"{\int", r"{\sin x}", r"\mathrm{d}x}", tex_to_color_map={r"e^x": BLUE, r"\sin x": RED}).move_to(DOWN * 0.5 + LEFT * 1.5)
        self.play(TransformMatchingTex(integral_sum_copy, split_integrals))
        self.next_slide()

        solved_integrals = MathTex(r"{e^x}", r"+", r"{(-\cos x)}", r" + C", tex_to_color_map={r"e^x": BLUE, r"(-\cos x)": RED}).move_to(DOWN * 0.5 + LEFT * 1.5)
        self.play(Unwrite(split_integrals[0]),
                  Unwrite(split_integrals[4]),
                  Unwrite(split_integrals[6]),
                  Unwrite(split_integrals[9]))
        self.play(ReplacementTransform(split_integrals[2], solved_integrals[1]),
                  ReplacementTransform(split_integrals[5], solved_integrals[3]),
                  ReplacementTransform(split_integrals[6], solved_integrals[4]),
                  ReplacementTransform(split_integrals[8], solved_integrals[5]),
                  ReplacementTransform(split_integrals[10], solved_integrals[7])
                  )
        self.next_slide()

        question_marks = MathTex("???").next_to(solved_integrals, RIGHT, buff = 2)
        self.play(Write(question_marks))
        self.next_slide()

        self.play(Unwrite(integral_sum), Unwrite(integral_product), Unwrite(solved_integrals), Unwrite(question_marks))        
        title = Text("Partielle Integration", gradient=(ManimColor("#AA00FF"), ManimColor("#0066FF"))).scale(2)
        subtitle = Text("GFS von Amy", color=GRAY).scale(1)
        subtitle.move_to(DOWN * 1.5)
        self.play(Write(title), Write(subtitle))
        self.next_slide()

        integral_text = MathTex(r"\int f(x) \mathrm{d}x := \text{Stammfunktionen von } f(x)", color=GRAY, tex_to_color_map={
            r"\int": RED,
            r"f(x)": BLUE,
            r"\mathrm{d}x": RED,
        }).scale(1.25)

        self.play(Unwrite(title), Unwrite(subtitle))
        self.play(Write(integral_text))
        self.next_slide()

        integral = MathTex(r"\int", r"f'(x)", r"\mathrm{d}x", r":=", r"f(x)", r"+", r"C", tex_to_color_map={
            r"\int": RED,
            r"f'(x)": BLUE,
            r"\mathrm{d}x": RED,
            r"f(x)": BLUE,
            r"C": RED,
        })

        integral_text_copy = integral_text.copy().move_to(UP * 3)
        integral.next_to(integral_text_copy, DOWN, buff = 0.5)
        self.play(Transform(integral_text, integral_text_copy))
        self.play(Write(integral))
        self.next_slide()

        integral_squared = MathTex(r"\int 2x \mathrm{d}x = x^2 + C", tex_to_color_map={
            r"\int": RED,
            r"2x": BLUE,
            r"\mathrm{d}x": RED,
            r"x^2": BLUE,
            r"C": RED,
        })
        integral_cos = MathTex(r"\int \cos x \mathrm{d}x = \sin x + C", tex_to_color_map={
            r"\int": RED,
            r"\cos x": BLUE,
            r"\mathrm{d}x": RED,
            r"\sin x": BLUE,
            r"C": RED,
        })
        
        integral_squared.move_to(DOWN * 2 + LEFT * 3)
        integral_cos.move_to(DOWN * 2 + RIGHT * 3)

        self.play(Transform(integral.copy(), integral_squared), Transform(integral.copy(), integral_cos))
        self.next_slide()
