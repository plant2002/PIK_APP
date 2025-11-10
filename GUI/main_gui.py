from tkinterdnd2 import TkinterDnD
from .start_page import StartGUI
from .analysis.main_page import AnalysisGUI
from .reimport_page import ReimportGUI
from .analysis import heli
from .analysis import failures


def launch_app():
    root = TkinterDnD.Tk()
    root.geometry("1024x682")
    root.configure(bg="#FFFFFF")

    frames = {}
    history = []         # full navigation history
    navigating_back = False  # flag so show_frame doesn't append during back

    def show_frame(page_name):
        nonlocal navigating_back

        # Destroy previous frame if it exists
        if 'current' in frames and frames['current']:
            try:
                frames['current'].destroy()
            except Exception:
                pass

        # Only record navigation if we're NOT going back
        if not navigating_back:
            history.append(page_name)

        # Page lookup
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
        }.get(page_name)

        if page_class is None:
            print(f"Unknown page: {page_name}")
            return

        # Create and show new frame
        frames['current'] = page_class(root, show_frame)
        frames['current'].page_name = page_name
        frames['current'].frame.tkraise()

    def go_back():
        """Go to the previous page in full history."""
        nonlocal navigating_back

        if len(history) < 2:
            print("No previous page in history.")
            return

        # Remove the current page
        history.pop()
        prev_page = history[-1]

        # Navigate without appending again
        navigating_back = True
        show_frame(prev_page)
        navigating_back = False

    # Expose to pages
    root.go_back = go_back

    # Start with the start page
    show_frame('start')
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()
