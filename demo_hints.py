from typing import Callable, Iterable, Literal, Sequence, cast


numbers: list[int|float]

numbers = [1, 2.0, 3]
numbers.append(4)
numbers.append(4.5)
# Type error: numbers.append('toto')

# tuple length and type of each element:
point_t: tuple[str, float, float] = 'A', 1.5, 4.5

name: str = point_t[0]

numbers_t: tuple[int, ...] = 1, 2, 3, 4, 5, 6

for n in numbers_t:
    print((n**2 + 1) * 3)

def headers(a: Literal['infer'] | int) -> None:
    if a == 'infer':
        print('Headers are infered')
    else:
        print('Headers are at line #', a)

headers('infer')
headers(5)
# headers('at line 5')

param: Literal['infer'] = 'infer'
headers(param)

def f(x: Literal[5] | str) -> None:
    pass

def h(x: Literal['toto']|Literal['titi']) -> None:
    pass

# custom annotation type
HeaderSpec = Literal['infer'] | int | Sequence[int]

def headers2(where: HeaderSpec) -> None:
    pass

# ok
headers2('infer')
headers2(2)
headers2([1,2,3])
headers2((1,2,3))
# wrong
# headers2('toto')
# headers2(['a', 2])


# PEP 695 (linter pycharm OK, mypy ko)
def search[T](container: list[T], element: T) -> tuple[int, T] | None:
    for i, v in enumerate(container):
        if v == element:
            return (i,v)
    return None 

values = ['1', '2', '3', 'aaa']
# ok
res = search(values, '2')
if res is not None:
    index, val = res
    print(f"found value {val} at index {index}") 
# ko 
#res = search(values, 'toto')


objects = [1, 2.0, 3, 'toto']

# static downcasting only !
n0 = cast(int, objects[0]) # n0 is considered as int
n1 = cast(int, objects[3])
print(n0, n1)

# Function types
def mymap(f: Callable[[int], int], iterable: Iterable[int], offset: int) -> Iterable[int]:
    return map(lambda x: f(x) + offset, iterable)

# ok
results: list[int] = list(mymap(lambda x: x**2+1, range(10), 3))
print(results)

# ko
mymap(lambda x,y: (x+y)**2+1, range(10), -1)


#f2: Callable[..., None]