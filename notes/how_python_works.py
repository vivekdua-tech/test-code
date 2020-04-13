'''

struct IntType = {
    str  * __doc__
    str  * __name__
    func * __add__
    func * __sub__
    func * __mul__
    ...
}

struct IntObject {            // 8 bytes * 3 -> 24 bytes 
    int refcnt;
    PyType * __class__;       // dunder class
    int value;
}

###### x = 10

IntObject *obj;

obj = malloc(sizeof(IntObject));
obj->refcnt = 1;
obj->__class__ = &IntType;
obj->value = 10;

PyDictStore(globals, "x", obj);

###### type(x) ######################

obj = PyDictLookup(globals, "x");
printf("%s\n", obj->__class__.__name__)

##### y = x ########################

obj = PyDictLookup(globals, "x");
obj->refcnt += 1;
PyDictStore(globals, "y", obj);

##### del y ########################

obj = PyDictLookup(globals, "y");
PyDictRemove(global, "y");
obj->refcnt -= 1;
if (obj->refcnt == 0) {
    free(obj);
}

##### del x ########################

obj = PyDictLookup(globals, "x");
PyDictRemove(global, "x");
obj->refcnt -= 1;
if (obj->refcnt == 0) {
    free(obj);
}




'''
