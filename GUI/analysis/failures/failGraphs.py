from tkinter import Frame, Label, Button, OptionMenu, StringVar, PhotoImage, Canvas, ttk
import os
from PIL import Image, ImageTk
from core.analysis.errorData import errorDataGraphs

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
ASSETS_PATH = os.path.join(ROOT_DIR, "assets").replace("\\", "/")

class FailGraphs:
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
        self.banner_image = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_failures/image_1.png"))
        self.analysis_other_button2 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_failures/button_2.png"))
        self.analysis_other_button3 = PhotoImage(file=os.path.join(ASSETS_PATH, "analysis/analysis_failures/button_3.png"))
        self.homeButton = Image.open(os.path.join(ASSETS_PATH, "home.png"))
        self.undoButton = Image.open(os.path.join(ASSETS_PATH, "undo.png"))
        self.homeButton = self.homeButton.resize((40, 40), Image.LANCZOS)
        self.undoButton = self.undoButton.resize((40, 40), Image.LANCZOS)
        self.homeButton = ImageTk.PhotoImage(self.homeButton)
        self.undoButton = ImageTk.PhotoImage(self.undoButton)

        # Background / banner
        self.canvas.create_rectangle(0.0, 0.0, 1024.0, 98.5, fill="#0033B8", outline="")
        self.canvas.create_text(27.5, 30.0, anchor="nw", text="PIK-APP for 350B2", fill="#FFFFFF",font=("InriaSans Regular", 30 * -1))
        self.canvas.create_image(804.0, 539.0, image=self.banner_image)

        # Top-right button to go back to start
        button_home = Button(self.canvas, image=self.homeButton, command=lambda: self.show_frame('start'), relief="flat")
        button_home.place(x=890.0, y=25.0) 

        button_undo = Button(self.canvas, image=self.undoButton, command=lambda: self.master.go_back(), relief="flat")
        button_undo.place(x=950.0, y=25.0)

        options_map = {
            "Errors between dates" : "FDEFT", #flightDateErrorFT
            "Dates with error" : "FDWE", #flightDateWithError
            "Number of error occurences in flights" : "ERFT", #flightsErrorFT
            "Flights with error" : "FWE", #flightsWithError
            "flighttime of flights when error occurred": 'FTEC', #flightTimeErrorCode
        }

        # Create button styles
        button_style = {
            "bg": "#0033B8",
            "fg": "#FFFFFF",
            "activebackground": "#002a94",  # slightly darker blue
            "activeforeground": "#FFFFFF",
            "font": ("Segoe UI", 10, "bold"),
            "relief": "flat",
            "bd": 0,
            "width": 25,
            "height": 2,
            "cursor": "hand2"
        }

        # Create a vertical stack of buttons in the middle of the grey rectangle
        start_y = 150
        spacing = 45

        for i, (label, key) in enumerate(options_map.items()):
            btn = Button(
                self.canvas,
                text=label,
                **button_style,
                command=lambda k=key: choose_graph(k))  # replace with your graphing function
            btn.place(x=630, y=start_y + i * spacing, width=340, height=35)

    def choose_graph(self, name):
        if name == "FDEFT":
            errorDataGraphs.FlightsDateErrorFT()
        elif name == "FDWE":
            errorDataGraphs.FlightsDateWithError
        elif name == "ERFT":
            errorDataGraphs.FlightsErrorFT()
        elif name == "FWE":
            errorDataGraphs.FlightsWithError()
        elif name == "FTEC":
            errorDataGraphs.FlightTimeErrorCode()
    
    def destroy(self):
        self.frame.destroy()
