from datetime import datetime

a = [x for x in range(3, 13)]
print(a)
value = []
print(value[0] if value else 0)

val = '2018,1'
date_object = datetime.strptime(val, '%Y,%m')

print(date_object.strftime("%b %y"))

print('sdada' + '123')


class B(object):
    def __init__(self):
        body = "aaa"
        self.context = {
            'body': body,
        }


class A(B):
    def __init__(self):
        super().__init__()
        self.context['body'] = self.context['body'] + "BBB"
        self.context = {
            **self.context,
        }
        print(self.context['body'])


class C(B):
    def __init__(self):
        super().__init__()

        print(self.context['body'])


b = B()
a = A()
c = C()

data = {
    'key': 100
}

print('{}\\xE2\\x80\\xAD\\xE2\\x80\\xAD'.format(data))

print('+381652522560')

name = 'Larry Lam'
if name:
    names = name.split(' ')
    given = names[0]
    family = names[len(names) - 1]
    print('{}, {}'.format(given, family))
