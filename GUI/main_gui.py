from tkinterdnd2 import TkinterDnD
from .start_page import StartGUI
from .analysis.main_page import AnalysisGUI
from .reimport_page import ReimportGUI
from .analysis import heli
from .analysis import failures

def launch_app():
    root = TkinterDnD.Tk()
    root.geometry("1024x682") #spreminjamo velikost okna?
    root.configure(bg="#FFFFFF")

    frames = {}

    def show_frame(page_name):
        # Safely destroy current frame if it exists
        if 'current' in frames and frames['current']:
            try:
                frames['current'].destroy()
            except Exception:
                pass

        # pages - doesn't work any other way
        page_class = {
            'start': StartGUI,
            'analysis': AnalysisGUI,
            'heliMain': heli.heliMain.HeliMain,
            'heliExport': heli.heliExport.HeliExport,
            'heliGraphs': heli.HeliGraphs,
            'failMain': failures.failMain.FailMain,
            'failGraphs': failures.failGraphs.FailGraphs,
            'failExport': failures.failExport.FailExport,
            'reimport': ReimportGUI,
            'information': None
        }[page_name]

        # Create and show the new page
        frames['current'] = page_class(root, show_frame)
        frames['current'].frame.tkraise()

    # Start with the start page
    show_frame('start')
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()
