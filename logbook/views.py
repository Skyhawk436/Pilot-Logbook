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
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
    )
from .model import LogbookModel  
from PyQt5.QtSql import QSqlQuery  

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
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deleteFlight)
        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.clicked.connect(self.clearLogbook)
        #display total flight hours
        self.totalHours = QLabel()
        self.totalHours.setText(f"Total Flight Hours: {getHours()}")
        
        
        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addWidget(self.totalHours)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)
        
    def openAddDialog(self):
        """Open the Add Flight dialog."""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.logbookModel.addFlight(dialog.data)
            self.table.resizeColumnsToContents()
            
    def deleteFlight(self):
        """Delete the selected entry from the database."""
        row = self.table.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected flight?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.logbookModel.deleteFlight(row)
            
    def clearLogbook(self):
        """Remove all entries from the database."""
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove all your flights?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.logbookModel.clearLogbook()
            
    
            
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
        layout.addRow("Destination:", self.destField)
        layout.addRow("Remarks:", self.remarksField)
        layout.addRow("Num_ins_app:", self.numinstField)
        layout.addRow("Num_landings:", self.numldgField)
        layout.addRow("Airplane_SEL:", self.selField)
        layout.addRow("Airplane_MEL:", self.melField)
        layout.addRow("Cross_country:", self.ccField)
        layout.addRow("Day:", self.dayField)
        layout.addRow("Night:", self.nightField)
        layout.addRow("Actual_instr:", self.actinstField)
        layout.addRow("Sim_instr:", self.siminstField)
        layout.addRow("Ground:", self.groundField)
        layout.addRow("Dual:", self.dualField)
        layout.addRow("PIC:", self.picField)
        layout.addRow("Total_flight_time:", self.totalField)
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
        
    def accept(self):
        """Accept the data provided through the dialog."""
        self.data = []
        for field in (self.dateField, self.identField, self.depField, self.destField,
                      self.remarksField, self.numinstField, self.numldgField, self.selField,
                      self.melField, self.ccField, self.dayField, self.nightField,
                      self.actinstField, self.siminstField, self.groundField, self.dualField,
                      self.picField, self.totalField):
            
            self.data.append(field.text())
            
        for field in (self.dateField, self.identField, self.totalField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide input for {field.objectName()}",
                )
                self.data = None  # Reset .data
                return

                

        if not self.data:
            return

        super().accept()
        

def getHours():
    """Gets sum of flight hours from database to display on main window"""
    quer = QSqlQuery()
    quer.exec(
            """
            SELECT Sum(Total_flight_time)
            FROM logbook
            """
            )
    quer.first()
    return quer.value(0)
    