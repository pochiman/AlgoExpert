""" 

##### Calendar Matching #####

Imagine that you want to schedule a meeting of a certain duration with a co-
worker. You have access to your calendar and your co-worker's calendar (both of 
which contain your respective meetings for the day, in the form of 
[startTime, endTime]), as well as both of your daily bounds (i.e., the earliest 
and latest times at which you're available for meetings every day, in the form of 
[earliestTime, latestTime]).

Write a function that takes in your calendar, your daily bounds, your co-worker's 
calendar, your co-worker's daily bounds, and the duration of the meeting that you 
want to schedule, and that returns a list of all the time blocks (in the form of 
[startTime, endTime]) during which you could schedule the meeting, ordered from 
earliest time block to latest.

Note that times will be given and should be returned in military time. 
For example: 8:30, 9:01, and 23:56.

Also note that the given calendar times will be sorted by start time in ascending 
order, as you would expect them to appear in a calendar application like Google 
Calendar.


##### Sample Input #####
calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30

##### Sample Output #####
[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]


##### Hints #####

Hint 1
In order to find blocks of time during which you and your coworker can have a 
meeting, you have to first find all of the unavailabilities between the two of 
you. An unavailability is any block of time during which at least one of you 
is busy. 

Hint 2
You'll have to start by taking into account the daily bounds; the daily bounds 
can be represented by two additional meetings in each of your calendars.

Hint 3
Once you've taken the daily bounds into account, you'll want to merge the two 
calendars into a single calendar of meetings and then flatten that calendar in 
order to eliminate overlapping and back-to-back meetings. This will give you a 
calendar of unavailabilities, from which you can pretty easily find the list 
of matching availabilities.

Optimal Space & Time Complexity
O(c1 + c2) time | O(c1 + c2) space - where c1 and c2 are the respective 
numbers of meetings in calendar1 and calendar2

"""





##### Solution 1 #####
# O(c1 + c2) time | O(c1 + c2) space - where c1 and c2 are the respective numbers of meetings in calendar1 and calendar2
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
  updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
  updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)
  mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2)
  flattenedCalendar = flattenCalendar(mergedCalendar)
  return getMatchingAvailabilities(flattenedCalendar, meetingDuration)

    
def updateCalendar(calendar, dailyBounds):
  updatedCalendar = calendar[:]
  updatedCalendar.insert(0, ["0:00", dailyBounds[0]])
  updatedCalendar.append([dailyBounds[1], "23:59"])
  return list(map(lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])], updatedCalendar))
    

def mergeCalendars(calendar1, calendar2):
  merged = []
  i, j = 0, 0
  while i < len(calendar1) and j < len(calendar2):
    meeting1, meeting2 = calendar1[i], calendar2[j]
    if meeting1[0] < meeting2[0]:
      merged.append(meeting1)
      i += 1
    else:
      merged.append(meeting2)
      j += 1
  while i < len(calendar1):
    merged.append(calendar1[i])
    i += 1
  while j < len(calendar2):
    merged.append(calendar2[j])
    j += 1
  return merged


def flattenCalendar(calendar):
  flattened = [calendar[0][:]]
  for i in range(1, len(calendar)):
    currentMeeting = calendar[i]
    previousMeeting = flattened[-1]
    currentStart, currentEnd = currentMeeting
    previousStart, previousEnd = previousMeeting
    if previousEnd >= currentStart:
      newPreviousMeeting = [previousStart, max(previousEnd, currentEnd)]
      flattened[-1] = newPreviousMeeting
    else:
      flattened.append(currentMeeting[:])
  return flattened
    

def getMatchingAvailabilities(calendar, meetingDuration):
  matchingAvailabilities = []
  for i in range(1, len(calendar)):
    start = calendar[i - 1][1]
    end = calendar[i][0]
    availabilityDuration = end - start
    if availabilityDuration >= meetingDuration:
      matchingAvailabilities.append([start, end])
  return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], matchingAvailabilities))        


def timeToMinutes(time):
  hours, minutes = list(map(int, time.split(":")))  
  return hours * 60 + minutes


def minutesToTime(minutes):
  hours = minutes // 60
  mins = minutes % 60
  hoursString = str(hours)
  minutesString = "0" + str(mins) if mins < 10 else str(mins)
  return hoursString + ":" + minutesString
