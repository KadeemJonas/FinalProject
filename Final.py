##############################
# Name: Caitlin Richardson and Kadeem Jonas 
# Date: May 5, 2022
# Description: Flippity Floppity! The Memory Game
###################################################

import threading
from tkinter import *
import random
from time import sleep
import RPi.GPIO as GPIO

card=[0,0,1,1,2,2]
random.shuffle(card)
card2=[0,0,1,1,2,2,3,3,4,4,5,5]
random.shuffle(card2)
card3=["*","*","|","|","[","[","]","]","$","$","%","%","&","&","@","@","#","#","^","^"]
random.shuffle(card3)
card4=[":O",":O",":o",":o","._.","._.",":)",":)",":(",":(","-_-","-_-","o_o","o_o",":P",":P","(-_-)","(-_-)","(:","(:","):","):",";)",";)","O_O","O_O","(._.)","(._.)","(O_O)","(O_O)"]
random.shuffle(card4)
card5=["hair","hair","hear","hear","here","here","hare","hare","bare","bare","beer","beer","bear","bear","Chile","Chile","chilly","chilly","chili","chili","meet","meet","meat","meat","basis","basis","bases","bases","basses","basses","two","two","to","to","too","too"]
random.shuffle(card5)
green = 18
green2 = 19
green3 = 20
red = 17
red2 = 16
red3 = 13

# use the Broadcom pin mode
 GPIO.setmode(GPIO.BCM)
  
# setup the output pins
GPIO.setup(green, GPIO.OUT)
GPIO.setup(green2, GPIO.OUT)
GPIO.setup(green3, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(red2, GPIO.OUT)
GPIO.setup(red3, GPIO.OUT)

#subprogram for if it matches
def yay():
    for i in range (3):
        GPIO.output(green, 1)
        GPIO.output(green2, 1)
        GPIO.output(green3, 1)
        sleep(0.05)
        GPIO.output(green, 0)
        GPIO.output(green2, 0)
        GPIO.output(green3, 0)
        sleep(0.05)
#subprogram for if it is not a match
def aw():
    for i in range (3):
        GPIO.output(red, 1)
        GPIO.output(red2, 1)
        GPIO.output(red3, 1)
        sleep(0.05)
        GPIO.output(red, 0)
        GPIO.output(red2, 0)
        GPIO.output(red3, 0)
        sleep(0.05)

#matches keep track card value
matches=[]
flips=0
pairs = 0
attempts = 0
#button_position keep tracks of which button is clicked
button_position=[]
class Match(Frame):
    global A
    def __init__(self, master):
        Frame.__init__(self, master)
    
    #create the game interface
    def start(self):
        global welcome, pick, classic, timed, tries, leave
        welcome=Label(self.master, text="Welcome To Our Memory Game")
        welcome.pack(padx=20)
        pick=Label(self.master, text="Choose the mode below")
        pick.pack(padx=20)
        classic=Button(self.master, text="Classic mode", bg="blue", fg="white", command=lambda: self.levelone("A"))
        timed=Button(self.master, text="Timed mode", bg="cyan", fg="white", command=lambda: self.levelone("C"))
        tries=Button(self.master, text="Attempts mode", bg="green", fg="white", command=lambda: self.levelone("B"))
        leave=Button(self.master, text="Exit Game", bg="red", fg="white", command=self.closegame)
        classic.pack(padx=20, fill = X)
        timed.pack(padx=20, fill = X)
        tries.pack(padx=20, fill = X)
        leave.pack(padx=20, fill = X)
     
    def clearFrame(self):
        global Finish
        
        returnhome.destroy()
        label.destroy()
        
    def home(self):
        global welcome, pick, classic, timed, tries, leave
        self.clearFrame()
        
    
        welcome=Label(self.master, text="Welcome To Our Memory Game")
        welcome.pack(padx=20)
        pick=Label(self.master, text="Choose the mode below")
        pick.pack(padx=20)
        classic=Button(self.master, text="Classic mode", bg="blue", fg="white", command=lambda: self.levelone("A"))
        timed=Button(self.master, text="Timed mode", bg="cyan", fg="white", command=lambda: self.levelone("C"))
        tries=Button(self.master, text="Attempts mode", bg="green", fg="white", command=lambda: self.levelone("B"))
        leave=Button(self.master, text="Exit Game", bg="red", fg="white", command=self.closegame)
        classic.pack(padx=20, fill = X)
        timed.pack(padx=20, fill = X)
        tries.pack(padx=20, fill = X)
        leave.pack(padx=20, fill = X)
    
    def closegame(self):
        # reset the GPIO pins
        #GPIO.cleanup()
        # exit the game
        exit(0)
    
    def timer(self):
        global expired, minute, second, stopwatch, stop, returnhome, label, level, Finish
        
        if minute>0:
            if second>0:
                second-=1
            elif second == 0:
                minute -= 1
                second = 59
        elif minute == 0:
            if second > 0:
                second -=1
            elif second == 0:
                expired = True
                #clear screen
                if (level == 1) :
                    b1.destroy()
                    b2.destroy()
                    b3.destroy()
                    b4.destroy()
                    b5.destroy()
                    b6.destroy()
                if (level == 2):
                    b1.destroy()
                    b2.destroy()
                    b3.destroy()
                    b4.destroy()
                    b5.destroy()
                    b6.destroy()
                    b7.destroy()
                    b8.destroy()
                    b9.destroy()
                    b10.destroy()
                    b11.destroy()
                    b12.destroy()
                if (level == 3):
                    b1.destroy()
                    b2.destroy()
                    b3.destroy()
                    b4.destroy()
                    b5.destroy()
                    b6.destroy()
                    b7.destroy()
                    b8.destroy()
                    b9.destroy()
                    b10.destroy()
                    b11.destroy()
                    b12.destroy()
                    b13.destroy()
                    b14.destroy()
                    b15.destroy()
                    b16.destroy()
                    b17.destroy()
                    b18.destroy()
                    b19.destroy()
                    b20.destroy()
                if (level == 4):
                    b1.destroy()
                    b2.destroy()
                    b3.destroy()
                    b4.destroy()
                    b5.destroy()
                    b6.destroy()
                    b7.destroy()
                    b8.destroy()
                    b9.destroy()
                    b10.destroy()
                    b11.destroy()
                    b12.destroy()
                    b13.destroy()
                    b14.destroy()
                    b15.destroy()
                    b16.destroy()
                    b17.destroy()
                    b18.destroy()
                    b19.destroy()
                    b20.destroy()
                    b21.destroy()
                    b22.destroy()
                    b23.destroy()
                    b24.destroy()
                    b25.destroy()
                    b26.destroy()
                    b27.destroy()
                    b28.destroy()
                    b29.destroy()
                    b30.destroy()
                if (level == 5):
                    b1.destroy()
                    b2.destroy()
                    b3.destroy()
                    b4.destroy()
                    b5.destroy()
                    b6.destroy()
                    b7.destroy()
                    b8.destroy()
                    b9.destroy()
                    b10.destroy()
                    b11.destroy()
                    b12.destroy()
                    b13.destroy()
                    b14.destroy()
                    b15.destroy()
                    b16.destroy()
                    b17.destroy()
                    b18.destroy()
                    b19.destroy()
                    b20.destroy()
                    b21.destroy()
                    b22.destroy()
                    b23.destroy()
                    b24.destroy()
                    b25.destroy()
                    b26.destroy()
                    b27.destroy()
                    b28.destroy()
                    b29.destroy()
                    b30.destroy()
                    b31.destroy()
                    b32.destroy()
                    b33.destroy()
                    b34.destroy()
                    b35.destroy()
                    b36.destroy()
                Finish.destroy()
                stopwatch.destroy()
                label=Label(self.master, text="YOU RAN OUT OF TIME! TRY AGAIN!")
                label.grid(row=1, column=0, columnspan=3)
                returnhome = Button(self.master, text="Return to Home Menu", command=self.home)
                returnhome.grid(row=0, column=0, columnspan=3)
                
        
        # Update Label.
        time_string = "{:02d}:{:02d}".format(minute, second)
        if (not expired):
            stopwatch.config(text=time_string)
            self.after(1000, self.timer)
        else:
            expired = False
        
    # what happens when you click a button in classic mode
    # arguments (button, value it takes from list, level, total pairs, which list to pull values from)
    def click(self, b, number, deck, level):
        global flips, End, matches, button_position, Next, pairs
        if b["text"]== " "and flips<2:
            b["text"]=deck[number]
            flips+=1
            #add the value of the card to a list
            matches.append(deck[number])
            button_position.append(b)
            
        #check for matches
        if len(matches)==2:
            #everytime two buttons are clicked make sure there is no text at the bottom of screen
            
            
            #if the two buttons clicked match
            if matches[0]==matches[1]:
                pairs += 1
                #if buttons match make them not buttons
                #https://stackoverflow.com/questions/53580507/disable-enable-button-in-tkinter           
                for button in button_position:
                    button["state"]= "disable"
                flips=0
                matches=[]
                button_position=[]
                yay()
            #if theres no match    
            else:
                End=Button(self.master, text="Click to flip cards back over", height = 3, width = 27 ,command=self.back)
                End.grid(row=6, column=3, columnspan = 3)
                aw()
 
    # what happens when you click a button in attempted tries mode 
    def clickA(self, b, number, deck, level):
        global flips, End, matches, button_position, Next, pairs, attempts, home, returnhome, label
        if b["text"]== " "and flips<2:
            b["text"]=deck[number]
            flips += 1
            #add the value of the card to a list
            matches.append(deck[number])
            button_position.append(b)
            
        #check for matches
        if len(matches)==2:
            #everytime two buttons are clicked make sure there is no text at the bottom of screen
                       
            #if the two buttons clicked match
            if matches[0]==matches[1]:
                pairs += 1
                flips = 0
                
                #if buttons match make them not buttons
                #https://stackoverflow.com/questions/53580507/disable-enable-button-in-tkinter           
                for button in button_position:
                    button["state"]= "disable"
                matches=[]
                button_position=[]
                yay()                
            #if theres no match    
            else:
                attempts += 1
                End=Button(self.master, text="Click to flip cards back over", height = 3, width = 27, command=self.back)
                End.grid(row=6, column=3, columnspan=3)
                aw()        
        if level == 1:
            max_tries = 5 #40 chances 46
        elif level == 2:
            max_tries = 10 #30 chances  50 
        elif level == 3:
            max_tries = 20 #25 chances 55
        elif level == 4:
            max_tries = 20 #20 chances 50
        elif level == 5:
            max_tries = 15 #+15 chances 50
        #if you run out of attempts
        if (attempts == max_tries):
            #clear screen
            if (level == 1) :
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                b5.destroy()
                b6.destroy()
            if (level == 2):
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                b5.destroy()
                b6.destroy()
                b7.destroy()
                b8.destroy()
                b9.destroy()
                b10.destroy()
                b11.destroy()
                b12.destroy()
            if (level == 3):
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                b5.destroy()
                b6.destroy()
                b7.destroy()
                b8.destroy()
                b9.destroy()
                b10.destroy()
                b11.destroy()
                b12.destroy()
                b13.destroy()
                b14.destroy()
                b15.destroy()
                b16.destroy()
                b17.destroy()
                b18.destroy()
                b19.destroy()
                b20.destroy()
            if (level == 4):
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                b5.destroy()
                b6.destroy()
                b7.destroy()
                b8.destroy()
                b9.destroy()
                b10.destroy()
                b11.destroy()
                b12.destroy()
                b13.destroy()
                b14.destroy()
                b15.destroy()
                b16.destroy()
                b17.destroy()
                b18.destroy()
                b19.destroy()
                b20.destroy()
                b21.destroy()
                b22.destroy()
                b23.destroy()
                b24.destroy()
                b25.destroy()
                b26.destroy()
                b27.destroy()
                b28.destroy()
                b29.destroy()
                b30.destroy()
            if (level == 5):
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                b5.destroy()
                b6.destroy()
                b7.destroy()
                b8.destroy()
                b9.destroy()
                b10.destroy()
                b11.destroy()
                b12.destroy()
                b13.destroy()
                b14.destroy()
                b15.destroy()
                b16.destroy()
                b17.destroy()
                b18.destroy()
                b19.destroy()
                b20.destroy()
                b21.destroy()
                b22.destroy()
                b23.destroy()
                b24.destroy()
                b25.destroy()
                b26.destroy()
                b27.destroy()
                b28.destroy()
                b29.destroy()
                b30.destroy()
                b31.destroy()
                b32.destroy()
                b33.destroy()
                b34.destroy()
                b35.destroy()
                b36.destroy()
                
            #display level failed
            attempts = 0
            flips = 0
            matches=[]
            button_position=[]
            End.destroy()
            Finish.destroy()
            label=Label(self.master, text="YOU RAN OUT OF TRIES! TRY AGAIN!")
            label.grid(row=1, column=0, columnspan=3)
            returnhome = Button(self.master, text="Return to Home Menu", command=self.home)
            returnhome.grid(row=0, column=0, columnspan=3)
            
    #what happens when you click a button in timed mode        
    def clickB(self, b, number, deck, level):
        global flips, End, matches, button_position, Next, pairs, minute, second
        
           
        if b["text"]== " "and flips<2:
            b["text"]=deck[number]
            flips+=1
            #add the value of the card to a list
            matches.append(deck[number])
            button_position.append(b)
            
        #check for matches
        if len(matches)==2:
            #everytime two buttons are clicked make sure there is no text at the bottom of screen
            
            #if the two buttons clicked match
            if matches[0]==matches[1]:
                pairs += 1
                #if buttons match make them not buttons
                #https://stackoverflow.com/questions/53580507/disable-enable-button-in-tkinter           
                for button in button_position:
                    button["state"]= "disable"
                flips=0
                matches=[]
                button_position=[]
                yay()
            #if theres no match    
            else:
                
                End=Button(self.master, text="Click to flip cards back over", height = 3, width = 27 ,command=self.back)
                End.grid(row=6, column=3, columnspan = 3)
                aw()               
    
    
    #how to get rid of label
    #https://stackoverflow.com/questions/52059974/how-to-delete-or-destroy-label-in-tkinter
    #flips the cards back over and then deletes the label and flip button for next turn
    def back(self):
        global button_position, flips, matches, l1, End
        flips = 0
        matches=[]
        for button in button_position:
            button["text"]= " "
        button_position=[]
        End.destroy()
   
    def check(self, level, total):
        global pairs, Next, label, End, home, returnhome
        if (level == 1 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            #create the next button
            Next=Button(self.master, text="Next Level", height = 3, width = 27,  command=lambda: self.leveltwo("A"))
            Next.grid(row=0,column=0)
        if (level == 2 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            b7.destroy()
            b8.destroy()
            b9.destroy()
            b10.destroy()
            b11.destroy()
            b12.destroy()
            #create the next button
            Next=Button(self.master, text="Next Level", height = 3, width = 27,  command=lambda: self.levelthree("A"))
            Next.grid(row=0,column=0)
        if (level == 3 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            b7.destroy()
            b8.destroy()
            b9.destroy()
            b10.destroy()
            b11.destroy()
            b12.destroy()
            b13.destroy()
            b14.destroy()
            b15.destroy()
            b16.destroy()
            b17.destroy()
            b18.destroy()
            b19.destroy()
            b20.destroy()
            #create the next button
            Next=Button(self.master, text="Next Level", height = 3, width = 27,  command=lambda: self.levelfour("A"))
            Next.grid(row=0,column=0)
            
        if (level == 4 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            b7.destroy()
            b8.destroy()
            b9.destroy()
            b10.destroy()
            b11.destroy()
            b12.destroy()
            b13.destroy()
            b14.destroy()
            b15.destroy()
            b16.destroy()
            b17.destroy()
            b18.destroy()
            b19.destroy()
            b20.destroy()
            b21.destroy()
            b22.destroy()
            b23.destroy()
            b24.destroy()
            b25.destroy()
            b26.destroy()
            b27.destroy()
            b28.destroy()
            b29.destroy()
            b30.destroy()
            
            #create the next button
            Next=Button(self.master, text="Next Level", height = 3, width = 27,  command=lambda: self.levelfive("A"))
            Next.grid(row=0,column=0)
            
        if (level == 5 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            b7.destroy()
            b8.destroy()
            b9.destroy()
            b10.destroy()
            b11.destroy()
            b12.destroy()
            b13.destroy()
            b14.destroy()
            b15.destroy()
            b16.destroy()
            b17.destroy()
            b18.destroy()
            b19.destroy()
            b20.destroy()
            b21.destroy()
            b22.destroy()
            b23.destroy()
            b24.destroy()
            b25.destroy()
            b26.destroy()
            b27.destroy()
            b28.destroy()
            b29.destroy()
            b30.destroy()
            b31.destroy()
            b32.destroy()
            b33.destroy()
            b34.destroy()
            b35.destroy()
            b36.destroy()
            #create the next button
            returnhome=Button(self.master, text="Return to Home", height = 3, width = 27, command=self.home)
            returnhome.grid(row=0,column=0)
            
    def checkA(self, level, total):
        global pairs, Next, label, End, returnhome
        if (level == 1 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            #create the next button
            Next=Button(self.master, text="Next Level", height = 3, width = 27,  command=lambda: self.leveltwo("B"))
            Next.grid(row=0,column=0)
        if (level == 2 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            b7.destroy()
            b8.destroy()
            b9.destroy()
            b10.destroy()
            b11.destroy()
            b12.destroy()
            #create the next button
            Next=Button(self.master, text="Next Level", height = 3, width = 27,  command=lambda: self.levelthree("B"))
            Next.grid(row=0,column=0)
        if (level == 3 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            b7.destroy()
            b8.destroy()
            b9.destroy()
            b10.destroy()
            b11.destroy()
            b12.destroy()
            b13.destroy()
            b14.destroy()
            b15.destroy()
            b16.destroy()
            b17.destroy()
            b18.destroy()
            b19.destroy()
            b20.destroy()
        
            #create the next button
            Next=Button(self.master, text="Next Level", height = 3, width = 27,  command=lambda: self.levelfour("B"))
            Next.grid(row=0,column=0)
            
        if (level == 4 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            b7.destroy()
            b8.destroy()
            b9.destroy()
            b10.destroy()
            b11.destroy()
            b12.destroy()
            b13.destroy()
            b14.destroy()
            b15.destroy()
            b16.destroy()
            b17.destroy()
            b18.destroy()
            b19.destroy()
            b20.destroy()
            b21.destroy()
            b22.destroy()
            b23.destroy()
            b24.destroy()
            b25.destroy()
            b26.destroy()
            b27.destroy()
            b28.destroy()
            b29.destroy()
            b30.destroy()
            
            #create the next button
            Next=Button(self.master, text="Next Level", height = 3, width = 27,  command=lambda: self.levelfive("B"))
            Next.grid(row=0,column=0)
            
        if (level == 5 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            b7.destroy()
            b8.destroy()
            b9.destroy()
            b10.destroy()
            b11.destroy()
            b12.destroy()
            b13.destroy()
            b14.destroy()
            b15.destroy()
            b16.destroy()
            b17.destroy()
            b18.destroy()
            b19.destroy()
            b20.destroy()
            b21.destroy()
            b22.destroy()
            b23.destroy()
            b24.destroy()
            b25.destroy()
            b26.destroy()
            b27.destroy()
            b28.destroy()
            b29.destroy()
            b30.destroy()
            b31.destroy()
            b32.destroy()
            b33.destroy()
            b34.destroy()
            b35.destroy()
            b36.destroy()
            #create the next button
            returnhome=Button(self.master, text="Return to Home", height = 3, width = 27, command=self.home)
            returnhome.grid(row=0,column=0)
    def checkB(self, level, total):
        global pairs, Next, label, End, home, stop, returnhome, stopwatch
        if (level == 1 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            
            #destroy buttons that are on the screen
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            stopwatch.destroy()
            
            #create the next button
            Next=Button(self.master, text="Next Level", height = 3, width = 27,  command=lambda: self.leveltwo("C"))
            Next.grid(row=0,column=0)
        if (level == 2 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            b7.destroy()
            b8.destroy()
            b9.destroy()
            b10.destroy()
            b11.destroy()
            b12.destroy()
            stopwatch.destroy()
            #create the next button
            Next=Button(self.master, text="Next Level", height = 3, width = 27,  command=lambda: self.levelthree("C"))
            Next.grid(row=0,column=0)
        if (level == 3 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            b7.destroy()
            b8.destroy()
            b9.destroy()
            b10.destroy()
            b11.destroy()
            b12.destroy()
            b13.destroy()
            b14.destroy()
            b15.destroy()
            b16.destroy()
            b17.destroy()
            b18.destroy()
            b19.destroy()
            b20.destroy()
            stopwatch.destroy()
            #create the next button
            Next=Button(self.master, text="Next Level", height = 3, width = 27,  command=lambda: self.levelfour("C"))
            Next.grid(row=0,column=0)
            
        if (level == 4 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            b7.destroy()
            b8.destroy()
            b9.destroy()
            b10.destroy()
            b11.destroy()
            b12.destroy()
            b13.destroy()
            b14.destroy()
            b15.destroy()
            b16.destroy()
            b17.destroy()
            b18.destroy()
            b19.destroy()
            b20.destroy()
            b21.destroy()
            b22.destroy()
            b23.destroy()
            b24.destroy()
            b25.destroy()
            b26.destroy()
            b27.destroy()
            b28.destroy()
            b29.destroy()
            b30.destroy()
            stopwatch.destroy()
            #create the next button
            Next=Button(self.master, text="Next Level", height = 3, width = 27,  command=lambda: self.levelfive("C"))
            Next.grid(row=0,column=0)
            
        if (level == 5 and pairs == total):
            #set pairs counter back to 0
            pairs = 0
            #create new label
            label=Label(self.master, text="Click above to continue")
            label.grid(row=10, column=0, columnspan=10)
            #destroy buttons that are on the screen
            Finish.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            b5.destroy()
            b6.destroy()
            b7.destroy()
            b8.destroy()
            b9.destroy()
            b10.destroy()
            b11.destroy()
            b12.destroy()
            b13.destroy()
            b14.destroy()
            b15.destroy()
            b16.destroy()
            b17.destroy()
            b18.destroy()
            b19.destroy()
            b20.destroy()
            b21.destroy()
            b22.destroy()
            b23.destroy()
            b24.destroy()
            b25.destroy()
            b26.destroy()
            b27.destroy()
            b28.destroy()
            b29.destroy()
            b30.destroy()
            b31.destroy()
            b32.destroy()
            b33.destroy()
            b34.destroy()
            b35.destroy()
            b36.destroy()
            stopwatch.destroy()
            
            #create the next button
            returnhome=Button(self.master, text="Return to Home", height = 3, width = 27, command=self.home)
            returnhome.grid(row=0,column=0)
    
    
    #create level 1
    #height and width of button
    #https://www.tutorialspoint.com/python/tk_button.htm
    #using lambda to pass arguments through a command
    #https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
    #hot to multi thread
    #https://www.youtube.com/watch?v=jnrCpA1xJPQ
    def levelone (self, modes):
        global b1, b2, b3, b4, b5, b6, Finish, stopwatch, minute, second, level
        #deletes everything from the previous welcome screen on gui
        classic.destroy()
        timed.destroy()
        tries.destroy()
        leave.destroy()
        pick.destroy()
        welcome.destroy()
        level = 1
        
        #decide which function belongs to which mode
        if modes == "A":
            mode = self.click
            verify = self.check 
        elif modes == "B":
            mode = self.clickA
            verify = self.checkA
        elif modes == "C":
            mode = self.clickB
            verify = self.checkB
            minute = 0
            second = 3
            stopwatch = Label(self.master, text=" ")
            stopwatch.grid(row = 0, column = 20)
            threading.Thread(target=self.timer).start()
        
       
        #sets up buttons on gui
        b1=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b1,0,card, 1))
        b2=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b2,1,card, 1))
        b3=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b3,2,card, 1))
        b4=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b4,3,card, 1))
        b5=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b5,4,card, 1))
        b6=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b6,5,card, 1))
        Finish=Button(self.master, text="Finished?",height = 3, width = 27, command=lambda: verify(1, 3))
        #put button on grid
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)
        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)
        Finish.grid(row=6, column=0, columnspan=3, sticky = N+E+S+W)
    
    #creates level 2 - larger grid
    def leveltwo(self, modes):
        global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, Finish, attempts, level, stopwatch, minute, second
        level = 2
        #destroy previous buttons and set up for each mode
        if modes == "A":
            label.destroy()
            Next.destroy()
            mode = self.click
            verify = self.check 
        elif modes == "B":
            label.destroy()
            Next.destroy()
            attempts = 0
            mode = self.clickA
            verify = self.checkA
        elif modes == "C":
            mode = self.clickB
            verify = self.checkB
            label.destroy()
            Next.destroy()
            minute = 0
            second = 45
            stopwatch = Label(self.master, text=" ")
            stopwatch.grid(row = 0, column = 20)
            threading.Thread(target=self.timer).start()
            
        
        #create buttons
        b1=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b1,0,card2, 2))
        b2=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b2,1,card2, 2))
        b3=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b3,2,card2, 2))
        b4=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b4,3,card2, 2))
        b5=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b5,4,card2, 2))
        b6=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b6,5,card2, 2))
        b7=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b7,6,card2, 2))
        b8=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b8,7,card2, 2))
        b9=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b9,8,card2, 2))
        b10=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b10,9,card2, 2))
        b11=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b11,10,card2, 2))
        b12=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b12,11,card2, 2))
        Finish=Button(self.master, text="Finished?", width=27, height=3, command=lambda: verify(2, 6))
        #put button on grid
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)
        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)
        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)
        b10.grid(row=3, column=0)
        b11.grid(row=3, column=1)
        b12.grid(row=3, column=2)
        Finish.grid(row=6, column=0, columnspan=3, sticky = N+E+S+W)
    #creates level 3 - larger grid and symbols
    def levelthree(self, modes):
        global stopwatch, minute, second, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, Finish, attempts, level
        
        level = 3
        #destroy previous buttons and set up for each mode
        if modes == "A":
            label.destroy()
            Next.destroy()
            mode = self.click
            verify = self.check 
        elif modes == "B":
            label.destroy()
            Next.destroy()
            attempts = 0
            mode = self.clickA
            verify = self.checkA
        elif modes == "C":
            mode = self.clickB
            verify = self.checkB
            label.destroy()
            Next.destroy()
            minute = 1
            second = 15
            stopwatch = Label(self.master, text=" ")
            stopwatch.grid(row = 0, column = 20)
            threading.Thread(target=self.timer).start()
            
        b1=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b1,0,card3, 3))
        b2=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b2,1,card3, 3))
        b3=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b3,2,card3, 3))
        b4=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b4,3,card3, 3))
        b5=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b5,4,card3, 3))
        b6=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b6,5,card3, 3))
        b7=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b7,6,card3, 3))
        b8=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b8,7,card3, 3))
        b9=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b9,8,card3, 3))
        b10=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b10,9,card3, 3))
        b11=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b11,10,card3, 3))
        b12=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b12,11,card3, 3))
        b13=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b13,12,card3, 3))
        b14=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b14,13,card3, 3))
        b15=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b15,14,card3, 3))
        b16=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b16,15,card3, 3))
        b17=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b17,16,card3, 3))
        b18=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b18,17,card3, 3))
        b19=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b19,18,card3, 3))
        b20=Button(self.master, text=" ",width=9, height=3, command=lambda: mode(b20,19,card3, 3))
        Finish=Button(self.master, text="Finished?", width=27, height=3, command=lambda: verify(3, 10))
        
        #put on grid
        b1.grid(row=0, column=0, sticky = N+E+S+W)
        b2.grid(row=0, column=1, sticky = N+E+S+W)
        b3.grid(row=0, column=2, sticky = N+E+S+W)
        b4.grid(row=0, column=3, sticky = N+E+S+W)
        b5.grid(row=0, column=4, sticky = N+E+S+W)
        b6.grid(row=1, column=0, sticky = N+E+S+W)
        b7.grid(row=1, column=1, sticky = N+E+S+W)
        b8.grid(row=1, column=2, sticky = N+E+S+W)
        b9.grid(row=1, column=3, sticky = N+E+S+W)
        b10.grid(row=1, column=4, sticky = N+E+S+W)
        b11.grid(row=2, column=0, sticky = N+E+S+W)
        b12.grid(row=2, column=1, sticky = N+E+S+W)
        b13.grid(row=2, column=2, sticky = N+E+S+W)
        b14.grid(row=2, column=3, sticky = N+E+S+W)
        b15.grid(row=2, column=4, sticky = N+E+S+W)
        b16.grid(row=3, column=0, sticky = N+E+S+W)
        b17.grid(row=3, column=1, sticky = N+E+S+W)
        b18.grid(row=3, column=2, sticky = N+E+S+W)
        b19.grid(row=3, column=3, sticky = N+E+S+W)
        b20.grid(row=3, column=4, sticky = N+E+S+W)
        Finish.grid(row=6, column=0, columnspan=3, sticky = N+E+S+W)
        
    def levelfour(self, modes):
        global stopwatch, minute, second, level, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, Finish, attempts
        level = 4
        #destroy previous buttons and set up for each mode
        if modes == "A":
            label.destroy()
            Next.destroy()
            mode = self.click
            verify = self.check 
        elif modes == "B":
            label.destroy()
            Next.destroy()
            attempts = 0
            mode = self.clickA
            verify = self.checkA
        elif modes == "C":
            mode = self.clickB
            verify = self.checkB
            label.destroy()
            Next.destroy()
            minute = 2
            second = 15
            stopwatch = Label(self.master, text=" ")
            stopwatch.grid(row = 0, column = 20)
            threading.Thread(target=self.timer).start()
       
        b1=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b1,0,card4, 4))
        b2=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b2,1,card4, 4))
        b3=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b3,2,card4, 4))
        b4=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b4,3,card4, 4))
        b5=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b5,4,card4, 4))
        b6=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b6,5,card4, 4))
        b7=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b7,6,card4, 4))
        b8=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b8,7,card4, 4))
        b9=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b9,8,card4, 4))
        b10=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b10,9,card4, 4))
        b11=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b11,10,card4, 4))
        b12=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b12,11,card4, 4))
        b13=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b13,12,card4, 4))
        b14=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b14,13,card4, 4))
        b15=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b15,14,card4, 4))
        b16=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b16,15,card4, 4))
        b17=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b17,16,card4, 4))
        b18=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b18,17,card4, 4))
        b19=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b19,18,card4, 4))
        b20=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b20,19,card4, 4))
        b21=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b21,20,card4, 4))
        b22=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b22,21,card4, 4))
        b23=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b23,22,card4, 4))
        b24=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b24,23,card4, 4))
        b25=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b25,24,card4, 4))
        b26=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b26,25,card4, 4))
        b27=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b27,26,card4, 4))
        b28=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b28,27,card4, 4))
        b29=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b29,28,card4, 4))
        b30=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b30,29,card4, 4))
        Finish=Button(self.master, text="Finished?", height=3, width = 27, command=lambda: verify(4, 15))
        
        #put on grid
        b1.grid(row=0, column=0, sticky = N+E+S+W)
        b2.grid(row=0, column=1, sticky = N+E+S+W)
        b3.grid(row=0, column=2, sticky = N+E+S+W)
        b4.grid(row=0, column=3, sticky = N+E+S+W)
        b5.grid(row=0, column=4, sticky = N+E+S+W)
        b6.grid(row=0, column=5, sticky = N+E+S+W)
        b7.grid(row=1, column=0, sticky = N+E+S+W)
        b8.grid(row=1, column=1, sticky = N+E+S+W)
        b9.grid(row=1, column=2, sticky = N+E+S+W)
        b10.grid(row=1, column=3, sticky = N+E+S+W)
        b11.grid(row=1, column=4, sticky = N+E+S+W)
        b12.grid(row=1, column=5, sticky = N+E+S+W)
        b13.grid(row=2, column=0, sticky = N+E+S+W)
        b14.grid(row=2, column=1, sticky = N+E+S+W)
        b15.grid(row=2, column=2, sticky = N+E+S+W)
        b16.grid(row=2, column=3, sticky = N+E+S+W)
        b17.grid(row=2, column=4, sticky = N+E+S+W)
        b18.grid(row=2, column=5, sticky = N+E+S+W)
        b19.grid(row=3, column=0, sticky = N+E+S+W)
        b20.grid(row=3, column=1, sticky = N+E+S+W)
        b21.grid(row=3, column=2, sticky = N+E+S+W)
        b22.grid(row=3, column=3, sticky = N+E+S+W)
        b23.grid(row=3, column=4, sticky = N+E+S+W)
        b24.grid(row=3, column=5, sticky = N+E+S+W)
        b25.grid(row=4, column=0, sticky = N+E+S+W)
        b26.grid(row=4, column=1, sticky = N+E+S+W)
        b27.grid(row=4, column=2, sticky = N+E+S+W)
        b28.grid(row=4, column=3, sticky = N+E+S+W)
        b29.grid(row=4, column=4, sticky = N+E+S+W)
        b30.grid(row=4, column=5, sticky = N+E+S+W)
        Finish.grid(row=6, column=0, columnspan=3, sticky = N+E+S+W)
    def levelfive(self, modes):
        global stopwatch, minute, second, level, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, Finish, attempts
        level = 5
        
        #destroy previous buttons and set up for each mode
        if modes == "A":
            label.destroy()
            Next.destroy()
            mode = self.click
            verify = self.check 
        elif modes == "B":
            label.destroy()
            Next.destroy()
            attempts = 0
            mode = self.clickA
            verify = self.checkA
        elif modes == "C":
            mode = self.clickB
            verify = self.checkB
            label.destroy()
            Next.destroy()
            minute = 3
            second = 0
            stopwatch = Label(self.master, text=" ")
            stopwatch.grid(row = 0, column = 20)
            threading.Thread(target=self.timer).start()
       
        b1=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b1,0,card5, 5))
        b2=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b2,1,card5, 5))
        b3=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b3,2,card5, 5))
        b4=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b4,3,card5, 5))
        b5=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b5,4,card5, 5))
        b6=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b6,5,card5, 5))
        b7=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b7,6,card5, 5))
        b8=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b8,7,card5, 5))
        b9=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b9,8,card5, 5))
        b10=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b10,9,card5, 5))
        b11=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b11,10,card5, 5))
        b12=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b12,11,card5, 5))
        b13=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b13,12,card5, 5))
        b14=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b14,13,card5, 5))
        b15=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b15,14,card5, 5))
        b16=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b16,15,card5, 5))
        b17=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b17,16,card5, 5))
        b18=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b18,17,card5, 5))
        b19=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b19,18,card5, 5))
        b20=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b20,19,card5, 5))
        b21=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b21,20,card5, 5))
        b22=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b22,21,card5, 5))
        b23=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b23,22,card5, 5))
        b24=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b24,23,card5, 5))
        b25=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b25,24,card5, 5))
        b26=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b26,25,card5, 5))
        b27=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b27,26,card5, 5))
        b28=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b28,27,card5, 5))
        b29=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b29,28,card5, 5))
        b30=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b30,29,card5, 5))
        b31=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b31,30,card5, 5))
        b32=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b32,31,card5, 5))
        b33=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b33,32,card5, 5))
        b34=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b34,33,card5, 5))
        b35=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b35,34,card5, 5))
        b36=Button(self.master, text=" ",width=6, height=2, command=lambda: mode(b36,35,card5, 5))
        
        Finish=Button(self.master, text="Finished?", width=27, height=1, command=lambda: verify(5, 18))
        
        #put on grid
        b1.grid(row=0, column=0, sticky = N+E+S+W)
        b2.grid(row=0, column=1, sticky = N+E+S+W)
        b3.grid(row=0, column=2, sticky = N+E+S+W)
        b4.grid(row=0, column=3, sticky = N+E+S+W)
        b5.grid(row=0, column=4, sticky = N+E+S+W)
        b6.grid(row=0, column=5, sticky = N+E+S+W)
        b7.grid(row=1, column=0, sticky = N+E+S+W)
        b8.grid(row=1, column=1, sticky = N+E+S+W)
        b9.grid(row=1, column=2, sticky = N+E+S+W)
        b10.grid(row=1, column=3, sticky = N+E+S+W)
        b11.grid(row=1, column=4, sticky = N+E+S+W)
        b12.grid(row=1, column=5, sticky = N+E+S+W)
        b13.grid(row=2, column=0, sticky = N+E+S+W)
        b14.grid(row=2, column=1, sticky = N+E+S+W)
        b15.grid(row=2, column=2, sticky = N+E+S+W)
        b16.grid(row=2, column=3, sticky = N+E+S+W)
        b17.grid(row=2, column=4, sticky = N+E+S+W)
        b18.grid(row=2, column=5, sticky = N+E+S+W)
        b19.grid(row=3, column=0, sticky = N+E+S+W)
        b20.grid(row=3, column=1, sticky = N+E+S+W)
        b21.grid(row=3, column=2, sticky = N+E+S+W)
        b22.grid(row=3, column=3, sticky = N+E+S+W)
        b23.grid(row=3, column=4, sticky = N+E+S+W)
        b24.grid(row=3, column=5, sticky = N+E+S+W)
        b25.grid(row=4, column=0, sticky = N+E+S+W)
        b26.grid(row=4, column=1, sticky = N+E+S+W)
        b27.grid(row=4, column=2, sticky = N+E+S+W)
        b28.grid(row=4, column=3, sticky = N+E+S+W)
        b29.grid(row=4, column=4, sticky = N+E+S+W)
        b30.grid(row=4, column=5, sticky = N+E+S+W)
        b31.grid(row=5, column=0, sticky = N+E+S+W)
        b32.grid(row=5, column=1, sticky = N+E+S+W)
        b33.grid(row=5, column=2, sticky = N+E+S+W)
        b34.grid(row=5, column=3, sticky = N+E+S+W)
        b35.grid(row=5, column=4, sticky = N+E+S+W)
        b36.grid(row=5, column=5, sticky = N+E+S+W)
        Finish.grid(row=6, column=0, columnspan=3, sticky = N+E+S+W)

expired = False
window = Tk()
window.title("Flippity Floppity")
window.geometry("600x400")
t=Match(window)
t.start()
window.mainloop()
