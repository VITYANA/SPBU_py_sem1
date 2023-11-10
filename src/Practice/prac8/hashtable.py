from dataclasses import dataclass
import typing

Key = typing.TypeVar("Key")
Value = typing.TypeVar("Value")


@dataclass
class HashTable:
    table: list[typing.Optional["Node"]]
    capacity: int = 1024
    size: int = 0


@dataclass
class Node:
    key: Key
    value: Value
    next: "Node" = None


def create_hashtable(capacity: int = 1024) -> HashTable:
    return HashTable([None] * capacity)


def delete_hashtable(hashtable: HashTable):
    for i in range(hashtable.capacity):
        elem_to_del = hashtable.table[i]

        def del_rec(elem_to_del):
            if elem_to_del.next is None:
                del elem_to_del
                return
            elem_to_del.next = del_rec(elem_to_del.next)

    del hashtable


def hash_func(hashtable: HashTable, key: Key) -> int:
    return hash(key) % hashtable.capacity


def put(hashtable: HashTable, key: Key, value: Value):
    index = hash_func(hashtable, key)
    if hashtable.table[index] is None:
        hashtable.table[index] = Node(key, value)
        hashtable.size += 1
    else:
        current = hashtable.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = hashtable.table[index]
        hashtable.table[index] = new_node
        hashtable.size += 1


def remove(hashtable: HashTable, key: Key) -> Value:
    index = hash_func(hashtable, key)
    if not has_key(hashtable, key):
        raise KeyError
    previous = None
    current = hashtable.table[index]
    return_value = current.value
    while current:
        if current.key == key:
            if previous:
                previous.next = current.next
            else:
                hashtable.table[index] = current.next
            hashtable.size -= 1
            return return_value
        previous = current
        current = current.next


def get(hashtable: HashTable, key: Key) -> Value:
    if not has_key(hashtable, key):
        raise KeyError
    index = hash_func(hashtable, key)
    return hashtable.table[index].value


def has_key(hashtable: HashTable, key: Key) -> bool:
    index = hash_func(hashtable, key)
    return hashtable.table[index] is not None


def items(hashtable: HashTable) -> list[tuple[Key, Value]]:
    list_to_return = []
    i = 0
    try:
        while len(list_to_return) != hashtable.size and i != hashtable.capacity:
            if hashtable.table[i] is not None:
                list_to_return.append(
                    (hashtable.table[i].key, hashtable.table[i].value)
                )
            i += 1
        return list_to_return
    except ValueError:
        raise ValueError("Some data have collision.")
