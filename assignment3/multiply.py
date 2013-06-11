import MapReduce
import sys

"""
Matrix multiplication in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

#hardcode the matrix dimensions
a_rows = 5# let a,b be 5x5 matrices
b_rows = 5
a_cols = 5
b_cols = 5


def mapper(record):
    # key: matrix ('a' or 'b')
    # value: (i (row), j (column), value)
    matrix = record[0]
    row = record[1]
    col = record[2]
    val = record[3]
    if matrix == "a":
        for k in range(b_cols):
            mr.emit_intermediate((row,k), (matrix,row,col,val))
    elif matrix == "b":
        for i in range(a_rows):
            mr.emit_intermediate((i,col), (matrix,row,col,val))
            
                       

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    a_cells = {}
    b_cells = {}
    for cell in list_of_values:
        if cell[0] == "a":
            a_cells[str(cell[2])] = cell[3]
        elif cell[0] == "b":
            b_cells[str(cell[1])] = cell[3]       
    mult_sum = 0
    for cell_id in a_cells:#if not in a, then result will only add 0
        if cell_id in b_cells:#must also be a value with that key in b dict
            mult_sum += a_cells[cell_id]*b_cells[cell_id]
    mr.emit((key[0],key[1],mult_sum))
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)