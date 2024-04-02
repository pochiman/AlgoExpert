""" 

[ Difficulty: Medium ]
[ Category: Famous Algorithms ]

##### Stable Internships #####

A company has hired N interns to each join one of N different teams. Each intern 
has ranked their preferences for which teams they wish to join, and each team has 
ranked their preferences for which interns they prefer.

Given these preferences, assign 1 intern to each team. These assignments should 
be "stable," meaning that there is no unmatched pair of an intern and a team such 
that both that intern and that team would prefer they be matched with each other.

In the case there are multiple valid stable matchings, the solution that is most 
optimal for the interns should be chosen (i.e. every intern should be matched with 
the best team possible for them).

Your function should take in 2 2-dimensional lists, one for interns and one for 
teams. Each inner list represents a single intern or team's preferences, ranked 
from most preferable to least preferable. These lists will always be of length N, 
with integers as elements. Each of these integers corresponds to the index of the 
team/intern being ranked. Your function should return a 2-dimensional list of 
matchings in no particular order. Each matching should be in the format 
[internIndex, teamIndex].


##### Sample Input #####
interns = [
  [0, 1, 2],
  [1, 0, 2],
  [1, 2, 0]
]

teams = [
  [2, 1, 0],
  [1, 2, 0],
  [0, 2, 1]
]

##### Sample Output #####
// This is the most optimal solution for interns
[
  [0, 0],
  [1, 1],
  [2, 2]
]

// This is also a stable matching, but it is suboptimal for the interns
// because interns 0 and 2 could have been given better team matchings
[
  [2, 0],
  [1, 1],
  [0, 2]
]

##### Hints #####

Hint 1
Try starting out by solving the most basic version of this problem. What would 
you do if every intern had a unique first choice?

Hint 2
If two interns had the same first choice, how can you decide which intern gets 
that team to keep the matchings stable?

Hint 3
To optimize performance, it might be helpful to first convert the input into a 
different data structure.

Optimal Space & Time Complexity
O(n^2) time | O(n^2) space - where n is the number of interns

"""





##### Solution 1 #####
# O(n^2) time | O(n^2) space - where n is the number of interns and teams
def stableInternships(interns, teams):
    chosenInterns = {}
    freeInterns = list(range(len(interns)))
    currentInternChoices = [0] * len(interns)

    teamMaps = []
    for team in teams:
        rank = {}
        for i, internNum in enumerate(team):
            rank[internNum] = i
        teamMaps.append(rank)

    while len(freeInterns) > 0:
        internNum = freeInterns.pop()

        intern = interns[internNum]
        teamPreference = intern[currentInternChoices[internNum]]
        currentInternChoices[internNum] += 1

        if teamPreference not in chosenInterns:
            chosenInterns[teamPreference] = internNum
            continue

        previousIntern = chosenInterns[teamPreference]
        previousInternRank = teamMaps[teamPreference][previousIntern]
        currentInternRank = teamMaps[teamPreference][internNum]

        if currentInternRank < previousInternRank:
            freeInterns.append(previousIntern)
            chosenInterns[teamPreference] = internNum
        else:
            freeInterns.append(internNum)

    matches = [[internNum, teamNum] for teamNum, internNum in chosenInterns.items()]
    return matches
