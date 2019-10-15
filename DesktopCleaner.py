import os
import shutil
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("_%b_%d_%Y_%H_%M_%S")
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

IMG = ['jpg','jpeg','png','tiff','bmp']
FILES = ['pdf','txt','doc','docx','xls','xlsx','ppt','pptx','psd','apk','eps','py']
ARCHIVES= ['rar','iso','zip']
VIDEOS=['mp4','mkv','3gp','wmv','webm','flv','avi']
MUSICS=['mp3','m4a','wav']

checkExist=True
try:

    MainFolder = os.path.join(desktop, r'Old_Desktop')
    MainFolderNOT= os.path.join(desktop, r'Old_Desktop'+dt_string)
    if not os.path.exists(MainFolder):
        os.makedirs(MainFolder)
        checkExist=True
        Exe_Folder=MainFolder+'/Exe_Files'
        Img_Folder=MainFolder+'/Images'
        File_Folder=MainFolder+'/Files'
        Archive_Folder=MainFolder+'/Archives'
        Other_Folder=MainFolder+'/Other'
        Video_Folder=MainFolder+'/Videos'
        Music_Folder=MainFolder+'/Music'

    else:
        os.makedirs(MainFolderNOT)
        checkExist=False
        Exe_Folder=MainFolderNOT+'/Exe_Files'
        Img_Folder=MainFolderNOT+'/Images'
        File_Folder=MainFolderNOT+'/Files'
        Other_Folder=MainFolderNOT+'/Other'
        Archive_Folder=MainFolderNOT+'/Archives'
        Video_Folder=MainFolderNOT+'/Videos'
        Music_Folder=MainFolderNOT+'/Music'

    os.makedirs(Exe_Folder)
    os.makedirs(Img_Folder)
    os.makedirs(File_Folder)
    os.makedirs(Other_Folder)
    os.makedirs(Archive_Folder)
    os.makedirs(Video_Folder)
    os.makedirs(Music_Folder)



    os.chdir(desktop)
    for file in os.listdir():
        try:
            if file.endswith('.exe'):
                shutil.move(file,Exe_Folder)
            for f in IMG:
                if file.endswith(f):
                    shutil.move(file,Img_Folder)
            for f in FILES:
                if file.endswith(f):
                    shutil.move(file,File_Folder)
            for f in ARCHIVES:
                if file.endswith(f):
                    shutil.move(file,Archive_Folder)
            for f in VIDEOS:
                if file.endswith(f):
                    shutil.move(file,Video_Folder)
            for f in MUSICS:
                if file.endswith(f):
                    shutil.move(file,Music_Folder)
            else:
                shutil.move(file,Other_Folder)
        except:
            continue
    if checkExist == True:      
        outFileName=MainFolder+'/ReadMe.txt'
        outFile=open(outFileName, "w")
        outFile.write("""Your Desktop Was Cleaned At {} Using My Software - Thank You For Your Trust In Me - Author [Mohamed Wael Bishr]""".format(dt_string))
        outFile.close()
    else:
        outFileName=MainFolderNOT+'/ReadMe.txt'
        outFile=open(outFileName, "w")
        outFile.write("""Your Desktop Was Cleaned At {} Using My Software - Thank You For Your Trust In Me - Author [Mohamed Wael Bishr]""".format(dt_string))
        outFile.close()
except:
    pass