#importing dependencies

print('My name is Kanakala Durga Prasanth. My roll no is 1901ee31')

import os
from numpy.core.numeric import NaN
import pandas as pd

ltp_dict={}
final_dict={}

def dict_maker(registered_roll,registered_dict,registered_sub):
	i=0
	for k in registered_roll:
		if k in registered_dict:
			registered_dict[k].append(registered_sub[i])
		else:
			registered_dict[k]=[]
			registered_dict[k].append(registered_sub[i])
		
		i+=1
	return registered_dict

def helper(temp,submitted_dict,s,roll):
			for i in temp:
				x=ltp_dict[i]
				#print(x[0][1])
	
				if x[0][1]!=0:
					if submitted_dict.count(i)!=x[0][1]:
						if temp.count(i)!=x[0][1]:
							diff=x[0][1]-temp.count(i)
							while diff>0:
								s.append(i)
								diff-=1
					s.append(i)
				else:
					continue
			
			for j in submitted_dict:
				x=ltp_dict[j]
				#if submitted_dict.count(j)!=x[1]:
				#	s.append(j)
				if j in s:
					s.remove(j)
			if len(s)!=0:		
				if roll in final_dict:
					final_dict[roll].append(s)
				else:
					final_dict[roll]=[]
					final_dict[roll].append(s)
				return roll

def ltp_to_bits(s): #function to create the no of bits
		count=0
		zeroes=0
		#bits=0
		for k in range(len(s)):
			if((s[k])=='0'):
				zeroes+=1
			
		count=3-zeroes
		return count

def check(submitted_dict,registered_dict,roll): #function to check the non submitted courses
	if roll in registered_dict:
		temp=registered_dict[roll].copy()
		n=len(temp)
		s=[]
		m=len(submitted_dict)
		if(n!=m):
			#temp.sort()
			#submitted_dict.sort()
			return helper(temp,submitted_dict,s,roll)
	

			
def feedback_not_submitted(): #main function to create analysis of the feedback

	
	ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3:'practical'}
	output_file_name = "course_feedback_remaining.xlsx" 
	path=os.getcwd()
	registered_file=pd.read_csv('course_registered_by_all_students.csv')
	registered_roll=registered_file['rollno'].values.tolist()
	registered_data=registered_file[['register_sem','schedule_sem','subno']].values.tolist()
	registered_sub=registered_file['subno'].values.tolist()
	#print(registered_sub)
	
	unique_registered_roll=set(registered_roll)
	registered_dict={}
	
	registered_dict=dict_maker(registered_roll,registered_dict,registered_sub)
	
	i=0
	registered_data_dict={}
	for k in registered_sub:
		#if k in registered_data_dict:
		#	registered_data_dict[k].append(registered_data[i])
		#else:
		registered_data_dict[k]=[]
		registered_data_dict[k]=registered_data[i]
		i+=1

	#print(registered_data_dict['EE202'])
	#exit()
	#print(registered_dict['1901EE31'])
	
	#print(registered_sub)
	#print('***********************************************************')
	#print(registered_roll)
	
	submitted_file=pd.read_csv("course_feedback_submitted_by_students.csv")
	submitted_sub=submitted_file['course_code'].values.tolist()
	submitted_roll=submitted_file['stud_roll'].values.tolist()
	unique_submitted_roll=set(submitted_file)
	submitted_dict={}

	

	submitted_dict=dict_maker(submitted_roll,submitted_dict,submitted_sub)
	#print(submitted_dict['1901EE31'])
	#print(submitted_file.head())
	info_file=pd.read_csv('studentinfo.csv')
	ltp_file=pd.read_csv('course_master_dont_open_in_excel.csv')
	#print(ltp_file.head())
	ltp_list=ltp_file['ltp'].values.tolist()
	ltp_sub=ltp_file['subno'].values.tolist()
	#print(ltp_sub)
	
	info_list=info_file[['Name','email','aemail','contact']].values.tolist()
	info_cont=info_file['contact'].values.tolist()
	#info_cont=int(info_cont)
	#f=int(info_cont[2])
	#print(type(f))
	#print(f)
	
	info_roll=info_file['Roll No'].values.tolist()
	
	dict_info={}

	l=0
	for k in info_roll:
		if k in dict_info:
			#if info_cont!=NaN:
				dict_info[k].append(info_list[l])
			#else:
			#	dict_info[k].append(info_list[l]+0)
		else:
			dict_info[k]=[]
			#if info_cont!=NaN:
			#	dict_info[k].append(info_list[l]+int(info_cont[l]))
			#else:
			#	dict_info[k].append(info_list[l]+0)
			dict_info[k].append(info_list[l])
		
		l+=1
	#print(dict_info['1901EE31'])

	#ltp_dict={}

	l=0
	for k in ltp_sub:
		bits=ltp_to_bits(ltp_list[l])
		if k in ltp_dict:
			
			ltp_dict[k].append([ltp_list[l],bits])
		else:
			ltp_dict[k]=[]
			ltp_dict[k].append([ltp_list[l],bits])
		
		l+=1
	
	#print(ltp_dict['CB102'])

	#print(info_file)
	s=[]
	for i in unique_registered_roll:
		if i in submitted_dict:
			temp=check(submitted_dict[i],registered_dict,i)
			s.append(temp)
		else:
			s.append(i)

	#print(type(registered_data_dict['NSO']))
	#output_data_file=pd.DataFrame()
	#output_data_file.columns=['rollno','register_sem','schedule_sem','subno','Name','email','aemail','contact']
	output_list=[]
	for i in final_dict:
		for j in final_dict[i]:
			for k in j:
				x=[]
				x.append(i)
				#print(j)
			
			
				x.extend(registered_data_dict[k])
				p=dict_info[i]
				#h=p[0]
				#v=p[0][0]
				#print(v)
				#print(type(v))
				#exit()
				#for l in p:
				x.append(p[0][0])
				x.append(p[0][1])
				x.append(p[0][2])
				x.append(str(p[0][3]))
				#print(x)
				
				output_list.append(x)
				#output_data_file.append(x)
	#output_data_file.columns=['rollno','register_sem','schedule_sem','subno','Name','email','aemail','contact']
	
	#final dataframe
	output_data=pd.DataFrame(output_list,columns=['rollno','register_sem','schedule_sem','subno','Name','email','aemail','contact'])
	#converting the dataframe to excel sheet
	output_data.to_excel(output_file_name)
	print(output_data.info())
	print(output_data.head())


	

		
	
#	print(s)



#for key in final:
#	print(final[key])
	
	

 



feedback_not_submitted() #calling main function
#for key in final:
#	print(key)
#	print(final[key])

#print(final['1901EE31'])

print('My name is Kanakala Durga Prasanth. My roll no is 1901ee31')
