import MapReduce
import sys

"""
Social network friend count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # table: table identifier
    # order_id: order_id contents
    person = record[0]
    friend = record[1]#acts as key
    mr.emit_intermediate(person, friend)

def reducer(key, list_of_friends):
    # key: person
    # value: list of friends (strings)
    total_friends = len(list_of_friends)
    mr.emit((key, total_friends))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)