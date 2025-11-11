from tkinter import Frame, Label, Button, PhotoImage, Canvas
import os
from PIL import Image, ImageTk

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
ASSETS_PATH = os.path.join(ROOT_DIR, "assets").replace("\\", "/")

class FailMain:
    def __init__(self, master, show_frame):
        self.master = master
        self.show_frame = show_frame
        self.selected_value = None
        self.current_option = "Basics"

        # --- Main Frame ---
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)

        # --- Canvas Base ---
        self.canvas = Canvas(self.frame, bg="#FFFFFF", height=682, width=1024)
        self.canvas.pack(fill="both", expand=True)

        # --- Subframes ---
        self.content_frame = Frame(self.canvas, bg="#D9D9D9")
        self.content_frame.place(x=601.0, y=117.0, width=399.0, height=240.0)

        self.output_frame = Frame(self.canvas, bg="#D9D9D9")
        self.output_frame.place(x=27.0, y=117.0, width=550.0, height=550.0)

        self.widgets_list = []
        self.result_label = None

        # --- Images ---
        self.banner_image = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_failures/image_1.png"))
        self.failures_button2 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_failures/button_2.png"))
        self.failures_button3 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_failures/button_3.png"))
        self.homeButton = Image.open(os.path.join(ASSETS_PATH, "home.png"))
        self.undoButton = Image.open(os.path.join(ASSETS_PATH, "undo.png"))
        self.homeButton = self.homeButton.resize((40, 40), Image.LANCZOS)
        self.undoButton = self.undoButton.resize((40, 40), Image.LANCZOS)
        self.homeButton = ImageTk.PhotoImage(self.homeButton)
        self.undoButton = ImageTk.PhotoImage(self.undoButton)

        # --- Banner / Header ---
        self.canvas.create_rectangle(0.0, 0.0, 1024.0, 98.5, fill="#0033B8", outline="")
        self.canvas.create_text(27.5, 30.0, anchor="nw", text="PIK-APP for 350B2",fill="#FFFFFF", font=("InriaSans Regular", 30 * -1))
        self.canvas.create_image(804.0, 539.0, image=self.banner_image)

        # --- Return Button (top-right) ---
        button_home = Button(self.canvas, image=self.homeButton, command=lambda: self.show_frame('start'), relief="flat")
        button_home.place(x=890.0, y=25.0) 

        button_undo = Button(self.canvas, image=self.undoButton, command=lambda: self.master.go_back(), relief="flat")
        button_undo.place(x=950.0, y=25.0)

        # --- Left Grey Panel ---
        self.canvas.create_rectangle(27.0, 117.0, 577.0, 667.0, fill="#D9D9D9", outline="")

        # --- Initialize the failure section ---
        self.show_fail_buttons()

    def show_fail_buttons(self):
        #export button
        Export = Button(self.canvas, image = self.failures_button2,borderwidth=0,highlightthickness=0,command=lambda: self.show_frame('failExport'),relief="flat")
        Export.place(x=823.0,y=259.0,width=165.0,height=50.0)

        #graphs button
        Graphs = Button(self.canvas, image = self.failures_button3, borderwidth=0, highlightthickness=0, command=lambda: self.show_frame('failGraphs'), relief="flat")
        Graphs.place(x=636.0, y=259.0, width=165.0, height=50.0)
        self.widgets_list.extend([Export, Graphs])


    def destroy(self):
        self.frame.destroy()
