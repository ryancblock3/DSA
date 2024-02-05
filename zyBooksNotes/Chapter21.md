# Algorithms

## Huffman Compression

Compression - Transforms data to use fewer bits.

Huffman Coding - Common compression technique that assigns fewer bits to frequent items using a binary tree.

## Heuristics

Heuristic - Technique that willingly accepts a non-optimal or less accurate solution in order to improve execution speed

Heuristic Algorithm - Algo that quickly determines a near optimal or appoximate solution.

Self-Adjusting Heuristic - an algo that modifies a data structure based on how that data structure is used.

## Python: Heuistics

from operator import attrgetter

class Item:
    def __init__(self, item_weight, item_value):
        self.weight = item_weight
        self.value = item_value
        

class Knapsack:
    def __init__(self, weight, items):
        self.max_weight = weight
        self.item_list = items


def knapsack_01(knapsack, item_list):
    # Sort the items in descending order based on value
    item_list.sort(key = attrgetter('value'), reverse = True)

    remaining = knapsack.max_weight
    for item in item_list:
        if item.weight <= remaining:
            knapsack.item_list.append(item)
            remaining = remaining - item.weight


# Main program
item_1 = Item(6, 25)
item_2 = Item(8, 42)
item_3 = Item(12, 60)
item_4 = Item(18, 95)
item_list = [item_1, item_2, item_3, item_4]
initial_knapsack_list = []

max_weight = int(input('Enter maximum weight the knapsack can hold: '))

knapsack = Knapsack(max_weight, initial_knapsack_list)
knapsack_01(knapsack, item_list)

print ('Objects in knapsack')
i = 1
sum_weight = 0
sum_value = 0

for item in knapsack.item_list:
    sum_weight += item.weight
    sum_value += item.value
    print ('%d: weight %d, value %d' % (i, item.weight,item.value))
    i += 1
print()

print('Total weight of items in knapsack: %d' % sum_weight)
print('Total value of items in knapsack: %d' % sum_value)

## Greedy Algorithms

Greedy Algorithm - A Algo that when presented with a list of options chooses the option that is optimal at that point in time.

Activity Selection Problem - A problem where 1 or more activites are available, each with a start and finish time, and the goal is to build the largest possible set of activites without time conflics. Example - Fit as many activites as possible into a vacation

## Dynamic Programming

Dynamic Programming - A problem solving technique that splits a problem into smaller subproblems, computes and stores solutions to subproblems in memoery and then uses the stored solutions to solve the larger problem.