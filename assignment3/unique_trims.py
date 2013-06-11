import MapReduce
import sys

"""
Social network friend count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # [id, string of nucleotides]
    key = record[0]
    nucleotides = record[1]
    trimmed_nucs = nucleotides[:-10]
    mr.emit_intermediate(trimmed_nucs, trimmed_nucs)

def reducer(key, list_of_trims):
    # key: person
    # value: list of connections/directional relations (strings)
    unique_trims = list(set(list_of_trims))
    #print len(unique_trims)
    for dna in unique_trims:
        mr.emit((dna))
        
                      

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)