def varfunc():
    var = 0
    print(f'var = {var}')
    var += 1
if __name__ == "__main__":
    for i in range(3):
        varfunc()
#类的属性
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print(Static.StaticVar)
print(Static.StaticVar)
a = Static()
for i in range(3):
    a.varfunc()