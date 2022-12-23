#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:51:00 2022

@author: nate

This module provides views to manage the logbook table.
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
    )
from .model import LogbookModel    

class Window(QMainWindow):
    """Main Window"""
    
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle("Flight Logbook")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.logbookModel = LogbookModel()
        self.setupUI()
        
        
    def setupUI(self):
        """Setup the main window's GUI."""
        # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.logbookModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # Create buttons
        self.addButton = QPushButton("Add...")
        self.deleteButton = QPushButton("Delete")
        self.clearAllButton = QPushButton("Clear All")
        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

class AddDialog(QDialog):
    """Add Flight dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Flight")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None
        self.setupUI()

    def setupUI(self):
        """Setup the Add Flight dialog's GUI."""
        # Create line edits for data fields
        self.dateField = QLineEdit()
        self.dateField.setObjectName("Date")
        self.identField = QLineEdit()
        self.identField.setObjectName("Aircraft_ident")
        self.depField = QLineEdit()
        self.depField.setObjectName("Depart")
        self.destField = QLineEdit()
        self.destField.setObjectName("Destination")
        self.remarksField = QLineEdit()
        self.remarksField.setObjectName("Remarks")
        self.numinstField = QLineEdit()
        self.numinstField.setObjectName("Num_inst")
        self.numldgField = QLineEdit()
        self.numldgField.setObjectName("Num_ldg")
        self.selField = QLineEdit()
        self.selField.setObjectName("Airplane_Sel")
        self.melField = QLineEdit()
        self.melField.setObjectName("Airplane_Mel")
        self.ccField = QLineEdit()
        self.ccField.setObjectName("cross_country")
        self.dayField = QLineEdit()
        self.dayField.setObjectName("Day")
        self.nightField = QLineEdit()
        self.nightField.setObjectName("Night")
        self.actinstField = QLineEdit()
        self.actinstField.setObjectName("Act_instr")
        self.siminstField = QLineEdit()
        self.siminstField.setObjectName("Sim_instr")
        self.groundField = QLineEdit()
        self.groundField.setObjectName("Ground_train")
        self.dualField = QLineEdit()
        self.dualField.setObjectName("Dual_recd")
        self.picField = QLineEdit()
        self.picField.setObjectName("PIC")
        self.totalField = QLineEdit()
        self.totalField.setObjectName("Total_flight_time")
        # Lay out the data fields
        layout = QFormLayout()
        layout.addRow("Date:", self.dateField)
        layout.addRow("Aircraft_ident:", self.identField)
        layout.addRow("Depart:", self.depField)
        layout.addRow("Depart:", self.depField)
        layout.addRow("Depart:", self.depField)
        layout.addRow("Depart:", self.depField)
        layout.addRow("Depart:", self.depField)
        layout.addRow("Depart:", self.depField)
        self.layout.addLayout(layout)
        # Add standard buttons to the dialog and connect them
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)
