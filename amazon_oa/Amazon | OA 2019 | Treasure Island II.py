#Problem Statement
Amazon | OA 2019 | Treasure Island II

You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in. There are other explorers trying to find the treasure. 
So you must figure out a shortest route to one of the treasure islands.
Assume the map area is a two dimensional grid, represented by a matrix of characters.
You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. 
The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. 
You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. 
Output the minimum number of steps to get to any of the treasure islands.

Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
def treasure_island(map):
    #TODO

def test_driver(input,result):
    print(input)
    ret = treasure_island(input)
    print("expected:58", "result:", ret)
    assert ret == result
input = [['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]
test_driver(input,3)
