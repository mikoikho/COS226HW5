# COS226HW5
Hash Something Out

Commit 1:
Optimization: Poor hash function using hash table 1 and linked-list style
To get a hash value, I took the movie title length and calculated its modulus by the table size, which was the length of the entire movie list. I figured it would be inefficient since those movie lengths would not vary much, and I got what I expected.
Statistics: 14901 unused buckets and collisions. Since it's a linked list, there would only be one collision before a movie title with the same hash value would be appended to the list at that hash value. Time to run was 0:00:00.002001. Will see how that compares to future runtimes.

Commit 2:
Optimization: Good hash function using hash table 1 and linked-list style to minimize wasted space
To get a hash value, I still used the movie title length, but also added the number of vowels in the title to the hash value. For the size, I used the longest title length. This led to a hash table size of 114, with 3 unused buckets and 14889 collisions. Time to run was 0:00:00.016830. The runtime was longer, but the hash table  and unused bucket sizes were drastically reduced. Even the collision number went down a little. Overall, it was a better outcome than commit #1, so the better hash function and hash table size attempt was a success.

Commit 3:
Optimization: Poor hash function using hash table 2 and linear probing to minimize collisions
To get a hash value, I used the movie quote length, cubed it, and added by the amount of letters w, p, and m there were in the quote. I tested a size 1.5*size of movies and just size of movies, and with the 1.5*size, I got 7500 unused buckets, 14,394,436 collisions, and a 0:00:02.976818 runtime. For the size of movies, I got 0 unused buckets, 27,599,863 collisions, and a 0:00:04.421303 runtime. Between the two, the size of movies nearly doubled the amount of collisions and runtime. Compared to linked-list, both of these got way more collisions and runtime. Commit 2 seems to be the best so far.

Commit 4:
Optimization: Good hash function using hash table 2 and linear probing to minimize collisions
To get a hash value, I got the counts of capital letters and vowels. I had three different equations: one for if there were an even number of characters in the string, one if there was at least one vowel if it was an odd number of characters, and the leftovers which would just take the length of the quote. I ran 1.5*size of movies, 1.25..., and just size of movies. The best ended up being 1.25*size with 3750 unused buckets, 12,523,689 collisions, and a 0:00:01.517210 runtime. This one just beat the 1.5*size of movies for commit 3, so I'll count it as a win. Commit 2 is the best overall, though.

Commit 5:
Optimization: Good hash function using hash table 1 and linked-list style to minimize wasted space
To get a hash value, I multiplied the length of the amount of characters there were in the title by 8 and subtracted that by 3 times the vowel count. I also got the size of the fixed array by dividing the number of movies by 100. I ended up with 0 unused buckets, 14850 collisions, and a runtime of 0:00:00.016303. This was just faster than commit 2 with less collisions, but with 0 unused buckets!

Overall:
Linked list definitely worked better for me than linear probing, which may have been because I didn't make my linear probing sizes big enough, which meant that overlapping hash values had to search much more, especially if the hash function led to values that were the same value. I had to keep note of how big the actually hash table would be when considering bucket size, and for minimizing collisions, linked list seems to be the best because it would at most be one before appending to the list at that one hash value. For minimizing bucket space, linear probing would seem better, but there would be so many collisions that it just was not worth it for the random functions that I plugged in based on the string that gets passed that were not based on any effective methods for getting a wide range of values to then take the modulus of. 
