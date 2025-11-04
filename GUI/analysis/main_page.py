from tkinter import Frame, Canvas, Button, Label, PhotoImage
import os
from .failures_section import FailuresSection
from .heliMain import OtherSection

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
ASSETS_PATH = os.path.join(ROOT_DIR, "assets")
ASSETS_PATH = ASSETS_PATH.replace("\\", "/")

class AnalysisGUI:
    def __init__(self, master, show_frame):
        self.master = master
        self.show_frame = show_frame
        self.selected_value = None
        self.current_option = "Basics"

        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)

        self.canvas = Canvas(self.frame, bg="#FFFFFF", height=682, width=1024)
        self.canvas.pack(fill="both", expand=True)

        self.content_frame = Frame(self.canvas, bg="#D9D9D9")
        self.content_frame.place(x=601.0, y=117.0, width=399.0, height=240.0)

        self.output_frame = Frame(self.canvas, bg="#D9D9D9")
        self.output_frame.place(x=27.0, y=117.0, width=550.0, height=550.0)

        self.widgets_list = []
        self.result_label = None

        # Load images (make sure all paths exist)
        self.analysisimage_image_1 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/image_1.png"))
        self.analysisbutton_image_1 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/button_1.png"))
        self.analysisbutton_image_2 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/button_2.png"))
        self.analysisbutton_image_3 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/button_3.png"))

        # Failures & Other buttons images
        self.analysis_failures_button2 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_failures/button_2.png"))
        self.analysis_failures_button3 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_failures/button_3.png"))
        self.analysis_other_button2 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_others/button_2.png"))
        self.analysis_other_button3 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_others/button_3.png"))

        # Background / banner
        self.canvas.create_rectangle(0.0, 0.0, 1024.0, 98.5, fill="#0033B8", outline="")
        self.canvas.create_text(27.5, 30.0, anchor="nw", text="PIK-APP for 350B2", fill="#FFFFFF",
                                font=("InriaSans Regular", 30 * -1))
        self.canvas.create_image(804.0, 539.0, image=self.analysisimage_image_1)

        # Top-right button to go back to start
        button_1 = Button(self.canvas, image=self.analysisbutton_image_1, borderwidth=0, highlightthickness=0, command=lambda: show_frame('start'), relief="flat")
        button_1.place(x=754.0, y=25.0, width=253.0, height=48.0)

        self.canvas.create_rectangle(27.0, 117.0, 577.0, 667.0, fill="#D9D9D9", outline="")

        # Initialize the basic screen
        self.show_basic_buttons()

    def show_basic_buttons(self):
        # Clear previous widgets
        for widget in self.widgets_list:
            widget.destroy()
        self.widgets_list = []

        # Instruction text
        text_label = Label(self.content_frame, text="SEE STATS FOR FAILURES OR HELICOPTER DATA",bg="#D9D9D9", font=("InriaSans Regular", 12))
        text_label.pack(pady=20)

        # Failures button
        button_failures = Button(self.content_frame, image=self.analysisbutton_image_3, command=lambda: self.show_frame('analysis_expo'), relief="flat")
        button_failures.pack(pady=5)

        # Other button
        button_other = Button(self.content_frame, image=self.analysisbutton_image_2, command=lambda: self.show_frame('analysis_Heli'), relief="flat")
        button_other.pack(pady=5)

        self.widgets_list.extend([text_label, button_failures, button_other])

    def change_canvas(self, option):
        # Clear previous widgets
        for widget in self.widgets_list:
            widget.destroy()
        self.widgets_list = []

        canvas = Canvas(self.content_frame, bg="#D9D9D9", width=399.0, height=240.0)
        canvas.pack(fill="both", expand=True)

        if option == "Failures":
            failures_section = FailuresSection(self.content_frame, self.master, self.show_frame)
            self.widgets_list.append(failures_section)

        elif option == "Other":
            self.frame.destroy()
            self.other_section = OtherSection(self.master, self.master, self.show_frame)
            self.other_section.pack(fill="both", expand=True)

    def destroy(self):
        self.frame.destroy()
