import os
from tkinter import *
from PIL import Image, ImageTk

#get file names from a folder 
file_list = os.listdir(r"C:\Users\Sornspeed\Desktop\cos\cos2210\pics\pics")
#cleprint(file_list)

save_path = os.getcwd()
# print("Current Working Directory is " + save_path)

os.chdir(r"C:\Users\Sornspeed\Desktop\cos\cos2210\pics\pics")
# print("Current Working Directory is " + os.getcwd())

#for each file, rename filename
remove = "0123456789"
table = str.maketrans("","",remove)

for file_name in file_list:
    os.rename(file_name, file_name.translate(table))

images=['athens','austin','bangalore','barcelona']
root=Tk()
img_list=[]
for i,img in enumerate(images):
    img_list.append(ImageTk.PhotoImage(Image.open(f"{img}.jpg")))
    lbl=Label(image=img_list[i])
    lbl.grid(row=0,column=i)
    
root.mainloop()

os.chdir(save_path)