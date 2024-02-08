def TOH(n,A,B,C):
    if n == 1:
        print("Move Disk from Source ", A, "to Destination ", C)

    TOH(n-1,A,C,B)
    print("Move disk", n , "from Source ", A , "to Destination ", C)

    TOH(n-1,B,A,C)

    n = 3
    TOH(n,"A","B","C")
