from collections import Counter, defaultdict, OrderedDict
import datetime 
from time import time
from array import array

li = [1,2,3,4,5,6,7,7]
sentence = 'blah blah blah thinking about python'
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['c'])

print(datetime.datetime.now())