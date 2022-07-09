# polynom_solver
Python script to get all roots of given polynom numerically

# Explaination
The basic idea is that all the roots of a polynomial lie between the roots of its derivative.<br>
Suppose we have a function f(x) = ax^n + bx^n-1 + ... + tx + c <br>
Then, finding all the roots of f'(x) (suppose i's {r1, r2, ..., r(n-1)}) we can split all rational numbers into n segments:<br>
[-∞; r1], [r1, r2], ..., [r(n-1), +∞] <br>
There should be at most 1 root of f(x) on each of these segments, so if f(ri) and f(r(i+1)) have different signs, on [ri, r(i+1)] there must be one root, otherwise there are no roots on this segment. Using binary search, we can find this root with any accuracy. <br>
<hr>
So, using this method, to find the roots of f(x) = ax^n + bx^n-1 + ... + tx + c, we should firstly find the roots of f'(x). And, to find the roots of f'(x), we can find the roots of f''(x). And to find the roots of f''(x), we can find the roots of f(3)(x)... Lowering the degree of the polynomial, we get f(n-1)(x) = Ax + B, the roots of which can be easily found.
<hr>
To mention, instead of -∞ and ∞ we will find such numbers B and T s.t. f(x) don't have any roots less than B and greater than T.

# Example
Let's have a look at this simple example: <br>
![image](https://user-images.githubusercontent.com/99137907/178109096-8c67eac4-b440-4273-a106-353637a54f23.png) <br>
As you can see, roots x1, x2, x3 of f(x) are separated by r1 and r2 - roots of f'(x), and, r1 and r2 lie on different sides relative to t1 - root of the f''(x).<br>
Program output:<br>
![image](https://user-images.githubusercontent.com/99137907/178110410-fedb616b-907a-43e2-8942-6a8ed4848f48.png)
