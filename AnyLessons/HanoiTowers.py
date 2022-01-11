def hanoi_towers(n, i, k):
    if n == 1:
        print(f"Move disk 1 from pin {i} to {k}")
    else:
        tmp = 6 - i - k
        hanoi_towers(n-1, i, tmp)
        print(f"Move disk {n} from pin {i} to {k}")
        hanoi_towers(n-1, tmp, k)


hanoi_towers(int(input()), 1, 2)
