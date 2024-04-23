def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi problem recursively.

    :param n: int - number of disks to move.
    :param source: str - name of the source peg.
    :param target: str - name of the target peg.
    :param auxiliary: str - name of the auxiliary peg.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Move top n-1 disks from source to auxiliary using target as auxiliary peg
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # Move nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Move n-1 disks from auxiliary to target using source as auxiliary peg
    tower_of_hanoi(n - 1, auxiliary, target, source)


if __name__ == "__main__":
    num_disks = 4  # Number of disks to move
    source_peg = 'A'
    target_peg = 'C'
    auxiliary_peg = 'B'

    print(f"Solving Tower of Hanoi problem with {num_disks} disks:")
    tower_of_hanoi(num_disks, source_peg, target_peg, auxiliary_peg)
