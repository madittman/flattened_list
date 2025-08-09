"""
Collection of helper functions.
"""

def issubsetof(list_1: list, list_2: list) -> bool:
    """Check if first list is subset of second list. Elements are kept in order."""
    if len(list_1) > len(list_2):
        return False
    for idx in range(len(list_1)):
        if list_1[idx] != list_2[idx]:
            return False
    return True