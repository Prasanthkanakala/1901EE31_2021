print("My name is Kanakala Durga Prasanth.My roll no is 1901EE31")
def isdigit(input_nums): #function to check whether the inputs are valid
    ans=True
    non_int=[]  #list to store the invalid entries
    for i in input_nums:
        if(isinstance(i,int)): #condition to check the validity of entry
            continue
        else:
            ans=False
            non_int.append(i)
    if(ans):
        return
    else:
        print('Please enter a valid input list')
        print('The invalid entries are {}'.format(non_int))

def get_memory_score(input_nums): #function to find the score of input
    vis=[0]*10 #list to store the count of entries
    score=0   #variable to store the result
    memory=[]  #list to store the memory elements 
    for i in input_nums:
        if(vis[i]==0):
            vis[i]+=1
            if(len(memory)<5):
                memory.append(i)
            else:
                memory.append(i)
                memory.pop(0)
        else:
            score+=1
            vis[i]+=1
            if(len(memory)<5):
                memory.append(i)
            else:
                memory.append(i)
                memory.pop(0)
    return score

input_nums = [3, 4, 5, 3, 2, 1]
isdigit(input_nums) #function to check whether the inputs are valid
print('Score : {}'.format(get_memory_score(input_nums)))