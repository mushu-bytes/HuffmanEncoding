from __future__ import annotations

from typing import Any, Optional


class Node:
    """Represents a node to be used in a doubly linked list."""
    def __init__(
            self,
            value: Any,
            prev: Optional[Node] = None,
            nxt: Optional[Node] = None):
        self.value = value

        # NOTE: This means that if prev and nxt are None, self.prev and
        # self.next will be self.  You may find this useful.  This means
        # that self.prev and self.next aren't Optional Nodes, they are
        # always Nodes.
        self.prev: Node = prev or self
        self.next: Node = nxt or self


class OrderedList:
    """A circular, doubly linked list of items, from lowest to highest.

    The contents of the list *must* have a accurate notation of less
    than and of equality.  That is to say, the contents of the list must
    implement both __lt__ and __eq__.
    """
    def __init__(self):
        self.size = 0
        self.dummy = Node(None)


def insert(lst: OrderedList, value: Any) -> None:
    # covered
    curr = lst.dummy
    """ 
    index until we hit the last node or when
    the value is not greater than curr.value
    we want to stop right when the next node is a dummy or when 
    the next node is greater than our value
    """
    while curr.next is not lst.dummy and value > curr.next.value:
        curr = curr.next

    new_node = Node(value, curr, curr.next)
    curr.next.prev = new_node
    curr.next = new_node
    lst.size += 1


def remove(lst: OrderedList, value: Any) -> None:
    curr = lst.dummy.next

    while curr.value != value:
        if curr is lst.dummy or curr.value > value:
            raise ValueError("value not in list")
        curr = curr.next

    curr.prev.next = curr.next
    curr.next.prev = curr.prev
    lst.size -= 1


def contains(lst: OrderedList, value: Any) -> bool:
    # covered
    curr = lst.dummy.next
    # stop crawling only if the val is dummy (we hit end) or
    # stop crawling when the the current value is > target
    while curr is not lst.dummy and value >= curr.value:
        if curr.value == value:
            return True
        curr = curr.next

    return False


def index(lst: OrderedList, value: Any) -> int:
    # covered
    curr = lst.dummy.next
    i = 0

    while curr is not lst.dummy and value >= curr.value:

        if curr.value == value:
            return i
        curr = curr.next
        i += 1

    raise ValueError("value not in list")


def get(lst: OrderedList, index: int) -> Any:
    # covered
    curr = lst.dummy.next
    if curr is lst.dummy:
        raise IndexError("invalid index")
    """
    check to see if curr.next because at that point
    going forward would be dummy
    """
    while index != 0:
        if curr.next is lst.dummy:
            raise IndexError("invalid index")
        curr = curr.next
        index -= 1

    return curr.value


def pop(lst: OrderedList, index: int) -> Any:
    # for this function, remember to check if the index is 0, the length of lst
    # one above the length of lst, and also to check whether the val has been
    # actually removed.
    curr = lst.dummy.next

    if curr is lst.dummy:
        raise IndexError("invalid index")

    while index != 0:
        if curr.next is lst.dummy:
            raise IndexError("invalid index")
        curr = curr.next
        index -= 1

    rem_val = curr.value
    curr.prev.next = curr.next
    curr.next.prev = curr.prev
    lst.size -= 1
    return rem_val


def is_empty(lst: OrderedList) -> bool:
    # covered
    return lst.size == 0


def size(lst: OrderedList) -> int:
    # covered
    return lst.size
