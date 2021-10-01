print('My name is Kanakala Durga Prasanth. My roll no is 1901ee31')

#impoting modules
import os
from openpyxl import Workbook
from openpyxl import load_workbook
import csv




def result_calculate(Spi,ws_sheet,Credits):   #Function to calculate final result    
    ws_sheet.append(["Semester No"]+[x for x in range(1,9)])
    #counting credits
    ws_sheet.append(["Semester wise Credits taken"]+Credits)
    ws_sheet.append(["SPI per sem"]+Spi)
    prefix_credits = [sum(Credits[:i+1]) for i in range(len(Credits))]
    ws_sheet.append(["Total Credits taken"]+prefix_credits) #counting total credits
    CPI_num=[Spi[i]*Credits[i] for i in range(len(Credits))] 
    #CPI calculation formula
    ws_sheet.append(["Total CPI "]+[round(sum(CPI_num[:i+1])/prefix_credits[i],2) for i in range(len(Spi))])
    return

def is_sheet_exist(sheet_name,wb_sheet): #function to check the existance of sheet ina workbook
    for sheet in wb_sheet.sheetnames:
        if sheet == sheet_name: #condition for checking the existance
            return 1
    return 0

def Spi_calculator(wb_sheet,grade_to_score): #function to calculate SPI
    Spi,Credits= [],[]  #initializing lists
    for sheet in wb_sheet.sheetnames[1:]:
        ws_sheet = wb_sheet[sheet]  
        credits = [int(cell.value) for cell in ws_sheet["E"][1:]]
        spi = [grade_to_score[cell.value.strip().strip("*")] for cell in ws_sheet["G"][1:]]
        Credits.append(sum(credits))
        #spi calculation formula
        Spi.append(round(sum([spi[i]*credits[i] for i in range(len(spi))])/sum(credits),2))
    return Spi,Credits

def get_workbook(data): #creating a workbook
    wb_sheet=Workbook()
    ws_sheet=wb_sheet.active
    ws_sheet.title = "Overall"
    wb_sheet.save(f'output\\{data[0]}.xlsx')
    return

def generate_marksheet(): #main function
    Directory =  "output"
    #checking the existence of directory
    if not os.path.exists(Directory):
        os.mkdir(Directory)

    #opening and reading subjects file
    Subject_data = open("subjects_master.csv", "r")
    subject_csv_file=csv.reader(Subject_data)
    subject_list =  [list(record) for record in subject_csv_file][1:] #creating a list of subject data
    #creating a dictionary to store the data
    subject_dict = {}
    length = 0
    #adding data
    for data in subject_list:
        subno = data[0] 
        if subno not in subject_dict: #checking for existant data
            subject_dict[subno] = data[1:]
            length = max(length,len(data[1]))  
    #opening and reading grades file
    score_data = open("grades.csv", "r")
    score_csv = csv.reader(score_data)
    #creating a list for score data
    score_list = [list(record) for record in score_csv][1:] 
    #initializing the counter
    counter=1
    for data in score_list:
        Roll,Sem_no, = data[0],data[1]  #initializing the roll no
        file_path='./output/'+'{}.xlsx'.format(Roll)
        if not os.path.isfile(file_path): #checking the exitance of a file
            get_workbook(data) #creating a new workbook
        #loading the workbook
        wb_sheet=load_workbook(r'output\\{}.xlsx'.format(Roll))
        #checking the existance of sheet
        if not is_sheet_exist(f'Sem{Sem_no}',wb_sheet):
            wb_sheet.create_sheet(f'Sem{Sem_no}',int(Sem_no))
            ws_sheet = wb_sheet["Sem{}".format(int(Sem_no))]
            ws_sheet.column_dimensions["C"].width = length
        ws_sheet = wb_sheet[f"Sem{int(Sem_no)}"]
        print("{0}making {1}, please wait till completion".format(counter,Sem_no))
        if ws_sheet.max_row==1 : #adding header row
            ws_sheet.append(["Sl No.","Subject No.","Subject Name","L-T-P","Credit","Subject Type","Grade"])
        SubCode,Credit,Grade,Sub_Type = data[2:] #initializing variables
        #initializing variables
        subname,ltp,crd = subject_dict[f"{SubCode}"][0],subject_dict[f"{SubCode}"][1],subject_dict[f"{SubCode}"][2]
        #adding data to sheet       
        ws_sheet.append([ws_sheet.max_row,SubCode,subname,ltp,crd,Sub_Type,Grade])
        wb_sheet.save(r'output\\{}.xlsx'.format(Roll))          
        counter+=1;
    #created a map to convert the grade to score in numericals       
    grade_to_score = {'AA':10,'AB':9,'BB':8,'BC':7,'CC':6,'CD':5,'DD':4,'F':0,'I':0,
                'AA*':10,'AB*':9,'BB*':8,'BC*':7,'CC*':6,'CD*':5,'DD*':4,'F*':0,'I*':0}
    #opening and reading names-roll file
    names_data = open("names-roll.csv","r")
    names_csv = csv.reader(names_data)
    #created a list for names
    names_list = [list(record) for record in names_csv][1:] 
    #adding data
    for data in names_list:
        name,Roll = data[1],data[0] #initializing the variables
        wb_sheet = load_workbook(r'output\\{}.xlsx'.format(Roll))
        ws_sheet =wb_sheet.active
        #adding data to sheets
        ws_sheet.column_dimensions["A"].width = 30
        ws_sheet.append(["RollNo",Roll])
        ws_sheet.append(["Name of Student",name])
        ws_sheet.append(["Branch/Department",Roll[4:6]])
        #calculating SPI
        Spi,Credits= Spi_calculator(wb_sheet,grade_to_score)
        #calculating results
        result_calculate(Spi,ws_sheet,Credits)
        
        wb_sheet.save(r'output\\{}.xlsx'.format(Roll)) 
    return
generate_marksheet() #calling the function

print('My name is Kanakala Durga Prasanth. My roll no is 1901ee31')