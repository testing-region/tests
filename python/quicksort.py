A = ["Q", "U", "E", "B", "R", "A", "C", "H", "O"]

# display l, r, and pivot at every recursive call


def quicksort(A: list[str], l: int, r: int) -> None:
    if l < r:
        p: int = partition(A, l, r)
        print(f"l: {l}, r: {r}, pivot: {p}")
        quicksort(A, l, p - 1)
        quicksort(A, p + 1, r)


def partition(A: list[str], l: int, r: int) -> int:
    x = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


print(A)
print()
quicksort(A, 0, len(A) - 1)
print()
print(A)
