

# O(v + e) time | O(v) space - where v is the number of vertices (people) in the
# friends graph and e is the number of edges (total friends) in the friends graph
def degreesOfSeparation(friendsLists, personOne, personTwo):
    degreesOne = getDegreesOfSeparation(friendsLists, personOne)
    degreesTwo = getDegreesOfSeparation(friendsLists, personTwo)
    numDegreesOverSixOne = getNumDegreesOverSix(friendsLists, degreesOne)
    numDegreesOverSixTwo = getNumDegreesOverSix(friendsLists, degreesTwo)
    if numDegreesOverSixOne == numDegreesOverSixTwo:
        return ""
    return personOne if numDegreesOverSixOne < numDegreesOverSixTwo else personTwo


def getDegreesOfSeparation(friendsLists, origin):
    degrees = {}
    visited = {}
    # We could use the `deque` object instead of a standard Python
    # list if we wanted to optimize our `.pop(0) operations.`
    queue = [{"person": origin, "degree": 0}]
    while len(queue) > 0:
        personInfo = queue.pop(0)
        person, degree = personInfo["person"], personInfo["degree"]
        degrees[person] = degree
        for friend in friendsLists[person]:
            if friend in visited:
                continue
            visited[friend] = True
            queue.append({"person": friend, "degree": degree + 1})
    for person in friendsLists:
        if person not in visited:
            degrees[person] = float("inf")
    return degrees


def getNumDegreesOverSix(friendsLists, degrees):
    numDegreesOverSix = 0
    for person in friendsLists:
        if degrees[person] > 6:
            numDegreesOverSix += 1
    return numDegreesOverSix
