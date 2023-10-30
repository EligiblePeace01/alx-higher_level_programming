#!/usr/bin/python3
"""Solves the N-qn puzzle"""

import sys


def bd_initialisatio(n):
    """Initialize."""
    bd = []
    [bd.append([]) for i in range(n)]
    [wr.append(' ') for i in range(n) for wr in bd]
    return (bd)


def bd_dcp(bd):
    """Return a bd_dcp."""
    if isinstance(bd, list):
        return list(map(bd_dcp, bd))
    return (bd)


def stl_get(bd):
    """Return the list."""
    slt = []
    for r in range(len(bd)):
        for c in range(len(bd)):
            if bd[r][c] == "Q":
                slt.append([r, c])
                break
    return (slt)


def xout(bd, wr, col):
    """something here."""

    for c in range(col + 1, len(bd)):
        bd[wr][c] = "x"

    for c in range(col - 1, -1, -1):
        bd[wr][c] = "x"

    for r in range(wr + 1, len(bd)):
        bd[r][col] = "x"

    for r in range(wr - 1, -1, -1):
        bd[r][col] = "x"
    c = col + 1
    for r in range(wr + 1, len(bd)):
        if c >= len(bd):
            break
        bd[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(wr - 1, -1, -1):
        if c < 0:
            break
        bd[r][c]
        c -= 1
    c = col + 1
    for r in range(wr - 1, -1, -1):
        if c >= len(bd):
            break
        bd[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(wr + 1, len(bd)):
        if c < 0:
            break
        bd[r][c] = "x"
        c -= 1


def rc_slt(bd, wr, qn, slt):
    """rc puzzle."""
    if qn == len(bd):
        slt.append(stl_get(bd))
        return (slt)

    for c in range(len(bd)):
        if bd[wr][c] == " ":
            tmp_bd = bd_dcp(bd)
            tmp_bd[wr][c] = "Q"
            xout(tmp_bd, wr, c)
            slt = rc_slt(tmp_bd, wr + 1, qn + 1, slt)

    return (slt)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqn N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    bd = bd_initialisatio(int(sys.argv[1]))
    slt = rc_slt(bd, 0, 0, [])
    for sol in slt:
        print(sol)
