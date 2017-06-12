import pickle

myfile = open('bdata', 'wb')
pickle.dump(9**33, myfile)
myfile.close()
