from manim import *

# Define colors for consistency
ROOT_COLOR = "#FF6B6B"  # Red for roots
TRUNK_COLOR = "#4ECDC4"  # Teal for trunks
DIVISION_COLOR_ANT = "#95E77D"  # Light green for anterior
DIVISION_COLOR_POST = "#FFB84D"  # Orange for posterior
CORD_COLOR_LATERAL = "#A78BFA"  # Purple for lateral cord
CORD_COLOR_MEDIAL = "#F472B6"  # Pink for medial cord
CORD_COLOR_POSTERIOR = "#60A5FA"  # Blue for posterior cord

# Terminal branch colors - related warm tones (yellow to orange spectrum)
BRANCH_COLOR_MUSC = "#FFD700"  # Gold
BRANCH_COLOR_AX = "#FFA500"    # Orange
BRANCH_COLOR_RAD = "#FF8C00"   # Dark Orange
BRANCH_COLOR_MED = "#FF6347"   # Tomato
BRANCH_COLOR_ULN = "#FF4500"   # Orange Red

LABEL_COLOR = WHITE
INJURY_COLOR = "#FF0000"  # Bright red for injury
AFFECTED_COLOR = "#CC0000"  # Darker red for affected areas

class BrachialPlexusConstruction(Scene):
    def construct(self):
        # Set dark background for aesthetic feel
        #self.camera.background_color = "#0a0e27"
        
        # Title
        title = Text("The Brachial Plexus", font_size=56, weight=BOLD, color=WHITE, disable_ligatures=True)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Define all vertices and edges for the graph
        vertices = ["C5", "C6", "C7", "C8", "T1", 
                   "ST", "MT", "IT",
                   "D_ST_A", "D_ST_P", "D_MT_A", "D_MT_P", "D_IT_A", "D_IT_P",
                   "LC", "MC", "PC",
                   "Musc", "Ax", "Rad", "Med", "Uln"]

        edges = [
            # Roots to Trunks
            ("C5", "ST"), ("C6", "ST"),
            ("C7", "MT"),
            ("C8", "IT"), ("T1", "IT"),
            
            # Trunks to Divisions
            ("ST", "D_ST_A"), ("ST", "D_ST_P"),
            ("MT", "D_MT_A"), ("MT", "D_MT_P"),
            ("IT", "D_IT_A"), ("IT", "D_IT_P"),
            
            # Divisions to Cords
            ("D_ST_A", "LC"), ("D_MT_A", "LC"),
            ("D_ST_P", "PC"), ("D_MT_P", "PC"), ("D_IT_P", "PC"),
            ("D_IT_A", "MC"),
            
            # Cords to Terminal Branches
            ("LC", "Musc"), ("LC", "Med"),
            ("MC", "Med"), ("MC", "Uln"),
            ("PC", "Ax"), ("PC", "Rad")
        ]

        # Custom layout
        layout = {
            "C5": [-6, 3.5, 0], "C6": [-6, 2.3, 0], "C7": [-6, 1.1, 0], "C8": [-6, -0.1, 0], "T1": [-6, -1.3, 0],
            "ST": [-4.2, 2.9, 0], "MT": [-4.2, 1.1, 0], "IT": [-4.2, -0.7, 0],
            "D_ST_A": [-2, 3.2, 0], "D_ST_P": [-2, 2.5, 0],
            "D_MT_A": [-2, 1.4, 0], "D_MT_P": [-2, 0.7, 0],
            "D_IT_A": [-2, -0.4, 0], "D_IT_P": [-2, -1.1, 0],
            "LC": [0.3, 2.5, 0], "MC": [0.3, -1.2, 0], "PC": [0.3, 0.6, 0],
            "Musc": [2.8, 3.2, 0], "Ax": [2.8, 2.0, 0], "Rad": [2.8, 0.8, 0],
            "Med": [2.8, -0.4, 0], "Uln": [2.8, -1.6, 0]
        }
        
        # Make division points invisible
        div_nodes = ["D_ST_A", "D_ST_P", "D_MT_A", "D_MT_P", "D_IT_A", "D_IT_P"]
        v_config = {node: {"radius": 0.07, "color": WHITE} for node in div_nodes}
        for node in vertices:
            if node not in div_nodes:
                v_config[node] = {"radius": 0.11, "color": WHITE}

        # Create Graph object
        plexus_graph = Graph(
            vertices, edges, layout=layout,
            vertex_config=v_config,
            edge_config={"stroke_width": 3.5, "color": "#555555"}
        )
        plexus_graph.scale(0.8)
        plexus_graph.move_to([0.8, -0.1, 0])
        
        # Mnemonics - all with disable_ligatures=True
        mnemonic_r = MarkupText("<b>R: Roots</b>\nC5-T1", font_size=20, color=ROOT_COLOR, disable_ligatures=True)
        mnemonic_t = MarkupText("<b>T: Trunks</b>\nSup, Mid, Inf", font_size=20, color=TRUNK_COLOR, disable_ligatures=True)
        mnemonic_d = MarkupText("<b>D: Divisions</b>\nAnt, Post", font_size=20, color=DIVISION_COLOR_ANT, disable_ligatures=True)
        mnemonic_c = MarkupText("<b>C: Cords</b>\nLat, Med, Post", font_size=20, color=CORD_COLOR_LATERAL, disable_ligatures=True)
        mnemonic_b = MarkupText("<b>B: Branches</b>\nTerminal nerves", font_size=20, color=BRANCH_COLOR_MUSC, disable_ligatures=True)
        
        mnemonic_group = VGroup(mnemonic_r, mnemonic_t, mnemonic_d, mnemonic_c, mnemonic_b)
        mnemonic_group.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        mnemonic_group.move_to([-5.5, 0, 0])
        
        mnemonic_background = SurroundingRectangle(
            mnemonic_group,
            buff=0.2,
            fill_color="#1a1f3a", 
            fill_opacity=0.95, 
            stroke_color="#4a5568", 
            stroke_width=3,
            corner_radius=0.2
        )
        
        # Animation Sequence
        self.play(FadeIn(mnemonic_background), run_time=0.5)
        self.play(Write(mnemonic_r), run_time=0.8)
        self.play(Create(plexus_graph), run_time=2.5)
        self.wait(0.5)
        
        # Store all labels and colored elements for later reference
        root_keys = ["C5", "C6", "C7", "C8", "T1"]
        root_nodes = VGroup(*[plexus_graph.vertices[v] for v in root_keys])
        root_edge_tuples = [("C5", "ST"), ("C6", "ST"), ("C7", "MT"), ("C8", "IT"), ("T1", "IT")]
        root_edges = VGroup(*[plexus_graph.edges[e] for e in root_edge_tuples])
        root_labels = VGroup(*[Text(v, font_size=14, weight=BOLD, color=WHITE, disable_ligatures=True).next_to(plexus_graph.vertices[v], LEFT, buff=0.3) for v in root_keys])
        
        self.play(
            LaggedStart(*[root_nodes[i].animate.set_color(ROOT_COLOR).scale(1.2) for i in range(len(root_nodes))], lag_ratio=0.15),
            run_time=1.5
        )
        self.play(
            LaggedStart(*[root_nodes[i].animate.scale(1/1.2) for i in range(len(root_nodes))], lag_ratio=0.15),
            run_time=0.8
        )
        self.play(
            LaggedStart(*[edge.animate.set_color(ROOT_COLOR) for edge in root_edges], lag_ratio=0.1),
            run_time=1.2
        )
        self.play(LaggedStart(*[Write(label) for label in root_labels], lag_ratio=0.15, run_time=1.5))
        self.wait(1)

        # Trunks
        trunk_keys = ["ST", "MT", "IT"]
        trunk_nodes = VGroup(*[plexus_graph.vertices[v] for v in trunk_keys])
        trunk_labels = VGroup(
            Text("Superior", font_size=11, weight=BOLD, color=TRUNK_COLOR, disable_ligatures=True).next_to(plexus_graph.vertices["ST"], UP, buff=0.25),
            Text("Middle", font_size=11, weight=BOLD, color=TRUNK_COLOR, disable_ligatures=True).next_to(plexus_graph.vertices["MT"], UP, buff=0.25),
            Text("Inferior", font_size=11, weight=BOLD, color=TRUNK_COLOR, disable_ligatures=True).next_to(plexus_graph.vertices["IT"], UP, buff=0.25)
        )
        
        self.play(Write(mnemonic_t), run_time=0.8)
        self.play(
            LaggedStart(*[node.animate.set_color(TRUNK_COLOR).scale(1.2) for node in trunk_nodes], lag_ratio=0.15),
            run_time=1.5
        )
        self.play(
            LaggedStart(*[node.animate.scale(1/1.2) for node in trunk_nodes], lag_ratio=0.15),
            run_time=0.8
        )
        self.play(LaggedStart(*[Write(label) for label in trunk_labels], lag_ratio=0.15, run_time=1.5))
        self.wait(1)

        # Divisions
        ant_div_tuples = [("ST", "D_ST_A"), ("MT", "D_MT_A"), ("IT", "D_IT_A")]
        post_div_tuples = [("ST", "D_ST_P"), ("MT", "D_MT_P"), ("IT", "D_IT_P")]
        ant_divs = VGroup(*[plexus_graph.edges[e] for e in ant_div_tuples])
        post_divs = VGroup(*[plexus_graph.edges[e] for e in post_div_tuples])
        
        div_label_ant_bg = RoundedRectangle(width=1.3, height=0.4, fill_color="#1a1f3a", fill_opacity=0.9, stroke_color=DIVISION_COLOR_ANT, stroke_width=2, corner_radius=0.1)
        div_label_ant_bg.move_to([0.8, 2.5, 0])
        div_label_ant = MarkupText("<b>Anterior</b>", color=DIVISION_COLOR_ANT, font_size=13, weight=BOLD, disable_ligatures=True).move_to([0.8, 2.5, 0])
        
        div_label_post_bg = RoundedRectangle(width=1.3, height=0.4, fill_color="#1a1f3a", fill_opacity=0.9, stroke_color=DIVISION_COLOR_POST, stroke_width=2, corner_radius=0.1)
        div_label_post_bg.move_to([0.8, -2.2, 0])
        div_label_post = MarkupText("<b>Posterior</b>", color=DIVISION_COLOR_POST, font_size=13, weight=BOLD, disable_ligatures=True).move_to([0.8, -2.2, 0])

        self.play(Write(mnemonic_d), run_time=0.8)
        self.play(
            LaggedStart(*[edge.animate.set_color(DIVISION_COLOR_ANT) for edge in ant_divs], lag_ratio=0.1),
            run_time=1.2
        )
        self.play(FadeIn(div_label_ant_bg), Write(div_label_ant), run_time=0.8)
        self.wait(0.3)
        
        self.play(
            LaggedStart(*[edge.animate.set_color(DIVISION_COLOR_POST) for edge in post_divs], lag_ratio=0.1),
            run_time=1.2
        )
        self.play(FadeIn(div_label_post_bg), Write(div_label_post), run_time=0.8)
        self.wait(1)

        # Cords
        cord_labels = VGroup(
            Text("Lateral", color=CORD_COLOR_LATERAL, font_size=11, weight=BOLD, disable_ligatures=True).next_to(plexus_graph.vertices["LC"], UP, buff=0.35),
            Text("Posterior", color=CORD_COLOR_POSTERIOR, font_size=11, weight=BOLD, disable_ligatures=True).next_to(plexus_graph.vertices["PC"], DOWN, buff=0.35),
            Text("Medial", color=CORD_COLOR_MEDIAL, font_size=11, weight=BOLD, disable_ligatures=True).next_to(plexus_graph.vertices["MC"], DOWN, buff=0.35)
        )

        self.play(Write(mnemonic_c), run_time=0.8)
        
        plexus_graph.vertices["LC"].generate_target()
        plexus_graph.vertices["LC"].target.set_color(CORD_COLOR_LATERAL).scale(1.2)
        self.play(MoveToTarget(plexus_graph.vertices["LC"]), run_time=0.8)
        self.play(plexus_graph.vertices["LC"].animate.scale(1/1.2), run_time=0.4)
        for edge_tuple in [("D_ST_A", "LC"), ("D_MT_A", "LC")]:
            self.play(plexus_graph.edges[edge_tuple].animate.set_color(CORD_COLOR_LATERAL), run_time=0.4)
        self.play(Write(cord_labels[0]), run_time=0.6)
        self.wait(0.3)
        
        plexus_graph.vertices["PC"].generate_target()
        plexus_graph.vertices["PC"].target.set_color(CORD_COLOR_POSTERIOR).scale(1.2)
        self.play(MoveToTarget(plexus_graph.vertices["PC"]), run_time=0.8)
        self.play(plexus_graph.vertices["PC"].animate.scale(1/1.2), run_time=0.4)
        for edge_tuple in [("D_ST_P", "PC"), ("D_MT_P", "PC"), ("D_IT_P", "PC")]:
            self.play(plexus_graph.edges[edge_tuple].animate.set_color(CORD_COLOR_POSTERIOR), run_time=0.3)
        self.play(Write(cord_labels[1]), run_time=0.6)
        self.wait(0.3)
        
        plexus_graph.vertices["MC"].generate_target()
        plexus_graph.vertices["MC"].target.set_color(CORD_COLOR_MEDIAL).scale(1.2)
        self.play(MoveToTarget(plexus_graph.vertices["MC"]), run_time=0.8)
        self.play(plexus_graph.vertices["MC"].animate.scale(1/1.2), run_time=0.4)
        self.play(plexus_graph.edges[("D_IT_A", "MC")].animate.set_color(CORD_COLOR_MEDIAL), run_time=0.4)
        self.play(Write(cord_labels[2]), run_time=0.6)
        self.wait(1)

        # Branches
        self.play(Write(mnemonic_b), run_time=0.8)
        
        branch_data = [
            ("Musc", BRANCH_COLOR_MUSC, [("LC", "Musc")], "Musculocutaneous"),
            ("Ax", BRANCH_COLOR_AX, [("PC", "Ax")], "Axillary"),
            ("Rad", BRANCH_COLOR_RAD, [("PC", "Rad")], "Radial"),
            ("Med", BRANCH_COLOR_MED, [("LC", "Med"), ("MC", "Med")], "Median"),
            ("Uln", BRANCH_COLOR_ULN, [("MC", "Uln")], "Ulnar"),
        ]
        
        branch_labels_list = []
        for node_key, color, edge_tuples, label_text in branch_data:
            plexus_graph.vertices[node_key].generate_target()
            plexus_graph.vertices[node_key].target.set_color(color).scale(1.3)
            self.play(MoveToTarget(plexus_graph.vertices[node_key]), run_time=0.6)
            self.play(plexus_graph.vertices[node_key].animate.scale(1/1.3), run_time=0.3)
            
            for edge_tuple in edge_tuples:
                self.play(plexus_graph.edges[edge_tuple].animate.set_color(color), run_time=0.4)
            
            label = Text(label_text, font_size=10, weight=BOLD, color=color, font="sans-serif", slant=NORMAL).next_to(plexus_graph.vertices[node_key], RIGHT, buff=0.25)
            self.play(Write(label), run_time=0.5)
            branch_labels_list.append(label)
            self.wait(0.4)
        
        self.wait(3)


class ErbsPalsyScene(Scene):
    def construct(self):
        self.camera.background_color = "#0a0e27"
        
        # Recreate the plexus graph
        vertices = ["C5", "C6", "C7", "C8", "T1", 
                   "ST", "MT", "IT",
                   "D_ST_A", "D_ST_P", "D_MT_A", "D_MT_P", "D_IT_A", "D_IT_P",
                   "LC", "MC", "PC",
                   "Musc", "Ax", "Rad", "Med", "Uln"]

        edges = [
            ("C5", "ST"), ("C6", "ST"), ("C7", "MT"), ("C8", "IT"), ("T1", "IT"),
            ("ST", "D_ST_A"), ("ST", "D_ST_P"),
            ("MT", "D_MT_A"), ("MT", "D_MT_P"),
            ("IT", "D_IT_A"), ("IT", "D_IT_P"),
            ("D_ST_A", "LC"), ("D_MT_A", "LC"),
            ("D_ST_P", "PC"), ("D_MT_P", "PC"), ("D_IT_P", "PC"),
            ("D_IT_A", "MC"),
            ("LC", "Musc"), ("LC", "Med"),
            ("MC", "Med"), ("MC", "Uln"),
            ("PC", "Ax"), ("PC", "Rad")
        ]

        layout = {
            "C5": [-6, 3.5, 0], "C6": [-6, 2.3, 0], "C7": [-6, 1.1, 0], "C8": [-6, -0.1, 0], "T1": [-6, -1.3, 0],
            "ST": [-4.2, 2.9, 0], "MT": [-4.2, 1.1, 0], "IT": [-4.2, -0.7, 0],
            "D_ST_A": [-2, 3.2, 0], "D_ST_P": [-2, 2.5, 0],
            "D_MT_A": [-2, 1.4, 0], "D_MT_P": [-2, 0.7, 0],
            "D_IT_A": [-2, -0.4, 0], "D_IT_P": [-2, -1.1, 0],
            "LC": [0.3, 2.5, 0], "MC": [0.3, -1.2, 0], "PC": [0.3, 0.6, 0],
            "Musc": [2.8, 3.2, 0], "Ax": [2.8, 2.0, 0], "Rad": [2.8, 0.8, 0],
            "Med": [2.8, -0.4, 0], "Uln": [2.8, -1.6, 0]
        }
        
        div_nodes = ["D_ST_A", "D_ST_P", "D_MT_A", "D_MT_P", "D_IT_A", "D_IT_P"]
        v_config = {node: {"radius": 0.07, "color": WHITE} for node in div_nodes}
        for node in vertices:
            if node not in div_nodes:
                v_config[node] = {"radius": 0.11, "color": WHITE}

        plexus_graph = Graph(
            vertices, edges, layout=layout,
            vertex_config=v_config,
            edge_config={"stroke_width": 3.5, "color": "#888888"}
        )
        plexus_graph.scale(0.75)
        plexus_graph.move_to([1, 0, 0])
        
        # Title
        title = MarkupText("<b>Clinical Correlate: Erb's Palsy</b>", font_size=44, color=WHITE, disable_ligatures=True)
        title.to_edge(UP, buff=0.3)
        
        # Create plexus first
        self.play(Write(title), run_time=1)
        self.play(Create(plexus_graph), run_time=1.5)
        self.wait(0.5)
        
        # Info box on left
        info_box = VGroup(
            MarkupText("<b>Mechanism:</b>", font_size=22, color=YELLOW, disable_ligatures=True),
            Text("Lateral traction on neck", font_size=18, color=WHITE, disable_ligatures=True),
            MarkupText("<b>Common causes:</b>", font_size=22, color=YELLOW, disable_ligatures=True),
            Text("• Birth trauma", font_size=16, color=WHITE, disable_ligatures=True),
            Text("• Motorcycle accidents", font_size=16, color=WHITE, disable_ligatures=True),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        info_box.to_corner(UL, buff=0.5)
        
        self.play(Write(info_box), run_time=2)
        self.wait(1)
        
        # HIGHLIGHT INJURY SITE - C5, C6, Superior Trunk
        injury_label = MarkupText("<b>INJURY SITE</b>", font_size=26, color=INJURY_COLOR, weight=BOLD, disable_ligatures=True)
        injury_label.next_to(plexus_graph.vertices["ST"], LEFT, buff=1.5)
        
        # Animate injury
        injured_nodes = VGroup(plexus_graph.vertices["C5"], plexus_graph.vertices["C6"], plexus_graph.vertices["ST"])
        injured_edges = VGroup(plexus_graph.edges[("C5", "ST")], plexus_graph.edges[("C6", "ST")])
        
        self.play(Write(injury_label), run_time=0.8)
        self.play(
            LaggedStart(*[node.animate.set_color(INJURY_COLOR).scale(1.4) for node in injured_nodes], lag_ratio=0.2),
            LaggedStart(*[edge.animate.set_color(INJURY_COLOR).set_stroke(width=6) for edge in injured_edges], lag_ratio=0.2),
            run_time=1.5
        )
        self.play(Flash(plexus_graph.vertices["ST"], color=INJURY_COLOR, flash_radius=0.6, line_length=0.3))
        self.wait(1)
        
        # HIGHLIGHT AFFECTED DOWNSTREAM STRUCTURES
        affected_label = MarkupText("<b>AFFECTED DOWNSTREAM</b>", font_size=22, color=AFFECTED_COLOR, weight=BOLD, disable_ligatures=True)
        affected_label.to_edge(DOWN, buff=0.5)
        
        self.play(Write(affected_label), run_time=0.8)
        
        # Divisions from superior trunk
        affected_divs = VGroup(
            plexus_graph.edges[("ST", "D_ST_A")],
            plexus_graph.edges[("ST", "D_ST_P")]
        )
        self.play(
            LaggedStart(*[edge.animate.set_color(AFFECTED_COLOR).set_stroke(width=5) for edge in affected_divs], lag_ratio=0.15),
            run_time=1
        )
        
        # Lateral cord (from anterior division)
        self.play(
            plexus_graph.vertices["LC"].animate.set_color(AFFECTED_COLOR).scale(1.3),
            plexus_graph.edges[("D_ST_A", "LC")].animate.set_color(AFFECTED_COLOR).set_stroke(width=5),
            run_time=0.8
        )
        
        # Posterior cord (from posterior division)
        self.play(
            plexus_graph.vertices["PC"].animate.set_color(AFFECTED_COLOR).scale(1.3),
            plexus_graph.edges[("D_ST_P", "PC")].animate.set_color(AFFECTED_COLOR).set_stroke(width=5),
            run_time=0.8
        )
        
        # Terminal nerves affected
        self.play(
            plexus_graph.vertices["Musc"].animate.set_color(AFFECTED_COLOR).scale(1.3),
            plexus_graph.edges[("LC", "Musc")].animate.set_color(AFFECTED_COLOR).set_stroke(width=5),
            run_time=0.7
        )
        musc_label = Paragraph("Musculocutaneous", font_size=11, weight=BOLD, color=AFFECTED_COLOR, line_spacing=0.5).next_to(plexus_graph.vertices["Musc"], RIGHT, buff=0.2)
        self.play(Write(musc_label), run_time=0.5)
        
        self.play(
            plexus_graph.vertices["Ax"].animate.set_color(AFFECTED_COLOR).scale(1.3),
            plexus_graph.edges[("PC", "Ax")].animate.set_color(AFFECTED_COLOR).set_stroke(width=5),
            run_time=0.7
        )
        ax_label = Text("Axillary", font_size=11, weight=BOLD, color=AFFECTED_COLOR, disable_ligatures=True).next_to(plexus_graph.vertices["Ax"], RIGHT, buff=0.2)
        self.play(Write(ax_label), run_time=0.5)
        
        self.wait(2)
        
        # Result description
        result_box = VGroup(
            MarkupText("<b>Result: 'Waiter's Tip' Posture</b>", font_size=24, color=YELLOW, disable_ligatures=True),
            Text("• Arm adducted & internally rotated", font_size=16, color=WHITE, disable_ligatures=True),
            Text("• Elbow extended", font_size=16, color=WHITE, disable_ligatures=True),
            Text("• Forearm pronated", font_size=16, color=WHITE, disable_ligatures=True),
            Text("• Wrist flexed", font_size=16, color=WHITE, disable_ligatures=True),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        result_box.to_corner(DR, buff=0.5)
        
        self.play(FadeIn(result_box), run_time=1.5)
        self.wait(4)


class KlumpkesPalsyScene(Scene):
    def construct(self):
        self.camera.background_color = "#0a0e27"
        
        # Recreate the plexus graph
        vertices = ["C5", "C6", "C7", "C8", "T1", 
                   "ST", "MT", "IT",
                   "D_ST_A", "D_ST_P", "D_MT_A", "D_MT_P", "D_IT_A", "D_IT_P",
                   "LC", "MC", "PC",
                   "Musc", "Ax", "Rad", "Med", "Uln"]

        edges = [
            ("C5", "ST"), ("C6", "ST"), ("C7", "MT"), ("C8", "IT"), ("T1", "IT"),
            ("ST", "D_ST_A"), ("ST", "D_ST_P"),
            ("MT", "D_MT_A"), ("MT", "D_MT_P"),
            ("IT", "D_IT_A"), ("IT", "D_IT_P"),
            ("D_ST_A", "LC"), ("D_MT_A", "LC"),
            ("D_ST_P", "PC"), ("D_MT_P", "PC"), ("D_IT_P", "PC"),
            ("D_IT_A", "MC"),
            ("LC", "Musc"), ("LC", "Med"),
            ("MC", "Med"), ("MC", "Uln"),
            ("PC", "Ax"), ("PC", "Rad")
        ]

        layout = {
            "C5": [-6, 3.5, 0], "C6": [-6, 2.3, 0], "C7": [-6, 1.1, 0], "C8": [-6, -0.1, 0], "T1": [-6, -1.3, 0],
            "ST": [-4.2, 2.9, 0], "MT": [-4.2, 1.1, 0], "IT": [-4.2, -0.7, 0],
            "D_ST_A": [-2, 3.2, 0], "D_ST_P": [-2, 2.5, 0],
            "D_MT_A": [-2, 1.4, 0], "D_MT_P": [-2, 0.7, 0],
            "D_IT_A": [-2, -0.4, 0], "D_IT_P": [-2, -1.1, 0],
            "LC": [0.3, 2.5, 0], "MC": [0.3, -1.2, 0], "PC": [0.3, 0.6, 0],
            "Musc": [2.8, 3.2, 0], "Ax": [2.8, 2.0, 0], "Rad": [2.8, 0.8, 0],
            "Med": [2.8, -0.4, 0], "Uln": [2.8, -1.6, 0]
        }
        
        div_nodes = ["D_ST_A", "D_ST_P", "D_MT_A", "D_MT_P", "D_IT_A", "D_IT_P"]
        v_config = {node: {"radius": 0.07, "color": WHITE} for node in div_nodes}
        for node in vertices:
            if node not in div_nodes:
                v_config[node] = {"radius": 0.11, "color": WHITE}

        plexus_graph = Graph(
            vertices, edges, layout=layout,
            vertex_config=v_config,
            edge_config={"stroke_width": 3.5, "color": "#888888"}
        )
        plexus_graph.scale(0.75)
        plexus_graph.move_to([1, 0, 0])
        
        # Title
        title = MarkupText("<b>Clinical Correlate: Klumpke's Palsy</b>", font_size=44, color=WHITE, disable_ligatures=True)
        title.to_edge(UP, buff=0.3)
        
        # Create plexus first
        self.play(Write(title), run_time=1)
        self.play(Create(plexus_graph), run_time=1.5)
        self.wait(0.5)
        
        # Info box on left
        info_box = VGroup(
            MarkupText("<b>Mechanism:</b>", font_size=22, color=YELLOW, disable_ligatures=True),
            Text("Hyper-abduction of arm", font_size=18, color=WHITE, disable_ligatures=True),
            MarkupText("<b>Common causes:</b>", font_size=22, color=YELLOW, disable_ligatures=True),
            Text("• Grabbing object during fall", font_size=16, color=WHITE, disable_ligatures=True),
            Text("• Birth injury", font_size=16, color=WHITE, disable_ligatures=True),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        info_box.to_corner(UL, buff=0.5)
        
        self.play(Write(info_box), run_time=2)
        self.wait(1)
        
        # HIGHLIGHT INJURY SITE - C8, T1, Inferior Trunk
        injury_label = MarkupText("<b>INJURY SITE</b>", font_size=26, color=INJURY_COLOR, weight=BOLD, disable_ligatures=True)
        injury_label.next_to(plexus_graph.vertices["IT"], LEFT, buff=1.5)
        
        # Animate injury
        injured_nodes = VGroup(plexus_graph.vertices["C8"], plexus_graph.vertices["T1"], plexus_graph.vertices["IT"])
        injured_edges = VGroup(plexus_graph.edges[("C8", "IT")], plexus_graph.edges[("T1", "IT")])
        
        self.play(Write(injury_label), run_time=0.8)
        self.play(
            LaggedStart(*[node.animate.set_color(INJURY_COLOR).scale(1.4) for node in injured_nodes], lag_ratio=0.2),
            LaggedStart(*[edge.animate.set_color(INJURY_COLOR).set_stroke(width=6) for edge in injured_edges], lag_ratio=0.2),
            run_time=1.5
        )
        self.play(Flash(plexus_graph.vertices["IT"], color=INJURY_COLOR, flash_radius=0.6, line_length=0.3))
        self.wait(1)
        
        # HIGHLIGHT AFFECTED DOWNSTREAM STRUCTURES
        affected_label = MarkupText("<b>AFFECTED DOWNSTREAM</b>", font_size=22, color=AFFECTED_COLOR, weight=BOLD, disable_ligatures=True)
        affected_label.to_edge(DOWN, buff=0.5)
        
        self.play(Write(affected_label), run_time=0.8)
        
        # Anterior division from inferior trunk
        self.play(
            plexus_graph.edges[("IT", "D_IT_A")].animate.set_color(AFFECTED_COLOR).set_stroke(width=5),
            run_time=0.8
        )
        
        # Medial cord
        self.play(
            plexus_graph.vertices["MC"].animate.set_color(AFFECTED_COLOR).scale(1.3),
            plexus_graph.edges[("D_IT_A", "MC")].animate.set_color(AFFECTED_COLOR).set_stroke(width=5),
            run_time=0.8
        )
        
        # Terminal nerves affected - Ulnar
        self.play(
            plexus_graph.vertices["Uln"].animate.set_color(AFFECTED_COLOR).scale(1.3),
            plexus_graph.edges[("MC", "Uln")].animate.set_color(AFFECTED_COLOR).set_stroke(width=5),
            run_time=0.7
        )
        uln_label = Text("Ulnar", font_size=11, weight=BOLD, color=AFFECTED_COLOR, font="sans-serif", slant=NORMAL).next_to(plexus_graph.vertices["Uln"], RIGHT, buff=0.2)
        self.play(Write(uln_label), run_time=0.5)
        
        # Median nerve (partially affected via medial cord contribution)
        self.play(
            plexus_graph.vertices["Med"].animate.set_color(AFFECTED_COLOR).scale(1.3),
            plexus_graph.edges[("MC", "Med")].animate.set_color(AFFECTED_COLOR).set_stroke(width=5),
            run_time=0.7
        )
        med_label = Text("Median (partial)", font_size=10, weight=BOLD, color=AFFECTED_COLOR, font="sans-serif", slant=NORMAL).next_to(plexus_graph.vertices["Med"], RIGHT, buff=0.2)
        self.play(Write(med_label), run_time=0.5)
        
        self.wait(2)
        
        # Result description
        result_box = VGroup(
            MarkupText("<b>Result: 'Claw Hand' Deformity</b>", font_size=24, color=YELLOW, disable_ligatures=True),
            Text("• Intrinsic hand muscle paralysis", font_size=16, color=WHITE, disable_ligatures=True),
            Text("• Hyperextension at MCP joints", font_size=16, color=WHITE, disable_ligatures=True),
            Text("• Flexion at IP joints", font_size=16, color=WHITE, disable_ligatures=True),
            Text("• Loss of finger abduction/adduction", font_size=16, color=WHITE, disable_ligatures=True),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        result_box.to_corner(DR, buff=0.5)
        
        self.play(FadeIn(result_box), run_time=1.5)
        self.wait(1)
        
        # Horner's syndrome note
        horner_note = MarkupText("<b>Associated: Horner's Syndrome</b>\n(if T1 injury affects sympathetic chain)", 
                                 font_size=16, color=YELLOW, disable_ligatures=True)
        horner_note.next_to(result_box, UP, buff=0.3)
        self.play(Write(horner_note), run_time=1)
        
        self.wait(4)


class NonTerminalBranchesScene(Scene):
    def construct(self):
        self.camera.background_color = "#0a0e27"
        
        # Title
        title = MarkupText("<b>Non-Terminal Branches of the Brachial Plexus</b>", 
                          font_size=44, color=WHITE, disable_ligatures=True)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=1)
        self.wait(0.5)
        
        # Create simplified plexus structure
        vertices = ["C5", "C6", "C7", "C8", "T1", 
                   "ST", "MT", "IT",
                   "LC", "MC", "PC"]
        
        edges = [
            ("C5", "ST"), ("C6", "ST"),
            ("C7", "MT"),
            ("C8", "IT"), ("T1", "IT"),
        ]
        
        layout = {
            "C5": [-5, 3.5, 0], "C6": [-5, 2.5, 0], "C7": [-5, 1.0, 0], 
            "C8": [-5, -0.5, 0], "T1": [-5, -1.5, 0],
            "ST": [-2.5, 3.0, 0], "MT": [-2.5, 1.0, 0], "IT": [-2.5, -1.0, 0],
            "LC": [0.5, 2.0, 0], "MC": [0.5, -1.5, 0], "PC": [0.5, 0.5, 0],
        }
        
        v_config = {node: {"radius": 0.12, "color": WHITE} for node in vertices}
        
        plexus = Graph(
            vertices, edges, layout=layout,
            vertex_config=v_config,
            edge_config={"stroke_width": 3, "color": "#666666"}
        )
        plexus.scale(0.9)
        
        self.play(Create(plexus), run_time=1.5)
        self.wait(0.5)
        
        # Define branch colors
        DORSAL_SCAP_COLOR = "#FF6B9D"
        LONG_THORACIC_COLOR = "#4ECDC4"
        SUPRASCAP_COLOR = "#FFD93D"
        NERVE_TO_SUBCLAV_COLOR = "#A8E6CF"
        LAT_PECT_COLOR = "#95B8D1"
        MED_PECT_COLOR = "#E8A87C"
        MED_CUT_ARM_COLOR = "#C9ADA7"
        MED_CUT_FOREARM_COLOR = "#B8A9C9"
        UPPER_SUBSCAP_COLOR = "#F4A6D7"
        LOWER_SUBSCAP_COLOR = "#9DBDFF"
        THORACODORSAL_COLOR = "#FFB5A7"
        
        # Category 1: FROM ROOTS
        cat1_title = MarkupText("<b>FROM ROOTS</b>", font_size=28, color=YELLOW, disable_ligatures=True)
        cat1_title.to_edge(LEFT, buff=0.5).shift(UP * 2.5)
        self.play(Write(cat1_title), run_time=0.8)
        self.wait(0.3)
        
        # Dorsal Scapular (C5)
        dorsal_scap_start = plexus.vertices["C5"].get_center()
        dorsal_scap_end = dorsal_scap_start + np.array([0.8, 0.5, 0])
        dorsal_scap_line = Line(dorsal_scap_start, dorsal_scap_end, color=DORSAL_SCAP_COLOR, stroke_width=3)
        dorsal_scap_dot = Dot(dorsal_scap_end, radius=0.08, color=DORSAL_SCAP_COLOR)
        dorsal_scap_label = Text("Dorsal Scapular\n(C5)", font_size=11, color=DORSAL_SCAP_COLOR, disable_ligatures=True)
        dorsal_scap_label.next_to(dorsal_scap_dot, RIGHT, buff=0.15)
        
        self.play(Create(dorsal_scap_line), run_time=0.5)
        self.play(FadeIn(dorsal_scap_dot), Write(dorsal_scap_label), run_time=0.7)
        self.wait(0.4)
        
        # Long Thoracic (C5, C6, C7)
        long_thor_start = plexus.vertices["C6"].get_center()
        long_thor_end = long_thor_start + np.array([0.8, -0.8, 0])
        long_thor_line = Line(long_thor_start, long_thor_end, color=LONG_THORACIC_COLOR, stroke_width=3)
        long_thor_dot = Dot(long_thor_end, radius=0.08, color=LONG_THORACIC_COLOR)
        long_thor_label = Text("Long Thoracic\n(C5-C7)", font_size=11, color=LONG_THORACIC_COLOR, disable_ligatures=True)
        long_thor_label.next_to(long_thor_dot, RIGHT, buff=0.15)
        
        # Show connections from C5, C6, C7
        c5_contrib = Line(plexus.vertices["C5"].get_center(), long_thor_end, color=LONG_THORACIC_COLOR, stroke_width=2, stroke_opacity=0.4)
        c6_contrib = Line(plexus.vertices["C6"].get_center(), long_thor_end, color=LONG_THORACIC_COLOR, stroke_width=2, stroke_opacity=0.4)
        c7_contrib = Line(plexus.vertices["C7"].get_center(), long_thor_end, color=LONG_THORACIC_COLOR, stroke_width=2, stroke_opacity=0.4)
        
        self.play(Create(c5_contrib), Create(c6_contrib), Create(c7_contrib), run_time=0.8)
        self.play(Create(long_thor_line), run_time=0.5)
        self.play(FadeIn(long_thor_dot), Write(long_thor_label), run_time=0.7)
        self.wait(0.8)
        
        # Category 2: FROM SUPERIOR TRUNK
        cat2_title = MarkupText("<b>FROM SUPERIOR TRUNK</b>", font_size=28, color=YELLOW, disable_ligatures=True)
        cat2_title.to_edge(LEFT, buff=0.5).shift(UP * 0.5)
        self.play(Write(cat2_title), run_time=0.8)
        self.wait(0.3)
        
        # Highlight superior trunk
        self.play(plexus.vertices["ST"].animate.set_color(TRUNK_COLOR).scale(1.2), run_time=0.5)
        self.play(plexus.vertices["ST"].animate.scale(1/1.2), run_time=0.3)
        
        # Suprascapular
        supra_start = plexus.vertices["ST"].get_center()
        supra_end = supra_start + np.array([1.2, 0.8, 0])
        supra_line = Line(supra_start, supra_end, color=SUPRASCAP_COLOR, stroke_width=3)
        supra_dot = Dot(supra_end, radius=0.08, color=SUPRASCAP_COLOR)
        supra_label = Text("Suprascapular", font_size=11, color=SUPRASCAP_COLOR, disable_ligatures=True)
        supra_label.next_to(supra_dot, RIGHT, buff=0.15)
        
        self.play(Create(supra_line), run_time=0.5)
        self.play(FadeIn(supra_dot), Write(supra_label), run_time=0.7)
        self.wait(0.4)
        
        # Nerve to Subclavius
        subclav_start = plexus.vertices["ST"].get_center()
        subclav_end = subclav_start + np.array([1.2, 0.3, 0])
        subclav_line = Line(subclav_start, subclav_end, color=NERVE_TO_SUBCLAV_COLOR, stroke_width=3)
        subclav_dot = Dot(subclav_end, radius=0.08, color=NERVE_TO_SUBCLAV_COLOR)
        subclav_label = Text("N. to Subclavius", font_size=11, color=NERVE_TO_SUBCLAV_COLOR, disable_ligatures=True)
        subclav_label.next_to(subclav_dot, RIGHT, buff=0.15)
        
        self.play(Create(subclav_line), run_time=0.5)
        self.play(FadeIn(subclav_dot), Write(subclav_label), run_time=0.7)
        self.wait(0.8)
        
        # Category 3: FROM LATERAL CORD
        cat3_title = MarkupText("<b>FROM LATERAL CORD</b>", font_size=28, color=YELLOW, disable_ligatures=True)
        cat3_title.to_edge(LEFT, buff=0.5).shift(DOWN * 1.0)
        self.play(Write(cat3_title), run_time=0.8)
        self.wait(0.3)
        
        # Highlight lateral cord
        self.play(plexus.vertices["LC"].animate.set_color(CORD_COLOR_LATERAL).scale(1.2), run_time=0.5)
        self.play(plexus.vertices["LC"].animate.scale(1/1.2), run_time=0.3)
        
        # Lateral Pectoral
        lat_pect_start = plexus.vertices["LC"].get_center()
        lat_pect_end = lat_pect_start + np.array([1.5, 0.5, 0])
        lat_pect_line = Line(lat_pect_start, lat_pect_end, color=LAT_PECT_COLOR, stroke_width=3)
        lat_pect_dot = Dot(lat_pect_end, radius=0.08, color=LAT_PECT_COLOR)
        lat_pect_label = Text("Lateral Pectoral", font_size=11, color=LAT_PECT_COLOR, disable_ligatures=True)
        lat_pect_label.next_to(lat_pect_dot, RIGHT, buff=0.15)
        
        self.play(Create(lat_pect_line), run_time=0.5)
        self.play(FadeIn(lat_pect_dot), Write(lat_pect_label), run_time=0.7)
        self.wait(0.8)
        
        # Category 4: FROM MEDIAL CORD
        cat4_title = MarkupText("<b>FROM MEDIAL CORD</b>", font_size=28, color=YELLOW, disable_ligatures=True)
        cat4_title.to_edge(LEFT, buff=0.5).shift(DOWN * 2.5)
        self.play(Write(cat4_title), run_time=0.8)
        self.wait(0.3)
        
        # Highlight medial cord
        self.play(plexus.vertices["MC"].animate.set_color(CORD_COLOR_MEDIAL).scale(1.2), run_time=0.5)
        self.play(plexus.vertices["MC"].animate.scale(1/1.2), run_time=0.3)
        
        # Medial Pectoral
        med_pect_start = plexus.vertices["MC"].get_center()
        med_pect_end = med_pect_start + np.array([1.5, -0.3, 0])
        med_pect_line = Line(med_pect_start, med_pect_end, color=MED_PECT_COLOR, stroke_width=3)
        med_pect_dot = Dot(med_pect_end, radius=0.08, color=MED_PECT_COLOR)
        med_pect_label = Text("Medial Pectoral", font_size=11, color=MED_PECT_COLOR, disable_ligatures=True)
        med_pect_label.next_to(med_pect_dot, RIGHT, buff=0.15)
        
        self.play(Create(med_pect_line), run_time=0.5)
        self.play(FadeIn(med_pect_dot), Write(med_pect_label), run_time=0.7)
        self.wait(0.4)
        
        # Medial Cutaneous Nerve of Arm
        med_cut_arm_start = plexus.vertices["MC"].get_center()
        med_cut_arm_end = med_cut_arm_start + np.array([1.5, -0.8, 0])
        med_cut_arm_line = Line(med_cut_arm_start, med_cut_arm_end, color=MED_CUT_ARM_COLOR, stroke_width=3)
        med_cut_arm_dot = Dot(med_cut_arm_end, radius=0.08, color=MED_CUT_ARM_COLOR)
        med_cut_arm_label = Text("Med. Cut. N. of Arm", font_size=10, color=MED_CUT_ARM_COLOR, disable_ligatures=True)
        med_cut_arm_label.next_to(med_cut_arm_dot, RIGHT, buff=0.15)
        
        self.play(Create(med_cut_arm_line), run_time=0.5)
        self.play(FadeIn(med_cut_arm_dot), Write(med_cut_arm_label), run_time=0.7)
        self.wait(0.4)
        
        # Medial Cutaneous Nerve of Forearm
        med_cut_fore_start = plexus.vertices["MC"].get_center()
        med_cut_fore_end = med_cut_fore_start + np.array([1.5, -1.3, 0])
        med_cut_fore_line = Line(med_cut_fore_start, med_cut_fore_end, color=MED_CUT_FOREARM_COLOR, stroke_width=3)
        med_cut_fore_dot = Dot(med_cut_fore_end, radius=0.08, color=MED_CUT_FOREARM_COLOR)
        med_cut_fore_label = Text("Med. Cut. N. of Forearm", font_size=10, color=MED_CUT_FOREARM_COLOR, disable_ligatures=True)
        med_cut_fore_label.next_to(med_cut_fore_dot, RIGHT, buff=0.15)
        
        self.play(Create(med_cut_fore_line), run_time=0.5)
        self.play(FadeIn(med_cut_fore_dot), Write(med_cut_fore_label), run_time=0.7)
        self.wait(0.8)
        
        # Clear left side for Category 5
        self.play(
            FadeOut(cat1_title), FadeOut(cat2_title), 
            FadeOut(cat3_title), FadeOut(cat4_title),
            run_time=0.8
        )
        
        # Category 5: FROM POSTERIOR CORD
        cat5_title = MarkupText("<b>FROM POSTERIOR CORD</b>", font_size=28, color=YELLOW, disable_ligatures=True)
        cat5_title.to_edge(LEFT, buff=0.5).shift(UP * 1.5)
        self.play(Write(cat5_title), run_time=0.8)
        self.wait(0.3)
        
        # Highlight posterior cord
        self.play(plexus.vertices["PC"].animate.set_color(CORD_COLOR_POSTERIOR).scale(1.2), run_time=0.5)
        self.play(plexus.vertices["PC"].animate.scale(1/1.2), run_time=0.3)
        
        # Upper Subscapular
        upper_sub_start = plexus.vertices["PC"].get_center()
        upper_sub_end = upper_sub_start + np.array([1.5, 0.8, 0])
        upper_sub_line = Line(upper_sub_start, upper_sub_end, color=UPPER_SUBSCAP_COLOR, stroke_width=3)
        upper_sub_dot = Dot(upper_sub_end, radius=0.08, color=UPPER_SUBSCAP_COLOR)
        upper_sub_label = Text("Upper Subscapular", font_size=11, color=UPPER_SUBSCAP_COLOR, disable_ligatures=True)
        upper_sub_label.next_to(upper_sub_dot, RIGHT, buff=0.15)
        
        self.play(Create(upper_sub_line), run_time=0.5)
        self.play(FadeIn(upper_sub_dot), Write(upper_sub_label), run_time=0.7)
        self.wait(0.4)
        
        # Thoracodorsal
        thoraco_start = plexus.vertices["PC"].get_center()
        thoraco_end = thoraco_start + np.array([1.5, 0.3, 0])
        thoraco_line = Line(thoraco_start, thoraco_end, color=THORACODORSAL_COLOR, stroke_width=3)
        thoraco_dot = Dot(thoraco_end, radius=0.08, color=THORACODORSAL_COLOR)
        thoraco_label = Text("Thoracodorsal", font_size=11, color=THORACODORSAL_COLOR, disable_ligatures=True)
        thoraco_label.next_to(thoraco_dot, RIGHT, buff=0.15)
        
        self.play(Create(thoraco_line), run_time=0.5)
        self.play(FadeIn(thoraco_dot), Write(thoraco_label), run_time=0.7)
        self.wait(0.4)
        
        # Lower Subscapular
        lower_sub_start = plexus.vertices["PC"].get_center()
        lower_sub_end = lower_sub_start + np.array([1.5, -0.2, 0])
        lower_sub_line = Line(lower_sub_start, lower_sub_end, color=LOWER_SUBSCAP_COLOR, stroke_width=3)
        lower_sub_dot = Dot(lower_sub_end, radius=0.08, color=LOWER_SUBSCAP_COLOR)
        lower_sub_label = Text("Lower Subscapular", font_size=11, color=LOWER_SUBSCAP_COLOR, disable_ligatures=True)
        lower_sub_label.next_to(lower_sub_dot, RIGHT, buff=0.15)
        
        self.play(Create(lower_sub_line), run_time=0.5)
        self.play(FadeIn(lower_sub_dot), Write(lower_sub_label), run_time=0.7)
        self.wait(2)
        
        # Summary note
        summary = VGroup(
            MarkupText("<b>Key Points:</b>", font_size=20, color=YELLOW, disable_ligatures=True),
            Text("• 11 major non-terminal branches", font_size=16, color=WHITE, disable_ligatures=True),
            Text("• Innervate shoulder/chest muscles", font_size=16, color=WHITE, disable_ligatures=True),
            Text("• Critical for proximal limb function", font_size=16, color=WHITE, disable_ligatures=True),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        summary.to_corner(DL, buff=0.5)
        
        self.play(FadeIn(summary), run_time=1.5)
        self.wait(3)