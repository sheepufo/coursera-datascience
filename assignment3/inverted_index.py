import MapReduce
import sys

"""
Inverted index in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    doc_id = record[0]
    doc_text = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, doc_id)

def reducer(key, list_of_documents):
    # key: word
    # value: list of occurrence counts
    all_docs = []
    for doc in list_of_documents:
        if doc not in all_docs:
            all_docs.append(doc)
    mr.emit((key, all_docs))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)