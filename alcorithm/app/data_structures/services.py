from app.common.utils import cat_file
from app.config import get_logger

__all__ = [
    "explain_array",
    "explain_set",
    "explain_heap",
    "explain_graph",
    "explain_queue",
    "explain_stack",
    "explain_binary_tree",
    "explain_hash_table",
    "explain_linked_list",
    "explain_binary_search_tree",
]

logger = get_logger()


# Функции теории для каждой структуры данных
def explain_array():
    logger.info(
        "Массив — это коллекция элементов фиксированного размера, "
        "в которой элементы хранятся в смежных ячейках памяти. "
        "Доступ к элементам осуществляется по индексу с временной сложностью O(1)."
    )
    logger.info(
        "Пример: массив целых чисел [1, 2, 3, 4, 5]. "
        "Доступ к третьему элементу: my_array[2]."
    )
    cat_file("array.py")


def explain_linked_list():
    logger.info(
        "Связный список состоит из узлов, каждый из которых содержит "
        "значение и ссылку на следующий узел. "
        "Позволяет динамически добавлять и удалять элементы, "
        "но доступ к элементам по индексу требует O(n)."
    )
    logger.info(
        "Пример: связный список: 1 -> 2 -> 3 -> 4. "
        "Для добавления элемента '0' в начало: head = Node(0, head)."
    )
    cat_file("linked_list.py")


def explain_stack():
    logger.info(
        "Стек — это структура данных, работающая по принципу LIFO (Last In, First Out), "
        "где последний добавленный элемент будет первым, который будет извлечен. "
        "Операции добавления и удаления имеют временную сложность O(1)."
    )
    logger.info(
        "Пример: стек, представляющий операции: push(1), push(2), pop() вернет 2."
    )
    cat_file("stack.py")


def explain_queue():
    logger.info(
        "Очередь — это структура данных, работающая по принципу FIFO (First In, First Out), "
        "где первый добавленный элемент будет первым, который будет извлечен. "
        "Также поддерживает операции добавления и удаления с временной сложностью O(1)."
    )
    logger.info(
        "Пример: очередь, представляющая операции: enqueue(1), enqueue(2), dequeue() вернет 1."
    )
    cat_file("queue.py")


def explain_hash_table():
    logger.info(
        "Хеш-таблица — это структура данных, которая хранит пары ключ-значение "
        "для быстрого доступа к данным. "
        "Хеш-функция преобразует ключ в индекс массива. "
        "Ожидаемая временная сложность поиска, добавления и удаления O(1)."
    )
    logger.info(
        "Пример: хеш-таблица: {'name': 'Alice', 'age': 30}. "
        "Доступ к значению по ключу: my_hash_table['name'] вернет 'Alice'."
    )
    cat_file("hash_table.py")


def explain_set():
    logger.info(
        "Множество — это коллекция уникальных элементов, не допускающая дубликатов. "
        "Поддерживает операции добавления, удаления и проверки наличия элемента с "
        "временной сложностью O(1)."
    )
    logger.info(
        "Пример: множество: {1, 2, 3}. "
        "Добавление элемента: my_set.add(4) делает множество {1, 2, 3, 4}."
    )
    cat_file("set.py")


def explain_binary_tree():
    logger.info(
        "Бинарное дерево — это структура данных, в которой каждый узел имеет не более "
        "двух потомков. Оно может использоваться для организации данных в упорядоченном виде."
    )
    logger.info(
        "Пример: бинарное дерево: 4 (корень) -> 2 (левый узел), 6 (правый узел)."
    )
    cat_file("binary_tree.py")


def explain_binary_search_tree():
    logger.info(
        "Бинарное дерево поиска — это бинарное дерево, в котором для каждого узла "
        "значения в левом поддереве меньше, чем значение узла, "
        "а в правом поддереве — больше. Позволяет эффективно находить элементы."
    )
    logger.info(
        "Пример: бинарное дерево поиска: 4 (корень) -> 2 (левый узел), 6 (правый узел). "
        "Для поиска 6: начиная с корня, идем вправо."
    )
    cat_file("binary_search_tree.py")


def explain_heap():
    logger.info(
        "Куча — это специализированное дерево, удовлетворяющее свойству кучи, "
        "где родительский узел больше (в max-heap) или меньше (в min-heap) своих дочерних узлов. "
        "Используется в алгоритме сортировки HeapSort."
    )
    logger.info(
        "Пример: max-heap: [10, 5, 6, 2, 3]. "
        "10 — корень, больше своих дочерних узлов 5 и 6."
    )
    cat_file("heap.py")


def explain_graph():
    logger.info(
        "Граф состоит из узлов (вершин) и ребер, соединяющих их. "
        "Графы могут быть ориентированными или неориентированными, "
        "и используются для моделирования отношений между объектами."
    )
    logger.info(
        "Пример: граф: A -- B (ребро между A и B), "
        "C -> D (ориентированное ребро от C к D)."
    )
    cat_file("graph.py")
