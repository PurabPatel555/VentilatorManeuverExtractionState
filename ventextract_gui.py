# -*- coding: utf-8 -*-
"""
VentExtract.ipynb
Purab Patel

"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import ion
ion()
import os
import sys
# Python program to create  
# a file explorer in Tkinter 
   
# import all components 
# from the tkinter library 
from Tkinter import *
   
# import filedialog module 
import tkFileDialog as filedialog 
   
# Function for opening the  
# file explorer window 
def browseFiles(): 
    OUT_PATH = filedialog.askdirectory(initialdir = "/", title = "Select Output Folder")
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select ASC File", 
                                          filetypes = (("ASC files", 
                                                        "*.ASC*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    # Change label contents 
    label_file_explorer.configure(text="File Opened: "+filename)
    
    RAW_DATA = filename #sys.argv[1]
    RAW_DATA_NAME = os.path.splitext(os.path.basename(RAW_DATA))[0]
    
    x_extract = np.genfromtxt(RAW_DATA, dtype=str, deletechars="b'")
    
    
    x = np.transpose(x_extract)
    x = x[:,1:]
    
    x = x.astype(float)
    id = 0 
    id_extract = []
    plotnum = 0
    fig = plt.figure(figsize=(100, 100))
    while True:
      xx = x[17,id:(id+5)]
      if (len(xx)==0):
        break
      if (xx[0] == 16 and xx[-1] == 16):
        plotnum = plotnum+1
        plt.subplot(16,1,plotnum)
        plt.plot(x[3,(id-1000):(id+1001)])
        id_extract.append(id)
        id = id+1002
      else:
        id = id+1
    
    plt.show()
    
    run = np.genfromtxt(RAW_DATA, dtype=str, deletechars="b'")
    run = np.transpose(run)
    
    for i, start in enumerate(id_extract):
      run_sample = np.hstack((np.transpose([run[:,0]]), run[:,(start-1000):(start+1001)]))
      run_sample = np.vstack((run_sample[0:6,:], run_sample[14,:]))
    
      np.savetxt((OUT_PATH + "/" + RAW_DATA_NAME+"-ZAM"+str(i+1)+'.ASC'), np.transpose(run_sample), fmt='%s', delimiter = '\t')
       
       
                                                                                                   
# Create the root window 
window = Tk() 
   
# Set window title 
window.title('File Explorer') 
   
# Set window size 
window.geometry("500x250") 
   
#Set window background color 
window.config(background = "white") 
   
# Create a File Explorer label 
label_file_explorer = Label(window,  
                            text = "ZAM Breath Extraction Program", 
                            width = 50, height = 4,  
                            fg = "blue") 
   
       
button_explore = Button(window,  
                        text = "Start", 
                        command = browseFiles)  
   
button_exit = Button(window,  
                     text = "Exit", 
                     command = exit)  
   
# Grid method is chosen for placing 
# the widgets at respective positions  
# in a table like structure by 
# specifying rows and columns 
label_file_explorer.grid(column = 1, row = 1) 
   
button_explore.grid(column = 1, row = 2) 
   
button_exit.grid(column = 1,row = 3) 
   
# Let the window wait for any events 
window.mainloop() 