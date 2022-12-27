#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 14:17:01 2022

@author: nate

This module provides a model to manage the logbook table.
"""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class LogbookModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        """Create and set up the model."""
        tableModel = QSqlTableModel()
        tableModel.setTable("logbook")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = (
            "ID",
            "Date",
            "Aircraft_ident",
            "Depart",
            "Destination",
            "Remarks",
            "Num_inst",
            "Num_ldg",
            "Airplane_Sel",
            "Airplane_Mel",
            "Cross_country",
            "Day",
            "Night",
            "Act_Instr",
            "Sim_Instr",
            "Ground_train",
            "Dual_recd",
            "PIC",
            "Total_flight_time")
        
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel
    
    
    def addFlight(self, data):
        """Add a flight to the database."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1), field)
        self.model.submitAll()
        self.model.select()
        
    def deleteFlight(self, row):
        """Remove an entry from the database."""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()
        
    def clearLogbook(self):
        """Remove all entries in the database."""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()