from typing import List

from helpers import issubsetof


class FlattenedList:
    """Multidimensional list that is kept flat."""

    def __init__(self):
        self.list: List[list] = []
        self.dimensions: List[str] = []  # names of dimensions

    def __repr__(self):
        substring: str = "[\n"
        for sublist in self.list:
            substring += self._sublist_repr(sublist)
        return substring + "]"

    def _sublist_repr(self, sublist: list, dimension: int = 0, substring: str = "") -> str:
        indention: str = dimension * "    "
        substring += f"{indention}{self.dimensions[dimension]}: {sublist[dimension]}"
        dimension += 1
        if not sublist[dimension:]:  # reached end of list
            return substring + ",\n"
        else:
            return self._sublist_repr(sublist, dimension, substring + "\n")

    def _remove_redundant_sublists(self, new_sublist: list):
        """Remove all sublists that contain less information than the new sublists."""
        for idx, sublist in enumerate(self.list):
            if issubsetof(sublist, new_sublist):
                # print("->", sublist, "==", new_sublist, "Deleting", self.list[idx])
                del self.list[idx]

    def add_dimension(self, name: str) -> None:
        if name in self.dimensions:
            raise Exception(f"Dimension name {name} already exists")
        self.dimensions.append(name)

    def add_sublists(self, new_sublists: List[list]) -> None:
        for new_sublist in new_sublists:
            if len(new_sublist) != len(self.dimensions):
                raise Exception(f"Sublist {new_sublist} has wrong dimension")
            if new_sublist in self.list:
                raise Exception(f"Sublist {new_sublist} already in list")

            self._remove_redundant_sublists(new_sublist)

        self.list.extend(new_sublists)
        self.list.sort()