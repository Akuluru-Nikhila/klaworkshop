


f=open(r'C:\Users\Nikhila\Desktop\kla\DataSet\Milestone3\Milestone3A_DataInput1.csv','r')
content=(f.readlines())
#print(content)
f2=open('Milestone3A.txt','w')
f2.write('Id,X,Y,Signal,Bincode\n')
print(''"statt--------------"'')
for i in content[1:]:
    data=i[:-1]
    i=i[:-1]
    i=i.split(',')
    signal=int(i[3])
    bid=0
    temp=''
    if signal > 199 and signal < 256:
        bid=504
    elif signal > 129 and signal < 200:
        bid=503
    elif signal > 99 and signal < 130:
        bid=502
    elif signal > 59 and signal < 100:
        bid=501
    elif signal < 60:
        bid=500


    temp=data+','+str(bid)+'\n'
    f2.write(temp)

f.close()
f=open('Milestone3.txt','r')
print(f.read())
f.close()

