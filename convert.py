import glob
import os
search = input("Enter the file extension need to be converted :")
convert = input("Enter the file extension to which it need to be converted :")
x = glob.glob("*."+search)
try:
  os.system('mkdir Output')
except:
  print("The directory has been already created")
for i in range(len(x)):
    print(x[i])
    try:
        os.system('ffmpeg -i '+str(x[i])+' -codec copy Output/'+str(i)+'.'+convert)
    except:
        print("Some error occurred while converting")

