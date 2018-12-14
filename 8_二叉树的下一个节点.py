class TreeNode(object):
    def __init__(self, value, father=None, left=None, right=None):
        self.value = value
        self.father = father
        self.left = left
        self.right = right


def next_node(node):
    """
    给定树中的一个节点，返回该节点在中序遍历中的下一个节点
    :param node: TreeNode
    :return: TreeNode
    """
    if node is None:
        return None

    # 先考虑节点有右子树的情况，则返回右子树中最靠左的节点
    if node.right is not None:
        node_next = node.right
        while node_next.left:
            node_next = node_next.left
        return node_next

    # 节点没有右子树时
    elif node.father is not None:
        # 如果节点是父节点的左子节点，则返回父节点
        if id(node.father.left) == id(node):
            node_next = node.father
            return node_next

        # 如果节点是父节点的右子节点，则向上搜寻直到找到是父节点左子节点的节点或者根节点
        elif id(node.father.right) == id(node):
            node_next = node.father
            while node_next.father:
                if id(node_next) == id(node_next.father.left):
                    return node_next.father
                node_next = node_next.father

    return None


def set_relation(father, left, right):
    father.left = left
    father.right = right
    left.father = father
    right.father = father


if __name__ == "__main__":
    node_i = TreeNode("i")
    node_h = TreeNode("h")
    node_g = TreeNode("g")
    node_f = TreeNode("f")
    node_e = TreeNode("e")
    node_d = TreeNode("d")
    node_c = TreeNode("c")
    node_b = TreeNode("b")
    node_a = TreeNode("a")
    set_relation(node_e, node_h, node_i)
    set_relation(node_c, node_f, node_g)
    set_relation(node_b, node_d, node_e)
    set_relation(node_a, node_b, node_c)

    res = next_node(node_g)
    print(res.value if res else None)