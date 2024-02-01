# Recusion

## Recursive Functions

Resursive Function - A function that calls itself.

def count_down(count):
    if count == 0:            
        print('Go!')                  
    else:                        
        print(count)             
        count_down(count-1)        
            
count_down(2)

## Recursive Algorithm: Search

Binary Search - Dividing a dataset in half depending on if value is greater or less than position

## Adding Output Statements for Debugging

Print indentation can be used to help debug a recursive function

## Creating a Recursive Function

Two Steps
    1. Write a Base Case - a case that returns a value without performing a recursive call. 
    2. Write recursive case

Determination for writing recursive functions
    1. Whether the problem has a naturally recursive solution
    2. Whether that solution is better than a non-recursive solution.

## Recursive Math Functions

Depth - a meausre of how many recursive calls of a function have been made but have not yet returned

## Recursive Exploration of all Possibilites

Recursion can be used to explore all possibilites such as possible reorderings of a words letter, all possible subsets of items, all possible paths between cities, etc.