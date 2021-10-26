import argparse
import sys
from .visualizer import Visualizer
from .sorters import bubble_sort, selection_sort, insertion_sort

def main():

    description = \
f"""
A program to visualze various sorting algorithms.

example usage:
sortz-cli --fps 60 bubble\
"""
    parser = argparse.ArgumentParser(prog = f"sortz-cli", description = description,
                                     formatter_class = argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--fps", type = int, help = "fps of visualizer (inc. by 10)",
                        choices = [1] + list(range(10, 241, 10)),
                        metavar = "{1-240}", default = 60)
    parser.add_argument("sorter", help = "sorting algorithm",
                        choices = ["bubble", "selection", "insertion"])

    if len(sys.argv) == 1:
        parser.print_help(sys.stdout)
        sys.exit(1)
    args = parser.parse_args()

    sorter = None
    if args.sorter == "bubble":
        sorter = bubble_sort
    elif args.sorter == "selection":
        sorter = selection_sort
    elif args.sorter == "insertion":
        sorter = insertion_sort

    v = Visualizer(sorter, args.fps)
    v.main_loop()

if __name__ == "__main__":
    main()
