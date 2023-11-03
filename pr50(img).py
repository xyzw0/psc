# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()
root.title("xyyz")

# Adding widgets to the root window
Label(root, text = 'namexyz’, font =(
'Verdana', 15)).pack(side = TOP, pady = 10)

# Creating a photoimage object to use image
photo = PhotoImage(file = r"D:\Users\location\Desktop\Python Practicals\abc.png")

# here, image option is used to
# set image on button
Button(root, text = 'Click Me !', image = photo).pack(side = TOP)

mainloop()
