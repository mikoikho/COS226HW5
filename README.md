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


Commit 4:


Commit 5:
