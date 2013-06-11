import MapReduce
import sys

"""
Social network: find asymmetric relationships in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record: [personA, personB] -> B is friend of A
    person = record[0]
    friend = record[1]
    mr.emit_intermediate("".join(sorted([person, friend])),[person, friend])
    #above line gives both (a,b) and (b,a) same key for the reduce function

def reducer(key, list_of_connections):
    # key: person
    # value: list of connections/directional relations (strings)
    if len(list_of_connections) == 1:#if key unidirectional
        mr.emit((list_of_connections[0][0], list_of_connections[0][1]))#emit connection
        mr.emit((list_of_connections[0][1],list_of_connections[0][0]))
        #and its inverse ^^
        
                      

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  
  
  
  