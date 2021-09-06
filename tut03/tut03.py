print('My name is Kanakala Durga Prasanth. My roll no is 1901EE31')

import os
 

 
def output_by_subject():
    
    DIRECTORY = "output_by_subject"
 
    if not os.path.exists(DIRECTORY): #checking the existence of directory
        os.makedirs(DIRECTORY)
    
    with open('regtable_old.csv', 'r') as info: #reading the csv file
        for sinfo in info: 
            data = sinfo.split(',')
            del data[4:8]  #removing unwanted columns
            del data[2:3]
            if (data[2] =="subno"):continue
            try:
                with open(f"output_by_subject\\{data[2]}.csv"): #adding heading
                    with open((f"output_by_subject\\{data[2]}.csv"), 'a') as head:
                        data=",".join(data)
                        head.write(data)

            except IOError:
                with open((f"output_by_subject\\{data[2]}.csv"), 'w') as body:
                        body.write("rollno,register_sem,subno,sub_type\n")
                        data=",".join(data)
                        body.write(data)
    return
 
 
def output_individual_roll():
    
    DIRECTORY = "output_individual_roll"
 
   
 
    if not os.path.exists(DIRECTORY):  #checking the existence of directory
        os.makedirs(DIRECTORY)
    
    with open('regtable_old.csv', 'r') as info: #reading the csv file
        for sinfo in info:
            data = sinfo.split(',')
            del data[4:8]  #removing unwanted columns
            del data[2:3]
            if (data[0] =="rollno"):continue
            try: 
                with open((f"output_individual_roll\\{data[0]}.csv")): #adding heading
                    with open((f"output_individual_roll\\{data[0]}.csv"), 'a') as head:
                        data=",".join(data)
                        head.write(data)

            except IOError:
                with open((f"output_individual_roll\\{data[0]}.csv"), 'w') as body:
                        body.write("rollno,register_sem,subno,sub_type\n")
                        data=",".join(data)
                        body.write(data)
    return
 
 
output_by_subject()
output_individual_roll()
 
