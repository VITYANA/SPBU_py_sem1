from dataclasses import dataclass
import typing

Key = typing.TypeVar("Key")
Value = typing.TypeVar("Value")
DefaultCapacity = 1024


@dataclass
class HashTable(typing.Generic[Key, Value]):
    table: list[typing.Optional["Node[Key, Value]"]]
    capacity: int = DefaultCapacity
    size: int = 0
    hs_func: typing.Callable[[typing.Any], Key] = hash

    def hash_func(self, key):
        return self.hs_func(key) % self.capacity


@dataclass
class Node(typing.Generic[Key, Value]):
    key: Key
    value: Value
    next: "Node" = None


def create_hashtable(capacity: int = 1024) -> HashTable:
    return HashTable([None] * capacity)


def delete_hashtable(hashtable: HashTable):
    for i in range(hashtable.capacity):
        elem_to_del = hashtable.table[i]

        def del_rec(elem_to_delete):
            if elem_to_delete is None:
                del elem_to_delete
                return
            if elem_to_delete.next is None:
                del elem_to_delete.next
                del elem_to_delete
                return
            del_rec(elem_to_delete.next)

        del_rec(elem_to_del)
    del hashtable


def put(hashtable: HashTable, key: Key, value: Value):
    index = hashtable.hash_func(key)
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
    index = hashtable.hash_func(key)
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
    index = hashtable.hash_func(key)
    return hashtable.table[index].value


def has_key(hashtable: HashTable, key: Key) -> bool:
    index = hashtable.hash_func(key)
    return hashtable.table[index] is not None


def items(hashtable: HashTable) -> list[tuple[Key, Value]]:
    list_to_return = []
    i = 0
    while len(list_to_return) != hashtable.size and i != hashtable.capacity:
        if hashtable.table[i] is not None:
            list_to_return.append((hashtable.table[i].key, hashtable.table[i].value))
        i += 1
    return list_to_return
