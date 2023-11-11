from src.Practice.prac8.hashtable import *


if __name__ == "__main__":
    hashtable_example = create_hashtable()
    print(hashtable_example)
    put(hashtable_example, 11, 11)
    put(hashtable_example, 10, 10)
    put(hashtable_example, 12, 12)
    put(hashtable_example, 13, 13)
    put(hashtable_example, 12, 15)
    print(remove(hashtable_example, 10))
    print(get(hashtable_example, 13))
    print(has_key(hashtable_example, 1))
    print(hashtable_example)
    print(items(hashtable_example))
    hashtable_example = delete_hashtable(hashtable_example)
    print(hashtable_example)
