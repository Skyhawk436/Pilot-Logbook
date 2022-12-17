#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:58:36 2022

@author: nate

This module provides the Logbook application
"""
import sys
from PyQt5.QtWidgets import QApplication
from .database import createConnection
from .views import Window

def main():
    """Logbook main funtion"""
    app = QApplication(sys.argv)
    #connect to the database before creating any window
    if not createConnection("logbook.sqlite"):
        sys.exit(1)
    #create main window
    win = Window()
    win.show()
    #run the event loop
    sys.exit(app.exec_())
    
