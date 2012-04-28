#A Sample Script from Sl4A ,demonstrating the full screen UI with Python :)

import android
droid=android.Android()

def eventloop():
  while True:
    event=droid.eventWait().result
    print event
    if event["name"]=="click":
      id=event["data"]["id"]
      if id=="button3":
        return
      elif id=="button2":
        droid.fullSetProperty("editText1","text","OK has been pressed")
      elif id=="button1":
        droid.fullSetProperty("textView1","text","Other stuff here")
        print droid.fullSetProperty("background","backgroundColor","0xff7f0000")
    elif event["name"]=="screen":
      if event["data"]=="destroy":
        return

print "Started"
layout="""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/background"
        android:orientation="vertical" android:layout_width="match_parent"
        android:layout_height="match_parent" android:background="#ff000000">
        <LinearLayout android:layout_width="match_parent"
                android:layout_height="wrap_content" android:id="@+id/linearLayout1">
                <Button android:id="@+id/button1" android:layout_width="wrap_content"
                        android:layout_height="wrap_content" android:text="Test 1"></Button>
                <Button android:id="@+id/button2" android:layout_width="wrap_content"
                        android:layout_height="wrap_content" android:text="Ok"></Button>
                <Button android:id="@+id/button3" android:layout_width="wrap_content"
                        android:layout_height="wrap_content" android:text="Cancel"></Button>
        </LinearLayout>
        <TextView android:layout_width="match_parent"
                android:layout_height="wrap_content" android:text="TextView"
                android:id="@+id/textView1" android:textAppearance="?android:attr/textAppearanceLarge" android:gravity="center_vertical|center_horizontal|center"></TextView>
        <EditText android:layout_width="match_parent"
                android:layout_height="wrap_content" android:id="@+id/editText1"
                android:tag="Tag Me" android:inputType="textCapWords|textPhonetic|number">
                <requestFocus></requestFocus>
        </EditText>
        <CheckBox android:layout_height="wrap_content" android:id="@+id/checkBox1" android:layout_width="234dp" android:text="Howdy, neighbors." android:checked="true"></CheckBox>
</LinearLayout>
"""
print layout
print droid.fullShow(layout)
eventloop()
print droid.fullQuery()
print "Data entered =",droid.fullQueryDetail("editText1").result
droid.fullDismiss()
