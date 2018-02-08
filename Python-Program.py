import random  #imports random module
from time import sleep #imports pauses
from datetime import datetime #imports a real clock
import webbrowser, os #imports Google Chrome Browser
from me import *  #imports my saved file
import string #imports the English Alphabet
from tkinter import *   #These Modules both Import the Python GUI
from tkinter import messagebox
from xml.dom import minidom  #Imports a XML Parser
from subprocess import call #Uploads to Dropbox from Pi
from turtle import * #For Animations

def start(begin):  #Begins our main Function sequence
    while True:  #begins an infinite loop
        
        if begin != 0:   #Boolean check
            print("False") #incorrect!
        
        elif begin == 0:   #another Boolean Check
            print("True") #Yes!
            sleep(1) #pause....
            break  #.....continue!
    
    number=(int(input("Please enter the amount of People in the Team..."))) #Enter the amount of People in the Team i.e. 3
    jobs = ['Chairperson', 'Secretary', 'Treasurer']  #These are the available positions in a nice LIST
    committee = {'Chairperson': 'N/A', 'Secretary': 'N/A', 'Treasurer': 'N/A'}  #This is the DICTIONARY of all the Committee Positions

    for x in range (1,number + 1):  #begins a variable range FOR LOOP
        person=input("Please enter the " + (str(x)) + "{}/{}/{} Person's name in the Team...".format('st', 'nd', 'rd')) #Enter the Name of the People applying for the Positions
        job = random.choice(jobs)  #a fair random choice of the Jobs....
        sleep(2) #pause
        print( person + " is the " + job)#Announcement of the Job
        sleep(1) #pause again
        if job == "Chairperson":   #So, basically, this whole piece of code occurs over and over again until all the people in the team have been elected. This code checks out that the list does not repeat itself over and over again and makes sure that a position is only elected once
            del jobs[0];    #removes the availability of the position
        elif job == "Secretary":  #next job
            del jobs[1];     #removes the availability of the position
        elif job == "Chairperson":  #next job
            del jobs[2];       #removes the availability of the position
        else:
            print("Error")    #An error just in case, to point it out 
        committee[job] = person;  #Adds the person to the position

        #Once. all the code is finished; then it formats the dictionary as a STRING
        committeestr = str(committee)
        

    target1 = open('committee.html', 'w')  #Opens a WRITE FILE i.e. HTML File for the Web
 
    target1.write("""<html>
<head></head><style> h1{ font-size: 15px; text-align: center; font-weight: bold;} </style>
<body><h1> """ + committeestr + """</h1> </html>""")   #Creates the HTML File needed to view the List of Positions on the WEB
 
    target1.close()  #Finishes with the File

    webbrowser.open_new_tab('committee.html')   #Opens up the new file to view!!

    #Upload = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /path/to/file/"
    #call ([Upload], shell=True)

    top = Tk()  #Starts TKinter
    top.geometry("100x100")   #Makes a nice box for the GUI
    def committeeCallBack():  #A function for our Dialog Box
        msg = messagebox.showinfo( "Committee", str(committee))  #Opens a message dialog box

    B = Button(top, text = "Show Team", command = committeeCallBack) #Creates and Formats a Button
    B.place(x = 50,y = 50)  #Postions it nicely

    C = Button(top, text = "Exit", command = quit).pack()  #Creates and Formats a Button to exit cleanly
    C.place(x = 75,y = 50) #Postions it nicely, once agin
    top.mainloop() #Begins the WIndow

#START OF THE ACTUAL PROGRAM*************

time = datetime.now()   #Gets a Clock
print("Timestamp: " + str(time))  #Shows the Time NOW
canvas = Screen()    #Operates a Turtle Drawing

number = random.randrange(0, 800)


turtle = Turtle()

for i in range(4):
    turtle.forward(100) #number
    turtle.left(90)  #number

canvas.exitonclick()
start(0)  #Starts the Main Code, beginnning with Booolean
#Did not get to Finish....
xmldoc = minidom.parse('example.xml')  #Takes an XML Document
alphabetletters = string.ascii_lowercase #Takes the English ASCII Alphabet
letter = random.choice(string.ascii_lowercase) #A String
