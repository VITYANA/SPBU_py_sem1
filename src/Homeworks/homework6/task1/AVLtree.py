from dataclasses import dataclass
from typing import Optional, Generic, TypeVar

Value = TypeVar("Value")
Key = TypeVar("Key")


@dataclass
class Tree(Generic[Key, Value]):
    root: Optional["TreeNode[Key, Value]"] = None
    size: int = 0


@dataclass
class TreeNode(Generic[Key, Value]):
    key: Key
    value: Optional[Value]
    height: int = 1
    left: Optional["TreeNode[Key, Value]"] = None
    right: Optional["TreeNode[Key, Value]"] = None


def create_tree_map():
    return Tree()


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


def put(tree: Tree, key: Key, value: Value):
    if tree.size != 0:
        new_root = put_node(tree.root, key, value)
        tree.root = new_root
    else:
        put_root(tree, key, value)
    tree.size += 1


def put_node(tree_root: TreeNode, key: Key, value: Value):
    if tree_root is None:
        return TreeNode(key, value)
    if key > tree_root.key:
        tree_root.right = put_node(tree_root.right, key, value)
    elif key < tree_root.key:
        tree_root.left = put_node(tree_root.left, key, value)
    else:
        tree_root.value = value
    return balance(tree_root)


def put_root(tree: Tree, key: Key, value: Value):
    tree.root = TreeNode(key, value)


def remove(tree: Tree, key: Key) -> "Value":
    return_val = get_value(tree, key)

    def binary_search_remove(node: TreeNode, key: Key) -> Optional["TreeNode"]:
        if node is None:
            raise ValueError(f"No {key} element in tree.")

        if node.key == key:
            if node.left is None and node.right is None:
                return None
            if node.left is not None and node.right is None:
                return balance(node.left)
            if node.left is None and node.right is not None:
                return balance(node.right)

            right_branch = node.right
            while right_branch.left:
                right_branch = right_branch.left
            node.value = right_branch.value
            node.key = right_branch.key
            if node.right is None:
                raise ValueError(f"No {key} element in tree.")
            node.right = binary_search_remove(node.right, node.key)

        elif node.left is None and node.right is None:
            raise ValueError(f"No {key} element in tree.")
        elif node.key > key:
            if node.left is None:
                raise ValueError(f"No {key} element in tree.")
            node.left = binary_search_remove(node.left, key)
        else:
            node.right = binary_search_remove(node.right, key)
        return balance(node)

    if tree.root is None:
        raise ValueError(f"No {key} element in tree.")
    else:
        binary_search_remove(tree.root, key)
    tree.size -= 1
    return return_val


def traverse(map: Tree, order: str) -> list["Value"]:
    def preorder(node: TreeNode) -> list["Value"]:
        def direct_order_right(node: TreeNode):
            if node.left and node.right:
                return (
                    [[node.key, node.value]]
                    + direct_order_right(node.right)
                    + direct_order_right(node.left)
                )
            if node.right:
                return [[node.key, node.value]] + direct_order_right(node.right)
            elif node.left:
                return [[node.key, node.value]] + direct_order_right(node.left)
            else:
                return [[node.key, node.value]]

        return direct_order_right(node)[::-1]

    def inorder(node: TreeNode) -> list["Value"]:
        if node.left and node.right:
            return [[node.key, node.value]] + inorder(node.left) + inorder(node.right)
        elif node.left:
            return [[node.key, node.value]] + inorder(node.left)
        elif node.right:
            return [[node.key, node.value]] + inorder(node.right)
        else:
            return [[node.key, node.value]]

    def postorder(node: TreeNode, array: list) -> list["Value"]:
        if node.left:
            postorder(node.left, array)
        array.append([node.key, node.value])
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


def get_tree_node(tree: Tree, key: Key) -> TreeNode:
    root = tree.root

    def recursion(root: TreeNode) -> TreeNode | None:
        if root is None:
            return None
        if key == root.key:
            return root
        if key < root.key and root.left is not None:
            return recursion(root.left)
        elif key > root.key and root.right is not None:
            return recursion(root.right)

    return recursion(root)


def get_value(tree: Tree, key: Key) -> "Value":
    if not has_key(tree, key):
        return -1
    return get_tree_node(tree, key).value


def has_key(tree: Tree, key: Key) -> bool:
    return get_tree_node(tree, key) is not None


def get_minimum(tree):
    def recursion(root):
        if root.left is not None:
            return recursion(root.left)
        return root.key

    return recursion(tree.root)


def get_maximum(tree):
    def recursion(root):
        if root.right is not None:
            return recursion(root.right)
        return root.key

    return recursion(tree.root)


def get_lower_bound(tree, key):
    if tree.root is None:
        raise ValueError("Tree is empty.")
    result = None
    actual_node = tree.root
    while actual_node is not None:
        if key > actual_node.key:
            actual_node = actual_node.right
        elif key < actual_node.key:
            result = actual_node.key
            actual_node = actual_node.left
        else:
            return actual_node.key
    if result is None:
        raise ValueError(f"No key in structure, bigger than {key}.")
    return result


def get_upper_bound(tree, key):
    if tree.root is None:
        raise ValueError("Tree is empty.")
    result = None
    actual_node = tree.root
    while actual_node is not None:
        if key >= actual_node.key:
            actual_node = actual_node.right
        elif key < actual_node.key:
            result = actual_node.key
            actual_node = actual_node.left
        else:
            return actual_node.key
    if result is None:
        raise ValueError(f"No key in structure, bigger than {key}.")
    return result


def separate_keys(keys, key):
    higher_keys, lower_keys = [], []
    for pair in keys:
        lower_keys.append(pair) if pair[0] < key else higher_keys.append(pair)
    return higher_keys, lower_keys


def split(tree, key):
    if tree.root is None:
        return Tree(), Tree()

    def recursion(previous_tree_node, actual_tree_node):
        if key == actual_tree_node.key:
            if previous_tree_node.key > actual_tree_node.key:
                previous_tree_node.left = None
            else:
                previous_tree_node.right = None
            return Tree(tree.root), Tree(actual_tree_node)
        if (key > actual_tree_node.key and actual_tree_node.right is None) or (
            key < actual_tree_node.key and actual_tree_node.left is None
        ):
            return tree, Tree()
        if key > actual_tree_node.key:
            return recursion(actual_tree_node, actual_tree_node.right)
        else:
            return recursion(actual_tree_node, actual_tree_node.left)

    if tree.size == 1 or key == tree.root.key:
        return tree, Tree()
    if key > tree.root.key:
        if tree.root.right is not None:
            return recursion(tree.root, tree.root.right)
        return tree, Tree()
    else:
        if tree.root.left is not None:
            return recursion(tree.root, tree.root.left)
        return tree, Tree()


def get_height_of_node(node):
    return node.height if node is not None else 0


def update_height(node):
    if node is None:
        raise Exception("Node is None.")
    node.height = max(get_height_of_node(node.right), get_height_of_node(node.left)) + 1


def get_balance_factor(node):
    return get_height_of_node(node.right) - get_height_of_node(node.left)


def rotate_right(node):
    child = node.left
    node.left = child.right
    child.right = node
    update_height(node), update_height(child)
    return child


def rotate_left(node):
    child = node.right
    node.right = child.left
    child.left = node
    update_height(node), update_height(child)
    return child


def balance(node):
    if node is None:
        raise Exception("Node is None.")
    update_height(node)
    balance_factor = get_balance_factor(node)
    if balance_factor == 2:
        if get_balance_factor(node.right) < 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)
    if balance_factor == -2:
        if get_balance_factor(node.left) > 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)
    return node


def merge(first_tree, second_tree):
    def recursion(first_tree_root, second_tree_root):
        if first_tree_root is None:
            return second_tree_root
        second_tree_root = recursion(first_tree_root.left, second_tree_root)
        second_tree_root = put_node(
            second_tree_root, first_tree_root.key, first_tree_root.value
        )
        second_tree_root = recursion(first_tree_root.right, second_tree_root)
        return second_tree_root

    second_tree.root = recursion(first_tree.root, second_tree.root)
    second_tree.size += first_tree.size
    return second_tree
