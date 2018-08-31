from gmail import GMail , Message 
mail=GMail ("baonguyen7897@gmail.com", "vuthikimoanh")
#bdy=''' 
#'''
msg=Message("huynq-xin nghỉ ốm", to="qhuydtvt@gmail.com", text="sáng nay ")# thêm , html = body 
mail.send(msg)