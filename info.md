# GD Challenge

Geometry Dash Challenge:

* Level ID: *TBD*
* Song ID: 508568 (The Falling Mysts // Dimrain47)
* Song Offset: 30.9s
* Background + Ground: 0x000000 (Black)

# Building Process

* Wanted to create a rev/parsing problem
    * Using some game/alternative medium
    * Build a boolean expression
    * Goal:
        * Level is a selector that lets you pick an arbitrary binary string of length `n`
        * There are `m` boolean expressions using up to all `n` variables
        * If the string satisfies all those expressions, the user can beat the level
    * Solution goal:
        * Get GD for free
        * Get to the level
        * Figure out how to copy the level or get the raw data (i.e. using hacks)
        * Play with level to figure out what to do
        * Figure out how the expression is encoded
        * Parse level data to retrieve expression
        * Plug into SAT solver

## Building the Level

Here's the general idea:

* We build a level that asks the contestant to solve some algorithmic problem to find the solution
* The level asks the contestant to make some sequence of inputs as to not die in the end
* The sequence of inputs that lets them survive is encoded some way as the flag
    * In this case, each input toggles one of `n` binary switches, and the state of the switches is the flag

1. Boolean expression component

My initial idea was to use spawn triggers that triggered groups of other spawn triggers (each expression would be made of many spawn trigger groups).  This seemed like

However, it also seemed a bit too basic- representing boolean expressions in an implication-graph like format was really canonical, so I wanted to try something else:

I thought it would be really cool to try using collision blocks, so that was the approach I took to creating this problem.  I thought it would help to represent the 
structure visually, and I eventually ended up on using collision blocks.  This is how:

* Boolean expressions can be represented in the form:

```
(x_1 OR x_2 OR x_3 OR ...) AND
(x_4 OR x_5 OR x_6 OR ...) AND
(x_7 OR x_8 OR x_9 OR ...) AND
(x_10 OR x_11 OR x_12 OR ...) ...
```

* Each expression will be a column of collision blocks, and the variables are rows, with one row reserved for the "off" state and one reserved for the "on" state.

The variables will sweep across horizontally, colliding with 

* When a variable collides with a column, it triggers another collision group to move down (and back up) over a "counter block" which then increments the number of correct expressions

As it turns out, move triggers override each other, creating a true "bitwise OR" effect

* The total number of correct expressions is counted and checked to match the total number to allow the player to pass.

Overall, this method limits us to around `n <= 1000` but `m` can be arbitrarily large in theory.

---

Lastly, some notes:

* Collision blocks take up the full width of the block, and will thus collide if they slide past one another.  This can be fixed by making them smaller
* One collision block must be "dynamic" and one must be "non-dynamic" for them to collide properly using the collision trigger

2. Input Component / Displaying bits

There were a couple of components 

* Setting input

Obviously, we want the contestant to be able to play the level like normal to understand what the actual problem is: 

A simple solution would be to use custom orbs to trigger setting a bit.  However, I thought it would be a bit less visual and intuitive, so I eventually settled with the player 
hitting an H-blocked obstacle which had a touch move trigger on top of it (they would only be a tiny bit above the ground to allow hitting many in a short period of time).  

The move trigger would then set the variable and also the display.

* Displaying input

Obviously, we would need to convey to the user what the input they were entering was and how to translate a "solution" to the level into the flag.  

I also figured that eventually the user would figure out that the blocks do not actually kill them and are functional, but the fact that it wasn't entirely obvious that you were
meant to hit the blocks was a concern.

I initially considered a design where trying to set the value would toggle a "1" text on and a "0" text off.  However, I wanted to conserve groups (since I would need one for each)
collision group/boolean variable and such a design would take two groups per variable.  A better design I came up with was surprisingly low-tech: text for both a 0 and 1 would be
always visible, but obscured by a moving "window" block that would block the 0 or 1 depending on which was set.  This design only took one group and was the best that I could do.
Additionally, this would also allow me to set the actual variable in the expression machine by adding the corresponding collision block to the group as well.

The last addition was purely aesthetic but still greatly important to the contestant: adding `flag{` and `}` to the input display conveys that it's the output format of the solution.

3. Output/Validation Component

All I do is add a count trigger at the very end that checks if the total number of passed expressions is exactly as expected.  If that is true, then the trigger activates a group
which turns off a spike wall.  Simple as that.

## Overall Thoughts

* Very interesting
* Went through some cool chalelnges, learned some cool 2.1 stuff
* Much like ASM/machine code