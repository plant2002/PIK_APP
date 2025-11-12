import os
import tkinter as tk
from tkinter import Frame, Button, Entry, Label, StringVar, Toplevel, messagebox
from tkinter import PhotoImage

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSETS_PATH = os.path.join(ROOT_DIR, "assets")
ASSETS_PATH = ASSETS_PATH.replace("\\", "/")

class loginGUI:
    def __init__(self, master, show_frame, logic):
        """
        master: main tkinter root or parent
        show_frame: callback to switch pages
        logic: external logic object (handles auth, db, etc.)
        """
        self.master = master
        self.show_frame = show_frame
        self.logic = logic  # Injected external logic
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)

        # Canvas and layout
        self.canvas = tk.Canvas(self.frame, width=1024, height=700, bg="white", highlightthickness=0)
        self.canvas.place(x=0, y=0)

        # Background
        self.startimage_image_1 = PhotoImage(file=os.path.join(ASSETS_PATH, "start/image_1.png"))
        self.startimage_image_2 = PhotoImage(file=os.path.join(ASSETS_PATH, "start/image_2.png"))
        self.canvas.create_image(512.0, 341.0, image=self.startimage_image_1)
        self.canvas.create_image(730.0, 526.5, image=self.startimage_image_2)

        self.canvas.create_rectangle(0.0, 0.0, 1024.0, 98.5, fill="#0033B8", outline="")
        self.canvas.create_text(27.5, 30.0, anchor="nw", text="PIK-APP for 350B2",
                                fill="#FFFFFF", font=("InriaSans Regular", 30 * -1))
        self.canvas.create_rectangle(31.5, 135.0, 339.5, 638.5, fill="#AAAAAA", outline="")

        # Central white box
        self.content_frame = Frame(self.canvas, bg="white", bd=2, relief="ridge")
        self.content_frame.place(relx=0.5, rely=0.55, anchor="center", width=500, height=400)

        # Default view
        self.show_login_page()

    # ---------------- LOGIN PAGE ----------------
    def show_login_page(self):
        self.clear_content_frame()

        Label(self.content_frame, text="Login", font=("Arial", 20, "bold"), bg="white").pack(pady=10)

        Label(self.content_frame, text="Email", bg="white").pack()
        email_entry = Entry(self.content_frame, width=40)
        email_entry.pack(pady=5)

        Label(self.content_frame, text="Password", bg="white").pack()
        password_entry = Entry(self.content_frame, width=40, show="*")
        password_entry.pack(pady=5)

        def do_login():
            email = email_entry.get()
            password = password_entry.get()
            result = self.logic.login(email, password)
            if result:
                messagebox.showinfo("Success", "Login successful!")
                self.show_frame("main")  # Switch to main app
            else:
                messagebox.showerror("Error", "Invalid email or password.")

        Button(self.content_frame, text="Login", command=do_login, width=20, bg="#0033B8", fg="white").pack(pady=10)
        Button(self.content_frame, text="Register", command=self.show_register_page, width=20).pack(pady=5)

    # ---------------- REGISTER PAGE ----------------
    def show_register_page(self):
        self.clear_content_frame()

        Label(self.content_frame, text="Register", font=("Arial", 20, "bold"), bg="white").pack(pady=10)

        fields = {}
        for field in ["Name", "Surname", "Email", "Password", "Company"]:
            Label(self.content_frame, text=field, bg="white").pack()
            entry = Entry(self.content_frame, width=40, show="*" if field == "Password" else "")
            entry.pack(pady=5)
            fields[field.lower()] = entry

        # Company suggestion list
        suggestion_box = tk.Listbox(self.content_frame, height=3)
        suggestion_box.pack(pady=5)
        suggestion_box.place_forget()  # hidden initially

        def on_company_type(event):
            query = fields["company"].get()
            if len(query) < 2:
                suggestion_box.place_forget()
                return

            suggestions = self.logic.suggest_company(query)
            suggestion_box.delete(0, tk.END)
            for s in suggestions:
                suggestion_box.insert(tk.END, s)

            if suggestions:
                suggestion_box.place(relx=0.5, rely=0.8, anchor="center", width=300)
            else:
                suggestion_box.place_forget()

        def select_suggestion(event):
            selection = suggestion_box.get(suggestion_box.curselection())
            fields["company"].delete(0, tk.END)
            fields["company"].insert(0, selection)
            suggestion_box.place_forget()

        fields["company"].bind("<KeyRelease>", on_company_type)
        suggestion_box.bind("<<ListboxSelect>>", select_suggestion)

        def create_new_company():
            popup = Toplevel(self.master)
            popup.title("Create New Company")
            popup.geometry("300x250")

            entries = {}
            for field in ["Name", "Address", "Country"]:
                Label(popup, text=field).pack()
                e = Entry(popup)
                e.pack(pady=3)
                entries[field.lower()] = e

            def save_company():
                data = {k: v.get() for k, v in entries.items()}
                success = self.logic.create_company(data)
                if success:
                    messagebox.showinfo("Success", "Company created successfully.")
                    popup.destroy()
                else:
                    messagebox.showerror("Error", "Could not create company.")

            Button(popup, text="Save", command=save_company).pack(pady=10)

        Button(self.content_frame, text="Create New Company", command=create_new_company).pack(pady=5)

        def do_register():
            data = {k: v.get() for k, v in fields.items()}
            result = self.logic.register(data)
            if result:
                messagebox.showinfo("Success", "Registration successful! Please log in.")
                self.show_login_page()
            else:
                messagebox.showerror("Error", "Registration failed.")

        Button(self.content_frame, text="Register", command=do_register, bg="#0033B8", fg="white").pack(pady=10)
        Button(self.content_frame, text="Back to Login", command=self.show_login_page).pack(pady=5)

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
