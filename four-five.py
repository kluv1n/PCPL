from lab_python_fp import field
import lab_python_fp.gen_random
import lab_python_fp.unique

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

rand = lab_python_fp.gen_random.gen_random(5,1,25)

print(rand)

lab_python_fp.field.field(goods,'color','title')

iter=lab_python_fp.unique.Unique([1 ,2 ,2 ,4])

for i in iter:
    print(i)

-----
from contextlib import contextmanager
import time

class cm_timer_1:
    def __enter__(self):
        self.start_time=time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time=time.time()
        print(f"Время выполнения cm_timer_1: {end_time - self.start_time:.6f} секунд")


@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"Время выполнения cm_timer_2: {end_time - start_time:.6f} секунд")


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(5.5)

-----
def field(goods, *args):
    assert len(args) > 0

    result = []

    if len(args) == 1:
        for item in goods:
            if args[0] in item and item[args[0]] is not None:
                result.append(item[args[0]])
    else:
        for item in goods:
            str_result = "{"
            skip = False
            for arg in args:
                if arg in item and item[arg] is not None:
                    str_result += f'{arg} : {item[arg]}'
                    if arg != args[-1]:
                        str_result += ", "
                else:
                    skip = True
                    break
            if not skip:
                str_result += "}"
                result.append(str_result)

    return result

---------
import random

def gen_random(amount:int,l:int,r:int):
    result = []
    for i in range(amount):
        result.append(random.randint(l,r))

    return result


-------
def print_result(input_func):
    def output_func(*args, **kwargs):
        print(input_func.__name__)
        result=input_func(*args, **kwargs)
        if isinstance(result,list):
            for i in result:
                print(i)
        elif isinstance(result,dict):
            for key,val in result.items():
                print('{} = {}'.format(key,val))
        else:
            print(result)

        return result
    return output_func

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('Hi!')
    test_1()
    test_2()
    test_3()
    test_4()



-------
import json
from cm_timer import cm_timer_1
from field import field
from gen_random import gen_random
from print_result import print_result

path = "D:/ооп python/pythonProject1/lab_python_fp/data_light.json"

with open(path, encoding="utf-8") as f:
    data = json.load(f)

@print_result
def f1(data):
    result=sorted(field(data,"job-name"))
    return result

@print_result
def f2(f1_result):
    return list(filter(lambda job: job.startswith("программист"), f1_result))

@print_result
def f3(f2_result):
    return list(map(lambda job: f"{job} с опытом Python", f2_result))

@print_result
def f4(f3_result):
    salaries = gen_random(len(f3_result), 100000, 200000)
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(f3_result, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))



--------
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = sorted(data,reverse=True)
    print(result)

    result_with_lambda = sorted(data,key=lambda x: -x)
    print(result_with_lambda)

--------
class Unique(object):
    def __init__(self, items, ignore_case=False):
        self.ignore_case = ignore_case
        self.items = set()
        self.index = 0

        for item in items:
            if ignore_case and isinstance(item, str):
                item = item.lower()
            self.items.add(item)

        self.unique_items = list(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.unique_items):
            result = self.unique_items[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
