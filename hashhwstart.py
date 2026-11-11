#######################################################################
# Mikolas Macion
# 11/7/2026
# Hash something out (HW5): Describe what the assignment is and how
# you did it... how does each has function work?
#######################################################################

# commit each time after attempting!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from datetime import datetime                                 # for tracking time
import time

# function will return a hash value 
def hashValue(title, sizeOfTable):
    # hash function 1
    value = len(title) # hash function will be adding up the number of characters in the string
    value %= sizeOfTable
    # hash function 2
    # hash function 3
    # hash function 4
    return value

# derive all data from csv file #
movies = []                                                   # create list
with open("MOCK_DATA.csv", "r", encoding="utf-8") as file:    # open file and read it, encoding is different from default
    next(file)                                                # skip header line
    text = file.readlines()                                   # make a list of strings by reading each line
    for line in text:                                         # loops through all string elements in texts list
        tempMovieData = []                                    # hold data for each movie
        for i in range(9):                                    # extract all parts of movie data (there are 9 parts for one movie)
            tempData = line.strip().split(',')[i]
            tempMovieData.append(tempData)                    # attach all parts into one list for the one movie
        movies.append(tuple(tempMovieData))                   # add all parts of movie list into movies list and unable to change

# start time to see how long it takes to construct the hash table
start_time = datetime.now()

# size of hash table will be amount of movies #
fixed_array = [None] * len(movies)

# linked list hash table with a poor hash function #
# extra info: if >1 keys collide, a linked list stores the values at that index
for movie in movies:
    key = hashValue(movie[0], len(movies))                   # hash table 1 (movie title as key)
    if(fixed_array[key] == None):
        fixed_array[key] = [movie]                           # put into title hash table, begin linkedList
    else:
        fixed_array[key].append(movie)                       # more than one value, append movie to linkedList
   
# end time     
end_time = datetime.now() 
  
# test prints  
#print(len(movies))
#print(movies[len(movies)-1])
#print(len(movies[0][0]))
#print(len(fixed_array[15]))

# statistics checking #
# s.c. 1: amount of wasted space (unused buckets)
waste_tally = 0                                              # count collisions
for i in fixed_array:
    if(i == None):
        waste_tally += 1
print(f"Unused buckets: {waste_tally}")
# s.c. 2: # of collisions that occured during construction
collision_tally = 0                                          # only 1 collision if there is at least piece of data since list will append
for i in fixed_array:
    if(i != None):
        collision_tally += len(i)-1                          # len starts at 1, so subtracting 1 for the first value                     
print(f"Amount of collisions: {collision_tally}")
# s.c. 3: time taken to construct the hash table
print(f"Time taken to run: {end_time - start_time}")

# extra info ############################################################
# hash table 1 (movie title as key)
#key = hashValue(movies[0], len(movies))
# put into title hash table
# hash table 2 (movie quote as key)
#key = hashValue(movies[8])
# put into the quote hash table
# linear probing, need at least 15000 size (since there are 15000 values)