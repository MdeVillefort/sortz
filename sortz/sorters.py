def bubble_sort(bars, once = False):
    """
    A simple bubble sort function.

    Parameters
    ----------
    bars : List[Tuple[pygame.Surface, pygame.Rect]]
        A list of game objects to be sorted by height
    once : bool
        A single iteration?

    Returns
    -------
    is_sorted : bool
        Has the array been sorted?
    """

    unsorted_until_index = len(bars) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(unsorted_until_index):
            if bars[i][1].height > bars[i + 1][1].height:
                bars[i], bars[i + 1] = bars[i + 1], bars[i]
                is_sorted = False
                if once: return is_sorted

        unsorted_until_index -= 1

    return is_sorted
