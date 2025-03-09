from manim.constants import Vector3D
from manim_slides import Slide
from manim_slides.slide import MANIM, MANIMGL

from manim import *


class PartialInt(Slide):
    def construct(self):
        integral_sum = MathTex(r"{\int", r"{e^x}", r"+", r"{", r"{\sin x}", r"\mathrm{d}x}", tex_to_color_map={r"e^x": BLUE, r"\sin x": RED})
        integral_product = MathTex(r"\int e^x \cdot {\sin x} \mathrm{d}x", tex_to_color_map={r"e^x": BLUE, r"\sin x": RED})

        integral_sum.move_to(UP * 1 + LEFT * 1.5)
        integral_product.next_to(integral_sum, RIGHT, buff = 2)

        self.next_slide()
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
        
        integral_copy_1 = integral.copy()
        integral_copy_2 = integral.copy()
        self.play(Transform(integral_copy_1, integral_squared), Transform(integral_copy_2, integral_cos))
        self.remove(integral_copy_1)
        self.remove(integral_copy_2)
        self.remove(integral_text)
        self.next_slide()

        self.play(
            Unwrite(integral),
            Unwrite(integral_text_copy),
            Unwrite(integral_squared),
            Unwrite(integral_cos),
        )
        self.next_slide()

        # Usage
        usage_int = MathTex(r"\int ", r"x", r"\cdot", r"\ln x", r"\mathrm{d}x")
        usage_int.move_to(UP * 2)

        self.play(Write(usage_int))
        self.next_slide()
        
        usage_sol_1 = MathTex(r"=\frac{1}{2}x^2", r"\cdot", r"\ln x", r"- \int", r"\frac{1}{2}x^2", r"\cdot", r"\frac{1}{x}", r"\mathrm{d}x")
        usage_sol_1.next_to(usage_int, DOWN)
        usage_int[1].set_color(RED)
        usage_sol_1[0].set_color(RED)
        usage_int_copy = usage_int.copy()[1]
        self.play(Transform(usage_int_copy, usage_sol_1[0]))
        self.next_slide()
        
        usage_int[1].set_color(WHITE)
        usage_sol_1[0].set_color(WHITE)
        usage_int[3].set_color(BLUE)
        usage_sol_1[2].set_color(BLUE)
        self.remove(usage_int_copy)
        usage_int_copy = usage_int.copy()[3]
        self.add(usage_int[1])
        self.add(usage_sol_1[0])
        self.play(Transform(usage_int_copy, usage_sol_1[2]), Write(usage_sol_1[1]))
        self.next_slide()

        usage_int[3].set_color(WHITE)
        usage_sol_1[2].set_color(WHITE)
        usage_int[1].set_color(RED)
        usage_sol_1[4].set_color(RED)
        self.remove(usage_int_copy)
        usage_int_copy = usage_int.copy()[1]
        self.add(usage_int[3])
        self.add(usage_sol_1[2])
        self.play(Transform(usage_int_copy, usage_sol_1[4]), Write(usage_sol_1[3]))
        self.next_slide()

        usage_int[1].set_color(WHITE)
        usage_sol_1[4].set_color(WHITE)
        usage_int[3].set_color(BLUE)
        usage_sol_1[6].set_color(BLUE)
        self.remove(usage_int_copy)
        usage_int_copy = usage_int.copy()[3]
        self.add(usage_int[1])
        self.add(usage_sol_1[4])
        self.play(Transform(usage_int_copy, usage_sol_1[6]), Write(usage_sol_1[5]), Write(usage_sol_1[7]))
        self.next_slide()

        usage_int[3].set_color(WHITE)
        usage_sol_1[6].set_color(WHITE)
        usage_sol_2 = MathTex(r"=\frac{1}{2}x^2", r"\cdot", r"\ln x", r"- \int", r"\frac{1}{2}x", r"\mathrm{d}x")
        usage_sol_2.next_to(usage_sol_1, DOWN)
        self.remove(usage_int_copy)
        usage_sol_1_copy = usage_sol_1.copy()
        self.add(usage_int[3])
        self.add(usage_sol_1[6])
        self.play(Transform(usage_sol_1_copy, usage_sol_2))
        self.next_slide()

        usage_sol_3 = MathTex(r"=\frac{1}{2}x^2", r"\cdot", r"\ln x", r"- \frac{1}{4}x^2", r"+C")
        usage_sol_3.next_to(usage_sol_2, DOWN)
        usage_sol_2_copy = usage_sol_2.copy()
        self.play(Transform(usage_sol_2_copy, usage_sol_3))
        self.next_slide()

        self.remove(usage_sol_1_copy)
        self.remove(usage_sol_2_copy)
        self.play(
            Unwrite(usage_int),
            Unwrite(usage_sol_1),
            Unwrite(usage_sol_2),
            Unwrite(usage_sol_3)
        )
        self.next_slide()

        # Proof
        tautology_1 = MathTex(r"\int (", r"F(x) \cdot g(x)", r")' \mathrm{d}x", r" = ", r"\int", r"(", r"F(x)", r"\cdot", r"g(x)", r")'", r"\mathrm{d}x")
        self.play(Write(tautology_1))
        self.next_slide()

        tautology_2 = MathTex(r"F(x) \cdot g(x)", r" = ", r"\int", r"f(x)", r"\cdot", r"g(x)", r"+", r"F(x)", r"\cdot", r"g'(x)", r"\mathrm{d}x")
        tautology_1_4_copy = tautology_1[4].copy()
        tautology_1_6_copy = tautology_1[6].copy()
        self.play(
            Unwrite(tautology_1[0]),
            Unwrite(tautology_1[2]),
            Unwrite(tautology_1[5]),
            Unwrite(tautology_1[7]),
            Unwrite(tautology_1[9]),
            Unwrite(tautology_1[10]),
        )
        self.play(
            Transform(tautology_1[1], tautology_2[0]),
            Transform(tautology_1[3], tautology_2[1]),
            Transform(tautology_1_4_copy, tautology_2[3]),
            Transform(tautology_1_6_copy, tautology_2[5]),
            Transform(tautology_1[4], tautology_2[7]),
            Transform(tautology_1[6], tautology_2[9]),
            Transform(tautology_1[8], tautology_2[10]),
        )
        self.remove(tautology_1)
        self.play(
            Write(tautology_2[2]),
            Write(tautology_2[4]),
            Write(tautology_2[6]),
            Write(tautology_2[8]),
        )
        self.next_slide()

        tautology_3 = MathTex(r"F(x) \cdot g(x)", r" = ", r"\int", r"f(x)", r"\cdot", r"g(x)", r"\mathrm{d}x", r"+", r"\int", r"F(x)", r"\cdot", r"g'(x)", r"\mathrm{d}x")
        for i in range(11):
            self.remove(tautology_1[i])
        self.remove(tautology_2)
        self.remove(tautology_1_6_copy)
        self.remove(tautology_1_4_copy)
        self.play(
            Transform(tautology_2[0], tautology_3[0]),
            Transform(tautology_2[1], tautology_3[1]),
            Transform(tautology_2[2], tautology_3[2]),
            Transform(tautology_2[3], tautology_3[3]),
            Transform(tautology_2[4], tautology_3[4]),
            Transform(tautology_2[5], tautology_3[5]),
            Transform(tautology_2[6], tautology_3[7]),
            Transform(tautology_2[7], tautology_3[9]),
            Transform(tautology_2[8], tautology_3[10]),
            Transform(tautology_2[9], tautology_3[11]),
            Transform(tautology_2[10], tautology_3[12]),
        )
        self.play(Write(tautology_3[6]), Write(tautology_3[8]))
        self.next_slide()

        tautology_4 = MathTex(r"\int", r"f(x)", r"\cdot", r"g(x)", r"\mathrm{d}x", r" = ", r"F(x) \cdot g(x)", r"-", r"\int", r"F(x)", r"\cdot", r"g'(x)", r"\mathrm{d}x")
        for i in range(11):
            self.remove(tautology_2[i])
        self.remove(tautology_3)
        self.play(
            Transform(tautology_3[0], tautology_4[6]),
            Transform(tautology_3[1], tautology_4[5]),
            Transform(tautology_3[2], tautology_4[0]),
            Transform(tautology_3[3], tautology_4[1]),
            Transform(tautology_3[4], tautology_4[2]),
            Transform(tautology_3[5], tautology_4[3]),
            Transform(tautology_3[6], tautology_4[4]),
            Transform(tautology_3[7], tautology_4[7]),
            Transform(tautology_3[8], tautology_4[8]),
            Transform(tautology_3[9], tautology_4[9]),
            Transform(tautology_3[10], tautology_4[10]),
            Transform(tautology_3[11], tautology_4[11]),
            Transform(tautology_3[12], tautology_4[12]),
        )
        self.next_slide()

        for i in range(13):
            self.remove(tautology_3[i])
        self.play(
            Unwrite(tautology_4),
        )
        self.next_slide()

        self.play(Unwrite(integral_sum), Unwrite(integral_product), Unwrite(solved_integrals), Unwrite(question_marks))        
        title = Text("Partielle Integration", gradient=(ManimColor("#AA00FF"), ManimColor("#0066FF"))).scale(2)
        subtitle = Text("GFS von Amy", color=GRAY).scale(1)
        subtitle.move_to(DOWN * 1.5)
        self.play(Write(title), Write(subtitle))
        self.next_slide()
