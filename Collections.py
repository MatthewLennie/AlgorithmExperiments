# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:12:51 2019
Brushing up on some of the less commonly talked about 
python data structures. 

@author: matt_
"""


from collections import deque, Counter, OrderedDict, defaultdict
#deque
#
#list-like container with fast appends and pops on either end
#
#New in version 2.4.
#
#Counter
#
#dict subclass for counting hashable objects
#
#New in version 2.7.
#
#OrderedDict
#
#dict subclass that remembers the order entries were added
#
#New in version 2.7.
#
#defaultdict
#
#dict subclass that calls a factory function to supply missing values
#
#New in version 2.5.


cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1


cnt2 = Counter()
for word in ['green', 'red', 'red', 'green', 'blue', 'blue','yellow']:
    cnt2[word] += 1

for el in cnt:
    print(el)    


print("2 Most common entries: {}".format(cnt.most_common(2)))


#This is awesome. 
word_count = Counter("blahblahblah")
number_count = Counter([1,2,3,1,2,3,1])
tuple_count = Counter([(1,2),(2,1),(1,2)])

#Operators 
print("Addition {}".format(cnt+cnt2))
print("Substraction {}".format(cnt-cnt2)) #doesn't give negatives!!
print("Union {}".format(cnt&cnt2)) #gives the minimum from both i.e. how many are present in both
print("Intersection {}".format(cnt|cnt2)) # gives maximum from both i.e. what is the maximum availiable from both

#%% deque

second = "mama"
d = deque('hahi')
d.extend(second)#In place
print("can extend deque in place:{}".format(d))
d.extendleft(second)
print("can extend on left hand side deque in place:{}".format(d))

print("get first instance of search{}".format(d.index('a')))
print("check for membership: {}".format('h' in d))

d.rotate(2)#inplace operation. 
print("rotate the deque: {}".format(d))

for i in range(2):
    print(d.pop())
    d.append('a')
    print(d.popleft())
    d.appendleft('z')

## Create a list with a given length 
#Great for rolling averages etc.. 
d = deque('hahao',5)
d.append('1')
print(d)

#%% Set
a = set('asdfasdfasdfadfqwerwqev')
print(a)
# adds the unique elements from another sequence
#extends set
a.update('zpoewasdf')

b = set('pqweor0')
## Careful about which way it applies
#subset means check that a is a subset of b
print("subset test: {}".format(a.issubset(b)))
#the functions will accept any iterators!!
print("subset test 2: {}".format(a.issubset(set('ad'))))

print("superset test: {}".format(a.issuperset(b)))
print("superset test 2: {}".format(a.issuperset(set('ad'))))

#elements in either
print("Union {}".format(a.union(b)))

# elements in both. 

print("Intersection {}".format(a.intersection(b)))

# elements in a but not b
print("difference {}".format(a.difference(b)))

# elements elements in one or the other, but not both. 
print("symmetric difference {}".format(a.symmetric_difference(b)))
#%% Default Dict. 
# Handles the case when you are counting. 
# automatically intializes new items saves you from having to use the
#stupid if case for new items and testing. 


example= 'asdfasdaaa'
example2= 'baddbabaaa'
ddict = defaultdict(int) 
for char in example:
    ddict[char] +=1

# can be also used to only add unique items to values! 
# nice way of counting unique elements belonging to each key.. 
ddict2 = defaultdict(set)
for char,char2 in zip(example,example2):
    ddict2[char].add(char2)



#%% Ordered Dict
    
example= 'asdfasdaaa'
example2= 'baddbabaaa'


o_dict = OrderedDict()

for char,char2 in zip(example,example2):
    o_dict[char] = char2 

    
    
# Can use it like a stack or queue with the popitem function 
# gives you front
print(o_dict.popitem(False))
# gives you back
print(o_dict.popitem())

