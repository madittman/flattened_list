from flattened_list import FlattenedList


if __name__ == '__main__':
    my_list = FlattenedList()
    my_list.add_dimension("season")
    my_list.add_sublists(
        [[1], [2], [3], [4]]
    )
    print(my_list)

    my_list.add_dimension("episode")
    my_list.add_sublists(
        [
            [1, 1], [1, 2], [1, 3], [1, 4], [1, 5],
            [2, 1], [2, 2], [2, 3],
            [4, 1],
        ]
    )
    print(my_list)

    my_list.add_dimension("character")
    my_list.add_sublists(
        [
            [1, 1, "Mark"], [1, 3, "Josef"],
            [4, 2, "Lyndon"],
        ]
    )
    print(my_list)

    my_list.remove_last_dimension()
    print(my_list)