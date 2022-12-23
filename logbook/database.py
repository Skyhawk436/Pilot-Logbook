#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:02:34 2022

@author: nate

This module provides a database connection.
"""
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def _createLogbookTable():
    """Create the contacts table in the database."""
    
    createTableQuery = QSqlQuery()
    createTableQuery.prepare(
        """
        CREATE TABLE IF NOT EXISTS logbook(
            Id INT PRIMARY KEY,
            Date TEXT,
            Aircraft_ident TEXT,
            Depart TEXT,
            Destination TEXT,
            Remarks TEXT,
            Num_instr_app INT,
            Num_ldg INT,
            Airplane_Sel FLOAT,
            Airplane_Mel FLOAT,
            cross_country FLOAT,
            Day FLOAT,
            Night FLOAT,
            Act_Instr FLOAT,
            Sim_Instr FLOAT,
            Ground_train FLOAT,
            Dual_recd FLOAT,
            PIC FLOAT,
            Total_flight_time FLOAT
           ) 
        """
        )
    
    return createTableQuery.exec_()


def createConnection(databaseName):
    """Create and open a database connection"""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)
    
    if not connection.open():
        QMessageBox.warning(
            None,
            "Logbook",
            f"Database Error: {connection.lastError().text()}",
            )
        return False
    
    _createLogbookTable()
    return True


    

    

