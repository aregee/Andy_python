#
#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 
#_author_:Aregee:rahul.nbg@gmail.com

""" A sl4a Python Script,Which Creates alert with mesage and executes the functions acording the your Choice ,
Like positive answer displays a personal alert message and pops up a pic from the gallery followed by an MP3..
Feel free to make changes and improve functionality :) """



import android
import time

droid = android.Android()

droid.dialogCreateAlert("Are You My Sweet<3 ?")
droid.dialogSetPositiveButtonText("Yes !")
droid.dialogSetNegativeButtonText("Not in 100 years")
droid.dialogShow()
while True: # Wait for events for up to 10 seconds.
  response=droid.eventWait(10000).result
  if response==None: # No events to process. exit.
    break
  if response["name"]=="dialog": # When you get a dialog event, exit loop
    break
  print response # Probably a location event.


droid.dialogDismiss()
def media_play():#Play  a Song For your GirlFriend
  droid.mediaPlayClose()
  print droid.mediaPlay("file:///sdcard/My_app_files/Breathless.mp3")
  start=time.time()
  while (droid.mediaIsPlaying().result) and time.time()-start<5000:
    print droid.mediaPlayInfo().result
    time.sleep(1)

  droid.mediaPlayStart("Breathless")
  print "Done"
def spinner():#Spinner PRogress
      title = 'Shit! :('
      message = 'My heart is Shattered, Trying to collect last Fragments of memories...'
      droid.dialogCreateSpinnerProgress(title, message)
      droid.dialogShow()
      time.sleep(2)
      droid.dialogDismiss()
      return True
      
def spinner_p():#Spinner PRogress
      title = 'Memories'
      message = 'Best Thing Ever Happned To Me...'
      droid.dialogCreateSpinnerProgress(title, message)
      droid.dialogShow()
      time.sleep(2)
      droid.dialogDismiss()
      return True
def what_i_feel():#Create an Alert and Provide Option To Select
      
      droid.dialogCreateAlert("I love you!")
      droid.dialogSetItems(["This is All I want to Say "])#Plays a Selected mp3 when tapped
      droid.dialogShow()
      #vibro = viber()
      result = droid.dialogGetResponse().result
      if result.has_key("item"):
        return result["item"]
      else:
        return -1 

if response==None:
  print "Timed out."
else:
  rdialog=response["data"] # dialog response is stored in data.
  if  rdialog.has_key("which"):
    result=rdialog["which"]
    if result=="positive":
      droid.notify('Honey',"Now even my phone says what my heart feels..")#test Notification 
      
      show =  what_i_feel()#Calls the Function to Display your Personal Message
      
      if show ==0:
        test=spinner_p()#calls the spinner progress
        url ="file:///sdcard/My_app_files/life.jpg"#Open An Image from the given location 
        mime = "image/jpeg"

        droid.startActivity('android.intent.action.VIEW',url,mime)
             	
        
      play = media_play()    
      vib = viber()
        
    elif result=="negative":
      test=spinner()    
      url ="file:///sdcard/My_app_files/me.jpg"
      mime = "image/jpeg"

      droid.startActivity('android.intent.action.VIEW',url,mime)  
  
  else:
    print "Unknown response=",response

def viber():
  droid.vibrate(200)
  droid.vibrate(500)
  droid.vibrate(200)
  droid.vibrate(500)
  droid.vibrate(1000)
#droid.dialogDismiss()not required :) 

