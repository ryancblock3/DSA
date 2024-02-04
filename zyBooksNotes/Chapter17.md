# Balanced Trees

## AVL: A Balanaced Tree

AVL Tree  - A BST with a height balalace property and specific operations to rebalance the tree when a node is inserted or removed. 

Height Balanced - for any node the heights of the nodes left and right subtrees differ by only 0 or 1

Balance Factor - Left subtree height minus the right subtree height

Non-existant left or right childs subree height is said to be -1

Minimizing binary tree height yeilds fastest searches, insertions and removals but maintaining min height requires extensive tree rearrangements.

An AVL tree only requires a few local rotations, but does not garuntee a min height.

AVL tree implementation can store the subree height as a member of each node.

## AVL Rotations

Rotation is a local rearrangement of a BST that maintains the BST ordering property while rebalancing the tree

AVLTreeUpdateHeight - updates a nodes height by taking the max of the child subree height and adding 1

AVLTreeSetChild - sets a node as the parents left or right child, updates the child parents pointer, and updates the parent nodes height

AVLTreeReplaceChild - replaces one of a nodes existing child pointers with a new value, utilizing AVLTreeSetChild to perform the replacement

AVLTreeGetBalance - computes a nodes balace factor by subtracting the right subress height from the left subtree height.

## AVL Insertions

Insertions may unbalnce an AVL tree, a rotation can be used to rebalance the AVL Tree

## AVL Removals

Removals remove the first-found matching node, and restructure to preseve all AVL tree requirements.

## Python: AVL Trees

[AVL Tree Python Code](../AVLTree.py)

## Red-Black Tree: A Balanced Tree

Red-Black Tree - A BST with two node types, red and black, and supporting opersations that ensure the tree is balanced when a node is inserted or removed. 

1. Every Node is red or black
2. Root is black
3. The red nodes children cannot be red
4. A null child is considered to be a black leaf node
5. All paths from a node to any null leaf descendant node must have the same number of black nodes.

## Red-Black Tree: Rotations

Rotation - Local rearrangement of a BST that maintains BST ordering while rebalancing the tree. Rotations are used during insert and remove operations to ensure that the red-black tree requirements hold.

## Red-Black Tree: Insertion

## Red-Black Tree: Removal

## Python: Red-Black Trees

