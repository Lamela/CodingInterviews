class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def construct_tree(preorder, inorder):
    """
    根据某二叉树的前序遍历和中序遍历结果，重建二叉树
    该二叉树中不包含重复数字
    """
    # 检查两个数组长度是否相同
    if not isinstance(preorder, list) or not isinstance(inorder, list) \
            or len(preorder) != len(inorder):
        return

    # 检查每个节点的值是否为整数
    for x, y in zip(preorder, inorder):
        if not isinstance(x, int) or not isinstance(y, int):
            return

    # 检查两个序列是否有重复值以及两个序列的集合是否相同
    preorder_set = set(preorder)
    inorder_set = set(inorder)
    if preorder_set != inorder_set or len(preorder) != len(preorder_set) or len(inorder) != len(inorder_set):
        return

    root = construct_tree_recursively(preorder=preorder, inorder=inorder)

    return root


def construct_tree_recursively(preorder, inorder):
    assert set(preorder) == set(inorder)

    if len(preorder) == 0:
        return None

    root_value = preorder[0]
    root = TreeNode(root_value)
    root_index = inorder.index(root_value)

    root.left = construct_tree_recursively(preorder=preorder[1:root_index+1],
                                           inorder=inorder[:root_index])
    root.right = construct_tree_recursively(preorder=preorder[root_index+1:],
                                            inorder=inorder[root_index+1:])

    return root


def print_level(node, position_name):
    if node is None:
        return
    print_level(node.left, "left")
    print_level(node.right, "right")
    print()
    print(position_name, " ", node.value, end=' ')


if __name__ == "__main__":
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    root = construct_tree(preorder=preorder, inorder=inorder)
    print_level(root, "root")