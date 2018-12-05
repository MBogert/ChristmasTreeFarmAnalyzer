from tkinter import *
import GUIProcessing

class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):

    	# Exit
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        # Spam Hello
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
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
        # List of species
        breeds = {"Balsalm Fir", "Fraser Fir", "Canaan Fir", "Douglass Fir", "Grand Fir", "Noble Fir", "Concolor Fir", "White Pine", "Scotch Pine", "Virginia Pine", "Blue Spruce", "Norway Spruce", "White Spruce", "Arizona Cypress", "Leyland Cypress", "Red Cedar"}
        # Selection container
        self.breedSelector = StringVar(self)
        # Dropdown
        self.breedMenu = OptionMenu(self, self.breedSelector, *breeds)
        self.breedMenu.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()