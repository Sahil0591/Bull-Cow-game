from tkinter import *
import GUI2

def show_result(window, win, attempts=None):
    for widget in window.winfo_children():
        widget.destroy()
    window.geometry("1536x864")
    window.configure(bg="#ffffff")
    window.title("Game Result")

    # Store images to prevent garbage collection
    window.images = {}

    # Background image
    window.images['background'] = PhotoImage(file="images/Result-BG1.png")
    canvas = Canvas(window, bg="#ffffff", height=864, width=1536, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    canvas.create_image(768, 432, image=window.images['background'])

    # Center message
    if win:
        if attempts == 1:
            msg = "Incredible! You solved it in just 1 attempt!"
        else:
            msg = f"You win! You solved the code in {attempts} attempts."
    else:
        msg = "You lose, try again!"

    label = Label(window, text=msg, font=("Arial", 24), bg="#bdf4f0")
    label.place(relx=0.5, rely=0.4, anchor="center")

    # Button images
    window.images['restart'] = PhotoImage(file="images/New-Game.png")
    window.images['quit'] = PhotoImage(file="images/QUIT.png")

    def restart():
        for widget in window.winfo_children():
            widget.destroy()
        GUI2.main_window(window)

    def quit_game():
        window.destroy()

    # Buttons with images
    restart_btn = Button(window, image=window.images['restart'], borderwidth=0, highlightthickness=0, command=restart, relief="flat", bg="#ffffff", activebackground="#ffffff")
    restart_btn.place(relx=0.4, rely=0.6, anchor="center")

    quit_btn = Button(window, image=window.images['quit'], borderwidth=0, highlightthickness=0, command=quit_game, relief="flat", bg="#ffffff", activebackground="#ffffff")
    quit_btn.place(relx=0.6, rely=0.6, anchor="center")
