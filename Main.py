import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sqlite3
import csv

    

import math


import MonthlyStatement

conn=sqlite3.connect("Midhun.db")
c=conn.cursor()

def createTableMonthlyStatement(): 
    conn = sqlite3.connect("Midhun.db")
    c=conn.cursor()
    c.execute("CREATE TABLE MonthlyStatement(S_No INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,DATE TEXT,BILL_NO TEXT,NAME_OF_PARTY TEXT,Tin_No INT,ITEMS TEXT,EXEMTED REAL,FIVE REAL,VAT_5 REAL,FOURTEEN_FIVE REAL,VAT_145 REAL,LESS_SCHEME REAL,ROUND_OFF REAL,TOTAL_PURCHASE REAL,TOTAL_VAT REAL,NET_TOTAL REAL)")
    conn.close()
def createTablePARTY():
    conn = sqlite3.connect("Midhun.db")
    c=conn.cursor()
    c.execute("CREATE TABLE PARTY(NAME TEXT,TIN INT)")
    conn.close()
    
try:
    
    createTablePARTY()# If table 'PARTY' already exists then do nothing . Else create table 'PARTY'
        
except:             
    pass

try:
    
    createTableMonthlyStatement()  # If table MonthlyStatement already exists then do nothing.Else create table MonthlyStatement
           
except:
    pass

sql="INSERT INTO PARTY(NAME,TIN) VALUES(?,?)"
def addData(party,tin):
    conn = sqlite3.connect("Midhun.db")
    c=conn.cursor()
    c.execute(sql,[(party),(tin)])
    conn.commit()
    conn.close()


def saveDataToDb(date,billNo,nameOfParty,tinNo,items,exemted,five,vat_5,fourteen_five,vat_145,lessScheme,roundOff,totalPurchase,totalVat,netTotal):
    try:
        conn=sqlite3.connect("Midhun.db")
        c=conn.cursor()
        c.execute("INSERT INTO MonthlyStatement(DATE,BILL_NO,NAME_OF_PARTY,Tin_No,ITEMS,EXEMTED,FIVE,VAT_5,FOURTEEN_FIVE,VAT_145,LESS_SCHEME,ROUND_OFF,TOTAL_PURCHASE,TOTAL_VAT,NET_TOTAL) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(date,billNo,nameOfParty,tinNo,items,exemted,five,vat_5,fourteen_five,vat_145,lessScheme,roundOff,totalPurchase,totalVat,netTotal))
        QMessageBox.information(None, "Data Saved to Midhun.db", "Data successfully saved to database!!")
        
        conn.commit()
    except Exception as e:
        QMessageBox.warning(None, "saveDataToDb Error", str(e))
        conn.close()
        
        
class Program(QMainWindow,MonthlyStatement.Ui_MainWindow):
    saveFlag=1
    def __init__(self,parent=None):
        super(Program,self).__init__(parent)
        self.setupUi(self)
        
        self.PushButtonNewSave.clicked.connect(self.NewSaveClicked)
        self.pushButtonSave.clicked.connect(self.savePressed)
        
        self.comboBoxParty.currentIndexChanged.connect(self.updateTin)
        
        self.doubleSpinBoxExemted.valueChanged.connect(self.updateTotal)
        self.doubleSpinBox5.valueChanged.connect(self.updateTotal)
        self.doubleSpinBox145.valueChanged.connect(self.updateTotal)
        self.doubleSpinBoxVat5.valueChanged.connect(self.updateTotal)
        self.doubleSpinBoxVat145.valueChanged.connect(self.updateTotal)
        self.doubleSpinBoxLessScheme.valueChanged.connect(self.updateTotal)
        self.doubleSpinBoxRoundOff.valueChanged.connect(self.roundOff)
        
        self.pushButtonEditDone.clicked.connect(self.editTable)
        self.actionExportToExcel.triggered.connect(self.exportToExcel)
        self.actionDeleteTableMonthlyStatement.triggered.connect(self.deleteMonthlyStatement)
        self.actionDeleteTableParty.triggered.connect(self.deleteTableParty)
        
        
        
        
        #self.initialisePartyEdit()
        self.initialiseComboBox()
        self.updateTableWidget()
    
    def roundOff(self):
        lessScheme=self.doubleSpinBoxLessScheme.value()
        
        roundOff=self.doubleSpinBoxRoundOff.value()       
               
        totalPurchase=self.doubleSpinBoxExemted.value()+self.doubleSpinBox5.value()+self.doubleSpinBox145.value()
        totalVat=self.doubleSpinBoxVat5.value()+self.doubleSpinBoxVat145.value()
        netTotal=totalPurchase+totalVat-lessScheme+roundOff
        
        self.doubleSpinBoxTotal.setValue(totalPurchase)
        self.doubleSpinBoxTotalVat.setValue(totalVat)
        self.doubleSpinBoxNetTotal.setValue(netTotal)
    def deleteMonthlyStatement(self):
        conn=sqlite3.connect("Midhun.db")
        conn.execute("DROP TABLE MonthlyStatement")
        conn.close()
        createTableMonthlyStatement()
        self.updateTableWidget()
        QMessageBox.information(self, "TABLE DELETED", "Table 'MonthlyStatement' successfully deleted!!")
    def deleteTableParty(self):
        conn=sqlite3.connect("Midhun.db")
        conn.execute("DROP TABLE PARTY")
        conn.close()
        createTablePARTY()
        self.updateTableWidget()
        self.comboBoxParty.clear()
        self.initialiseComboBox()
        #self.initialisePartyEdit()
        QMessageBox.information(self, "TABLE DELETED", "Table 'PARTY' successfully deleted!!")

    def NewSaveClicked(self):
        addData(str(self.lineEditNewParty.text()),str(self.lineEditNewTin.text()))
        
        
        
        self.comboBoxParty.clear()
        self.initialiseComboBox()
        #self.initialisePartyEdit()
        self.lineEditNewParty.clear()
        self.lineEditNewTin.clear()
        
        self.comboBoxParty.setFocus()
        
    def updateTotal(self):
        
        lessScheme=self.doubleSpinBoxLessScheme.value()
        
        #roundOff=self.doubleSpinBoxRoundOff.value()       
               
        totalPurchase=self.doubleSpinBoxExemted.value()+self.doubleSpinBox5.value()+self.doubleSpinBox145.value()
        totalVat=self.doubleSpinBoxVat5.value()+self.doubleSpinBoxVat145.value()
        #netTotal=totalPurchase+totalVat-lessScheme+roundOff
        
        netTotal=totalPurchase+totalVat-lessScheme
        
        whole = math.floor(netTotal)    
        frac = netTotal - whole
        if frac>0.5:
            temp=math.ceil(netTotal)
            roundOff=temp-netTotal
        elif frac<0.5:
            temp=math.floor(netTotal)
            roundOff=temp-netTotal
        elif frac==0.50:
            temp=math.ceil(netTotal)
            roundOff=0.50
        else:
            temp=netTotal
            roundOff=0.0
        #print roundOff
        
        netTotal=netTotal+roundOff
        
        self.doubleSpinBoxTotal.setValue(totalPurchase)
        self.doubleSpinBoxTotalVat.setValue(totalVat)
        self.doubleSpinBoxNetTotal.setValue(netTotal)
        self.doubleSpinBoxRoundOff.setValue(roundOff)
    
    def savePressed(self):
        
        try:
            qdate=str(self.dateEdit.date())
                                  
            date=self.extractDate(qdate)
                       
            billNo=str(self.lineEditBillNo.text())
            nameOfParty=str(self.comboBoxParty.currentText())
            tinNo=str(self.lineEditTin.text())
            items=str(self.lineEditItems.text())
            
            exemted=str(self.doubleSpinBoxExemted.value())
            
            five=str(self.doubleSpinBox5.value())
            
            vat_5=str(self.doubleSpinBoxVat5.value())
            
            fourteen_five=str(self.doubleSpinBox145.value())
            
            vat_145=str(self.doubleSpinBoxVat145.value())
            
            lessScheme=str(self.doubleSpinBoxLessScheme.value())
            
            roundOff=str(self.doubleSpinBoxRoundOff.value())
            
            totalPurchase=str(self.doubleSpinBoxTotal.value())
            
            totalVat=str(self.doubleSpinBoxTotalVat.value())
            
            netTotal=str(self.doubleSpinBoxNetTotal.value())
            
            
            
            saveDataToDb(date,str(billNo),str(nameOfParty),str(tinNo),str(items),str(exemted),str(five),str(vat_5),str(fourteen_five),str(vat_145),str(lessScheme),str(roundOff),str(totalPurchase),str(totalVat),str(netTotal))
            
            self.updateTableWidget()
            
            self.clearData()
            
            
            
            #QMessageBox.information(self, "SAVE PRESSED!!", "Save button pressed twice")
                
        except Exception as e:
            QMessageBox.information(self, "savePressed", str(e))
    def clearData(self):
        self.dateEdit.clear()
        self.lineEditBillNo.clear()
        self.lineEditItems.clear()
        
        self.doubleSpinBoxExemted.setValue(0.00)
        self.doubleSpinBox5.setValue(0.00)
        self.doubleSpinBox145.setValue(0.00)
        self.doubleSpinBoxVat5.setValue(0.00)
        self.doubleSpinBoxVat145.setValue(0.00)
        self.doubleSpinBoxLessScheme.setValue(0.00)
        self.doubleSpinBoxRoundOff.setValue(0.00)
        self.doubleSpinBoxTotal.setValue(0.00)
        self.doubleSpinBoxTotalVat.setValue(0.00)
        self.doubleSpinBoxNetTotal.setValue(0.00)
        
        self.dateEdit.setFocus()
        #self.dateEdit.selectAll()
        
    def extractDate(self,qdate):
        #print qdate
        year,month,day=qdate.split(",")
        year=year.split("(")
        year=year[1]
        #print "Year = ",year
        month=month.strip()
        #print "Month = ",month
        day=day.split(")")
        day=day[0]
        day=day.strip()
        #print "Day = ",day
        date=(day+"/"+month+"/"+year)
        #print date
        return date
        
        
    def updateTin(self):
        #print self.comboBoxParty.currentText()
        try:
            self.lineEditTin.setText(self.tinDict[str(self.comboBoxParty.currentText())])
        except Exception as e:
            #QMessageBox.warning(self, "updateTin Error", str(e))
            pass
        
    def initialiseComboBox(self):
        
        conn=sqlite3.connect("Midhun.db")
        partyList=conn.execute("SELECT NAME FROM PARTY")
        tinList=conn.execute("SELECT TIN FROM PARTY")
        
        party = '|'.join(['>>'.join(map(str, row)) for row in partyList])
        tin='|'.join(['>>'.join(map(str, row)) for row in tinList])
        
        party=party.split('|')
        tin=tin.split('|')
                        
        self.tinDict=dict(zip(party,tin))
              
        for each_item in self.tinDict.keys():
            each_item=str(each_item)
            
            self.comboBoxParty.addItem(each_item)
        conn.close()
    def updateTableWidget(self):
        conn=sqlite3.connect("Midhun.db")
        c=conn.cursor()
        c.execute("SELECT * FROM MonthlyStatement")
        allSQLRows= c.fetchall()
        
        self.tableWidget.setRowCount(len(allSQLRows)) ##set number of rows
        self.tableWidget.setColumnCount(16) ##this is fixed for myTableWidget, ensure that both of your tables, sql and qtablewidged have the same number of columns
                
        row = 0
               
                
        c.execute("SELECT * FROM MonthlyStatement")
        cur=c.fetchall()   
        for i,row in enumerate(cur):
            for j,val in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val))) 
        conn.close()   
    def exportToExcel(self):
        try:
            
            conn = sqlite3.connect("Midhun.db")
            cursor = conn.cursor()
            #cursor.execute("SELECT * FROM MonthlyStatement")
            cursor.execute("SELECT DATE,BILL_NO,NAME_OF_PARTY,Tin_No,ITEMS,EXEMTED,FIVE,VAT_5,FOURTEEN_FIVE,VAT_145,LESS_SCHEME,ROUND_OFF,TOTAL_PURCHASE,TOTAL_VAT,NET_TOTAL FROM MonthlyStatement")
            
            
            csv_writer = csv.writer(open("MonthlyStatement.csv", "wb"))
            csv_writer.writerow([i[0] for i in cursor.description]) # write headers
            csv_writer.writerows(cursor)
            del csv_writer # this will close the CSV file
            QMessageBox.information(self, "Data Exported!!", "Table exported as MonthlyStatement.csv!")
        except Exception as e:
            QMessageBox.warning(self, "exportToExcel Error!!", str(e))
    '''def initialisePartyEdit(self):
        self.comboBoxSelectParty.clear()
        conn=sqlite3.connect("Midhun.db")
        partyList=conn.execute("SELECT NAME FROM PARTY")
        
        
        party = '|'.join(['>>'.join(map(str, row)) for row in partyList])
        #tin='|'.join(['>>'.join(map(str, row)) for row in tinList])
        
        party=party.split('|')
        #tin=tin.split('|')
                        
        
              
        for each_item in party:
            each_item=str(each_item)
            
            self.comboBoxSelectParty.addItem(each_item)
        conn.close()'''
    def editTable(self):
        conn=sqlite3.connect("Midhun.db")
        c=conn.cursor()
        SNo=self.spinBoxSNo.value()
        option=self.comboBoxOptions.currentText()
        
        if option=='DELETE':
            c.execute("DELETE FROM MonthlyStatement WHERE S_No=?",[(SNo)])
            conn.commit()
        self.updateTableWidget()
        self.comboBoxParty.clear()
        self.initialiseComboBox()
        conn.close()
        '''try:
            conn=sqlite3.connect("Midhun.db")
            c=conn.cursor()
            nameOfParty=str(self.comboBoxSelectParty.currentText())
            if str(self.comboBoxSelectTable.currentText())=="Both":
                
                
                #if str(self.comboBoxOptions.currentText())=="DELETE ENTRY":
                c.execute("DELETE FROM MonthlyStatement WHERE NAME_OF_PARTY=?",[(nameOfParty)])
                c.execute("DELETE FROM PARTY WHERE NAME=?",[(nameOfParty)])
                conn.commit()
                #print nameOfParty
                QMessageBox.information(self, "editTable", "Row deleted from both tables")
            elif str(self.comboBoxSelectTable.currentText())=="MonthlyStatement":
                c.execute("DELETE FROM MonthlyStatement WHERE NAME_OF_PARTY=?",[(nameOfParty)])
                conn.commit()
                QMessageBox.information(self, "editTable", "Row deleted from table 'MonthlyStatement' !!")
            self.updateTableWidget()
            self.comboBoxParty.clear()
            self.initialiseComboBox()
            self.comboBoxSelectParty.clear()
            #self.initialisePartyEdit()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "editTable Error", str(e))'''
        
        
app=QApplication(sys.argv)
form=Program()
form.show()
app.exec_()