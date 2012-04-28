#
#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 
#_author_:Aregee:rahul.nbg@gmail.com
# A Script for ASE(sl4a) to maniupluate your media file extensions to hide them from the gallery :)
# Feel free to make changes and improve functionality :)
#
import android,sys,glob,os
droid=android.Android()

#Choose which list type you want.
def getlist():
  droid.dialogCreateAlert("What Do Want To Do !")
  droid.dialogSetItems(["Hide_images","Restore_images","Hide_videos","Restore_Videos"])
  droid.dialogSetPositiveButtonText("Okay")
  droid.dialogSetNegativeButtonText("Bitch Please!")

  droid.dialogShow()
  result=droid.dialogGetResponse().result
  if result.has_key("item"):
    return result["item"]
  else:
    return -1
def hide():
        for fi in glob.glob("*.png"):

                os.rename(fi, fi[:-3] + "php")

        for fi in glob.glob("*.jpg"):

                os.rename(fi, fi[:-3] + "exe")

        for fi in glob.glob("*.jpeg"):

                os.rename(fi, fi[:-4] + "asp")
        for fi in glob.glob("*.gif"):

                os.rename(fi, fi[:-3] + "txt")


def restore():
        for fi in glob.glob("*.php"):

                os.rename(fi, fi[:-3] + "png")

        for fi in glob.glob("*.exe"):

                os.rename(fi, fi[:-3] + "jpg")

        for fi in glob.glob("*.asp"):

                os.rename(fi, fi[:-3] + "jpeg")
        for fi in glob.glob("*.txt"):

                os.rename(fi, fi[:-3] + "gif")

def Vhide():

        for fi in glob.glob("*.flv"):

                os.rename(fi, fi[:-3] + "jar")

        for fi in glob.glob("*.wmv"):

                os.rename(fi, fi[:-3] + "pl")

        for fi in glob.glob("*.avi"):

                os.rename(fi, fi[:-3] + "pyc")
        for fi in glob.glob("*.mp4"):

                os.rename(fi, fi[:-3] + "js")

def Vrestore():
        for fi in glob.glob("*.jar"):

                os.rename(fi, fi[:-3] + "flv")

        for fi in glob.glob("*.pl"):

                os.rename(fi, fi[:-2] + "wmv")

        for fi in glob.glob("*.pyc"):

                os.rename(fi, fi[:-3] + "avi")
        for fi in glob.glob("*.js"):

                os.rename(fi, fi[:-2] + "mp4")



#Choose List
listtype=getlist()
if listtype<0:
  print "No item chosen"
  sys.exit()

if listtype==0:
  #droid.dialogSetItems(options)
  hide()
elif listtype==1:
  
  restore() 
elif listtype==2:
  
  Vhide()
elif listtype==3:
  Vrestore()
droid.dialogSetPositiveButtonText("OK")
droid.dialogSetNegativeButtonText("Cancel")
droid.dialogShow()
result=droid.dialogGetResponse().result
# droid.dialogDismiss() # In most modes this is not needed.
if result==None:
  print "Time out"
elif result.has_key("item"):
  item=result["item"];
  print "Chosen item=",item,"=",options[item]
else:
  print "Result=",result
  print "Selected=",droid.dialogGetSelectedItems().result
print "Done"

