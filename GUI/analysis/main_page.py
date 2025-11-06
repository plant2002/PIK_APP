from tkinter import Frame, Canvas, Button, Label
from PIL import Image, ImageTk
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
ASSETS_PATH = os.path.join(ROOT_DIR, "assets").replace("\\", "/")

class AnalysisGUI:
    def __init__(self, master, show_frame):
        self.master = master
        self.show_frame = show_frame
        self.selected_value = None
        self.current_option = "Basics"

        # --- Main Frame ---
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)

        # --- Canvas ---
        self.canvas = Canvas(self.frame, bg="#FFFFFF", height=682, width=1024)
        self.canvas.pack(fill="both", expand=True)

        # --- Subframes ---
        self.content_frame = Frame(self.canvas, bg="#D9D9D9")
        self.content_frame.place(x=601.0, y=117.0, width=399.0, height=240.0)
        self.output_frame = Frame(self.canvas, bg="#D9D9D9")
        self.output_frame.place(x=27.0, y=117.0, width=550.0, height=550.0)

        self.widgets_list = []
        self.result_label = None

        # --- Load Images ---
        self.analysisimage_image_1 = Image.open(os.path.join(ASSETS_PATH, "analysis/image_1.png"))

        # Other buttons
        self.analysisbutton_image_2 = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "analysis/button_2.png")))
        self.analysisbutton_image_3 = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "analysis/button_3.png")))
        self.homeButton = Image.open(os.path.join(ASSETS_PATH, "home.png"))
        self.undoButton = Image.open(os.path.join(ASSETS_PATH, "undo.png"))
        self.homeButton = self.homeButton.resize((40, 40), Image.LANCZOS)
        self.undoButton = self.undoButton.resize((40, 40), Image.LANCZOS)
        self.homeButton = ImageTk.PhotoImage(self.homeButton)
        self.undoButton = ImageTk.PhotoImage(self.undoButton)

        # --- Banner / Header ---
        self.canvas.create_rectangle(0.0, 0.0, 1024.0, 98.5, fill="#0033B8", outline="")
        self.canvas.create_text(27.5, 30.0, anchor="nw", text="PIK-APP for 350B2", fill="#FFFFFF", font=("InriaSans Regular", 30 * -1))
        self.canvas.create_image(804.0, 539.0, image=ImageTk.PhotoImage(self.analysisimage_image_1))

        # --- Left grey panel ---
        self.canvas.create_rectangle(27.0, 117.0, 577.0, 667.0, fill="#D9D9D9", outline="")

        # --- Initialize main buttons ---
        self.show_basic_buttons()

    # --- Basic buttons in content frame ---
    def show_basic_buttons(self):
        # Clear previous widgets
        for widget in self.widgets_list:
            widget.destroy()
        self.widgets_list = []

        # Instruction text
        text_label = Label(self.content_frame, text="SEE STATS FOR FAILURES OR HELICOPTER DATA",bg="#D9D9D9", font=("InriaSans Regular", 12))
        text_label.pack(pady=20)

        # Failures button
        button_failures = Button(self.content_frame, image=self.analysisbutton_image_3, command=lambda: self.show_frame('failMain'), relief="flat")
        button_failures.pack(pady=5)

        # Other button
        button_other = Button(self.content_frame, image=self.analysisbutton_image_2, command=lambda: self.show_frame('heliMain'), relief="flat")
        button_other.pack(pady=5)

        button_home = Button(self.canvas, image=self.homeButton, command=lambda: self.show_frame('start'), relief="flat")
        button_home.place(x=890.0, y=25.0) 

        button_undo = Button(self.canvas, image=self.undoButton, command=lambda: self.master.go_back(), relief="flat")
        button_undo.place(x=950.0, y=25.0)

        self.widgets_list.extend([text_label, button_failures, button_other])

    def destroy(self):
        self.frame.destroy()
