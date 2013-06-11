# Little tests, etc. for assignment 3


a = [["one", "two", "three"], ["a", "g", "woo"], ["what", "ok"]]
b = [x for x in a if len(x)==3]
print b
## ^^ so dumb of you... had a in front of list dec.. ie b=a[.....]


a_list = ["a", "b", "c", "d", "efdaf", "zdlfjka", "baba", "mama", "aca"]
print a_list
print sorted(a_list)


b_list = ["a", "a", "a", "b", "b"]
print set(b_list)


for i in range(5):
    print i