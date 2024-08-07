""" 

[ Difficulty: Medium ]
[ Category: Strings ]

##### Reverse Words In String #####

Write a function that takes in a string of words separated by one or more 
whitespaces and returns a string that has these words in reverse order. 
For example, given the string "tim is great", your function should return 
"great is tim".

For this problem, a word can contain special characters, punctuation, and 
numbers. The words in the string will be separated by one or more whitespaces, 
and the reversed string must contain the same whitespaces as the original string. 
For example, given the string "whitespaces    4" you would be expected to return 
"4    whitespaces".  

Note that you're not allowed to use any built-in split or reverse 
methods/functions. However, you are allowed to use a built-in join 
method/function.

Also note that the input string isn't guaranteed to always contain words.


##### Sample Input #####
string = "AlgoExpert is the best!"

##### Sample Output #####
"best! the is AlgoExpert"


##### Hints #####

Hint 1
There are at least two ways to solve this problem, and both require locating 
the words in the string. How can you find all of the words in the string?

Hint 2
If you're able to locate all of the words in the string, the next step is to 
figure out how many spaces are between them. If you can create a list that 
contains all of the words in the string and all of the spaces between them, 
then all you need to do is reverse the list and recreate the string using the 
reversed list.

Hint 3
A potentially easier approach to this problem is to start by reversing the 
entire string. Once the entire string has been reversed, the words will be in 
the correct order, but each word will also be reversed. From here, all you have 
to do is reverse all of the individual words in this new string. By doing this, 
you'll restore each reversed word back to its original order, and you'll have 
the desired output.

Optimal Space & Time Complexity
O(n) time | O(n) space - where n is the length of the string

"""





##### Solution 1 #####
# O(n) time | O(n) space - where n is the length of the string
def reverseWordsInString(string):
    words = []
    startOfWord = 0
    for idx in range(len(string)):
        character = string[idx]

        if character == " ":
            words.append(string[startOfWord:idx])
            startOfWord = idx
        elif string[startOfWord] == " ":
            words.append(" ")
            startOfWord = idx

    words.append(string[startOfWord:])

    reverseList(words)
    return "".join(words)


def reverseList(list):
    start, end = 0, len(list) - 1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1





##### Solution 2 #####
# O(n) time | O(n) space - where n is the length of the string
def reverseWordsInString(string):
    characters = [char for char in string]
    reverseListRange(characters, 0, len(characters) - 1)
  
    startOfWord = 0
    while startOfWord < len(characters):
        endOfWord = startOfWord
        while endOfWord < len(characters) and characters[endOfWord] != " ":
            endOfWord += 1

        reverseListRange(characters, startOfWord, endOfWord - 1)
        startOfWord = endOfWord + 1
      
    return "".join(characters)    


def reverseListRange(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1
