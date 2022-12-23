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
            "Id",
            "Date",
            "Aircraft_ident",
            "Depart",
            "Destination",
            "Remarks",
            "Num_inst",
            "Num_ldg",
            "Airplane_Sel",
            "Airplane_Mel",
            "cross_country",
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