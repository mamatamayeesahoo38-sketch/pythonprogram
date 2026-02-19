dict
______

it is a key value pair .
key is immutable
value is mutable
dict  is mutable

insertion order not preserved.

duplicate key not allow

index and slicing concept not avaliable.


d={}
print(type(d))

o/p:
dict


d={1:"A",2:"B",5:"C",4:10}
print(d)
o/p:

{1: 'A', 2: 'B', 5: 'C', 4: 10}


d={1:"A",2:"B",5:"C",4:10,2:"E"}
print(d)

o/p:
{1: 'A', 2: 'E', 5: 'C', 4: 10}



d={1:"A",2:"B",5:"C",4:10,2:"E"}
print(d.keys())
print(d.values())


o/p:
dict_keys([1, 2, 5, 4])
dict_values(['A', 'E', 'C', 10])







print("enter dict data")
d=eval(input())
print(d)

C:\Users\HP\Desktop\javascript program>py demo.py
enter dict data
{1:"A",2:"B",4:"C"}
{1: 'A', 2: 'B', 4: 'C'}



d={1:"A",2:"B",5:"C",4:10,2:"E"}
d.pop(2)
print(d)

o/p:
{1: 'A', 5: 'C', 4: 10}




d={1:"A",2:"B",5:"C",4:10,2:"E"}
d.popitem()
print(d)

o/p:
{1: 'A', 2: 'E', 5: 'C'}


d={1:"A",2:"B",5:"C",4:10,2:"E"}
d.clear()
print(d)

o/p:
{ }




d={1:"A",2:"B",5:"C",4:10,2:"E"}
print(d[5])
print(d.get(5))


o/p:
C
C


d={1:"A",2:"B",5:"C",4:10,2:"E"}
#print(d[7]) error
print(d.get(7))

o/p:
none




d={1:"A",2:"B",5:"C",4:10,2:"E"}
for i in d:
    print(i,d[i])

o/p:
1 A
2 E
5 C
4 10






d={1:"A",2:"B",5:"C",4:10,2:"E"}
print(d.items())

o/p:
C:\Users\HP\Desktop\javascript program>py demo.py
dict_items([(1, 'A'), (2, 'E'), (5, 'C'), (4, 10)])



d={1:"A",2:"B",5:"C",4:10,2:"E"}
for k,v in d.items():
    print(k,v)

o/P:
1 A
2 E
5 C
4 10



d={1:"A",2:"B",5:"C",4:10,2:"E"}
for k in d.keys():
    print(k,d[k])

o/p:
1 A
2 E
5 C
4 10


d={}
d=d.fromkeys("welcome")
print(d)

o/p:
{'w': None, 'e': None, 'l': None, 'c': None, 'o': None, 'm': None}


d={}
d=d.fromkeys("welcome","ok")
print(d)

o/p:
{'w': 'ok', 'e': 'ok', 'l': 'ok', 'c': 'ok', 'o': 'ok', 'm': 'ok'}


d={1:"A",2:"B",5:"C",4:10,2:"E"}
print(d.setdefault(1))
print(d.setdefault(7))
print(d)
print(d.setdefault(5,"C"))
print(d.setdefault(8,"F"))
print(d.setdefault(5,"H"))
print(d)

o/p:
A
None
{1: 'A', 2: 'E', 5: 'C', 4: 10, 7: None}
C
F
C
{1: 'A', 2: 'E', 5: 'C', 4: 10, 7: None, 8: 'F'}





d={1:"A",2:"B",5:"C",4:10,2:"E"}
d.update({3:"u"})
print(d)

o/p:
{1: 'A', 2: 'E', 5: 'C', 4: 10, 3: 'u'}


d={1:"A",2:"B",5:"C",4:10,2:"E"}
d.clear()
print(d)

o/p:
{ }


d={1:"A",2:"B"}
d1=d
d.update({3:"C"})
print(d)
print(d1)

o/p:
{1: 'A', 2: 'B', 3: 'C'}
{1: 'A', 2: 'B', 3: 'C'}


d={1:"A",2:"B"}
d1=d.copy()
d.update({3:"C"})
print(d)
print(d1)

o/p:
{1: 'A', 2: 'B', 3: 'C'}
{1: 'A', 2: 'B'}


dict comphersion
____________________

d={x:x*2 for x in [1,2,3,4]}
print(d)

o/p:
{1:1,2:4,3:6,4:8}


https://chatgpt.com/share/68d1561b-1144-8008-8b1b-2477907e1105

https://chatgpt.com/share/686e90c7-d520-8008-adef-9466d8d53d89




L=[1,5,6,4,2]
L1=[]
for i in L:
    L1.append(i)
print(L1)


L=[1,5,6,4,2]
L1=[i for i in L]
print(L1)



2. Squares of numbers
L=[1,5,6,4,2]
L1=[]
for i in L:
    L1.append(i**2)
print(L1)


L=[1,5,6,4,2]
L1=[i**2 for i in L]
print(L1)



Tuple Comprehension in Python

👉 Strictly speaking, there is no tuple comprehension in Python.

If you write parentheses ( ) instead of square brackets [ ], Python creates a generator expression, not a tuple.

The generator produces values one by one instead of building the whole list in memory.

✅ Example 1: List vs "Tuple Comprehension"
L = [x*x for x in range(5)]     # List comprehension
print(L)   # [0, 1, 4, 9, 16]

T = (x*x for x in range(5))     # Generator expression
print(T)   # <generator object <genexpr> at 0x...>


🔹 T is not a tuple, it’s a generator.

✅ Example 2: Converting generator to tuple
T = tuple(x*x for x in range(5))
print(T)   #