[problem](https://cses.fi/problemset/task/1620)

This is a common stack algorithm where we maintain an increasing stack.

What's increasing stack.

    The elements in stack are stored in increasing order.(big numbers on top)

    and any new number that comes will pop all values greater than it.

Why we need increasing stack here?
    
    First property of increasing stack is numbers on top are the right most numbers (as expected in question)

    Plus for current number in array we want a number just smaller than itself which we can get popping elements from stack until a number smaller than our current number appears on top of our stack.

NOTE: here in stack we are maintaining index values instead of actual values since in output they expect position of number instead of actual number.