# HiddenDiversity
Combinatorics Project regarding Balls and Bins - filling a certain target fraction of the bins.
For a recent paper for a class, I thought it would be interested and mildly amusing to take brute-forcing to the next level.
This program creates a list of currently-hardcoded size 14, and fills it with random integers from 0 to 5.
Now for the brute force:
  It recursively searches through every unique way to iterate through the list.
    If it is an element already visited - return.
     Otherwise, add it to the 'visited' list for this recursive descent and then call the same function but with the new visited list and each other element in the list.
     
The end result being it searches through every possible way to iterate through a list.


Why python?
The algorithm is already so wildly inefficient, the effect the language would have isn't going to be that big of a deal.
The Big O efficiency is N!, so at that point changing to something like C could allow us to do n+1 in reasonable time, but just isn't worth the headache.
