from types import MethodType
from enum import Enum, unique


class Student(object):
    pass


def set_age(self, age):
    self.age = age


s = Student()
s.name = 'Bob'
print(s.name)
# 给实例绑定一个方法
s.set_age = MethodType(set_age, s)
s.set_age(18)
print(s.age)


def set_score(self, score):
    self.score = score


Student.sex = 'Man'
Student.set_score = set_score

s1 = Student()
s1.set_score(95)
print(s1.score)


class Teacher(object):
    __slots__ = ('name', 'sex', 'age', 'set_age')


t = Teacher()
t.age = 27
print(t.age)
Teacher.sex = 'Women'
print(t.sex)
# t.address = 'Beijing'
Teacher.set_age = set_age
t.set_age(25)
print(t.age)

# @property


class Animal(object):

    def __init__(self):
        self.__name = 'Animal'

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type


dog = Animal()
dog.type = 'dog'
print(dog.type)


class Dog(Animal, Student):
    pass


class Cat(Animal, Teacher):
    pass


class Bob(Dog, Cat):
    pass


print(Bob.__mro__)


# 定制类

print(dog)


def get_str(self):
    return '这是Animal类'


Animal.__str__ = get_str
print(dog)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            step = n.step
            if start is None:
                start = 0
            if step is None:
                step = 1
            if stop is None:
                stop = 20
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


for n in Fib():
    print(n)

f = Fib()
print(f[6])
print(f[:])
print(f[:6:2])
x = list(range(30))
print(x)
print(x[::2])


def get_attr(self, attr):
    if attr == 'country':
        return lambda: 'China'
    return 'None'


Student.__getattr__ = get_attr
print(s.country())
print(s.address)


def call(self, address='Beijing'):
    print('My name is %s, I live in %s' % (self.name, address))


Student.__call__ = call
s()
print(callable(Student()))
print(callable([1, 2, 3, 4, 5]))

# Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Web = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Month(2))
print(Weekday.Mon)
print(Weekday['Fri'])
print(Weekday(3).value)


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Test(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


bart = Test('bart', Gender.Male)
print(bart.gender == Gender.Male)


# MetaClass

def fn(self, name='world'):
    print('Hello, %s' % name)


Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
h.hello()


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        print('type.__new__()')
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


mylist = MyList()
mylist.add(9)
print(mylist)


# metaclass 实现ORM
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


print(StringField('name'))
print(IntegerField('age'))


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mappings: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (
            self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Heyefu', email='527380349@qq.com', password='123456')

u.save()
