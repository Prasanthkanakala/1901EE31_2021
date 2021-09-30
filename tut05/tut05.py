print('My name is Kanakala Durga Prasanth. My roll no is 1901ee31')

import csv
import os
from openpyxl import Workbook
from openpyxl import load_workbook

def helper(data):   #function to add subject name, ltp to data
    with open('subjects_master.csv','r') as info:
        sinfo=csv.reader(info)
        for sub in sinfo:
            if(data[0]==sub[0]):
                data.insert(1,sub[1])
                data.insert(2,sub[2])
                
    return data

def generate_marksheet():
    DIRECTORY="output" 
    if not os.path.exists(DIRECTORY): #checking the existence of directory
        os.makedirs(DIRECTORY)
    header=['Subno','Subject name','L-T-P','Credit','Grade','subject type']
    with open('grades.csv','r') as info:
        sinfo=csv.reader(info)
        for data in sinfo:
            rollno=data[0]
            del data[0:2]
            if(rollno=="rollno"):
                continue
            data=helper(data)
            sheetname='{}.xlsx'.format(rollno)
            path='./output/'+sheetname

            if(os.path.isfile(path)): #adding data to sheet
                 wb=load_workbook(r'output\\{}.xlsx'.format(rollno))
                 xsheet=wb.active
                 xsheet.append(data)
                 wb.save(r'output\\{}.xlsx'.format(rollno))
                 
            else: #creating a new sheet and adding header to sheet 
                    wb=Workbook()
                    xsheet=wb.active
                    xsheet.append(header)
                    xsheet.append(data)
                    wb.save(f'output\\{rollno}.xlsx')
    return

generate_marksheet()

