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
    history = []

    def show_frame(page_name):
        # Safely destroy current frame if it exists
        nonlocal history
        if 'current' in frames and frames['current']:
            try:
                history.append(frames['current'].page_name)
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
        frames['current'].page_name = page_name
        frames['current'].frame.tkraise()
    
    #call history, return to previous page
    def go_back():
        if history:
            prev_page = history.pop()  # Get last visited
            show_frame(prev_page)
        else:
            print("No previous page in history.")
    
    #expose it so it can be called by other functions
    root.go_back = go_back

    # Start with the start page
    show_frame('start')
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()
