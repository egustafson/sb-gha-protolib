import sys

from greet import greeter


def main() -> None:
    """Print the greeting produced by ``greeter`` for the CLI argument."""
    if len(sys.argv) != 2:
        print("Not sure who you are.")
        return

    print(greeter(sys.argv[1]))


if __name__ == "__main__":
    main()
