# Object Types / Data Types

- **Number (Immutable)** : `1234`, `3.1415`, `3+4j`, `0b111`, `Decimal()`, `Fraction()`
- **String (Immutable)** : `'spam'`, `"Bob's"`, `b'a\x01c'`, `u'sp\xc4m'`
- **List (Mutable)** : `[1, [2, 'three'], 4.5]`, `list(range(10))`
- **Tuple (Immutable)** : `(1, 'spam', 4, 'U')`, `tuple('spam')`, `namedtuple`
- **Dictionary (Mutable)** : `{'food': 'spam', 'taste': 'yum'}`, `dict(hours=10)`
- **Set (Mutable)** : `set('abc')`, `{'a', 'b', 'c'}`
- **frozenset (Immutable)** : `frozenset(['a','b','c'])`

- **File (Mutable/Stateful)** : `open('eggs.txt')`, `open(r'C:\ham.bin', 'wb')`

- **Boolean (Immutable)** : `True`, `False`
- **None (Immutable)** : `None`
- **Functions, Modules, Classes (Generally Immutable definitions, 
  but attributes can be reassigned)**

## Advanced
- **Decorators** → Return new objects, don’t mutate originals directly.  
- **Generators / Iterators (Stateful/Mutable as consumed)**  
- **Metaprogramming constructs** → Can dynamically create/modify classes,  
  but underlying types follow the same mutability rules above.
