import pywhatkit
import datetime
msg=input("Enter Msg: ")
number=input("Enter Number: ")
pywhatkit.sendwhatmsg("+91"+number,msg,datetime.datetime.now().hour,datetime.datetime.now().minute+1)