import android
droid = android.Android()
url ="file:///sdcard/download/me.jpg"
mime = "image/jpeg"

droid.startActivity('android.intent.action.VIEW',url,mime)

