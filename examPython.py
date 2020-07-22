#### Lession 1 ####
print('#### Lession 1 ####')
x = 5
y = x + 3
x = x - 1
z = 10
x = x + z
print('x: {}, y: {}, z: {}'.format(x, y, z))
''' x: 14, y: 8, z: 10 '''

#### Lession 2 ####
print('#### Lession 2 ####')
print(14//4, 14%4, 14.0/4)
''' print(3 - 2 - 3,5) '''

#### Lession 3 ####
print('#### Lession 3 ####')
print(2*'No' + 3*'!')
print(2 * ('No' + 3*'!'))
''' NoNo!!! '''
''' No!!!No!!! '''

#### Lession 4 ####
print('#### Lession 4 ####')
print('how\nis it\nnow')
''' how
    is it 
    now '''

#### Lession 5 ####
print('#### Lession 5 ####')
for z in [2, 4, 7, 9]:
 print(z - 1)
''' 1  
    3
    6
    8 '''

#### Lession 6 ####
print('#### Lession 6 ####')
print('2' + '3')
''' 23 '''

#### Lession 7 ####
print('#### Lession 7 ####')
def f1():
 print('Hi')
def f2():
 print('Lo')
f2()
f1()
f1()
''' Lo
    Hi 
    Hi '''

#### Lession 8 ####
print('#### Lession 8 ####')
def func():
 print('Yes')
print('No')
func()
''' No
    Yes '''

#### Lession 9 ####
print('#### Lession 9 ####')
def func(x):
 print(2*x)
func(5)
func(4)
''' 10 '''
''' 8 '''

#### Lession 10 ####
print('#### Lession 10 ####')
def func(x):
 return x - 1
print(func(3) * func(5))
''' 8 '''

#### Lession 11 ####
print('#### Lession 11 ####')
n = 3 
for x in [2, 5, 8]:
 n = n + x
print(n)
''' 18 '''

#### Lession 12 ####
print('#### Lession 12 ####')
print(list(range(3)))
''' [0, 1 ,2] '''

#### Lession 13 ####
print('#### Lession 13 ####')
for i in range(3):
 print('Hello again!')
 ''' Hello again! '''
 ''' Hello again! '''
 ''' Hello again! '''

#### Lession 14 ####
print('#### Lession 14 ####')
for i in range(4):
    print(i)
''' 0
    1
    2   
    3 '''

#### Lession 15 ####
print('#### Lession 15 ####')
def s(x):
 return x*x
for n in [1, 2, 10]:
 print(s(n))
''' 1 '''
''' 4 '''
''' 100 '''

#### Lession 16 ####
print('#### Lession 16 ####')
def s(x):
 return x*x
tot = 0
for n in [1, 3, 5]:
 tot = tot + s(n)
print(tot) 
''' 35 '''

#### Lession 17 ####
print('#### Lession 17 ####')
x = 2.5679
y = 9.0
print('Answers {:.3f} and {:.3f}'.format(x, y))
''' 'Answers 2.568 and 9.000 '''

#### Lession 18 ####
print('#### Lession 18 ####')
d = dict()
d['left'] = '<<'
d['right'] = '>>'
print('{left} and {right} or {right} and {left}'.format(**d))
''' << and >> or >> and << '''

#### Lession 19 ####
print('#### Lession 19 ####')
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
print('n1 - ' + str(n1))
print('n2 - ' + str(n2))

#### Lession 20 ####
print('#### Lession 20 ####')
for s in range(5):
    print('s')
''' s 
    s
    s
    s
    s '''

#### Lession 21 ####
print('#### Lession 21 ####')
x = 3
y = '24'
print(x + int(y))
''' 27 '''

#### Lession 22 ####
print('#### Lession 22 ####')
wordList = ['Jose', 'Sue', 'Ivan']
def wordTwice(x):
    print(str(x) + ' ' + str(x))
for i in wordList:
    wordTwice(i)
''' Jose Jose
    Sue Sue
    Ivan Ivan '''

#### Lession 23 ####
print('#### Lession 23 ####')
d = dict()
d['name'] = 'Juan'
d['phone'] = '508-1234'
print('Name: {name}, Phone: {phone}'.format(**d))

#### Lession 24 ####
print('#### Lession 24 ####')
def doubleList(numberList):
    print(numberList * 2)
for i in [3, 1, 5]:
     doubleList(i)
''' 6
    2
    10 '''

#### Lession 25 ####
print('#### Lession 25 ####')
def process(x):
    print(x)
for i in ['Joe', 'Sue', 'Ann', 'Yan']:
    process(i)

#### Lession 26 ####
print('#### Lession 26 ####')
def sqrProd(x, y):
    return ((x * y)*(x * y))
print(sqrProd(2,5))

