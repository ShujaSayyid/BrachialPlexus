"""Brachial Plexus “Cable‑Car” Animation
================================================
Full working Manim scene illustrating the formation of the brachial plexus
(roots → trunks → divisions → cords → terminal branches) together with
brief clinical highlights (Erb’s and Klumpke palsies).

Usage
-----
Install Manim CE ≥ 0.18::

    pip install manim

Render the scene (low‑quality preview)::

    manim -pql brachial_plexus_manim.py BrachialPlexusScene

Render the scene (high‑quality movie)::

    manim -pqh brachial_plexus_manim.py BrachialPlexusScene

Author: ChatGPT (OpenAI o3)
Date: 2025‑07‑05
"""
from manim import *


class BrachialPlexusScene(Scene):
    """Animated overview of the human brachial plexus."""

    def construct(self):
        # -----------------------------
        # 1. ROOTS (C5 – T1)
        # -----------------------------
        root_labels = ["C5", "C6", "C7", "C8", "T1"]
        root_y = [2, 1, 0, -1, -2]
        root_x = -6

        roots = VGroup()
        for label, y in zip(root_labels, root_y):
            node = Dot(point=[root_x, y, 0], radius=0.08, color=BLUE_D)
            txt = Text(label, font_size=28, weight=BOLD).next_to(node, LEFT, buff=0.15)
            roots.add(VGroup(node, txt))
        self.play(FadeIn(roots))

        # -----------------------------
        # 2. TRUNKS (Upper, Middle, Lower)
        # -----------------------------
        trunk_x = -4
        trunk_data = {
            "Upper": (root_y[0] + root_y[1]) / 2,
            "Middle": root_y[2],
            "Lower": (root_y[3] + root_y[4]) / 2,
        }

        trunks = VGroup()
        for name, y in trunk_data.items():
            node = Dot(point=[trunk_x, y, 0], radius=0.1, color=GREEN_D)
            txt = Text(name, font_size=26).next_to(node, RIGHT if name != "Middle" else UP, buff=0.15)
            trunks.add(VGroup(node, txt))
        self.play(GrowFromCenter(trunks))

        # Connect roots → trunks
        root_to_trunk = VGroup(
            *[Line(roots[i][0].get_center(), trunks[0][0].get_center(), color=GRAY) for i in (0, 1)],
            Line(roots[2][0].get_center(), trunks[1][0].get_center(), color=GRAY),
            *[Line(roots[i][0].get_center(), trunks[2][0].get_center(), color=GRAY) for i in (3, 4)],
        )
        self.play(Create(root_to_trunk))

        # -----------------------------
        # 3. DIVISIONS (Anterior/Posterior for each trunk)
        # -----------------------------
        div_x = -2
        divisions = VGroup()
        div_pos = {}
        for idx, trunk in enumerate(trunks):
            base_y = trunk[0].get_y()
            # Anterior division (slightly superior)
            a = Dot([div_x, base_y + 0.3, 0], radius=0.07, color=YELLOW_E)
            a_lbl = Text("A", font_size=24).next_to(a, UP, buff=0.05)
            divisions.add(VGroup(a, a_lbl))
            div_pos[f"{idx}_A"] = a.get_center()
            # Posterior division (slightly inferior)
            p = Dot([div_x, base_y - 0.3, 0], radius=0.07, color=ORANGE)
            p_lbl = Text("P", font_size=24).next_to(p, DOWN, buff=0.05)
            divisions.add(VGroup(p, p_lbl))
            div_pos[f"{idx}_P"] = p.get_center()
        self.play(FadeIn(divisions))

        # Connect trunks → divisions
        trunk_to_div = VGroup()
        for idx, trunk in enumerate(trunks):
            trunk_center = trunk[0].get_center()
            trunk_to_div.add(Line(trunk_center, div_pos[f"{idx}_A"], color=GRAY))
            trunk_to_div.add(Line(trunk_center, div_pos[f"{idx}_P"], color=GRAY))
        self.play(Create(trunk_to_div))

        # -----------------------------
        # 4. CORDS (Lateral, Posterior, Medial)
        # -----------------------------
        cord_x = 0
        cords = VGroup()
        cord_data = {
            "Lateral": 1,
            "Posterior": 0,
            "Medial": -1,
        }
        for name, y in cord_data.items():
            node = Dot([cord_x, y, 0], radius=0.12, color=PURPLE_E)
            txt = Text(name, font_size=26).next_to(node, RIGHT, buff=0.16)
            cords.add(VGroup(node, txt))
        self.play(GrowFromCenter(cords))

        # Connect divisions → cords
        div_to_cord = VGroup(
            # Lateral cord: anterior divisions of Upper & Middle trunks
            Line(div_pos["0_A"], cords[0][0].get_center(), color=GRAY),
            Line(div_pos["1_A"], cords[0][0].get_center(), color=GRAY),
            # Posterior cord: all posterior divisions
            *[Line(div_pos[f"{i}_P"], cords[1][0].get_center(), color=GRAY) for i in range(3)],
            # Medial cord: anterior division of Lower trunk
            Line(div_pos["2_A"], cords[2][0].get_center(), color=GRAY),
        )
        self.play(Create(div_to_cord))

        # -----------------------------
        # 5. TERMINAL BRANCHES
        # -----------------------------
        branch_x = 3.2
        branch_specs = [
            ("Musculocutaneous", cords[0][0].get_y() + 0.6),
            ("Median", cords[0][0].get_y() - 0.2),
            ("Ulnar", cords[2][0].get_y() - 0.6),
            ("Radial", cords[1][0].get_y()),
            ("Axillary", cords[1][0].get_y() + 0.8),
        ]
        branches = VGroup()
        cord_to_branch = VGroup()
        for name, y in branch_specs:
            node = Dot([branch_x, y, 0], radius=0.08, color=RED_D)
            txt = Text(name, font_size=24).next_to(node, RIGHT, buff=0.16, aligned_edge=LEFT)
            branches.add(VGroup(node, txt))
            if name in {"Musculocutaneous", "Median"}:
                src = cords[0][0].get_center()
            elif name == "Ulnar":
                src = cords[2][0].get_center()
            else:  # Radial & Axillary from posterior cord
                src = cords[1][0].get_center()
            cord_to_branch.add(Line(src, node.get_center(), color=GRAY))
        self.play(Create(cord_to_branch), FadeIn(branches))

        # -----------------------------
        # 6. TITLE
        # -----------------------------
        title = Text("Brachial Plexus Overview", font_size=34, weight=BOLD).to_edge(UP)
        self.play(Write(title))

        # -----------------------------
        # 7. CLINICAL CORRELATES (Erb & Klumpke Palsies)
        # -----------------------------
        erb_rect = SurroundingRectangle(VGroup(roots[0], roots[1], trunks[0]), color=RED_D, buff=0.35)
        kl_rect = SurroundingRectangle(VGroup(roots[3], roots[4], trunks[2]), color=RED_D, buff=0.38)
        erb_lbl = Text("Erb's Palsy", font_size=28, color=RED_E).next_to(erb_rect, UP)
        kl_lbl = Text("Klumpke Palsy", font_size=28, color=RED_E).next_to(kl_rect, DOWN)

        self.play(Create(erb_rect), FadeIn(erb_lbl))
        self.wait(1)
        self.play(Uncreate(erb_rect), FadeOut(erb_lbl))
        self.play(Create(kl_rect), FadeIn(kl_lbl))
        self.wait(1)
        self.play(Uncreate(kl_rect), FadeOut(kl_lbl))

        # Hold final frame
        self.wait(2)
