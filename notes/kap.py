'Analyze the Kaprekar process'
# https://en.wikipedia.org/wiki/6174_(number)

from pprint import pprint

def kap(n):
    '''Compute one step in the Kaprekar process

        >>> kap(3524)
        3087
        >>> kap(3087)
        8352
        >>> kap(6174)
        6174
        >>> kap(6174)
        6174

    '''
    s = '%04d' % n
    t = list(s)
    t.sort()
    small = int(''.join(t))
    t.sort(reverse=True)
    big = int(''.join(t))
    return big - small

if False and __name__ == '__main__':

    import doctest

    print(doctest.testmod())

# http://webgraphviz.com/

# Step 1: Convert the data to a convenient form
kapdict = {}
for i in range(10000):
    target = kap(i)
    kapdict['%04d' % i] = '%04d' % target

# Step 2: Analysis
firsts = set(kapdict.keys()) - set(kapdict.values())
rest = set(kapdict.keys()) - firsts
assert len(firsts) + len(rest) == len(kapdict)

# Step 3: Output Formatting
for i in sorted(rest):
    target = kapdict[i]
    print(f'{i} -> {target};')
