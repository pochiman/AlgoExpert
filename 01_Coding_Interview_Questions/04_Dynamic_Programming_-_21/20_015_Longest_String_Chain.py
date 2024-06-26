""" 

[ Difficulty: Very Hard ]
[ Category: Dynamic Programming ]

##### Longest String Chain #####

Given a list of strings, write a function that returns the longest string chain that 
can be built from those strings.

A string chain is defined as follows: let string A be a string in the initial array; 
if removing any single character from string A yields a new string B that's contained 
in the initial array of strings, then strings A and B form a string chain of length 2. 
Similarly, if removing any single character from string B yields a new string C that's 
contained in the initial array of strings, then strings A, B, and C form a string 
chain of length 3.

The function should return the string chain in descending order (i.e., from the 
longest string to the shortest one). Note that string chains of length 1 don't exist; 
if the list of strings doesn't contain any string chain formed by two or more strings, 
the function should return an empty array.

You can assume that there will only be one longest string chain.


##### Sample Input #####
strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "labde", "abcdef"]

##### Sample Output #####
["abcdef", "abcde", "abde", "ade", "ae"]


##### Hints #####

Hint 1
For each string, you will have to remove every letter one at a time to see if the 
resulting strings are contained in the input list of strings. What data structure 
lends itself to quickly checking if these strings are located in the list of 
input strings? 

Hint 2
Realize that every string in the input list of strings potentially has a string 
chain (and therefore a longest string chain) that starts with itself. Compute all 
of these string chains and store them so that you don't have to compute them more 
than once.

Hint 3
Sort the input list of strings (from shortest to longest string) in order to 
simplify the problem. Iterate through the list of sorted strings, and for each 
string, compute the longest string chain that starts with itself. To do so, try 
removing every letter from each string and seeing if the resulting strings are 
in the input list of strings; you can do so in constant time by dumping every 
string in a hash table. In the hash table, store the longest string chain of 
every string as you compute them. As you iterate through longer strings, 
whenever you find a shorter string for which you've already computed the 
longest string chain, you can very quickly append the longer string to that 
already-computer string chain. Do this for every string, and you'll eventually 
find the longest string chain that you're looking for.

Hint 4
Do you need to store every string's longest string chain mentioned in Hint #3, or 
can you store less information per string so as to take up less auxiliary space?

Optimal Space & Time Complexity
O(n * m^2 + nlog(n)) time | O(nm) space - where n is the number of strings 
and m is the length of the longest string

"""





##### Solution 1 #####
# O(n * m^2 + nlog(n)) time | O(nm) space - where n is the number of strings and 
# m is the length of the longest string
def longestStringChain(strings):
    # For every string, imagine the longest string chain that starts with it. 
    # Set up every string to point to the next string in its respective longest 
    # string chain. Also keep track of the lengths of these longest string chains.
    stringChains = {}
    for string in strings:
        stringChains[string] = {"nextString": "", "maxChainLength": 1}

    # Sort the strings based on their length so that whenever we visit a 
    # string (as we iterate through them from left to right), we can 
    # already have computed the longest string chains of any smaller strings.
    sortedStrings = sorted(strings, key=len)
    for string in sortedStrings:
        findLongestStringChain(string, stringChains)  

    return buildLongestStringChain(strings, stringChains)


def findLongestStringChain(string, stringChains):
    # Try removing every letter of the current string to see if the 
    # remaining strings form a string chain.
    for i in range(len(string)):
        smallerString = getSmallerString(string, i)
        if smallerString not in stringChains:
            continue
        tryUpdateLongestStringChain(string, smallerString, stringChains)    


def getSmallerString(string, index):
    return string[0:index] + string[index + 1 :]


def tryUpdateLongestStringChain(currentString, smallerString, stringChains):
    smallerStringChainLength = stringChains[smallerString]["maxChainLength"]  
    currentStringChainLength = stringChains[currentString]["maxChainLength"]  
    # Update the string chain of the current string only if the smaller string leads 
    # to a longer string chain.
    if smallerStringChainLength + 1 > currentStringChainLength:
        stringChains[currentString]["maxChainLength"] = smallerStringChainLength + 1
        stringChains[currentString]["nextString"] = smallerString  


def buildLongestStringChain(strings, stringChains):
    # Find the string that starts the longest string chain.
    maxChainLength = 0
    chainStartingString = ""
    for string in strings:
        if stringChains[string]["maxChainLength"] > maxChainLength:
            maxChainLength = stringChains[string]["maxChainLength"]
            chainStartingString = string

    # Starting at the string found above, build the longest string chain.
    ourLongestStringChain = []
    currentString = chainStartingString
    while currentString != "":
        ourLongestStringChain.append(currentString)
        currentString = stringChains[currentString]["nextString"]

    return [] if len(ourLongestStringChain) == 1 else ourLongestStringChain
