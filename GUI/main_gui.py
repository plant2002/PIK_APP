from tkinterdnd2 import TkinterDnD
from .start_page import StartGUI
from .analysis.main_page import AnalysisGUI
from .reimport_page import ReimportGUI
from .analysis.heliMain import OtherSection
from .analysis.failures_section import FailuresSection
from .analysis.heliExport import HeliExport
from .analysis.heliGraphs import HeliGraphs

def launch_app():
    root = TkinterDnD.Tk()
    root.geometry("1024x682")
    root.configure(bg="#FFFFFF")

    frames = {}

    def show_frame(page_name):
        # Safely destroy current frame if it exists
        if 'current' in frames and frames['current']:
            try:
                frames['current'].destroy()
            except Exception:
                pass

        # Pick the correct page class
        page_class = {
            'start': StartGUI,
            'analysis': AnalysisGUI,
            'analysis_Heli': OtherSection,
            'heliExport': HeliExport,
            'heliGraphs': HeliGraphs,
            'analysis_Fail': FailuresSection,
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
