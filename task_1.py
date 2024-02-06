from helpers.shuffle_array import shuffle_array


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, array=None):
        self.head = None
        if array:
            for i in array:
                self.append(i)

    def __str__(self) -> str:
        result = ""
        current = self.head
        while current:
            result += str(current.data) + " -> "
            current = current.next
        result += "None"
        return result

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    # 1. Реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 2. Cортування вставками
    def insertion_sort(self):
        def sorted_insert(head, node):
            if not head or node.data < head.data:
                node.next = head
                return node
            else:
                current = head
                while current.next and current.next.data < node.data:
                    current = current.next
                node.next = current.next
                current.next = node
                return head

        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            sorted_head = sorted_insert(sorted_head, current)
            current = next_node
        self.head = sorted_head

    # 3. Об'єднання двох відсортованих списків в один відсортований список
    def merge_sorted_lists(self, list2):
        dummy = Node(0)
        tail = dummy

        list1_current = self.head
        list2_current = list2.head

        while list1_current and list2_current:
            if list1_current.data < list2_current.data:
                tail.next = list1_current
                list1_current = list1_current.next
            else:
                tail.next = list2_current
                list2_current = list2_current.next
            tail = tail.next

        if list1_current:
            tail.next = list1_current
        elif list2_current:
            tail.next = list2_current

        self.head = dummy.next


def main():
    print("# Завдання 1")
    linked_list = LinkedList(chr(i + 96) for i in range(1, 10))
    print(f"Оригінальний список: {linked_list}")

    linked_list.reverse()
    print(f"Реверсований список: {linked_list}")

    print()
    print("# Завдання 2")
    shuffled_list = LinkedList(shuffle_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 0]))
    print(f"Перемішаний список: {shuffled_list}")
    shuffled_list.insertion_sort()
    print(f"Відсортований список: {shuffled_list}")

    print()
    print("# Завдання 3")
    linked_list_1 = LinkedList([2, 5, 11, 17, 23, 31, 41, 47, 59, 67, 73, 83, 97])
    linked_list_2 = LinkedList([3, 7, 13, 19, 29, 37, 43, 53, 61, 71, 79, 89])
    print(f"Список 1: {linked_list_1}")
    print(f"Список 2: {linked_list_2}")
    linked_list_1.merge_sorted_lists(linked_list_2)
    print(f"Об'єднаний список: {linked_list_1}")


if __name__ == "__main__":
    main()
