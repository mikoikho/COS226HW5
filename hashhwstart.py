#######################################################################
# Mikolas Macion
# 11/7/2026
# Hash something out (HW5): Describe what the assignment is and how
# you did it... how does each has function work?
#######################################################################

# you did the ss for commit 3 so just add all the stuff into github
# you ran it 1.5 times the size of the list and then also just the size of the list (linear probing)

# commit each time after attempting!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from datetime import datetime                                 # for tracking time
import time

# function will return a hash value 
def hashValue(movieElement, sizeOfTable):
    
    # hash function 1
    #value = len(movieElement) # hash function will be adding up the number of characters in the string
    
    # hash function 2, optimization goal is t minimize collisions, add amount of vowels to h.f. 1
    #vowels = 'aeiou'
    #vowel_count = 0                                          # initialize vowel count                  
    #for char in movieElement.lower():                        # convert title to all lowercase
        #if char in vowels:
            #vowel_count += 1
    #value = len(movieElement) + vowel_count
    
    # hash function 3
    #consonants = 'wpm'                                       # choosing 3 consonants to track                     
    #randomLetter_count = 0
    #for char in movieElement.lower():                  
            #if char in consonants:
                #randomLetter_count += 1                      # tally amount of chosen consonants in title
    #value = len(movieElement) ** 3 + randomLetter_count      # cube the length of the movie quote as well     
                             
    # hash function 4
    lowercase_count = 0
    vowels = 'aeiou'
    vowel_count = 0     
    for char in movieElement:
        if char.islower():
            lowercase_count += 1
        if char.lower() in vowels:
            vowel_count += 1                                                  
    if (len(movieElement)//2 == 0):                           # if even amount of chars in string
        value = len(movieElement)**2 + lowercase_count**2
    elif vowel_count != 0:
        value = len(movieElement) * vowel_count**4
    else: 
        value = len(movieElement)
    
    value %= sizeOfTable                                      # ensure value is within size of the table
    return value

# derive all data from csv file #
movies = []                                                   # create list         
#longest_title = 0                                            # create variable for determining linked list size, commit 2 
with open("MOCK_DATA.csv", "r", encoding="utf-8") as file:    # open file and read it, encoding is different from default
    next(file)                                                # skip header line
    text = file.readlines()                                   # make a list of strings by reading each line
    for line in text:                                         # loops through all string elements in texts list
        tempMovieData = []                                    # hold data for each movie
        for i in range(9):                                    # extract all parts of movie data (there are 9 parts for one movie)
            tempData = line.strip().split(',')[i]
            tempMovieData.append(tempData)                    # attach all parts into one list for the one movie
            #if i == 0:
                #if longest_title < len(tempMovieData[i]):
                    #longest_title = len(tempMovieData[i]) 
        movies.append(tuple(tempMovieData))                   # add all parts of movie list into movies list and unable to change

# start time to see how long it takes to construct the hash table
start_time = datetime.now()

# size of hash table #
# commits 1/2 are linked list, commits 3/4 are linear probing
# poor optimization (commit 1), amount of movies
#fixed_array = [None] * len(movies)
# minimize wasted space (commit 2), longest length of movies used as size
#fixed_array = [None] * longest_title
# poor optimization (commit 3), amount of movies * 1.5
#fixed_array = [None] * int(1.5 * len(movies))
#fixed_array = [None] * len(movies)
# good optimization (commit 4)
fixed_array = [None] * int(1.5 * len(movies))
#print(f'Length of hash table is {len(fixed_array)}')        # testing

# linked list hash table with a poor hash function #
# extra info: if >1 keys collide, a linked list stores the values at that index
# for linear probing, # of collisions will be different as there can be more than one collision per element
collision_tally = 0                                          # start collision tally here for commits 3 and 4
for movie in movies:
    # linked list
    #key = hashValue(movie[0], len(movies))                  # hash table 1 (movie title as key)
    #key = hashValue(movie[0], longest_title)                # hash table 2
    #if(fixed_array[key] == None):
        #fixed_array[key] = [movie]                          # put into title hash table, begin linkedList
    #else:
        #fixed_array[key].append(movie)                      # more than one value, append movie to linkedList
    # linear probing
    key =  hashValue(movie[8], len(fixed_array))             # hash table 3 (movie quote as key)
    while fixed_array[key] != None:
        key += 1
        collision_tally += 1                                 # linear probing implemented
        if key == len(fixed_array):                          # if key is at the end of the array
            key = 0                                          # send key back to start of array
    fixed_array[key] = movie

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
#collision_tally = 0                                         # only 1 collision if there is at least piece of data since list will append
#for i in fixed_array:                                       # ^ applies to linked list hash tables only
    #if(i != None):
        #collision_tally += len(i)-1                         # len starts at 1, so subtracting 1 for the first value                     
print(f"Amount of collisions: {collision_tally}")
# s.c. 3: time taken to construct the hash table
print(f"Time taken to run: {end_time - start_time}")

# extra info ############################################################
# hash table 1 (movie title as key)
#key = hashValue(movies[loop][0], size of hash table)
# put into title hash table
# hash table 2 (movie quote as key)
#key = hashValue(movies[loop][8], size of hash table)
# put into the quote hash table
# linear probing, need at least 15000 size (since there are 15000 values)