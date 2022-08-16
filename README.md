# Grade_Calc
Given a desired GPA, grade range (for example: A+ -> B), and the number of courses, calculates every possible arrangement of (A's, B's and/or C's) for achieving that GPA. 

Columbia's GPA system weights as the following:

A+ : 4.33

A  : 4.00

A- : 3.67

B+ : 3.33

B  : 3.00

B- : 2.67

C+ : 2.33

C  : 2.00


User prompted to input (program constraints):

1) Number of Courses, for example 31
2) Desired GPA, say 3.7
3) GPA Variability, go with 0.5% (means GPA range for calculation is now 3.6815 -> 3.7185)
4) Highest Grade Earned, try "A+"
5) Lowest Grade Earned , take "B"

Program can then generate all possibilities for achieivng that GPA, given the contraints, and outputs results to a txt file.

Structure of each, follows: [GPA, [# of A+'s, # of A's, # of A-'s, # of B+'s, # of B's]] for example [3.69, [0, 3, 28, 0, 0]]

Student earned GPA of 3.69
from...

0, A+ grades

3, A grades

28, A- grades

0, B+ grades

0, B- grades


Here is the full list of possibilties provided the contraints above:

[fille.txt](https://github.com/shaylchetty/Grade_Calc/files/9201104/fille.txt)


https://user-images.githubusercontent.com/102982612/181311630-02462d4f-db42-4955-95b6-c3cb329f9d6c.mov



The program can also print a neater version of the output to the console (though I personally prefer the txt!):


https://user-images.githubusercontent.com/102982612/181306163-02327287-1aeb-4800-9a3c-39f0d3a95d76.mov


This project was programmed over the summer as a personal project. 

Because it was relatively computationally heavy, it provided me with a genuine understanding of computaional complexity and the importance of making programs that run efficiently.
