Lockers
--------

This script verifies the Lockers Puzzle:

A janitor is standing before a row of 100 lockers. He starts by opening
the lockers. Then staring at the 2nd locker, he closes 2, 4, 6, ..., 100.
On the 3rd pass he toggles (opens if closes; closes if opens) the
lockers which are multiples of 3. He repeats this until he has made 100
passes, toggling the lockers which are the multiples of n in the nth pass.
When he finishes the 100th pass which lockers are open?

Ans: The perfect squares.

Why? Consider that on the nth pass, the lockers < n remain in their 
current state. This means 1 will always be open. 2 will also be closed,
as will every prime because they are opened on the first pass, and closed
on their pass. The squares are only touched by 3 passes, so they will be 
open (ie, 25th locker is opened in pass 1, closed in pass 5, and opened
again in pass 25).  For other composite numbers, there are always an
even number of multiples that effect the door. Each pair opens, and then 
closes.

Examples: 42 = 1, 2, 3, 6, 7, 14, 21, and 42
          88 = 1, 2, 4, 8, 11, 22, 44, and 88

So for 88, 1 and 2 open and close. 4 and 8 open and close. 11 and 22 
open and close, and then 44 and 88 open and close.


