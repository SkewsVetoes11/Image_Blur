import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
import os
from PIL import Image, ImageFilter

root = Tk()
root.geometry("1000x480")
root.title('Image Blur')

input_dir = StringVar()
input_dir.set("Not Defined!")

mode = "-1"


def gaussian_blur(img, filepath, degree):
    img_rgb = img.convert("RGB")
    gaussImage = img_rgb.filter(ImageFilter.GaussianBlur(degree))
    gaussImage.save(filepath + " " + "Blur Degree " + str(degree) + ".png")


def iterate_dir(directory, degree):
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            f = f.replace('\\', '/')
            if "Blur" not in filename:
                img = Image.open(f)
                gaussian_blur(img, f, degree)


def select_dir():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "":
        input_dir.set("Not Defined!")
    else:
        input_dir.set(str(folder_selected))


myLabel = Label(root, text="Input Directory: ")
label1 = Label(root, textvariable=input_dir)
select_btn = Button(root, text="Select Directory", command=select_dir)

myLabel.grid(column=0, row=1)
label1.grid(column=1, row=1)
select_btn.grid(column=2, row=1)


def on_select():
    selected_option = radio_var.get()
    global mode
    mode = selected_option


# Create a variable to hold the selected option
radio_var = tk.StringVar()

# Create Radiobuttons
radio_button1 = tk.Radiobutton(root, text="Blur with Single Degree", variable=radio_var, value="1",
                               command=on_select)
radio_button2 = tk.Radiobutton(root, text="Blur with Degree Range", variable=radio_var, value="2",
                               command=on_select)

Label(root, text="Mode: ").grid(column=0, row=2)
radio_button1.grid(column=1, row=2, padx=5, pady=15)
radio_button2.grid(column=2, row=2)

Label(root, text="If single degree, input degree").grid(column=0, row=3, pady=15)
Label(root, text="If range degree, input range").grid(column=0, row=4, pady=15)

single_deg = tk.Entry(root)
single_deg.grid(column=1, row=3)

low_deg = tk.Entry(root)
low_deg.grid(column=1, row=4)
Label(root, text="to").grid(column=2, row=4)
hi_deg = tk.Entry(root)
hi_deg.grid(column=3, row=4)


def execute():
    global single_deg, input_dir
    if input_dir.get() == "Not Defined!":
        showinfo(title="Error", message="Please specify an input directory!")
    if mode == "1":
        deg = single_deg.get()
        try:
            deg_int = int(deg)
            iterate_dir(input_dir.get(), deg_int)
        except:
            showinfo(title="Error", message="Please check your degree value!")
    elif mode == "2":

        try:
            deg_low = int(low_deg.get())
            deg_high = int(hi_deg.get())
            for i in range(deg_low, deg_high + 1):
                iterate_dir(input_dir.get(), i)

        except:
            showinfo(title="Error", message="Please check your degree value!")


    else:
        showinfo(title="Error", message="Please select a mode!")

    pass


select_btn = Button(root, text="Execute!", command=execute)
select_btn.grid(row=5, column=3, sticky=tk.E, pady=20)

root.mainloop()
