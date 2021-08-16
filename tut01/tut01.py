
print("My name is Kanakala Durga Prasanth. My Roll no is 1901EE31")


def meraki_helper(n):
    """This will detect meraki number"""
    if(n<10):
        print("Yes-{} is a meraki number".format(n))
        return 1
    a=str(n)
    i=0
    while(i<len(a)-1):
        if(abs(int(a[i])-int(a[i+1]))==1):
            i+=1
        else:
            print("No-{} is not a meraki number".format(n))
            return 0
    print("Yes-{} is a meraki number".format(n))
    return 1
        



input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
count1=0
count2=0
for i in input:
    if(meraki_helper(i)):
        count1+=1
    else:
        count2+=1
print("The input list contains {} meraki and {} non meraki numbers".format(count1,count2))
