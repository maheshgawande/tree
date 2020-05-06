# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:25:53 2020

@author: mahesh
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Binary_tree:
    def __init__(self):
        self.root = None


    def insert(self, data):
        new_node = Node(data)
        insert_status = False
        if self.root is None:
            self.root = new_node
            insert_status = True
        else:
            cur_node = self.root
            q = []
            q.append(cur_node)
            while len(q) != 0:
                temp = q.pop(0)
                if temp.data == data:
                    break

                if temp.left is None:
                    temp.left = new_node
                    insert_status = True
                    break
                else:
                    q.append(temp.left)
                
                if temp.right is None:
                    temp.right = new_node
                    insert_status = True
                    break
                else:
                    q.append(temp.right)

        return insert_status


    def del_deepest(self, d_node):
        root = self.root
        q = []
        q.append(root)
        while len(q) != 0:
            temp = q.pop(0)
            if temp == d_node:
                temp = None
                return

            if temp.right is not None:
                if temp.right == d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)

            if temp.left is not None:
                if temp.left == d_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)


    def delete(self, key):
        if self.root is None:
            return

        del_status = False
        root = self.root
        if root.left is None and root.right is None:
            if root.data == key:
                root = self.root = None
                del_status = True
        else:
            temp = None
            key_node = None
            q = []
            q.append(root)
            while len(q) != 0:
                temp = q.pop(0)

                if temp.data == key:
                    key_node = temp
                    break

                if temp.left is not None:
                    q.append(temp.left)

                if temp.right is not None:
                    q.append(temp.right)

            if key_node:
                x = temp.data
                self.del_deepest(temp)
                key_node.data = x
                del_status = True

        return del_status


    def display(self):
        if self.root is None:
            print('Tree is empty.')
            return

        root = self.root
        tl = []
        q = []
        q.append(root)
        while len(q) != 0:
            temp = q.pop(0)
            tl.append(temp.data)
            if temp.left is not None:
                q.append(temp.left)

            if temp.right is not None:
                q.append(temp.right)

        print(tl)


    def count(self):
        count = 0
        root = self.root
        q = []
        q.append(root)
        while len(q) != 0:
            temp = q.pop(0)
            count += 1
            if temp.left is not None:
                q.append(temp.left)

            if temp.right is not None:
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


if __name__ == "__main__":
    def not_num():
        print('\nOnly numbers are allowed.\n')

    bt = Binary_tree()
    while True:
        try:
            choice = int(input('''1. Insert into tree
2. Display tree
3. Delete from tree
4. Height of tree and count of nodes
5. Exit
Enter your choose: '''))
        except ValueError:
            not_num()
        else:
            if choice == 1:
                print('\n----------------------------------------')
                try:
                    data = input('Enter data to be inserted in tree: ')
                except ValueError:
                    not_num()
                else:
                    data_inserted = bt.insert(data)
                    if data_inserted:
                        bt.display()
                    else:
                        print('Duplicate entries not allowed.')

                print('----------------------------------------\n')
            elif choice == 2:
                print('\n----------------------------------------')
                bt.display()
                print('----------------------------------------\n')
            elif choice == 3:
                print('\n----------------------------------------')
                bt.display()
                try:
                    data = input('Enter data to be deleted: ')
                except ValueError:
                    not_num()
                else:
                    data_deleted = bt.delete(data)
                    if data_deleted:
                        bt.display()
                    else:
                        print(f'{data} is not in the tree.')

                print('----------------------------------------\n')
            elif choice == 4:
                print('\n----------------------------------------')
                print(f'Height of tree: {bt.height()}')
                print(f'Nodes in tree: {bt.count()}')
                print('----------------------------------------\n')
            elif choice == 5:
                break
            else:
                print('Wrong choice. Try again.')