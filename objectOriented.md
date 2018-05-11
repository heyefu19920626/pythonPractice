# ���������(Object Oriented Programming)

- [Class-Instance](#class-instance)
- [Access-Restriction](#access-restriction)
- [Polymorphism](#polymorphism)
- [GetObjectInfomation](#get-object-infor)
- [ClassAndInstanceProperty](#class-instance-property)
<div id="class-instance"></div>

### ���ʵ��
- OOP�Ѷ�����Ϊ����Ļ�����Ԫ��һ��������������ݺͲ������ݵĺ��� 
- ������̵ĳ�����ưѼ����������Ϊһϵ�е�����ϣ���һ�麯����˳��ִ��
- �������ĳ�����ưѼ����������Ϊһ�����ļ��ϣ���ÿ�����󶼿��Խ����������󷢹�������Ϣ����������Щ��Ϣ������������ִ�о���һϵ����Ϣ�ڸ�������֮�䴫��
- ��������Ϣʵ���Ͼ��ǵ��ö����Ӧ�Ĺ������������ǳ�֮Ϊ����ķ�����Method��
- ���ݷ�װ���̳кͶ�̬���������������ص�
- �����������Ҫ�ĸ�������ࣨClass����ʵ����Instance��
- ����ͨ�ĺ�����ȣ������ж���ĺ���ֻ��һ�㲻ͬ�����ǵ�һ��������Զ��ʵ������self�����ң�����ʱ�����ô��ݸò���
- ���__init__���캯��
```python
# ������object��ʾ�̳е��࣬���û�У���дobject
class Student(object):
    """docstring for Student"""

    #  ���췽��
    def __init__(self, name, score=90):
        self.name, self.score = name, score

    def print_score(self):
        print('%s�ĳɼ���:%s' % (self.name, self.score))


tom = Student('tom')
print(tom)
tom.print_score()
```
- Python�����ʵ���������κ�����

<div id="access-restriction"></div>

### ��������
- ���ڲ����Բ����ⲿ���ʣ����԰����Ե�����ǰ���������»���__
- ʵ���ϻ��ǿ��Է���,ͨ��_Student__score,��_����__������,��ΪPython�����������__name�����ĳ���_Student__name,��ͬ��Python�������п��ܸĳɲ�ͬ�ĵı�����
- ����Ϊ�ⲿ����get��set�ӿ�
```python
class Student(object):
    """docstring for Student"""

    #  ���췽��
    def __init__(self, name, score=90):
        self.name, self.__score = name, score

    def print_score(self):
        print('%s�ĳɼ���:%s' % (self.name, self.__score))


tom = Student('tom')
print(tom)
tom.print_score()
print(tom._Student__score)
```

<div id="polymorphism"></div>

### �̳кͶ�̬
- ����һ��class��ʱ�򣬿��Դ�ĳ�����е�class�̳У��µ�class��Ϊ���ࣨSubclass���������̳е�class��Ϊ���ࡢ������ࣨBase class��Super class��
- �̳п��԰Ѹ�������й��ܶ�ֱ���ù����������Ͳ���������������ֻ��Ҫ�����Լ����еķ�����Ҳ���԰Ѹ��಻�ʺϵķ���������д
- ��̬���Ե�Ѽ�������ص�����˼̳в���̬���������Ǳ����
```python
class Animal(object):

    def run(self):
        print('Animal is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run(animal):
    if isinstance(animal, Animal):
        animal.run()
    else:
        print('�봫��Animal')


cat = Cat()
run(cat)


class Dog(Animal):

    def run(self):
        print('Dog is running...')


run(Dog())
run(Student('Bob'))
```

<div id="get-object-infor"></div>

### ��ȡ������Ϣ

- type
    - type()�������ض�Ӧ��Class����
    - ��if������ж�,����ʹ��typesģ���ж���ĳ���
- isinstance
    - isinstance()�Ϳ��Ը������ǣ�һ�������Ƿ���ĳ������
- dir
    - dir()������������һ�������ַ�����list�����磬���һ��str������������Ժͷ���
    - ����__xxx__�����Ժͷ�����Python�ж�����������;��,����__len__�������س���
- ���������״̬
    - ʹ��getattr(), setattr(),�Լ�hasattr()ֱ�Ӳ�������״̬
    - ֻ���ڲ�֪��������Ϣ��ʱ�����ǲŻ�ȥ��ȡ������Ϣ
```python
# type
print(type(123))
print(types.FunctionType == type(run))
# isinstance
print(isinstance(cat, Animal))
print(isinstance(123, str))
# dir
print(dir('abc'))
# attr
print(hasattr(cat, 'run'))
print(hasattr(cat, 'runs'))
try:
    print(cat.name)
except Exception as e:
    print(e)
setattr(cat, 'name', 'Tome')
print(cat.name)
fn = getattr(cat, 'run')
fn()


def readImage(fp):
    # ��������ϣ�����ļ���fp�ж�ȡͼ����������Ҫ�жϸ�fp�����Ƿ����read������
    # ������ڣ���ö�����һ��������������ڣ����޷���ȡ
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
```

<div id="class-instance-property"></div>

# ʵ�����Ժ�������
- ��ʵ�������Եķ�����ͨ��ʵ������,����ͨ��self������һ����__init__������
- �౾����Ҫ��һ�����Կ���ֱ����class�ж���,������Թ������У�����ʵ�������Է���
- ��ͬ���Ƶ�ʵ�����Խ����ε������ԣ���ɾ��ʵ�����Ժ���ʹ����ͬ�����ƣ����ʵ��Ľ���������
```python
class Student(object):
    """docstring for Student"""
    email = 'test@email'

    #  ���췽��
    def __init__(self, name, score=90):
        # self.name, self.email, self.__score = name, 'test@email', score
        self.name, self.__score = name, score

    def print_score(self):
        print('%s�ĳɼ���:%s, �����ǣ�%s' % (self.name, self.__score, self.email))


tom = Student('tom')
print(tom)
print(tom.email)
Student.email = 'modify@email'
tom.print_score()
print(tom._Student__score)
bob = Student('Bob')
bob.print_score()
print(Student.email)
print(bob.email)
```