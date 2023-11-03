from dataclasses import dataclass
from typing import Optional, Generic, TypeVar

V = TypeVar("V")


@dataclass
class Tree(Generic[V]):
    root: Optional["TreeNode[V]"]
    size: int = 0


@dataclass
class TreeNode(Generic[V]):
    key: Optional[int]
    value: Optional[V]
    left: Optional["TreeNode[V]"]
    right: Optional["TreeNode[V]"]


def create_tree_map():
    return Tree(None)


def delete_tree_map(tree):
    root = tree.root

    def recursive_delete(root):
        if root:
            recursive_delete(root.left)
            recursive_delete(root.right)
            root.left, root.right, root.key, root.value = None, None, None, None
            tree.size -= 1

    recursive_delete(root)
    tree.root = None


def put(tree: Tree, key: int, value: V):
    if tree.size != 0:
        put_node(tree.root, key, value)
    else:
        put_root(tree, key, value)
    tree.size += 1


def put_node(tree_root: TreeNode, key: int, value: V):
    if tree_root is None:
        return TreeNode(key, value, None, None)
    if key > tree_root.key:
        tree_root.right = put_node(tree_root.right, key, value)
    elif key < tree_root.key:
        tree_root.left = put_node(tree_root.left, key, value)
    return tree_root


def put_root(tree: Tree, key: int, value: V):
    tree.root = TreeNode(key, value, None, None)


def remove(tree: Tree, key: int) -> "V":
    return_val = get_value(tree, key)

    def binary_search_remove(node: TreeNode, key: int) -> Optional["TreeNode"]:
        if node is None:
            return None

        if node.key == key:
            if node.left is None and node.right is None:
                return None
            if node.left is not None and node.right is None:
                return node.left
            if node.left is None and node.right is not None:
                return node.right

            right_branch = node.right
            while right_branch.left:
                right_branch = right_branch.left
            node.value = right_branch.value
            node.key = right_branch.key
            node.right = binary_search_remove(node.right, node.key)

        elif node.left is None and node.right is None:
            raise ValueError(f"No {key} element in tree.")
        elif node.key > key:
            node.left = binary_search_remove(node.left, key)
        else:
            node.right = binary_search_remove(node.right, key)
        return node

    if tree.root is None:
        raise ValueError(f"No {key} element in tree.")
    else:
        binary_search_remove(tree.root, key)
    tree.size -= 1
    return return_val


def traverse(map: Tree, order: str) -> list["V"]:
    def preorder(node: TreeNode) -> list["V"]:
        def direct_order_right(node: TreeNode):
            if node.left and node.right:
                return (
                    [node.value]
                    + direct_order_right(node.right)
                    + direct_order_right(node.left)
                )
            if node.right:
                return [node.value] + direct_order_right(node.right)
            elif node.left:
                return [node.value] + direct_order_right(node.left)
            else:
                return [node.value]

        return direct_order_right(node)[::-1]

    def inorder(node: TreeNode) -> list["V"]:
        if node.left and node.right:
            return [node.value] + inorder(node.left) + inorder(node.right)
        elif node.left:
            return [node.value] + inorder(node.left)
        elif node.right:
            return [node.value] + inorder(node.right)
        else:
            return [node.value]

    def postorder(node: TreeNode, array: list) -> list["V"]:
        if node.left:
            postorder(node.left, array)
        array.append(node.value)
        if node.right:
            postorder(node.right, array)
        return array

    if map.root is None and order in ("inorder", "postorder", "preorder"):
        return []
    if order == "inorder":
        return inorder(map.root)
    elif order == "postorder":
        return postorder(map.root, [])
    elif order == "preorder":
        return preorder(map.root)
    else:
        raise ValueError(f"Have no {order} traverse.")


def get_tree_node(tree: Tree, key: int) -> TreeNode:
    root = tree.root

    def recursion(root: TreeNode) -> TreeNode:
        if key == root.key:
            return root
        if key < root.key and root.left is not None:
            return recursion(root.left)
        elif key > root.key and root.right is not None:
            return recursion(root.right)

    return recursion(root)


def get_value(tree: Tree, key: int) -> "V":
    root = tree.root
    if not has_key(tree, key):
        raise ValueError(f"Tree dont have such key {key}.")
    return get_tree_node(tree, key).value


def has_key(tree: Tree, key: int) -> bool:
    root = tree.root
    return get_tree_node(tree, key) is not None
