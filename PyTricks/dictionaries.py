import collections

d = collections.OrderedDict(one=1, two=2, three=3)
d['four'] = 4
d.keys()
d.values()


dd = collections.defaultdict(list)
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr. Sniffles')

dd['dogs']



chain = collections.ChainMap(d, dd)
chain['dogs']
chain['cats']

from types import MappingProxyType

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

read_only['one']

read_only['one'] = 5

writable['one'] = 4

#tuples

t = ('one', 'two', 'three')
t + ('four',)

#array.array
import array

arr = array.array('f', (1, 1.5, 2.0, 2.5))

arr[1] = 23
arr
del arr[1]

arr.append(42)

arr

astr = 'abcd'

astr
astr[1] = 'x'