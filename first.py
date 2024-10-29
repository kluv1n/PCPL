import sys
#классы
class bisquare():
    def __init__(self):
        self.coef_a=0.0
        self.coef_b=0.0
        self.coef_c=0.0
        self.kol_roots=0
        self.roots=[]


    def input_coef(self, index, text):
        try:
            coef_str=sys.argv[index]
        except:
            print(text)
            coef_str=input()
        coef=float(coef_str)
        return coef


    def get_coef(self):
        self.coef_a=self.input_coef(1,"Введите A:")
        self.coef_b=self.input_coef(2,"Введите B:")
        self.coef_c=self.input_coef(3,"Введите C:")



    def solution(self):
        a=self.coef_a
        b=self.coef_b
        c=self.coef_c
        d=b*b-4*a*c
        if d<0.0:
            self.kol_roots=0
        elif d==0.0:
            t=(-b+(d**0.5))/(2*a)
            if t<0.0:
                self.kol_roots=0
            elif t==0.0:
                self.roots.append(t)
                self.kol_roots=1
            else:
                self.roots.append(t**0.5)
                self.roots.append(-(t**0.5))
                self.kol_roots=2
        else:
            t1=(-b+(d**0.5))/(2*a)
            t2=(-b-(d**0.5))/(2*a)
            if t1<0.0:
                if t2<0.0:
                    self.kol_roots=0
                elif t2==0.0:
                    self.kol_roots=1
                    self.roots.append(0)
                else:
                    self.kol_roots=2
                    self.roots.append(t2**0.5)
                    self.roots.append(-(t2**0.5))
            elif t1==0.0:
                if t2<0.0:
                    self.kol_roots=1
                    self.roots.append(0)
                elif t2==0.0:
                    self.kol_roots=1
                    self.roots.append(0)
                else:
                    self.kol_roots=3
                    self.roots.append(0)
                    self.roots.append(t2**0.5)
                    self.roots.append(-(t2**0.5))
            else:
                if t2<0.0:
                    self.kol_roots=2
                    self.roots.append(t1**0.5)
                    self.roots.append(-(t1**0.5))
                elif t2==0.0:
                    self.kol_roots=3
                    self.roots.append(t1**0.5)
                    self.roots.append(-(t1**0.5))
                    self.roots.append(0)

                else:
                    self.kol_roots=4
                    self.roots.append(t1**0.5)
                    self.roots.append(-(t1**0.5))
                    self.roots.append(t2**0.5)
                    self.roots.append(-(t2**0.5))


    def print_roots(self):
        if self.kol_roots != len(self.roots):
            print(('Ошибка. Уравнение содержит {} действительных корней, ' + \
                   'но было вычислено {} корней.').format(self.kol_roots, len(self.kol_roots)))
        else:
            if self.kol_roots == 0:
                print('Нет корней')
            elif self.kol_roots == 1:
                print('Один корень: {}'.format(self.roots[0]))
            elif self.kol_roots == 2:
                print('Два корня: {} и {}'.format(self.roots[0], \
                                                  self.roots[1]))
            elif self.kol_roots == 3:
                print('Три корня: {}, {} и {}'.format(self.roots[0], \
                                                  self.roots[1], \
                                                  self.roots[2]))
            elif self.kol_roots == 4:
                print('Четыре корня: {}, {}, {} и {}'.format(self.roots[0], \
                                                  self.roots[1], \
                                                  self.roots[2], \
                                                  self.roots[3]))



def main():
    k = bisquare()
    k.get_coef()
    k.solution()
    k.print_roots()


if __name__ == "__main__":
    main()