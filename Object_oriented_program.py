import datetime

class Family:

    def __init__(self, name, surname, birthday, telephone):

        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.birthday = birthday
        self.email = self.name + '.' + self.surname + '@gmail.com'

    def age(self):

        today = datetime.date.today()
        age = today.year - self.birthday.year

        if today < datetime.date(today.year, self.birthday.month, self.birthday.day):
            age -= 1
        return age

    def fullname(self):
        return '{} {}'.format(self.name,self.surname)


    def __repr__(self):
        return 'Family({} - {} - {})'.format(self.name,self.surname,self.telephone)

    def __str__(self):
        return '{} {} {}'.format(self.fullname(),self.email, self.age())

    def __add__(self, other):
        return self.age() + other.age()

    def __len__(self):
        return len(self.fullname())


person = Family('John', 'Urban', datetime.date(1984,8,28), '07887392185')
person1 = Family('James', 'Urban', datetime.date(1963,4,18), '07967343265')
person2 = Family('Nina', 'Jones', datetime.date(1963,4,11), '07777755432')
person3 = Family('coco', 'Jones', datetime.date(2012,7,12), '0756221445')
person4 = Family('Tina', 'Kuvac', datetime.date(1994,8,16), '07995435565')

print(repr(person1))
print(str(person3))
print(person2+person1)


#print (person2.__str__())
#print(person4.__repr__())

print(len(person))