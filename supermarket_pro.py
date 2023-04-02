from datetime import datetime
name=input("Enter your name:")

lists='''
Rice    RS 20/kg
Sugar   Rs 20/kg
Clogate Rs 70/each
Maggi   Rs 50/kg
Salt    Rs 20/kg
Boost   Rs 50/each
Panner  Rs 100/kg
 oil    Rs 160/kg
'''
#decleration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rate for items
items={'rice':20,
'sugar':20,
'clogate':70,
'maggi':50,
'salt':20,
'boost':50,'panner':100,'oil':160}
option=int(input("for list of items press1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
    if item in items.keys():
        price=quantity*(items[item])
        pricelist.append((item,quantity,items,price))
        totalprice+=price
        ilist.append(item)
        qlist.append(quantity)
        plist.append(price)
        gst=(totalprice*5)/100
        finalamount=gst+totalprice    
    else:
        print("sorry you entered item is not available")
else:
    print("you entered wrong number")
inp=input("can i bill the items yes or no:")
if inp=='yes':
    pass
    if finalamount!=0:
        print(25*"=","Rockz supermaket",25*"=")
        print(28*" ","vijayawada")
        print("Name:",name,30*" ","Date:",datetime.now())
        print(75*"_",)
        print("sno:",8*" ",4*" ","Quantity",8*" ","price")
        for i in range(len(pricelist)):
            print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
        print(75*"_")
    print(50*" ","Totalamount:",'Rs',totalprice)
    print("gst amount",50*" ",'Rs',gst)
    print(75*"_")
    print(50*"_",'finalamount:','Rs',finalamount)
    print(75*"_")
    print(50*" ","Thanks for visiting")
    print(115*" ")


