from time import sleep
import yaml
from yaml.loader import SafeLoader
import datetime;

#ouputfile
output=open('Milestone1B.txt','w')

def timefunction():
    return datetime.datetime.now()

def timefunction2(mainkey,data):
    activity=data[mainkey]['Activities']
    for key in activity:
        temp=str(mainkey)+'.'+key
        s=str(timefunction())+';'+str(temp)+' Entry'+'\n'
        output.write(s)
        if 'Activities' in data[mainkey]['Activities'][key]:
            timefunction3(mainkey,data[mainkey]['Activities'][key],key)
        if 'Inputs' in (data[mainkey]['Activities'][key]):
            inputs=data[mainkey]['Activities'][key]['Inputs']
            time=inputs['ExecutionTime']
            inputs='('+inputs['FunctionInput']+', '+inputs['ExecutionTime']+')'+'\n'
            s=str(timefunction())+';'+str(temp)+' '+'Executing ' +str('TimeFunction')+' '+str(inputs)
            sleep(int(time))
            output.write(s)
        s=str(timefunction())+';'+str(temp)+' Exit'+'\n'
        output.write(s)
def timefunction3(mainkey,data,keys):
    activity=data['Activities']
    print('keys in three')
    for key in activity:
        temp=str(mainkey)+'.'+str(keys)+'.'+key
        s=str(timefunction())+';'+str(temp)+' Entry'+'\n'
        output.write(s)
        print(key)
        if 'Activities' in activity[key]:
            print('Calling 4 with'+str(activity[key].keys()))
            timefunction4(mainkey,activity[key],temp)
        if 'Inputs' in (data['Activities'][key]):
            inputs=data['Activities'][key]['Inputs']
            time=inputs['ExecutionTime']
            inputs='('+inputs['FunctionInput']+', '+inputs['ExecutionTime']+')'+'\n'
            s=str(timefunction())+';'+str(temp)+' '+'Executing '+str('TimeFunction')+' '+str(inputs)
            sleep(int(time))
            
            output.write(s)
        s=str(timefunction())+';'+str(temp)+' Exit'+'\n'
        output.write(s)
def timefunction4(mainkey,data,keys):
    activity=data['Activities']
    for key in activity:
        #t=threading.Thread(target=timefuntion5,args=key)
        temp=str(keys)+'.'+key
        s=str(timefunction())+';'+str(temp)+' Entry'+'\n'
        output.write(s)
        print(key)
        
        if 'Inputs' in (data['Activities'][key]):
            inputs=data['Activities'][key]['Inputs']
            time=inputs['ExecutionTime']
            inputs='('+inputs['FunctionInput']+', '+inputs['ExecutionTime']+')'+'\n'
            s=str(timefunction())+';'+str(temp)+' '+'Executing '+str('TimeFunction')+' '+str(inputs)
            sleep(int(time))
            
            output.write(s)
        s=str(timefunction())+';'+str(temp)+' Exit'+'\n'
        output.write(s)

    



f=open(r'C:\Users\Nikhila\Desktop\kla\DataSet\Milestone1\Milestone1B.yaml','r')
data=yaml.load(f,Loader=SafeLoader)
#print(data)
mainkey=list(data.keys())
mainkey=mainkey[0]
s=str(timefunction())+';'+str(mainkey)+' Entry'+'\n'
output.write(s)
timefunction2(mainkey,data)

s=str(timefunction())+';'+str(mainkey)+' Exit'+'\n'
output.write(s)
print('-------------')
output.close()
#Printing on the terminal
f=open('Milestone1B.txt','r')
print(f.read())
