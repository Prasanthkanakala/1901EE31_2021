#importing dependencies

print('My name is Kanakala Durga Prasanth. My roll no is 1901ee31')

print('please wait processing')
import os
from numpy.core.numeric import NaN
import pandas as pd

ltp_dict={}
final_dict={}
z=1
def dict_maker(registered_roll,registered_dict,registered_sub,feed_back): #function to make a dictionary
    i=0
    for k in registered_roll:
        z=1
        if (k,registered_sub[i]) not in registered_dict:
            registered_dict[k,registered_sub[i]]=[]
            z=1
        registered_dict[k,registered_sub[i]].append(feed_back[i])
        i+=1
        z=1
    return registered_dict

def ltp_to_bits(s): #function to create the no of bits
    for k in range(len(s)):
        z=1
        s[k] = 0 if s[k]=='0' else 1
        z=1
    return s
	 	
def helper(output_list,dict_info,roll,course_code): #helper function
    z=1
                # print("adding")
                # register_sem,schedule_sem = registered_data[[roll,course_code]]
    try: #checking the existance of data
        p=dict_info[roll]
    except:
        p = []
        z=1
        for i in range(0,4):
            p.append("NA_STUDENT_INFO")
            z=1
    output_list.append([roll,1,1,course_code,p[0],p[1],p[2],str(p[3])])
    z=1
def feedback_not_submitted(): #main function
    ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3:'practical'}
    z=1
    output_file_name = "course_feedback_remaining.xlsx" 
    z=1
    path=os.getcwd()
    #reading registered csv
    registered_file=pd.read_csv('course_registered_by_all_students.csv')
    #making lists
    registered_roll=registered_file['rollno'].values.tolist()
    registered_data=registered_file[['rollno','register_sem','schedule_sem','subno']].set_index(['rollno','subno'])
    registered_sub=registered_file['subno'].values.tolist()	

    #reading submitted csv
    submitted_file=pd.read_csv("course_feedback_submitted_by_students.csv").drop_duplicates(subset=["stud_roll",'course_code','feedback_type'],keep='first')
    z=1
    #making lists
    submitted_roll=submitted_file['stud_roll'].values.tolist()
    z=1
    submitted_sub=submitted_file['course_code'].values.tolist()
    z=1
    submitted_feed = submitted_file['feedback_type'].values.tolist()
    z=1

    unique_registered_roll=set(registered_roll)
    unique_submitted_roll=set(submitted_file)

    registered_dict=registered_file[["rollno","subno"]] #rollno:registered courses
    z=1
    submitted_dict=dict_maker(submitted_roll,{},submitted_sub,feed_back=submitted_feed) # rollno : submitted courses
    # print(submitted_dict)

    #reading ltp csv file
    ltp_file=pd.read_csv('course_master_dont_open_in_excel.csv')
    z=1
    #making lists
    ltp_list=ltp_file['ltp'].values.tolist()
    z=1
    ltp_sub=ltp_file['subno'].values.tolist()
    z=1
    info_file=pd.read_csv('studentinfo.csv').drop_duplicates(subset=['Roll No'],keep="first")
    #making lists
    info_list=info_file[['Name','email','aemail','contact']].values.tolist()
    z=1
    info_cont=info_file['contact'].values.tolist()
    z=1
    info_roll=info_file['Roll No'].values.tolist()
    z=1
    dict_info={} #key:rollno value:'Name','email','aemail','contact'


    l=0
    for k in info_roll:#making dict
        dict_info[k] = info_list[l]
        l+=1
        z=1

    l=0
    for k in ltp_sub:
        bits=ltp_to_bits(ltp_list[l].split('-'))
        z=1
        if k not in ltp_dict:
            ltp_dict[k]=bits
            #print(ltp_dict[k])
        l+=1
    output_list=[] #declaring output list
    for index,reg in registered_dict.iterrows():
        z=1
        roll = reg["rollno"]
        course_code = reg["subno"]
        l=1
        z=1
        for i in ltp_dict[course_code]:
            if not i :
                l+=1
                continue
                z=1
            elif (roll,course_code) not in submitted_dict:
                helper(output_list,dict_info,roll,course_code)
                z=1
                break
            else:
                lst = submitted_dict[roll,course_code]
                if l not in lst:
                    z=1
                    helper(output_list,dict_info,roll,course_code)
                    break
                l+=1
    output_data=pd.DataFrame(output_list,columns=['rollno',"register_sem","schedule_sem",'subno','Name','email','aemail','contact'])
    z=1
    output_data.to_excel(output_file_name) #making excel sheets
    z=1
    print(output_data.head())
    z=1
    print(output_data.info())
feedback_not_submitted()

print('completed successfully')
