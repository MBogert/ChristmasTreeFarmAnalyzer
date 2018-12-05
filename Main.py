from tkinter import *
import PIL.Image
import PIL.ImageTk
import GUIProcessing
import Variables

class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createFrame(self):

        # Initialize Frame
        self.canvas = Canvas(self)
        self.canvas["width"] = 600
        self.canvas["height"] = 347

        # Create Image
        img = PIL.Image.open("PrettyImage.png")
        self.photo = PIL.ImageTk.PhotoImage(img)
        self.canvas.create_image(20, 20, anchor = NW, image = self.photo)

        # Pack
        self.canvas.pack()

    def createWidgets(self):

    	# Exit
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        # Spam Hello
        self.hi_there = Button(self)
        self.hi_there["text"] = "Submit Farm"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side": "left"})

        # Input Field (Address)
        self.address = Entry(self)
        self.address["text"] = "Farm Address"
        self.address.pack({"side": "left"})

        # Input Field (Acreage)
        self.acres = Entry(self)
        self.acres["text"] = "Farm Size (in acres)"
        self.acres.pack({"side": "left"})


        # Input Field (Tree Species)
        # Selection container
        self.breedSelector = StringVar(self)
        # Dropdown
        self.breedMenu = OptionMenu(self, self.breedSelector, *Variables.breeds)
        self.breedMenu.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createFrame()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()