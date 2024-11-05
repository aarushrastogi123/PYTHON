
'''def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    greeting = func("Hi")
    print(greeting)
greet(shout)
greet(whisper)'''

'''names=['a','b','c','d']
def addgreeting(name:str):
    return "Hello " + name
nameandgreeting=(map(addgreeting,names))
print(nameandgreeting)
for i in (nameandgreeting):
    print(i)

def is_even(num:int)->bool:
    return num%2!=0

nums=[1,2,3,4,5,6,7,8]
evens=filter(is_even,nums)
print(list(evens))

def higherorder(n:int)->int:
    return lambda x:x**n
power3=higherorder(3)
b=[]
for i in range(9):
    b.append(power3(i+1))
print(b)'''

import collections
Scientist=collections.namedtuple('Scientist', ['name','born','field'])
# Define an immutable tuple for scientists
scientists = (   
    Scientist(name="Albert Einstein",born= 1879,field= "Physics"),
    Scientist(name="Marie Curie",born= 1867,field= "Chemistry"),
    Scientist(name="Isaac Newton",born= 1643,field= "Physics"),
    Scientist(name="Charles Darwin",born= 1809,field= "Biology"),
    Scientist(name="Niels Bohr",born= 1885,field= "Physics")
)
for i in scientists:
    print(i)

print('\n')
names_ages=tuple(map(lambda x : {'name':x.name,'age':2017-x.born},scientists))
print(names_ages)

print('\n')
ace=tuple(filter(lambda x: x.field=="Physics",scientists))
print(ace)

print('\n')
from functools import reduce
total_age=reduce(lambda acc,val:acc+val['age'],names_ages,0)
print(total_age)

print('\n')
acing={'Physics':[],'Chemistry':[],'Biology':[]}
def reducer(acc,val):
    a=(val.name,val.born)
    acc[val.field].append(a)
    return acc
scientists_by_field=reduce(reducer,scientists,acing)
print(scientists_by_field)

print('\n')
scientists_by_field2=reduce(reducer,scientists,collections.defaultdict(list))
print(scientists_by_field2)





    
