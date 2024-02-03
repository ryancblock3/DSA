# Hash Tables

## Hash Tables

Hash Table - A data structure that stores unordered items by mapping (or hashing) each item to a location in an array

Main advantage of a hash table is searching/inserting/removing and item may only be O(1)

Key - Value used to map to an index

Bucket - array element that the Hash Function sorts itms into.

Modulo Operator % - computes the integer remainder when dividing two numbers

Example - 20 element has table - key % 20 will map keys to a bucket indices 0 to 19

Collisions - Occurs when item being inserted into has table maps to the same bucket as an existing item in the hash table

Chaining - Collision resolution where each bucket has a list of items.

Open Addressing - Collision resolution where it is resolved by looking for an empty bucket elsewhere in the table

## Chaining

Chaining - handles collisions by using a list for each bucket where each list may store multiple items that map to the same bucket. Uses key to determine bucket then inserts into that buckets list. Searching determines the bucket and searches the buckets list. Likewise for removes.

## Linear Probing

Linear Probing handles collision by starting at the keys mapped bucket then lineraly searches subsequent buckets until an empty bucket is found.

Empty-Since-Start - bucket that has been empty since the hash table was created

Empty-After-Removal - bucket had an item removed that caused the bucket to now be empty

Searches only stops for empty-since-start not empty-after-removal

Removal starts at the items initial bucket and searches each bucket after until a matching item is foumd, or an empty since start bucket is found, or all buckets have been probed.

## Quadratic Probing

Quadratic Probing handles collision by starting at the keys mapped bucket then quadratically searches subsequent buckets until an empby bucket is found.

Mapped Bucket is H (H + c1 * i + c2 * i^2) mod (tablesize)

## Double Hashing

Double Hashing - Collision resolution technique that uses 2 different hash functions to compute buckets

## Hash Table Resizing

Resizing perserves all existing items while increasing the number of buckets

Commonly resized to the next prime number greater than or equal to N * 2

Load Factor - number of items in the hash table divided by the number of blocks

Loaf factor is used to decide when to resize the hash table

## Common Hash Functions

Perfect hash function - maps items to bucks with no collisions

A good hash function should uniformy distribute items into buckets

Modulo Hash - uses remainder from division of the key by hash table size N

Mid-Square Hash - squares the key, extracts R digits from the results middle and returns the remainder of the middle digits divided by hash table size N.

Multiplicative String Hash -  repeatedly multiples the hash value and adds the ASCII or Unicode value of each character in the string

## Direct Hashing

Direct Hash Function uses the items key as the bucket index

Direct Access Table - A hash table with a direct hash function

Limitations of Direct Hashing
1. All keys must be non-negative integers
2. The hash tables size = the largest key value plus 1

## Hashing Algorithms: Cryptography, Password Hashing

Cryptography - field of study focused on transmitting data securly

Cryptographic Hash Function - A hash functiond esigned specifically for cyptography

Password Hashing Function - a hashing function that produces a hash value for a password. Databases commonly store a users password hash as opposed to the actual passowrd

## Python: Hash Tables3

[Python Hash Table](../HashTables.py)
