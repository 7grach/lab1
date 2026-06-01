class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Добавить элемент в конец очереди"""
        self.items.append(item)

    def dequeue(self):
        """Удалить и вернуть первый элемент"""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.pop(0)  # удаление из начала - O(n)

    def peek(self):
        """Посмотреть первый элемент без удаления"""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)