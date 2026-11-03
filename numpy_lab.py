# Note: Professor Colburn's lab, copied as is 11/2/26
"""
NumPy Essentials for Working with Engineering Data
==================================================

Engineering data (sensor readings, measurements, simulation output) is often
collected in a Python LIST. Lists are great for collecting values one at a
time, but they cannot do math on every element at once. A NumPy ARRAY can.
That is the whole reason we will use NumPy in upcoming assignments.

The four ideas in this demo:
    1. Convert a list to an array with np.array(...)
    2. Do math on a whole array at once (no loop)
    3. Compare neighboring elements using slices (a[:-1] and a[1:])
    4. Find and count events with np.where(...) and np.cumsum(...)

How to use this file:
    - Run it once and read the printed output next to the code.
    - Answer the "EXPLORE" questions (write answers as comments).
    - Do the "TRY IT" changes and re-run.
    - Finish the exercises at the bottom.
"""

import numpy as np


# ---------------------------------------------------------------------------
# 1. Lists vs. arrays
# ---------------------------------------------------------------------------
print("=== 1. Lists vs. arrays ===")

# Angle readings (radians) of a swinging pendulum, recorded at equal time steps
angles_list = [0.5, 0.3, 0.1, -0.2, -0.4, -0.3, -0.1, 0.2, 0.4]

# Convert once, at the start of a function or section of code
angles = np.array(angles_list)

print("list: ", angles_list)
print("array:", angles)
print("number of elements:", len(angles))

# Whole-array math: every element is multiplied by 2
print("array * 2:", angles * 2)

# The same thing on a list repeats the list instead of doing math
print("list * 2: ", angles_list * 2)

# EXPLORE 1:
#   a) What does angles_list * 2 do? Why is that not what we want for physics?
#   b) What error do you get from angles_list * 0.5? (Try it, then delete it.)
#   c) Does np.array(angles_list) change angles_list?
#   d) Why do we convert once at the start of a function instead of in a loop?


# ---------------------------------------------------------------------------
# 2. Whole-array math (no loops)
# ---------------------------------------------------------------------------
print("\n=== 2. Whole-array math ===")

# np.sin, np.cos, and np.degrees work on every element at once.
# Here we turn pendulum angles into the position of the swinging mass.
length = 1.0  # pendulum length in meters

angles_deg = np.degrees(angles)  # radians -> degrees
x = length * np.sin(angles)      # horizontal position of the bob
y = -length * np.cos(angles)     # vertical position (down is negative)

print("angles (deg):", np.round(angles_deg, 1))
print("x (m):", np.round(x, 3))
print("y (m):", np.round(y, 3))

# TRY IT:
#   a) Change length to 2.0 and re-run. Which arrays change?
#   b) Print the largest absolute angle in degrees: np.max(np.abs(angles_deg))
#   c) Make a time array for 9 samples spaced 0.1 s apart:
#      times = np.arange(9) * 0.1   and print it.


# ---------------------------------------------------------------------------
# 3. Comparing neighbors with slices
# ---------------------------------------------------------------------------
print("\n=== 3. Comparing neighbors ===")

# To detect a CHANGE between one step and the next, line the array up with a
# copy of itself shifted by one:
#     a[:-1] is every element except the last   (the "before" values)
#     a[1:]  is every element except the first  (the "after" values)
before = angles[:-1]
after = angles[1:]

print("before:", before)
print("after: ", after)

# The pendulum crosses equilibrium when the angle changes sign, so
# before * after is negative.
product = before * after
print("product:", np.round(product, 3))

# A comparison on an array gives an array of True/False values
sign_changed = product < 0
print("sign changed:", sign_changed)

# EXPLORE 3:
#   a) How many elements does `before` have compared to `angles`? Why?
#   b) Where are the True values in `sign_changed`, and what do they mean
#      physically?
#   c) Why does before * after go negative only when the sign changes?
#   d) What happens to the product if an angle is exactly 0.0?


# ---------------------------------------------------------------------------
# 4. Finding and counting events
# ---------------------------------------------------------------------------
print("\n=== 4. Finding and counting events ===")


def find_crossings(angles):
    """Return the indices where the angle crosses equilibrium."""
    angles = np.array(angles)
    # np.where(...)[0] gives the POSITIONS where the condition is True.
    # `before` starts at index 0 and `after` starts at index 1, so add 1 to
    # get the index in the full array.
    return np.where(angles[:-1] * angles[1:] < 0)[0] + 1


crossings = find_crossings(angles_list)
print("crossing indices:", crossings)
print("angles just after each crossing:", angles[crossings])

# Running count at every step:
# mark each crossing with a 1, then take a cumulative sum.
flags = np.zeros(len(angles), dtype=int)
flags[crossings] = 1
crossing_count = np.cumsum(flags)
swing_count = crossing_count // 2  # one swing = two crossings

print("crossing count at each step:", crossing_count)
print("swing count at each step:   ", swing_count)

# EXPLORE 4:
#   a) Does np.where(...)[0] return values or positions?
#   b) Why does find_crossings add + 1?
#   c) What does np.cumsum do to the flags array?
#   d) Why is it handy to have the running swing count stored in an array
#      with one value per time step?


# ---------------------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------------------
# Data: a bouncing ball's vertical velocity in m/s (negative while falling,
# positive while rising) and its height in m. A bounce happens when the
# velocity changes from negative to positive.
velocities_list = [0.0, -2.0, -4.0, -6.0, 4.8, 2.8, 0.8, -1.2, -3.2, 2.5, 0.5, -1.5]
heights_list = [2.0, 1.9, 1.5, 0.0, 0.1, 0.5, 0.7, 0.6, 0.2, 0.0, 0.2, 0.1]

# Exercise 1: Convert both lists to arrays named `velocities` and `heights`.
#   Compute speeds = np.abs(velocities) and print the maximum speed (np.max).


# Exercise 2: Convert `heights` from meters to centimeters in one line,
#   with no loop.


# Exercise 3: Write find_impacts(velocities) that returns the indices where
#   the velocity changes from negative (< 0) to positive (> 0).
#   Hint: combine two comparisons with &, with parentheses around each:
#       (before < 0) & (after > 0)
#   Remember the + 1.
def find_impacts(velocities):
    """Return the indices where a floor impact occurred (down to up)."""
    pass


# Exercise 4: Use your find_impacts result to build a `bounce_count` array
#   that gives the number of bounces that have happened at every step.
#   (Use np.zeros, index with the impact indices, then np.cumsum.) Print it.

# Check your answers:
#   find_impacts(velocities_list) should return [4 9]
#   the last value of bounce_count should be 2


# ---------------------------------------------------------------------------
# COMMON MISTAKES
# ---------------------------------------------------------------------------
# - Doing math on a list: list * float raises an error. Convert with
#   np.array(...) first.
# - Forgetting the + 1 after np.where(...), so the indices are off by one.
# - Using `and` instead of `&` to combine array comparisons (`and` fails on
#   arrays), or forgetting the parentheses around each comparison.
# - Mixing degrees and radians: np.sin and np.cos expect radians.
# - Forgetting `import numpy as np` at the top of your file.