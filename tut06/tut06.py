print("My name is Kanakala Durga Prasanth. My roll no is 1901ee31")


#importing dependencies
import os
import re

def rename_Breaking_bad(webseries_name,season_padding,episode_padding):
    #creating path
    path=os.path.join(os.getcwd(),"srt",webseries_name)
    title='Breaking Bad'
    sea_pad=season_padding
    epi_pad=episode_padding
    #listing out the files available in a directory
    for name in os.listdir(path):
        src=os.path.join(path,name)
        #splitting out the name based on delimiters
        name=name.split(".")
        file_type=name[-1]
        name=name[0].split(" ")
        name=name[2]
        #searching for the season pattern
        matches = re.findall(r"s[0-9][0-9]", name)
        if len(matches) == 1:
            season = int(matches[0][1:])
            new_season = str(season)
            #adding pad to string
            new_season = new_season.zfill(int(sea_pad))
        #searching for the episode pattern
        matches = re.findall(r"e[0-9][0-9]", name)
        if len(matches) == 1:
            episode = matches[0][1:]
            episode = int(episode)
            new_ep = str(episode)
            #adding pad to string
            new_ep = new_ep.zfill(int(epi_pad))
            #Adding final name
            f_name=title+" - "+"Season "+ str(new_season)+" Episode "+str(new_ep)+"."+file_type
            des=os.path.join(path,f_name)
            if not os.path.isfile(des):
                os.rename(src,des)
            else :
                os.remove(src)
    print("Breaking Bad series is renamed")
    return
#function to rename GOT
def rename_Gameofthrones(webseries_name,season_padding,episode_padding):
    #Creating path
    path=os.path.join(os.getcwd(),"srt",webseries_name)
    title='Game of Thrones'
    sea_pad=season_padding
    epi_pad=episode_padding
    #listing out available files in given directory
    for name in os.listdir(path):
            src=os.path.join(path,name)
            #splitting title
            name=name.split(".")
            file_type=name[-1]
            name=name[0].split("-")
            ep_name='-'.join(name[2:])
            name=name[1]
            sea_num,ep_num=[str(int(x)) for x in name.split("x")]
            #Adding final title
            f_name=title+" - "+"Season "+ sea_num.zfill(sea_pad)+" Episode "+ep_num.zfill(epi_pad)+" - "+ep_name+"."+file_type
            des=os.path.join(path,f_name)
            if not os.path.isfile(des):
                os.rename(src,des)
            else :
                os.remove(src)
    print("GOT series is renamed")
    return

#Function to rename Lucifer series
def rename_Lucifer(webseries_name,season_padding,episode_padding):
    #creating path
    path=os.path.join(os.getcwd(),"srt",webseries_name)
    title='Lucifer'
    sea_pad=season_padding
    epi_pad=episode_padding
    #listing out the files in given directories
    for name in os.listdir(path):
            src=os.path.join(path,name)
            #Splitting names
            name=name.split(".")
            file_type=name[-1]
            name=name[0].split("-")
            ep_name='-'.join(name[2:])
            name=name[1]
            sea_num,ep_num=[str(int(x)) for x in name.split("x")]
            #adding final name to file
            f_name=title+" - "+"Season "+ sea_num.zfill(sea_pad)+" Episode "+ep_num.zfill(epi_pad)+" - "+ep_name+"."+file_type
            des=os.path.join(path,f_name)
            if not os.path.isfile(des):
                os.rename(src,des)
            else :
                os.remove(src)
    print("Lucifer series is renamed")
    return

    
def regex_renamer(): #Main Function

    # Taking input from the user

    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")

    webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))

    if webseries_num==1 :  #Sending call for function to rename
        #checking condition for existance of an error
        try:   
            rename_Breaking_bad('Breaking Bad',season_padding,episode_padding)
        except:
            print("\n  Webseries is already renamed")
            
    elif webseries_num==2: #sending call for function to rename
        try:
            rename_Gameofthrones('Game of Thrones',season_padding,episode_padding)
        except:
            print("\n Webseries is already renamed")
    elif webseries_num==3:  #sending call for function rename
        try:
            rename_Lucifer('Lucifer',season_padding,episode_padding)
        except:
            print("\n webseries is already renamed")  


regex_renamer()  #calling main function