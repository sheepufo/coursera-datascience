import MapReduce
import sys

"""
Relational join in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # table: table identifier
    # order_id: order_id contents
    table = record[0]
    order_id = record[1]#acts as key
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_elements):
    # key: word
    # value: list of occurrence counts
    order_id = key
    
    for entry in list_of_elements:
        if(len(entry) == 10):
            order = entry
            break
    line_items = [item for item in list_of_elements if len(item)==17]
    combined = []#put order list in front of each line_items row
    for item in line_items:
        combined.append(order+item)
    #print combined 
    for row in combined:   
        mr.emit(row)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)