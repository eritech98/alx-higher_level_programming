
ix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for lis in matrix:
        for elem in lis:
            if lis.index(elem) == 0:
                print("{:d}".format(elem), end="")
            else:
                print(" {:d}".format(elem), end="")
        print() __name__ == "__main__":
