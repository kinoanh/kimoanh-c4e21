import datetime 
from gmail import GMail , Message
now=datetime.datetime.now()
print(now.hour)
send=False
while True:
    if now.hour ==7 :
        send= False
        mail=GMail ("baonguyen7897@gmail.com", "vuthikimoanh")
        mes=Message("kimoanh", to="Tubi8556789@gmail.com", text=" đây là tin nhắn từ động được gửi từ Gmail : baonguyen7897@gmail.com , cám ơn , kim oanh ")

        mail.send(mes)
        break