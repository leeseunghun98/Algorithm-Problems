import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
pos = [0 for _ in range(n+1)]
for i in range(n):
    pos[inorder[i]] = i

def make_tree(inorder_start, inorder_finish, post_start, post_finish):
    if inorder_start > inorder_finish or post_start > post_finish:
        return
    root = postorder[post_finish]
    middle_tree_nodes = pos[root]
    print(root, end=" ")
    make_tree(inorder_start, middle_tree_nodes-1, post_start, post_start + 
    middle_tree_nodes - 1 - inorder_start)
    make_tree(middle_tree_nodes+1, inorder_finish, post_finish - inorder_finish + 
    middle_tree_nodes, post_finish-1)

make_tree(0, n-1, 0, n-1)
















# # index로 바꾸기
# def make_tree(inorder, postorder):
#     root = postorder[-1]
#     middle_tree_nodes = inorder.index(root)
#     print(root, end=" ")
#     if middle_tree_nodes >= 1:
#         make_tree(inorder[:middle_tree_nodes], postorder[:middle_tree_nodes])
#     if middle_tree_nodes < len(inorder)-1:
#         make_tree(inorder[middle_tree_nodes+1:], postorder[middle_tree_nodes:-1])

# make_tree(inorder, postorder)
