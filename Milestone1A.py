from time import sleep
import yaml
from yaml.loader import SafeLoader
import datetime;

#ouputfile
output=open('Milestone1A.txt','w')

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
    for key in activity:
        temp=str(mainkey)+'.'+str(keys)+'.'+key
        s=str(timefunction())+';'+str(temp)+' Entry'+'\n'
        output.write(s)
        if 'Activities' in data['Activities'][key]:
            timefunction3(mainkey,data[mainkey]['Activities'][key])
        if 'Inputs' in (data['Activities'][key]):
            inputs=data['Activities'][key]['Inputs']
            time=inputs['ExecutionTime']
            inputs='('+inputs['FunctionInput']+', '+inputs['ExecutionTime']+')'+'\n'
            s=str(timefunction())+';'+str(temp)+' '+'Executing '+str('TimeFunction')+' '+str(inputs)
            sleep(int(time))
            
            output.write(s)
        s=str(timefunction())+';'+str(temp)+' Exit'+'\n'
        output.write(s)
    



    



f=open(r'c:/Users/Nikhila/Desktop/kla/DataSet/Milestone1/Milestone1A.yaml','r')
data=yaml.load(f,Loader=SafeLoader)
#print(data)
mainkey=list(data.keys())
mainkey=mainkey[0]
s=str(timefunction())+';'+str(mainkey)+' Entry'+'\n'
output.write(s)
#print(data[mainkey]['Activities']['TaskA']['Inputs'])
timefunction2(mainkey,data)

s=str(timefunction())+';'+str(mainkey)+' Exit'+'\n'
output.write(s)
print('-------------')
output.close()
#Printing on the terminal
f=open('Milestone1A.txt','r')
print(f.read())
