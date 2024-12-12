# Hints / Annotation Types

## Links
- Real Python article: https://realpython.com/python-type-checking/
- Generic type declaration (python 3.12): https://peps.python.org/pep-0695/

## Simplifications

typing.List[int] => list[int]
idem Dict, Tuple

typing.Union[int,float] => int | float

typing.Optional[int] => int | None

## Misc
typing.Any

## Typing of tuples vs lists
list i.e. list[Any]
list[int|float] 
list[int] : homegeneous

tuple[str, float, float]: heterogeneous 
Example: ('A', 2.0, 3.5)

typing.Sequence[T] generalize list[T], tuple[T, ...]