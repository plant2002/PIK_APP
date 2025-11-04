from tkinter import Frame, Label, Button, OptionMenu, StringVar, PhotoImage, Canvas
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
ASSETS_PATH = os.path.join(ROOT_DIR, "assets").replace("\\", "/")

class HeliGraphs:
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

        # images
        self.banner_image = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_others/image_1.png"))
        self.return_home = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_others/button_1.png"))
        self.analysis_other_button2 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_others/button_2.png"))
        self.analysis_other_button3 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_others/button_3.png"))

        # Background / banner
        self.canvas.create_rectangle(0.0, 0.0, 1024.0, 98.5, fill="#0033B8", outline="")
        self.canvas.create_text(27.5, 30.0, anchor="nw", text="PIK-APP for 350B2", fill="#FFFFFF",font=("InriaSans Regular", 30 * -1))
        self.canvas.create_image(804.0, 539.0, image=self.banner_image)

        # Top-right button to go back to start
        button_1 = Button(self.canvas, image=self.return_home, borderwidth=0, highlightthickness=0, command=lambda: show_frame('start'), relief="flat")
        button_1.place(x=754.0, y=25.0, width=253.0, height=48.0)

        self.canvas.create_rectangle(27.0, 117.0, 577.0, 667.0, fill="#D9D9D9", outline="")

        # Initialize the basic screen
        #self.show_heli_buttons()
    def destroy(self):
        self.frame.destroy()