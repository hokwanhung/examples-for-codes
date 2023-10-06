import tkinter as tk

root = tk.Tk()

# Define the default GUI size.
root.geometry("800x500")
root.title("My First GUI")

label = tk.Label(root, text="Hellow World!", font=('Arial', 18))
# Define the padding of the element (just like CSS).
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10)

buttonframe = tk.Frame(root)
# Define how many columns and how much width does each column has.
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
# "sticky=tk.W+tk.E" streches the btn1 to the border of the container.
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

# Inside the pack layout of the buttonframe, lies the grid layout of buttons.
buttonframe.pack(fill='x')

anotherbtn = tk.Button(root, text='TEST')
# Similar to absolute position of CSS layouts.
anotherbtn.place(x=200, y=200, height=100, width=100)


button = tk.Button(root, text="Click Me!", font=('Arial', 18))
button.pack(padx=10, pady=10)

root.mainloop()
