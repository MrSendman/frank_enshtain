f = open('input.txt', 'r').read().split('\n',)
f[0] = int(f[0])
if len(f[1:]) == f[0]:
    print(f)
    for i in f:
        i = str(f[i])
        i = i.split()
    class Student:
        height = 0
        gender =0
        music = 0
        hebbits =0

        def desc_hei(self):
            print(self.height)

    Student1 = Student()
    Student1.height = 23
    Student1.desc_hei()
else:
    print('make a norma list ok?')