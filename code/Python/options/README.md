# Options

## \_\_slots_\_
<div style="text-align: justify">
In Python classes attributes are stored in a dictionary, which are flexible since we can add and remove data a
runtime without any error. On the other hand, this approach is quite slow and hard to maintain from a software engineer
point of view. <br>
Through slots python provides a way to statically declare the attributes that can be defined in a class, but not their types.
</div>

Example:

``` python
class MyMainModel:
    __slots__ = ('parser', 'y', 'z', 'opt')
```

Declaring a class in this way, the following syntax will raise an exception:

``` python
a = MyMainModel()
a.w = "Hello world"
```

### \_\_slots\_\_: Inheritance
With _\_slots__ you should not declare a same-named attribute in two classes that will inherit each other,
the base-class memory will be overwritten. 


### \_\_slots\_\_: Performance
<div style="text-align: justify">
In spite of flexibility slots are providing faster-memory access (up to 20% with python 3.10) and a better management of
the memory.  
</div>

## Slots and Options
The code in demo.py will show a way to use argparse(available by default in python) and slots. The code build a model with two
sub-models where the sub-models has their option plus their father options. Please note:
- argparse's "parents" option can deal with more than one father. 
- if using multiple inheritance be aware on how to call super properly.
- Options are not linked since we are re-assigning them. Changing a father option from a child will not affect other classes but the 
one we are operating on.
