Lockers
--------

This script verifies the Lockers Puzzle:

A janitor is standing before a row of 100 lockers. He starts by opening
the lockers. Then staring at the 2nd locker, he closes 2, 4, 6, ..., 100.
On the 3rd pass he toggles (opens if closes; closes if opens) the
lockers which are multiples of 3. He repeats this until he has made 100
passes, toggling the lockers which are the multiples of n in the nth pass.
When he finishes the 100th pass which lockers are open?

Ans: The pderfect squares.

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

Bit Lockers
------------

The above solution is wasteful of space. We only need 1 bit per locker because 
it's either open or closed. We see this clearly in the toggle operation which
uses the bit-wise ^ with 1 to open or close the locker.  By using a list we
are forcing python to use more bits of storage for each locker.  In python, 
each integer values is an object of class int. You can use sys.getsizeof()
on to get the number of bytes for storage (ref: https://stackoverflow.com/questions/17574076/what-is-the-difference-between-len-and-sys-getsizeof-methods-in-python)

For my machine, this is 24 bytes at least for numbers through 100.  This means
we are using at least 2400 bytes to store the state of the locker.

A better way to do this is to use 100 bits directly. This version of the 
problem is in bit_lockers.py which uses a 100 bit int value to store the locker states. 
This uses python's ability to create arbitraily large values ince 2^128 is rather huge. 
Still it's only using 40 bytes of storage so we are still way ahead of the game. 
This value uses the ^ bit operator to toggle the loccker state as before, and it 
uses the & bit operator to determine the state of a locker. Finally, it uses the << 
bit shift operator to produce mask values which can operate on a given locker.
While some languages may work directly on memory and use the CPU's shift
operation, << in python continues to oeprate on the built in int class.
However, the biggest mask created is 1 << 99, and this is still only
40 bytes. 

For languages that don't have int objects, you would need to continue
using lists of storage blocks that you can use. This is shown in 
bit_lockers2.py which uses a list of 4 32 bit integers. Using integer divide
and modulo you can figure out which list item stores each locker, and 
what offset from 0 to 31 has to be used to access it. In this case, we are
now using 4 24 byte integer values for storage, plus 24 bytes each time
a flag is used.  
