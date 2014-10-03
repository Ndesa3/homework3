import data_load
import indexer 
import searcher

d = indexer.get_traversal_data("raw_data.pickle.txt")
searcher.search(d)

