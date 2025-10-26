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

class BrachialPlexusConstruction(Scene):
    def construct(self):
        # Set dark background for aesthetic feel
        #self.camera.background_color = "#0a0e27"
        
        # Title
        title = Text("The Brachial Plexus", font_size=56, weight=BOLD, color=WHITE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=1)
        # SPEED CONTROL: Change self.wait(1) - larger number = longer pause
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

        # Custom layout - expanded to reduce overlap with better spacing
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
        # Add visible config for other nodes
        for node in vertices:
            if node not in div_nodes:
                v_config[node] = {"radius": 0.11, "color": WHITE}

        # Create Graph object - SCALE CONTROL: increase 0.8 to make bigger
        plexus_graph = Graph(
            vertices, edges, layout=layout,
            vertex_config=v_config,
            edge_config={"stroke_width": 3.5, "color": "#555555"}
        )
        plexus_graph.scale(0.8)
        plexus_graph.move_to([0.8, -0.1, 0])
        
        # Move mnemonics to left side with elegant background - FIXED SIZE
        # Create all mnemonic text first to calculate proper height
        mnemonic_r = MarkupText("<b>R: Roots</b>\nC5-T1", font_size=20, color=ROOT_COLOR)
        mnemonic_t = MarkupText("<b>T: Trunks</b>\nSup, Mid, Inf", font_size=20, color=TRUNK_COLOR)
        mnemonic_d = MarkupText("<b>D: Divisions</b>\nAnt, Post", font_size=20, color=DIVISION_COLOR_ANT)
        mnemonic_c = MarkupText("<b>C: Cords</b>\nLat, Med, Post", font_size=20, color=CORD_COLOR_LATERAL)
        mnemonic_b = MarkupText("<b>B: Branches</b>\nTerminal nerves", font_size=20, color=BRANCH_COLOR_MUSC)
        
        # Arrange mnemonics vertically with consistent spacing
        mnemonic_group = VGroup(mnemonic_r, mnemonic_t, mnemonic_d, mnemonic_c, mnemonic_b)
        mnemonic_group.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        mnemonic_group.move_to([-5.5, 0, 0])  # Center on y-axis, left side of screen
        
        # Create background that fits the text group perfectly
        mnemonic_background = SurroundingRectangle(
            mnemonic_group,
            buff=0.2,
            fill_color="#1a1f3a", 
            fill_opacity=0.95, 
            stroke_color="#4a5568", 
            stroke_width=3,
            corner_radius=0.2
        )
        
        # --- Animation Sequence ---
        
        # 1. Roots
        root_keys = ["C5", "C6", "C7", "C8", "T1"]
        root_nodes = VGroup(*[plexus_graph.vertices[v] for v in root_keys])
        root_edge_tuples = [("C5", "ST"), ("C6", "ST"), ("C7", "MT"), ("C8", "IT"), ("T1", "IT")]
        root_edges = VGroup(*[plexus_graph.edges[e] for e in root_edge_tuples])
        root_labels = VGroup(*[Text(v, font_size=14, weight=BOLD, color=WHITE).next_to(plexus_graph.vertices[v], LEFT, buff=0.3) for v in root_keys])
        
        # Show mnemonic background and first item
        self.play(FadeIn(mnemonic_background), run_time=0.5)
        self.play(Write(mnemonic_r), run_time=0.8)
        
        # ANIMATION SPEED: change run_time (larger = slower)
        # Create graph with neutral colors first
        self.play(Create(plexus_graph), run_time=2.5)
        self.wait(0.5)
        
        # Highlight and color root nodes smoothly (no glitch)
        self.play(
            LaggedStart(*[root_nodes[i].animate.set_color(ROOT_COLOR).scale(1.2) for i in range(len(root_nodes))], lag_ratio=0.15),
            run_time=1.5
        )
        self.play(
            LaggedStart(*[root_nodes[i].animate.scale(1/1.2) for i in range(len(root_nodes))], lag_ratio=0.15),
            run_time=0.8
        )
        
        # Color root edges
        self.play(
            LaggedStart(*[edge.animate.set_color(ROOT_COLOR) for edge in root_edges], lag_ratio=0.1),
            run_time=1.2
        )
        self.play(LaggedStart(*[Write(label) for label in root_labels], lag_ratio=0.15, run_time=1.5))
        self.wait(2)

        # 2. Trunks
        trunk_keys = ["ST", "MT", "IT"]
        trunk_nodes = VGroup(*[plexus_graph.vertices[v] for v in trunk_keys])
        
        trunk_labels = VGroup(
            Text("Superior", font_size=11, weight=BOLD, color=TRUNK_COLOR).next_to(plexus_graph.vertices["ST"], UP, buff=0.25),
            Text("Middle", font_size=11, weight=BOLD, color=TRUNK_COLOR).next_to(plexus_graph.vertices["MT"], UP, buff=0.25),
            Text("Inferior", font_size=11, weight=BOLD, color=TRUNK_COLOR).next_to(plexus_graph.vertices["IT"], UP, buff=0.25)
        )
        
        self.play(Write(mnemonic_t), run_time=0.8)
        # ANIMATION SPEED: change lag_ratio (smaller = faster grouping, larger = slower)
        self.play(
            LaggedStart(*[node.animate.set_color(TRUNK_COLOR).scale(1.2) for node in trunk_nodes], lag_ratio=0.15),
            run_time=1.5
        )
        self.play(
            LaggedStart(*[node.animate.scale(1/1.2) for node in trunk_nodes], lag_ratio=0.15),
            run_time=0.8
        )
        self.play(LaggedStart(*[Write(label) for label in trunk_labels], lag_ratio=0.15, run_time=1.5))
        self.wait(2)

        # 3. Divisions
        div_edge_tuples = [
            ("ST", "D_ST_A"), ("ST", "D_ST_P"),
            ("MT", "D_MT_A"), ("MT", "D_MT_P"),
            ("IT", "D_IT_A"), ("IT", "D_IT_P")
        ]
        ant_div_tuples = [("ST", "D_ST_A"), ("MT", "D_MT_A"), ("IT", "D_IT_A")]
        post_div_tuples = [("ST", "D_ST_P"), ("MT", "D_MT_P"), ("IT", "D_IT_P")]
        
        ant_divs = VGroup(*[plexus_graph.edges[e] for e in ant_div_tuples])
        post_divs = VGroup(*[plexus_graph.edges[e] for e in post_div_tuples])
        
        # Labels positioned ABOVE and BELOW the plexus
        div_label_ant_bg = RoundedRectangle(width=1.3, height=0.4, fill_color="#1a1f3a", fill_opacity=0.9, stroke_color=DIVISION_COLOR_ANT, stroke_width=2, corner_radius=0.1)
        div_label_ant_bg.move_to([0.8, 2.5, 0])  # Above the plexus
        div_label_ant = MarkupText("<b>Anterior</b>", color=DIVISION_COLOR_ANT, font_size=13, weight=BOLD).move_to([0.8, 2.5, 0])
        
        div_label_post_bg = RoundedRectangle(width=1.3, height=0.4, fill_color="#1a1f3a", fill_opacity=0.9, stroke_color=DIVISION_COLOR_POST, stroke_width=2, corner_radius=0.1)
        div_label_post_bg.move_to([0.8, -2.2, 0])  # Below the plexus
        div_label_post = MarkupText("<b>Posterior</b>", color=DIVISION_COLOR_POST, font_size=13, weight=BOLD).move_to([0.8, -2.2, 0])

        self.play(Write(mnemonic_d), run_time=0.8)
        # ANIMATION SPEED: run_time controls duration (increase = slower, decrease = faster)
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
        self.wait(2)

        # 4. Cords
        cord_keys = ["LC", "MC", "PC"]
        cord_edge_tuples = [
            ("D_ST_A", "LC"), ("D_MT_A", "LC"),
            ("D_ST_P", "PC"), ("D_MT_P", "PC"), ("D_IT_P", "PC"),
            ("D_IT_A", "MC")
        ]
        cord_nodes = VGroup(*[plexus_graph.vertices[v] for v in cord_keys])
        
        # Cord labels with better positioning
        cord_labels = VGroup(
            Text("Lateral", color=CORD_COLOR_LATERAL, font_size=11, weight=BOLD).next_to(plexus_graph.vertices["LC"], UP, buff=0.35),
            Text("Posterior", color=CORD_COLOR_POSTERIOR, font_size=11, weight=BOLD).next_to(plexus_graph.vertices["PC"], DOWN, buff=0.35),
            Text("Medial", color=CORD_COLOR_MEDIAL, font_size=11, weight=BOLD).next_to(plexus_graph.vertices["MC"], DOWN, buff=0.35)
        )

        self.play(Write(mnemonic_c), run_time=0.8)
        
        # Animate lateral cord
        plexus_graph.vertices["LC"].generate_target()
        plexus_graph.vertices["LC"].target.set_color(CORD_COLOR_LATERAL).scale(1.2)
        self.play(MoveToTarget(plexus_graph.vertices["LC"]), run_time=0.8)
        self.play(plexus_graph.vertices["LC"].animate.scale(1/1.2), run_time=0.4)
        for edge_tuple in [("D_ST_A", "LC"), ("D_MT_A", "LC")]:
            self.play(plexus_graph.edges[edge_tuple].animate.set_color(CORD_COLOR_LATERAL), run_time=0.4)
        self.play(Write(cord_labels[0]), run_time=0.6)
        self.wait(0.3)
        
        # Animate posterior cord
        plexus_graph.vertices["PC"].generate_target()
        plexus_graph.vertices["PC"].target.set_color(CORD_COLOR_POSTERIOR).scale(1.2)
        self.play(MoveToTarget(plexus_graph.vertices["PC"]), run_time=0.8)
        self.play(plexus_graph.vertices["PC"].animate.scale(1/1.2), run_time=0.4)
        for edge_tuple in [("D_ST_P", "PC"), ("D_MT_P", "PC"), ("D_IT_P", "PC")]:
            self.play(plexus_graph.edges[edge_tuple].animate.set_color(CORD_COLOR_POSTERIOR), run_time=0.3)
        self.play(Write(cord_labels[1]), run_time=0.6)
        self.wait(0.3)
        
        # Animate medial cord
        plexus_graph.vertices["MC"].generate_target()
        plexus_graph.vertices["MC"].target.set_color(CORD_COLOR_MEDIAL).scale(1.2)
        self.play(MoveToTarget(plexus_graph.vertices["MC"]), run_time=0.8)
        self.play(plexus_graph.vertices["MC"].animate.scale(1/1.2), run_time=0.4)
        self.play(plexus_graph.edges[("D_IT_A", "MC")].animate.set_color(CORD_COLOR_MEDIAL), run_time=0.4)
        self.play(Write(cord_labels[2]), run_time=0.6)
        self.wait(2)

        # 5. Branches - INDIVIDUAL ANIMATIONS WITH UNIQUE COLORS
        self.play(Write(mnemonic_b), run_time=0.8)
        
        # Define branch data: (node, color, edges, label_text)
        branch_data = [
            ("Musc", BRANCH_COLOR_MUSC, [("LC", "Musc")], "Musculocutaneous"),
            ("Ax", BRANCH_COLOR_AX, [("PC", "Ax")], "Axillary"),
            ("Rad", BRANCH_COLOR_RAD, [("PC", "Rad")], "Radial"),
            ("Med", BRANCH_COLOR_MED, [("LC", "Med"), ("MC", "Med")], "Median"),
            ("Uln", BRANCH_COLOR_ULN, [("MC", "Uln")], "Ulnar"),
        ]
        
        # Animate each branch individually
        for node_key, color, edge_tuples, label_text in branch_data:
            # Pulse and color the node
            plexus_graph.vertices[node_key].generate_target()
            plexus_graph.vertices[node_key].target.set_color(color).scale(1.3)
            self.play(MoveToTarget(plexus_graph.vertices[node_key]), run_time=0.6)
            self.play(plexus_graph.vertices[node_key].animate.scale(1/1.3), run_time=0.3)
            
            # Color the connecting edges
            for edge_tuple in edge_tuples:
                self.play(plexus_graph.edges[edge_tuple].animate.set_color(color), run_time=0.4)
            
            # Write the label
            label = Text(label_text, font_size=10, weight=BOLD, color=color).next_to(plexus_graph.vertices[node_key], RIGHT, buff=0.25)
            self.play(Write(label), run_time=0.5)
            self.wait(0.4)
        
        self.wait(3)


class ErbsPalsyScene(Scene):
    def construct(self):
        # Set background
        self.camera.background_color = "#0a0e27"
        
        title = MarkupText("<b>Clinical Correlate: Erb's Palsy</b>", font_size=48, color=WHITE).to_edge(UP, buff=0.4)
        self.play(Write(title))
        self.wait(0.5)

        # Info box background
        info_bg = RoundedRectangle(
            width=6, height=4.5,
            fill_color="#1a1f3a", fill_opacity=0.9,
            stroke_color=ROOT_COLOR, stroke_width=2.5,
            corner_radius=0.2
        ).shift(DOWN * 0.5)
        
        mechanism_text = MarkupText("<b>Mechanism:</b> Lateral traction on neck", font_size=28, color=WHITE).move_to([0, 1.2, 0])
        injury_text = MarkupText("<b>Injury Site:</b> C5, C6 (Superior Trunk)", font_size=28, color=RED).move_to([0, 0.3, 0])
        
        result_title = MarkupText("<b>Result: 'Waiter's Tip' Posture</b>", font_size=26, color=ROOT_COLOR).move_to([0, -0.6, 0])
        posture_desc = MarkupText(
            "<b>•</b> Arm adducted, internally rotated\n"
            "<b>•</b> Elbow extended\n"
            "<b>•</b> Forearm pronated",
            font_size=22, color=WHITE
        ).move_to([0, -1.6, 0])
        
        self.play(FadeIn(info_bg))
        self.play(Write(mechanism_text), run_time=1)
        self.play(Write(injury_text), run_time=1)
        self.play(Flash(injury_text, color=YELLOW, flash_radius=0.8))
        self.wait(0.5)
        self.play(Write(result_title), run_time=0.8)
        self.play(Write(posture_desc), run_time=1.2)
        self.wait(3)


class KlumpkesPalsyScene(Scene):
    def construct(self):
        # Set background
        self.camera.background_color = "#0a0e27"
        
        title = MarkupText("<b>Clinical Correlate: Klumpke's Palsy</b>", font_size=48, color=WHITE).to_edge(UP, buff=0.4)
        self.play(Write(title))
        self.wait(0.5)

        # Info box background
        info_bg = RoundedRectangle(
            width=6, height=4.5,
            fill_color="#1a1f3a", fill_opacity=0.9,
            stroke_color=BRANCH_COLOR_ULN, stroke_width=2.5,
            corner_radius=0.2
        ).shift(DOWN * 0.5)
        
        mechanism_text = MarkupText("<b>Mechanism:</b> Hyper-abduction of arm", font_size=28, color=WHITE).move_to([0, 1.2, 0])
        injury_text = MarkupText("<b>Injury Site:</b> C8, T1 (Inferior Trunk)", font_size=28, color=RED).move_to([0, 0.3, 0])
        
        result_title = MarkupText("<b>Result: 'Claw Hand' Deformity</b>", font_size=26, color=BRANCH_COLOR_MED).move_to([0, -0.6, 0])
        posture_desc = MarkupText(
            "<b>•</b> Paralysis of intrinsic hand muscles\n"
            "<b>•</b> Hyperextension of MCP joints\n"
            "<b>•</b> Flexion of IP joints",
            font_size=22, color=WHITE
        ).move_to([0, -1.6, 0])
        
        horner_text = MarkupText("<b>Associated:</b> Horner's Syndrome (T1 injury)", font_size=20, color=YELLOW).to_edge(DOWN, buff=0.5)
        
        self.play(FadeIn(info_bg))
        self.play(Write(mechanism_text), run_time=1)
        self.play(Write(injury_text), run_time=1)
        self.play(Flash(injury_text, color=YELLOW, flash_radius=0.8))
        self.wait(0.5)
        self.play(Write(result_title), run_time=0.8)
        self.play(Write(posture_desc), run_time=1.2)
        self.play(Write(horner_text), run_time=0.8)
        self.wait(3)