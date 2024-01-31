# Chapter 4 - Branching

## If-else Branches

Branch is a sequence of statements only executed under a certain condition.

If-Else branch has two branches
First branch is executed if expression is true
Else the other branch is executed

Three or more branches can be executed by using If-elseif-else branches

**Code Example**

if x equals -1
     Put "Disagrees" to output
else if x equals 0
     Put "Neutral" to output
else if x equals 1
     Put "Agrees" to output
else
     Put "Invalid entry" to output

## Detecting equal values with branches

Equality operatior = (==)

Inequaluty operator = (!=)

Boolean = True or False

If-else executes one group of statements when an expression is true, and another group when the expression is false.

Multi-branch if-else statements use elif if there are multiple if statements. Each expression is checked in sequence. As soon as one branch's expression is found to be True, that branch executes and no other branch is considered. If no statement is true the else statement is executed.

if

elif

else

## Detecting Ranges with Branches (General)

An if-elseif-else structure can detect number ranges with each branch.

if x < 10 
else if x < 20
else if x < 30
else


## Detecting Ranges with Branches

Relational Operators - Compare operands values to eachother.

< Less than
> Greater Than
<= Less than or equal to
>= Greater than or equal to

Lower branches are only reached if above branches are false.

Operator chaining - a < b < c, read left to right. If a < b is true than b < c is evaluated.

## Detecting ranges using logical operators

Logical operators treat operands as True or False, and evaluates them.

AND - both operands are True

OR - at least one operand is True

NOT - True when one operand is False

Common use of logical operators is to dectect if a value is within a range.

Boolean operators - must be capitalized like True & False

and - both true

or - at least one true

not - at least one false

Can use logical operators to detect ranges. Multi branch if else statements can be used without gaps.

## Detecting Ranges with Gaps

An if-else statement can be used for ranges with gaps.

if age <= 12
elif age >= 65
else

## Detecting Multiple Features with Branches

Independent branches, where eash if-else statement has different meanings

A branch can include any valid statements, including another if-else statement. This is know as nested if-else statements.

if sales_type == 2:
    if sales_bonus < 5: <- Nested if-else
        sales_bonus = 10
    else: <- Nested if-else
        sales_bonus = sales_bonus + 2
else:
    sales_bonus = sales_bonus + 1

## Comparing Data Types and Common Errors

Relational and equality operators work for integer, string, and floating-point, although floating-point should not be used due to imprecise representation of floating-point numbers.

Numbers are arithmetically compared

Strings are compared by converting each character to a numerical value

Lists & Tuples are compared by ordered comparison of every element in the sequence.

Dictionaries are only compared with == and 1=

Common errors-
= instead of == 
=> instead of >=
!> 
<>

## Membership and Identity Operators

in and not in operators are known as membership operators, they yeild a True or False

Membership operators can be used to check if a string is a substring, or matching subset of characters of a larger string. For example 'abc' in '123abcd' returns true.

is and is not are Identity Operators 
x is y is True
x is not y is False

"==" is not the same as an identity operator

## Order of Evaluation

Order of Evaluation
1. ()
2. * / % + -
3. < <= > >= == !=
4. not
5. and
6. or

Common Error is to write an expression that is evaluated in a different order than expected, it is good practice to use parentheses in expression to make the intended order explicit.

## Code Blocks and Indentation

Code block - series of statements grouped together.

Code blocks are defined by indentation level.

DONT mix tabs and spaces.

Acceptable number of columns of text is 80-120 but leans more heavily towards 80 columns.

One tab == 4 spaces

## Conditional Expressions

Conditional expressions have the following form

expr_when_true if condition else expre_when_false

Conditional expressions has three operands and are reffered to as ternary operation.

Common practice is to restrict usage of conditional expressions as it is difficult to read and comprehend.