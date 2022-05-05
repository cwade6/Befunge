# Befunge
In this repository the Befunge file is my python befunge interpreter and my code. Befunge is a 2-dimetional esotric programing langguage. The rules my language follow are below. 
+	   Addition: Pop two values a and b, then push the result of a+b
-	   Subtraction: Pop two values a and b, then push the result of b-a
*	   Multiplication: Pop two values a and b, then push the result of a*b
/	   Integer division: Pop two values a and b, then push the result of b/a, rounded down. According to the specifications, if a is zero, ask the user what result            they want.
%	   Modulo: Pop two values a and b, then push the remainder of the integer division of b/a.
!	   Logical NOT: Pop a value. If the value is zero, push 1; otherwise, push zero.
`	   Greater than: Pop two values a and b, then push 1 if b>a, otherwise zero.
>	   PC direction right
<	   PC direction left
^	   PC direction up
v	   PC direction down
?	   Random PC direction
_	   Horizontal IF: pop a value; set direction to right if value=0, set to left otherwise
|	   Vertical IF: pop a value; set direction to down if value=0, set to up otherwise
\"	 Toggle stringmode (push each character's ASCII value all the way up to the next ")
:	   Duplicate top stack value
\	   Swap top stack values
$	   Pop top of stack and discard
.	   Pop top of stack and output as integer
,	   Pop top of stack and output as ASCII character
#	   Bridge: jump over next command in the current direction of the current PC
&	   Get integer from user and push it
~	   Get character from user and push it
@	   End program
0 – 9	 Push corresponding number onto the stack

The arrow keys are the parts of the program that picks the driection they run as it can run in multiple directions.
You can run this program in the command line by running benfunge(program) with program being a doc string program or the variable name of a program. For example befunge(""" "!dlroW ,olleH">:v
                |,<
                @  """) works or program = """ "!dlroW ,olleH">:v
                |,<
                @  """    befunge(program) works
Sample programs can be found in the file tiltled sample programs. The docstrings are written so you can copy paste them to run on the command line.
