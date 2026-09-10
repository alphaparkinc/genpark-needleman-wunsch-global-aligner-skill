from client import NeedlemanWunsch

def main():
    print("=== Testing Needleman-Wunsch Global Aligner ===")
    nw = NeedlemanWunsch(match=1, mismatch=-1, gap=-1)
    s1 = "GATTACA"
    s2 = "GCATGCU"
    score = nw.align(s1, s2)
    print(f"Global alignment score for '{s1}' and '{s2}': {score}")

    assert score > -10
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
