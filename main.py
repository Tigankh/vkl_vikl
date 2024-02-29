import tkinter
from tkmacosx import Button

window = tkinter.Tk()
window.geometry('800x700')
label = tkinter.Label(text='\t\tвыкл\t\t       ', font=('Arial', 40), bg='green')
label.grid(row=0, column=1, columnspan=2)
label2 = tkinter.Label(text='', height=17)
label2.grid(row=1)

btn = Button(text='Выключатель', bg='blue', width=140, height=130, command=lambda: change_button())
btn.grid(row=5, column=1, columnspan=2)


def change_button():
    if label.cget('text') == '\t\tвыкл\t\t       ':
        label.configure(text='\t\tвкл\t\t       ', bg='yellow')
    else:
        label.configure(text='\t\tвыкл\t\t       ', bg='green')


window.mainloop()

