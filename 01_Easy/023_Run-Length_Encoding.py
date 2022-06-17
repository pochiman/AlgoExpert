""" 

##### Run-Length Encoding #####

Write a function that takes in a non-empty string and returns its run-length 
encoding.

From Wikipedia, "run-length encoding is a form of lossless data compression in 
which runs of data are stored as a single data value and count, rather than as the 
original run."  For this problem, a run of data is any sequence of consecutive, 
identical characters.  So the run "AAA" would be run-length-encoded as "3A".

To make things more complicated, however, the input string can contain all sorts 
of special characters, including numbers.  And since encoded data must be 
decodable, this means that we can't naively run-length-encode long runs.  For 
example, the run "AAAAAAAAAAAA" (12 As), can't naively be encoded as 
"12A", since this string can be decoded as either "AAAAAAAAAAAA" or "1AA".  
Thus, long runs (runs of 10 or more characters) should be encoded in a split 
fashion; the aforementioned run should be encoded as "9A3A". 


##### Sample Input #####
string = "AAAAAAAAAAAAABBCCCCDD"

##### Sample Output #####
"9A4A2B4C2D"


##### Hints #####

Hint 1
Traverse the input string and count the length of each run.  As you traverse 
the string, what should you do when you reach a run of length 9 or the end 
of a run?

Hint 2
When you reach a run of length 9 or the end of a run, store the computed 
count for the run as well as its character (you'll likely need a list for these 
computed counts and characters), and reset the count to 1 before 
continuing to traverse the string.

Hint 3
Make sure that your solution correctly handles the last run in the string.

Optimal Space & Time Complexity
O(n) time | O(n) space - where n is the length of the input string

"""





##### Solution 1 #####
# O(n) time | O(n) space - where n is the length of the input string
def runLengthEncoding(string):
  # The input string is guaranteed to be non-empty,
  # so our first run will be of at least length 1.
  encodedStringCharacters = []
  currentRunLength = 1

  for i in range(1, len(string)):
    currentCharacter = string[i]
    previousCharacter = string[i - 1]

    if currentCharacter != previousCharacter or currentRunLength == 9:
      encodedStringCharacters.append(str(currentRunLength))
      encodedStringCharacters.append(previousCharacter)
      currentRunLength = 0

    currentRunLength += 1

  # Handle the last run.
  encodedStringCharacters.append(str(currentRunLength))
  encodedStringCharacters.append(string[len(string) - 1])

  return "".join(encodedStringCharacters)
