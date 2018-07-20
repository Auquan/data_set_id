import os
print ("version3")
open('./historicalData/my_newfile.txt', 'a').close()
os.rename('./historicalData/my_newfile.txt', './historicalData/my_oldfile.txt')
