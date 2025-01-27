from tkinter import *

cnvt = ""
def convert(y):
    x = int(y)
    print(x)
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
background_img = PhotoImage(file = f"background1.png")
background = canvas.create_image(
    702.0, 523.5,
    image=background_img)
img0 = PhotoImage(file = f"submit.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = convert(cnvt),
    relief = "flat")
b0.place(
    x = 1226, y = 500,
    width = 246,
    height = 86)
img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = cnvt + "0" ,
    relief = "flat")
b1.place(
    x = 1311, y = 398,
    width = 75,
    height = 60)
img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = cnvt + "1",
    relief = "flat")
b2.place(
    x = 1225, y = 172,
    width = 75,
    height = 60)
img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = cnvt + "2",
    relief = "flat")
b3.place(
    x = 1311, y = 172,
    width = 75,
    height = 60)
img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = cnvt + "3",
    relief = "flat")
b4.place(
    x = 1397, y = 172,
    width = 75,
    height = 60)
img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = cnvt + "4",
    relief = "flat")
b5.place(
    x = 1225, y = 247,
    width = 75,
    height = 60)
img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = cnvt + "5",
    relief = "flat")
b6.place(
    x = 1311, y = 247,
    width = 75,
    height = 60)
img7 = PhotoImage(file = f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = cnvt + "6",
    relief = "flat")
b7.place(
    x = 1397, y = 247,
    width = 75,
    height = 60)
img8 = PhotoImage(file = f"img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = cnvt + "7",
    relief = "flat")
b8.place(
    x = 1225, y = 322,
    width = 75,
    height = 60)
img9 = PhotoImage(file = f"img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = cnvt + "8",
    relief = "flat")
b9.place(
    x = 1311, y = 322,
    width = 75,
    height = 60)
img10 = PhotoImage(file = f"img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = cnvt + "9",
    relief = "flat")
b10.place(
    x = 1397, y = 322,
    width = 75,
    height = 60)
canvas.create_rectangle(
    1007, 229, 1007+50, 229+50,
    fill = "#d3ffcb",
    outline = "")
canvas.create_rectangle(
    1080, 229, 1080+50, 229+50,
    fill = "#c6e4ff",
    outline = "")

window.resizable(True, True)
window.mainloop()
