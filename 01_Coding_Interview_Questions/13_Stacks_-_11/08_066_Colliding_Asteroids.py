"""

[ Difficulty: Medium ]
[ Category: Stacks ]

##### Colliding Asteroids #####

You're given an array of integers asteroids, where each integer represents the 
size of an asteroid. The sign of the integer represents the direction the asteroid 
is moving (positive = right, negative = left). All asteroids move at the same 
speed, meaning that two asteroids moving in the same direction can never collide.

For example, the integer 4 represents an asteroid of size 4 moving to the right. 
Similarly, -7 represents an asteroid of size 7 moving to the left.

If two asteroids collide, the smaller asteroid (based on absolute value) explodes. 
If two colliding asteroids are the same size, they both explode.

Write a function that takes in this array of asteroids and returns an array of 
integers representing the asteroids after all collisions occur.


##### Sample Input #####
asteroids = [-3, 5, -8, 6, 7, -4, -7]

##### Sample Output #####
            // The -3 moves left, having no collisions.
            // The 5 moves right, colliding with the -8 and being destroyed by it.
            // The 6 never collides with another asteroid.
            // The 7 first collides with the -4, destroying it.
[-3, -8, 6] // The 7 and the -7 then collide, both being destroyed.    

##### Hints #####

Hint 1
Try approaching this problem one step at a time. What happens if there is only 1 
asteroid? Then what possible scenarios can occur if a second asteroid is added 
after it?

Hint 2
Two asteroids of the same direction will never collide, since all asteroids have 
the same speed.

Hint 3
A stack will be a useful data structure for solving this problem. With each added 
asteroid, pop asteroids off of the top of the stack until the new asteroid is no 
longer colliding with other asteroids before it.

Optimal Space & Time Complexity
O(n) time | O(n) space - where n is the number of asteroids

"""





##### Solution 1 #####
# O(n) time | O(n) space - where n is the number of asteroids
def collidingAsteroids(asteroids):
    resultStack = []
    for asteroid in asteroids:
        if asteroid > 0:
            resultStack.append(asteroid)
            continue

        while True:
            if len(resultStack) == 0 or resultStack[-1] < 0:
                resultStack.append(asteroid)
                break

            asteroidSize = abs(asteroid)
            if resultStack[-1] > asteroidSize:
                break

            if resultStack[-1] == asteroidSize:
                resultStack.pop()
                break

            resultStack.pop()

    return resultStack