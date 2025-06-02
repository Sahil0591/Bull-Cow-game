from tkinter import *
import GUI2
buttonstate=False
def btn_clicked():
    for widget in window.winfo_children():
        widget.destroy()
    GUI2.main_window(window)
window = Tk()
window.geometry("1536x864")
window.configure(bg = "#ffffff")

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 864,
    width = 1536,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
background_img = PhotoImage(file = f"Bull & Cow game/images/background.png")
background = canvas.create_image(
    768.0, 432.0,
    image=background_img)
img0 = PhotoImage(file = f"Bull & Cow game/images/img0.png")
b = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")
b.place(
    x = 861, y = 647,
    width = 187,
    height = 52)
window.resizable(True, True)
window.mainloop()