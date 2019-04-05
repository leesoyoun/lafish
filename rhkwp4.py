r= input(' 가격을 입력하시오 ') #r은 원래  가격
gkfdls=input ('할인율을 입력하시오 ') #gkfdls은 할인율 
r=int(r)
gkfdls=int (gkfdls)

wlsgkf=gkfdls*0.01 #wlsgkf은 할인율 변환 


chd = r-(r* wlsgkf)
chd=float(chd)

print ("할인된 가격은 " , chd )
