from typing import List


# This does not work at all,  thought with a good datastructure
# the problem would become trivial it did not, probably makes more
# sense to just use a bunch ifs.

def add1(val):
    return val + 1


def sub1(val):
    return 1


op_map = {
    "up": add1,
    "down": sub1
}


class Solution:
    def candy(self, ratings: List[int]) -> int:
        root = Node(is_root=True)
        for i, rating in enumerate(ratings):
            left_rating, right_rating = self.left(i, ratings), self.right(i, ratings)
            if self.is_bottom(left_rating, rating, right_rating):
                n = root.add_child(rating, "up")
            elif self.is_top(left_rating, rating, right_rating):
                n = root.add_child(rating, "down")
            elif i == 0 and rating > right_rating:
                n = root.add_child(rating, "down")
            else:
                n.add_child(rating)

    @staticmethod
    def is_bottom(left_rating, rating, right_rating):
        return left_rating >= rating <= right_rating

    @staticmethod
    def is_top(left_rating, rating, right_rating):
        return left_rating <= rating >= right_rating

    @staticmethod
    def calc_direction(left_rating, rating, right_rating):
        if rating < right_rating:
            return "up"
        elif rating > right_rating:
            return "down"
        elif left_rating == rating == right_rating:
            return "flat"

    @staticmethod
    def right(i, subset):
        if i == len(subset) - 1:
            return 100_000
        return subset[i + 1]

    @staticmethod
    def left(i, subset):
        if i == 0:
            return 100_000
        return subset[i - 1]


class Node:
    def __init__(self, rating=None, direction=None, is_root=False):
        self.is_root = is_root
        self.nodes = []
        self.rating = rating
        self.direction = direction

    def add_child(self, *args, **kwargs):
        n = Node(*args, **kwargs)
        self.nodes.append(n)
        return n

    def print_struct(self):
        if self.is_root:
            print(f" -- Root --")
        if self.nodes:
            print(" -- ".join([node.__repr__() for node in self.nodes]))
            print(" -- ".join([str(node.nodes) for node in self.nodes]))

    def __repr__(self):
        if self.direction == "down":
            return f"{self.rating} down"
        return f"{self.rating} up"






s = Solution()
s.candy([1,2,87,87,87,2,1])
s = Solution()
s.candy([1,0,2])
