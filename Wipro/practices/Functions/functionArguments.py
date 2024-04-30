'''To use tuple or list then you have to use *list use "*" before variable lenth.
if you want to work on dict then you can use dic() or **keyValue use "**" before the variable and place it in last.
'''

def details(name, address):
    print(name)
    print(address)

details("Jack",["Shadowfight 4", "story mode", "personel Mode"])  
'''Jack
['Shadowfight 4', 'story mode', 'personel Mode']''' 

# the same can be written as

def powers(name, *powers):
    print(name)
    print(powers)
    print(type(powers)) # it wil give as tuple

powers('Itu', "Time manipulation", "Shadow swift", "Multi attack speciality")

'''Itu
('Time manipulation', 'Shadow swift', 'Multi attack speciality')'''

def some(s1, *s2, s3="Optional"):
    print(s1)
    print(s2)
    print(s3)

some("New", "old", "is", "Gold", "time")

'''New
('old', 'is', 'Gold', 'time')
Optional

if you want to change the s3 from optional to different then you have to use key
'''
some("New", "times", "are", "bad", "but", "have", 'many', "facilities", s3="Mandatory")

'''New
('times', 'are', 'bad', 'but', 'have', 'many', 'facilities')
Mandatory'''


def args(cstmrName, *items, itemsWithQty, delivery="Home"):
    print("Customer Name",cstmrName)
    print("Itmes to bring",items)
    print("Items with qty",itemsWithQty)
    print("Delivery to",delivery)

args("Sarge", "Red meat", "Fish", "Banana","Badam", "Pista", itemsWithQty=dict(milk = "1 litre", eggs = 12))

'''Customer Name Sarge
Itmes to bring ('Red meat', 'Fish', 'Banana', 'Badam', 'Pista')
Items with qty {'milk': '1 litre', 'eggs': 12}
Delivery to Home'''

'''Instead of that you can write that'''

def arg(cstmrName, *items, delivery = "Home", **itemsWithQty):
    print("Customer Name",cstmrName)
    print("Itmes to bring",items)
    print("Items with qty",itemsWithQty)
    print("Delivery to",delivery)
    
arg("Azuma", "long knife", "serielization", "Shodow down", "Shadow knife", eggs = 5, bananas  = 5, meat = "1 Kg", delivery="office")

'''Delivery to Home
Customer Name Azuma
Itmes to bring ('long knife', 'serielization', 'Shodow down', 'Shadow knife')
Items with qty {'eggs': 5, 'bananas': 5, 'meat': '1 Kg'}
Delivery to office'''

# Unpacking the arguments

# if you want to pass the list as an arfgument then you have to use * to the variable

def aa(a1, *a2, a3 = "Default"):
    print(a1, a2, a3)

lst = ["aa1",'aa2', 'aa3', 'aa4']

aa("b1", *lst)

# similary for ** dct also
dct = dict(eggs = 5, lemons = 2)
# Now both list/tuple or dict at a time

def tupleDict(name, *lst, defaults = "Not mandatory", **dct ):
    print(name)
    print(lst)
    print(dct)
    print(defaults)

tupleDict("Both tuple and dict ", *lst, **dct, defaults= "Mandatory")

'''Both tuple and dict
('aa1', 'aa2', 'aa3', 'aa4')
{'eggs': 5, 'lemons': 2}
Mandatory
'''



