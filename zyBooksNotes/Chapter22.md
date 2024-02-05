# B-Trees

## B-Trees

B-Tree - A tree with order K is a tree where nodes can have up to K-1 keys and up to K children

Order - Maximium number of children a node can have

B Tree Properties
1. All keys in a B-tree must be distinct.
2. All leaf nodes must be at the same level.
3. An internal node with N keys must have N+1 children.
4. Keys in a node are stored in sorted order from smallest to largest.
5. Each key in a B-tree internal node has one left subtree and one right subtree. All left subtree keys are < that key, and all right subtree keys are > that key.

2-3-4 Trees - Order of 4 B-Tree

## 2-3-4 Tree Search Algorithm

BTreeSearch(node, key) {
   if (node is not null) {
      if (node has key) {
         return node
      }
      if (key < node⇢A) {
         return BTreeSearch(node⇢left, key)
      }
      else if (node⇢B is null || key < node⇢B) {
         return BTreeSearch(node⇢middle1, key)
      }
      else if (node⇢C is null || key < node⇢C) {
         return BTreeSearch(node⇢middle2, key)
      }
      else {
         return BTreeSearch(node⇢right, key)
      }
   }
   return null
}

## 2-3-4 Tree Insert Algorithm

BTreeSplit(tree, node, nodeParent) {
   if (node is not full) {
      return null
   }

   splitLeft = new BTreeNode(node⇢A, node⇢left, node⇢middle1)
   splitRight = new BTreeNode(node⇢C, node⇢middle2, node⇢right)
   if (nodeParent is not null) {
      BTreeInsertKeyWithChildren(nodeParent, node⇢B, splitLeft, splitRight)
   }
   else {
      nodeParent = new BTreeNode(node⇢B, splitLeft, splitRight)
      tree⇢root = nodeParent
   }
   return nodeParent
}

BTreeInsertKeyWithChildren(parent, key, leftChild, rightChild) {
   if (key < parent⇢A) {
      parent⇢C = parent⇢B
      parent⇢B = parent⇢A
      parent⇢A = key
      parent⇢right = parent⇢middle2
      parent⇢middle2 = parent⇢middle1
      parent⇢middle1 = rightChild
      parent⇢left = leftChild
   }
   else if (parent⇢B is null || key < parent⇢B) {
      parent⇢C = parent⇢B
      parent⇢B = key
      parent⇢right = parent⇢middle2
      parent⇢middle2 = rightChild
      parent⇢middle1 = leftChild
   }
   else {
      parent⇢C = key
      parent⇢right = rightChild
      parent⇢middle2 = leftChild
   }
}

BTreeInsert(node, key) {
   if (key is in node) {
      return null // duplicates not allowed
   }
   if (node is full) {
      node = BTreeSplit(tree, node, nodeParent)
   }
   if (node is not leaf) {
      if (key < node⇢A)
         return BTreeInsert(node⇢left, key)
      else if (node⇢B is null || key < node⇢B)
         return BTreeInsert(node⇢middle1, key)
      else if (node⇢C is null || key < node⇢C)
         return BTreeInsert(node⇢middle2, key)
      else
         return BTreeInsert(node⇢right, key)
   }
   else {
      BTreeInsertIntoLeaf(node, key)
      return node
   }
}

## 2-3-4 Tree Rotations and Fusion

Rotation - a rearrangement of keys between 3 nodes that maintains all 2-3-4 tree properties in the process

Right Rotation on a node causes the node to lose one key and the node's right sibling to gain one key

Left Rotation on a node causes the node to lose one key and the node's left sibling to gain one key

## 2-3-4 Tree Removal

BTreeRemove(tree, key) {
   if (tree⇢root is leaf with 1 key &&
      tree⇢root⇢A == key) {
      tree⇢root = null
      return true
   }
 
   cur = tree⇢root
   while (cur != null) {
      if (cur has 1 key and cur != tree⇢root) {
         cur = BTreeMerge(cur)
      }
      keyIndex = BTreeGetKeyIndex(cur, key)
      if (keyIndex != -1) {
         if (cur is leaf) {
            BTreeRemoveKey(cur, keyIndex)
            return true
         }
         tmpChild = BTreeGetChild(cur, keyIndex + 1)
         tmpKey = BTreeGetMinKey(tmpChild)
         BTreeRemove(tree, tmpKey)
         BTreeKeySwap(tree⇢root, key, tmpKey)
         return true
      }
         
      cur = BTreeNextNode(cur, key)
   }
   return false
}

## Python: 2-3-4 Trees

# Node234 class - represents a node in a 2-3-4 tree
class Node234:
    def __init__(self, key_A, left_child = None, middle1_child = None):
        self.A = key_A
        self.B = None
        self.C = None
        self.left = left_child
        self.middle1 = middle1_child
        self.middle2 = None
        self.right = None
    
    # Returns the left, middle1, middle2, or right child if the child_index
    # argument is 0, 1, 2, or 3, respectively.
    # Returns None if the child_index argument is < 0 or > 3.
    def get_child(self, child_index):
        if child_index == 0:
            return self.left
        elif child_index == 1:
            return self.middle1
        elif child_index == 2:
            return self.middle2
        elif child_index == 3:
            return self.right
        return None

    # Returns 0, 1, 2, or 3 if the child argument is this node's left,
    # middle1, middle2, or right child, respectively.
    # Returns -1 if the child argument is not a child of this node.
    def get_child_index(self, child):
        if child is self.left:
            return 0
        elif child is self.middle1:
            return 1
        elif child is self.middle2:
            return 2
        elif child is self.right:
            return 3
        return -1

    # Returns this node's A, B, or C key, if the key_index argument is
    # 0, 1, or 2, respectively.
    # Returns None if the key_index argument is < 0 or > 2.
    def get_key(self, key_index):
        if key_index == 0:
            return self.A
        elif key_index == 1:
            return self.B
        elif key_index == 2:
            return self.C
        return None

    # Returns 0, 1, or 2, if the key argument is this node's A, B, or
    # C child, respectively.
    # Returns -1 if the key argument is not a key of this node.
    def get_key_index(self, key):
        if key == self.A:
            return 0
        elif key == self.B:
            return 1
        elif key == self.C:
            return 2
        return -13

class Node234:
    # Appends 1 key and 1 child to this node.
    # Preconditions:
    # 1. This node has 1 or 2 keys
    # 2. key > all keys in this node
    # 3. Child subtree contains only keys > key
    def append_key_and_child(self, key, child):
        if self.B == None:
            self.B = key
            self.middle2 = child
        else:
            self.C = key
            self.right = child
    
    # Returns the number of keys in this node, which will be 1, 2, or 3.
    def count_keys(self):
        if self.C != None:
            return 3
        elif self.B != None:
            return 2
        return 1

    # Returns True if this node has the specified key, False otherwise.
    def has_key(self, key):
        return self.A == key or self.B == key or self.C == key

    # Inserts a new key into the proper location in this node.
    # Precondition: This node is a leaf and has 2 or fewer keys
    def insert_key(self, key):
        if key < self.A:
            self.C = self.B
            self.B = self.A
            self.A = key
        elif self.B == None or key < self.B:
            self.C = self.B
            self.B = key
        else:
            self.C = key

    # Inserts a new key into the proper location in this node, and
    # sets the children on either side of the inserted key.
    # Precondition: This node has 2 or fewer keys
    def insert_key_with_children(self, key, leftChild, rightChild):
        if key < self.A:
            self.C = self.B
            self.B = self.A
            self.A = key
            self.right = self.middle2
            self.middle2 = self.middle1
            self.middle1 = rightChild
            self.left = leftChild
        elif self.B == None or key < self.B:
            self.C = self.B
            self.B = key
            self.right = self.middle2
            self.middle2 = rightChild
            self.middle1 = leftChild
        else:
            self.C = key
            self.right = rightChild
            self.middle2 = leftChild

    # Returns True if this node is a leaf, False otherwise.
    def is_leaf(self):
        return self.left == None

    # Returns the child of this node that would be visited next in the
    # traversal to search for the specified key
    def next_node(self, key):
        if key < self.A:
            return self.left
        elif self.B == None or key < self.B:
            return self.middle1
        elif self.C == None or key < self.C:
            return self.middle2
        return self.right

    # Removes key A, B, or C from this node, if key_index is 0, 1, or 2,
    # respectively. Other keys and children are shifted as necessary.
    def remove_key(self, key_index):
        if key_index == 0:
            self.A = self.B
            self.B = self.C
            self.C = None
            self.left = self.middle1
            self.middle1 = self.middle2
            self.middle2 = self.right
            self.right = None
        elif key_index == 1:
            self.B = self.C
            self.C = None
            self.middle2 = self.right
            self.right = None
        elif key_index == 2:
            self.C = None
            self.right = None

    # Removes and returns the rightmost child. Two possible cases exist:
    # 1. If this node has a right child, right is set to None, and the
    #    previous right value is returned.
    # 2. Else if this node has a middle2 child, middle2 is set to None, and
    #    the previous right value is returned.
    # 3. Otherwise no action is taken, and None is returned.
    # No keys are changed in any case.
    def remove_rightmost_child(self):
        removed = None
        if self.right != None:
            removed = self.right
            self.right = None
        elif self.middle2 != None:
            removed = self.middle2
            self.middle2 = None
        return removed

    # Removes and returns the rightmost key. Three possible cases exist:
    # 1. If this node has 3 keys, C is set to None and the previous C value is returned.
    # 2. If this node has 2 keys, B is set to None and the previous B value is returned.
    # 3. Otherwise no action is taken and None is returned.
    # No children are changed in any case.
    def remove_rightmost_key(self):
        removed = None
        if self.C != None:
            removed = self.C
            self.C = None
        elif self.B != None:
            removed = self.B
            self.B = None
        return removed

    # Sets the left, middle1, middle2, or right child if the child_index
    # argument is 0, 1, 2, or 3, respectively.
    # Does nothing if the child_index argument is < 0 or > 3.
    def set_child(self, child, child_index):
        if child_index == 0:
            self.left = child
        elif child_index == 1:
            self.middle1 = child
        elif child_index == 2:
            self.middle2 = child
        elif child_index == 3:
            self.right = child

    # Sets this node's A, B, or C key if the key_index argument is 0, 1, or
    # 2, respectively.
    # Does nothing if the key_index argument is < 0 or > 2.
    def set_key(self, key, key_index):
        if key_index == 0:
            self.A = key
        elif key_index == 1:
            self.B = key
        elif key_index == 2:
            self.C = key

class Tree234:
    # Initializes the tree with the root node reference set to None.
    def __init__(self):
        self.root = None

    # Inserts a new key into this tree, provided the tree doesn't already
    # contain the same key.
    def insert(self, key, node = None, node_parent = None):
        # Special case for empty tree
        if self.root == None:
            self.root = Node234(key)
            return self.root

        # If the node argument is null, recursively call with root
        if node == None:
            return self.insert(key, self.root, None)

        # Check for duplicate key
        if node.has_key(key):
            # Duplicate keys are not allowed
            return None

        # Preemptively split full nodes
        if node.C != None:
            node = self.split(node, node_parent)

        if not node.is_leaf():
            if key < node.A:
                return self.insert(key, node.left, node)
            elif node.B == None or key < node.B:
                return self.insert(key, node.middle1, node)
            elif node.C == None or key < node.C:
                return self.insert(key, node.middle2, node)
            else:
                return self.insert(key, node.right, node)
        
        # key can be inserted into leaf node
        node.insert_key(key)
        return node

    # Searches this tree for the specified key. If found, the node containing
    # the key is returned. Otherwise None is returned.
    def search(self, key):
        return self.search_recursive(key, self.root)

    # Recursive helper method for search.
    def search_recursive(self, key, node):
        if node == None:
            return None
            
        # Check if the node contains the key
        if node.has_key(key):
            return node
        
        # Recursively search the appropriate subtree
        if key < node.A:
            return self.search_recursive(key, node.left)
        elif node.B == None or key < node.B:
            return self.search_recursive(key, node.middle1)
        elif node.C == None or key < node.C:
            return self.search_recursive(key, node.middle2)
        return self.search_recursive(key, node.right)

    # Splits a full node, moving the middle key up into the parent node.
    def split(self, node, node_parent):
        split_left = Node234(node.A, node.left, node.middle1)
        split_right = Node234(node.C, node.middle2, node.right)
        if node_parent is not None:
            node_parent.insert_key_with_children(node.B, split_left, split_right)
        else:
            # Split root
            node_parent = Node234(node.B, split_left, split_right)
            self.root = node_parent
        
        return node_parent

class Tree234:
    # Initializes the tree with the root node reference set to None.
    def __init__(self):
        self.root = None

    # Inserts a new key into this tree, provided the tree doesn't already
    # contain the same key.
    def insert(self, key, node = None, node_parent = None):
        # Special case for empty tree
        if self.root == None:
            self.root = Node234(key)
            return self.root

        # If the node argument is null, recursively call with root
        if node == None:
            return self.insert(key, self.root, None)

        # Check for duplicate key
        if node.has_key(key):
            # Duplicate keys are not allowed
            return None

        # Preemptively split full nodes
        if node.C != None:
            node = self.split(node, node_parent)

        if not node.is_leaf():
            if key < node.A:
                return self.insert(key, node.left, node)
            elif node.B == None or key < node.B:
                return self.insert(key, node.middle1, node)
            elif node.C == None or key < node.C:
                return self.insert(key, node.middle2, node)
            else:
                return self.insert(key, node.right, node)
        
        # key can be inserted into leaf node
        node.insert_key(key)
        return node

    # Searches this tree for the specified key. If found, the node containing
    # the key is returned. Otherwise None is returned.
    def search(self, key):
        return self.search_recursive(key, self.root)

    # Recursive helper method for search.
    def search_recursive(self, key, node):
        if node == None:
            return None
            
        # Check if the node contains the key
        if node.has_key(key):
            return node
        
        # Recursively search the appropriate subtree
        if key < node.A:
            return self.search_recursive(key, node.left)
        elif node.B == None or key < node.B:
            return self.search_recursive(key, node.middle1)
        elif node.C == None or key < node.C:
            return self.search_recursive(key, node.middle2)
        return self.search_recursive(key, node.right)

    # Splits a full node, moving the middle key up into the parent node.
    def split(self, node, node_parent):
        split_left = Node234(node.A, node.left, node.middle1)
        split_right = Node234(node.C, node.middle2, node.right)
        if node_parent is not None:
            node_parent.insert_key_with_children(node.B, split_left, split_right)
        else:
            # Split root
            node_parent = Node234(node.B, split_left, split_right)
            self.root = node_parent
        
        return node_parent