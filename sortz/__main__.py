import argparse
import sys
from .visualizer import Visualizer
from .sorters import bubble_sort, selection_sort

def main():

    description = \
f"""
A program to visualze various sorting algorithms.

example usage:
sortz-cli --fps 60 bubble\
"""
    parser = argparse.ArgumentParser(prog = f"sortz-cli", description = description,
                                     formatter_class = argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--fps", type = int, help = "fps of visualizer",
                        choices = range(1, 121), metavar = "{1-120}")
    parser.add_argument("sorter", help = "sorting algorithm",
                        choices = ["bubble", "selection"])

    if len(sys.argv) == 1:
        parser.print_help(sys.stdout)
        sys.exit(1)
    args = parser.parse_args()

    sorter = None
    if args.sorter == "bubble":
        sorter = bubble_sort
    elif args.sorter == "selection":
        sorter = selection_sort

    v = Visualizer(sorter, args.fps)
    v.main_loop()

if __name__ == "__main__":
    main()
