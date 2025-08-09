# FlattenedList
**A type that holds a list with _n_ dimensions but the list is kept flat.**

This turned out to be useful for implementing an equally distributed random selection
of elements on a multidimensional list where the nesting is not equally distributed.

## Quick Start

The flattened list can be any multidimensional data.
To show it, take the series [Futurama](https://en.wikipedia.org/wiki/Futurama):
```python
futurama = FlattenedList()
futurama.add_dimension("season")
futurama.add_sublists(
    [[1], [2], [3]]
)

futurama.add_dimension("episode")
futurama.add_sublists(
    [
        *[[1,i] for i in range(1, 14)],  # season 1 has 13 episodes
        *[[2,i] for i in range(1, 20)],  # season 2 has 19 episodes
        *[[3,i] for i in range(1, 23)],  # season 3 has 22 episodes
    ]
)
```

To print out this list, just use the built-in _print_ function:
```python
print(futurama)
```
The output will be the following (shortened here).
```sh
[
season: 1
    episode: 1,
season: 1
    episode: 2,
...
season: 1
    episode: 13,
season: 2
    episode: 1,
...
season: 2
    episode: 19,
season: 3
    episode: 1,
...
season: 3
    episode: 22,
]
```

However, the list is kept flat in memory. To see how it actually looks like, run
```python
print(futurama.list)
```
and you get the following output.
```sh
[[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [2, 12], [2, 13], [2, 14], [2, 15], [2, 16], [2, 17], [2, 18], [2, 19], [2, 20], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13], [3, 14], [3, 15]]
```

The name of the dimensions are kept in a separate list.

You can now run an equally distributed random selection on the list
```python
from random import randint

random_idx = randint(0, len(futurama.list))
random_episode = futurama.list[random_idx]
```
and each episode has the same chance of being selected, no matter how many episodes per season.

An arbitrary number of dimensions can be added as long as new elements keep the dimensions:
```python
futurama.add_dimension("minute")
futurama.add_sublists(
    [
        [1, 1, 44], [1, 3, 32],
        [4, 2, 11],  # this adds season 4 automatically
    ]
)
print(futurama)
```
Now the list looks like this (shortened here):
```sh
[
season: 1
    episode: 1
        minute: 44,
season: 1
    episode: 2,
season: 1
    episode: 3
        minute: 32,
...
season: 3
    episode: 22,
season: 4
    episode: 2
        minute: 11,
]
```