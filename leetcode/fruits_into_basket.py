from typing import *
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        basket_1, basket_2 = [], []
        fruit_type_1, fruit_type_2 = -1, -1
        max_fruits, len_trees = 0, len(tree)
        i = 0
        while(i < len_trees):
            fruits = 0
            fruit_type_1 = tree[i]
            if not basket_1:
                basket_1.append(fruit_type_1)
                fruits += 1
            stop = False
            j = i + 1
            while ( not stop and j < len_trees):
                if (tree[j] == fruit_type_1):
                    basket_1.append(tree[j])
                    fruits += 1
                    j += 1
                    continue
                if not basket_2:
                    fruit_type_2 = tree[j]
                    fruit_2_index = j
                if (tree[j] == fruit_type_2):
                    basket_2.append(tree[j])
                    fruits += 1
                    j += 1
                else:
                    stop = True
            if (fruits > max_fruits):
                max_fruits = fruits
            if (j >= len_trees):
                return max_fruits
            basket_1, basket_2 = [], []
            fruit_type_1, fruit_type_2 = -1, -1
            i = fruit_2_index
            fruit_2_index = len_trees + 1
        return max_fruits