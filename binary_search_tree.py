# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:59:39 2020

@author: mahesh
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class Binary_search_tree:
    def __init__(self):
        self.root = None


    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            cur_node = self.root
            while True:
                if new_node.data > cur_node.data:
                    if cur_node.right == None:
                        cur_node.right = new_node
                        cur_node.right.parent = cur_node
                        print('Data added.')
                        return
                    else:
                        cur_node = cur_node.right
                elif new_node.data < cur_node.data:
                    if cur_node.left == None:
                        cur_node.left = new_node
                        cur_node.left.parent = cur_node
                        print('Data added.')
                        return
                    else:
                        cur_node = cur_node.left
                else:
                    print('Duplicate data not allowed.')
                    return


    def get_min(self, cur_node):
        while cur_node.left != None:
            cur_node = cur_node.left

        return cur_node


    def del_node(self, d_node):
        parent_node = d_node.parent
        if d_node.left == None and d_node.right == None:
            if d_node == self.root:
                self.root = d_node = None
            else:
                if parent_node.left == d_node:
                    parent_node.left = d_node = None
                else:
                    parent_node.right = d_node = None
        elif d_node.left == None:
            if d_node == self.root:
                self.root = d_node.right
                d_node = None
            else:
                if parent_node.left == d_node:
                    parent_node.left = d_node.right
                else:
                    parent_node.right = d_node.right
        elif d_node.right == None:
            if d_node == self.root:
                self.root = d_node.left
                d_node = None
            else:
                if parent_node.left == d_node:
                    parent_node.left = d_node.left
                else:
                    parent_node.right = d_node.left
        else:
            temp = self.get_min(d_node.right)
            d_node.data = temp.data
            self.del_node(temp)


    def delete(self, key):
        if self.root == None:
            print('Tree is empty.')
            return

        del_status = False
        cur_node = self.root
        key_node = None
        ht = self.height()
        while ht != 0:
            if cur_node.data == key:
                key_node = cur_node
                break

            if key > cur_node.data and cur_node.right != None:
                cur_node = cur_node.right
            elif key < cur_node.data and cur_node.left != None:
                cur_node = cur_node.left

            ht -= 1

        if key_node:
            self.del_node(key_node)
            del_status = True

        return del_status


    def display(self):
        if self.root == None:
            print('Tree is empty.')
            return
        
        root = self.root
        tl = []
        q = []
        q.append(root)
        while len(q) != 0:
            temp = q.pop(0)
            tl.append(temp.data)
            if temp.left != None:
                q.append(temp.left)

            if temp.right != None:
                q.append(temp.right)

        print(tl)


    def inorder(self):
        if self.root == None:
            print('Tree is empty')
            return

        self._inorder(self.root)


    def _inorder(self, cur_node):
        if cur_node != None:
            self._inorder(cur_node.left)
            print(cur_node.data, end=' ')
            self._inorder(cur_node.right)


    def preorder(self):
        if self.root == None:
            print('Tree is empty')
            return

        self._preorder(self.root)


    def _preorder(self, cur_node):
        if cur_node != None:
            print(cur_node.data, end=' ')
            self._preorder(cur_node.left)
            self._preorder(cur_node.right)


    def postorder(self):
        if self.root == None:
            print('Tree is empty')
            return

        self._postorder(self.root)


    def _postorder(self, cur_node):
        if cur_node != None:
            self._postorder(cur_node.left)
            self._postorder(cur_node.right)
            print(cur_node.data, end=' ')


    def count(self):
        if self.root == None:
            return
        
        count = 0
        root = self.root
        q = []
        q.append(root)
        while len(q) != 0:
            temp = q.pop(0)
            count += 1
            if temp.left != None:
                q.append(temp.left)

            if temp.right != None:
                q.append(temp.right)

        return count


    def height(self):
        if self.root == None:
            return 0

        return self._height(self.root, 0)


    def _height(self, cur_node, ht):
        if cur_node == None:
            return ht

        left_ht = self._height(cur_node.left, ht+1)
        right_ht = self._height(cur_node.right, ht+1)

        return max(left_ht, right_ht)


if __name__ == '__main__':
    def not_num():
        print('\nOnly numbers are allowed.\n')

    bst = Binary_search_tree()
    while True:
        try:
            choice = int(input('''1. Insert into tree
2. Display tree
3. Delete from tree
4. Height of tree and nodes is tree
5. Exit
Enter your choose: '''))
        except ValueError:
            not_num()
        else:
            if choice == 1:
                print('\n----------------------------------------')
                try:
                    data = int(input('Enter data to be inserted: '))
                except ValueError:
                    not_num()
                else:
                    bst.insert(data)
                    bst.display()

                print('----------------------------------------\n')
            elif choice == 2:
                print('\n----------------------------------------')
                try:
                    traverse = int(input('''1. Inorder
2. preorder
3. postorder
Enter your choose: '''))
                except ValueError:
                    not_num()
                else:
                    if traverse == 1:
                        bst.inorder()
                    elif traverse == 2:
                        bst.preorder()
                    elif traverse == 3:
                        bst.postorder()
                    else:
                        print('Wrong choice.')

                print('\n')

                print('----------------------------------------\n')
            elif choice == 3:
                print('\n----------------------------------------')
                bst.display()
                try:
                    data = int(input('Enter data to be deleted: '))
                except ValueError:
                    not_num()
                else:
                    data_deleted = bst.delete(data)
                    if data_deleted:
                        print('Data deleted.')
                        bst.display()
                    else:
                        print(f'{data} is not in the tree.')

                print('----------------------------------------\n')
            elif choice == 4:
                print('\n----------------------------------------')
                print(f'Height of tree: {bst.height()}')
                print(f'Nodes in tree: {bst.count()}')
                print('----------------------------------------\n')
            elif choice == 5:
                break
            else:
                print('\nWrong choice. Try again.\n')