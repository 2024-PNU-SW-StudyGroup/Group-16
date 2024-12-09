def mismatch_count(s1, s2):
    return sum(1 for c1, c2 in zip(s1, s2) if c1 != c2)

def find_approximate_matches(dna, sub, k):
    result = []
    for i in range(len(dna)-len(sub)+1):
        if mismatch_count(dna[i:i+len(sub)], sub) <= k:
            result.append(i)
    return result

def main():
    dna = input()
    sub = input()
    k = int(input())

    indices = find_approximate_matches(dna, sub, k)
    print(indices)

if __name__ == "__main__":
    main()