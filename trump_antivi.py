import os
import webbrowser
from Tkinter import *
from tkMessageBox import *

#the basics
root = Tk()
root.title("Donald Trump Virus Scanner")
root.geometry("680x420")

#functions
def callback():
	showwarning("Totally", "It's gonna be uuge.")
def vote():
	if askyesno("On Our Side?", "Did you actually vote for Trump?"):
		showwarning("Drones Disabled", "Good to hear!")
	else:
		showinfo("Fake News", "I'll be speaking about you on my Twitter")
def twitter():
#	os.system("firefox https://twitter.com/realDonaldTrump")
	webbrowser.open_new("https://twitter.com/realDonaldTrump")

#frame
app = Frame(root)
app.grid()
label = Label(app, text = "Making your computer great again!")
#msg = Message(root, text = "I'm gonna get rid of all the viruses, and make the hackers pay for it!")
button1 = Button(app, fg= "white", width= "20", height= "3", text = "Click to build a firewall.", command=callback)
button2 = Button(app, fg= "red", width= "30", height= "3", text = "I'm gonna ask you just one question...", command=vote)
button3 = Button(app, text= "Click to go to Trump's Twitter", command=twitter)
label.grid()
button1.grid()
button2.grid()
button3.grid()

#keep at bottom
#msg.pack()
root.mainloop()

