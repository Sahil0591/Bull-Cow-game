from tkinter import *
import GUI2

def show_result(window, win, attempts=None):
    for widget in window.winfo_children():
        widget.destroy()
    window.geometry("1536x864")
    window.configure(bg="#ffffff")
    window.title("Game Result")

    # Center message
    if win:
        msg = f"You win! You solved the code in {attempts} attempts."
    else:
        msg = "You lose, try again!"

    label = Label(window, text=msg, font=("Arial", 24), bg="#ffffff")
    label.pack(expand=True)

    # Button frame at the bottom
    btn_frame = Frame(window, bg="#ffffff")
    btn_frame.pack(side=BOTTOM, pady=40)

    def restart():
        for widget in window.winfo_children():
            widget.destroy()
        GUI2.main_window(window)

    def quit_game():
        window.destroy()

    restart_btn = Button(btn_frame, text="Restart", font=("Arial", 16), width=12, command=restart)
    restart_btn.pack(side=LEFT, padx=20)

    quit_btn = Button(btn_frame, text="Quit", font=("Arial", 16), width=12, command=quit_game)
    quit_btn.pack(side=RIGHT, padx=20)
