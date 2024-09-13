# Build Failures

# [Difficulty:_Hard]
# [Category:_Searching]

  Engineering teams at big tech companies often have systems in place that
  continuously test their latest code builds.

  If all tests pass, the latest build is usually said to be green; if some tests
  fail, the latest build is typically said to be broken.

  If a build is broken, it means that until someone fixes the underlying issue
  (a faulty test case or buggy code), any engineer working off of the latest
  code in the repository will be working on a broken build with failing tests.

  Naturally, engineering teams care about how quickly broken builds get fixed,
  so they'll sometimes track how much time goes by with a broken build.

  We'll call a "build run" a set of consecutive hours during which the latest
  build is green, then becomes broken, until it goes back to green; a build run
  will be represented by a list of booleans--specifically a list of `true`s 
  followed by `false`s. For example, the build run `[true, true, true, false, false]` 
  means that for three hours, the latest build was green, and then for two hours, it was broken. After those last two hours, the build got fixed, and a new build run was started.

  One meaningful value that engineering teams sometimes care about is the "green
  percentage" of a build run: the percentage of time that a build run is green.
  For example, the green percentage of the example build run above is 60%, since
  the build was green for three hours out of the five consecutive hours of the
  build run.

  Write a function that takes in a non-empty list of build runs and returns the
  greatest number of consecutive build runs with strictly decreasing green
  percentages. This will indicate the period of time when our engineers were
  increasingly the slowest to fix broken builds.

  If there are no two consecutive build runs with strictly decreasing green
  percentages, your function should return `-1`.

  Note that, by definition, each build run `must` start with at
  least one or more `true`s followed by at least one or more `false`s; `true`s and 
  `false`s will never be alternating within a single build run.

# [Sample_Input]

  buildRuns = [
    [true, true, true, false, false],
    [true, true, true, true, false],
    [true, true, true, true, true, true, false, false, false],
    [true, false, false, false, false, false],
    [true, true, true, true, true, true, true, true, true, true, true, true, false],
    [true, false],
    [true, true, true, true, false, false],
  ]

# [Sample_Output]

  3
  // The second build run has a green percentage of 80%.
  // The third build run has a green percentage of ~66.66%.
  // The fourth build run has a green percentage of ~16.66%.
  // This is the greatest number of consecutive build runs
  // with a strictly decreasing green percentage.

# Hints

# [Hint_1]

  Try mapping each build run to its green percentage. Once you have a list of green percentages, you can find the longest strictly-decreasing sublist.

# [Hint_2]

  You can use binary search to optimally find the first false in each build run and to optimally calculate each build run's green percentage.

# [Optimal_Space_&_Time_Complexity]

  O(nlog(m)) time | O(1) space - where n is the number of build runs and m is the length of the longest build run
