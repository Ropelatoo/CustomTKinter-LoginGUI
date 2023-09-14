import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Calvo's Cat Curse")
        self.center_window(600, 600)

        # Load original image
        original_image = Image.open(r"D:\PyCharm\Projects\CustomTKinter-LoginGUI\img\calvocat.jpeg")

        # Resize the image
        self.resized_image = original_image.resize((600, 600))

        # Convert to tkinter
        self.image_tk = ImageTk.PhotoImage(self.resized_image)

        image_label = ctk.CTkLabel(self, image=self.image_tk, text="")
        image_label.pack(padx=10, pady=10)

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")

# Create the main window
mainwindow = ctk.CTk()
mainwindow.geometry("500x500")
mainwindow.title("CustomTKinter Login GUI")

pattern1 = "Roboto", 12
pattern2 = "Roboto", 18, "bold"
pattern3 = "Roboto", 11

# Login title text
text = ctk.CTkLabel(mainwindow, text=("CustomTKinter Login GUI"), font=(pattern2))
text.pack(padx=10, pady=10)

# Insert email text
text_insertmail = ctk.CTkLabel(mainwindow, text=("Insert your e-mail please"), font=(pattern1))
text_insertmail.pack(padx=10, pady=1)

# E-mail entry box
email = ctk.CTkEntry(mainwindow, placeholder_text="E-mail", width=300, font=(pattern1))
email.pack(padx=10, pady=10)

# Insert password text
text_insertpass = ctk.CTkLabel(mainwindow, text=("Insert your password please"), font=(pattern1))
text_insertpass.pack(padx=10, pady=1)

# Password entry box
password = ctk.CTkEntry(mainwindow, placeholder_text="Password", width=300, font=(pattern1), show="*")
password.pack(padx=10, pady=10)

# Remember Login
checkbox = ctk.CTkCheckBox(mainwindow, text="Remember Login?", font=(pattern1))
checkbox.pack(padx=10, pady=10)

# Create an instance of ToplevelWindow when needed
def open_toplevel():
    toplevel_window = ToplevelWindow(mainwindow)

# Login Button
button = ctk.CTkButton(mainwindow, text=("Login"), cursor="hand2", font=(pattern1), command=open_toplevel)
button.pack(padx=10, pady=10)

creator = ctk.CTkLabel(mainwindow, text=("Created by: @ropelatoo"), font=(pattern3))
creator.pack(padx=10, pady=50, side="bottom")

# End here
mainwindow.mainloop()