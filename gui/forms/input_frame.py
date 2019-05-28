###
#
# CIS Top of Atmosphere Radiance Calibration
#
# Program Description : GUI for the Landsat Buoy Calibration program
# Created By          : Benjamin Kleynhans
# Creation Date       : May 28, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : May 28, 2019
# Filename            : input_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
import tarca_gui
from gui.forms import notebook

class Input_Frame(tarca_gui.Tarca_Gui):
    
    def create_input_frame(self, master):
        
        self.input_frame = ttk.Frame(master)
        master.input_frame = self.input_frame
        
        self.input_frame.pack(anchor = 'w')
        
        notebook.Notebook(master)
        
    
    def __init__(self, master):
        
        self.create_input_frame(master)