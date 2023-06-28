[problem](https://cses.fi/problemset/task/1619/)

To get to know max people present in restaurant in same time. I need to know how many people are present inside at any moment of time, then I can take maximum of all. 

## Thought 1

We can maintain an array to get the count at any moment of time. 

    The idea being if a person was present from time a to time b. Then we can simply raise the value of all elements in our array from index a to b by one.(This action can be done in constant time with prefix sum techinque). 

This approach is very good **BUT** there is a big flaw with above solution. The contraint for time is a billion and obvisouly we can't create a billion sized array. 

**However** This was a good and simple O(n) solution for constraint under million. 

## Thought 2

The flaw with our previous approach is that we are maintaining count for **each** timestamp between entry and exit. Which is totally unnecessary. Rather we can maintain this data in **DISCRETE** manner. 

Meaning only storing starting and ending in array.

    The idea now is keeping all the entry and exit timestamp in a data structure. Plus along with timestamp we also need to know how many people entered/leave the restaurant. 

Hence which is that data structure which stores key value pair with best insertion and lookup time? 

    Yes that is none other than map (in c++), HashSet(in java) and dictionary (in python).

    For each timestamp we increment it's mapped value 1 if a person enters or decrement by 1 if a person leaves. 

    Finally we can extract all the timestamp and sort them in ascending order and iterate over them calculating number of people present at that moment and take max out of all of them.

time - 
Creating map - O(n)

sorting keys - O(nlogn)

calculating ans - O(n)

Note: In my java solution I have used treemap since it's keys are already in sorted order. Although it's doesn't do much help time complexity wise.

## Thought 3

What there is more to it??

Yes in our last approach we used the power of hashmap to solve it in given time but is there a way to solve without it? Yes there is a **GENIUS** solution.

    We can solve this with simple array. Ultimately we are sorting all timestamps anyway so their value doesn't matter but just their relative order which does matter. 

In this approach also we will sort all timestamps but how do we differencitate whether a person came in or went out at that moment? 

    That's where this solution is genius, all the timestamp which for entry of a person will be made even by multiplying by 2.
    
    And all the timestamp in which person exits will be made odd by multiplying by 2 and adding 1.

Yes this destroys their value but their relative order doesn't change hence number of people present in restaurant at that interval will be the same. 

    To store all timestamps entry/exit we require array of size 2n.

Once the above operatins are applied we can simply sort it and iterate over it.

    For even timestamp value increase the number of people by 1 and for odd value decrease it by 1.
    take maximum of all of it.

time - 

making array - O(n)

sorting array - 2nlogn(2n)

getting answer - O(2n)




