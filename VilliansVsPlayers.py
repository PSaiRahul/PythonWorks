def main():
    out = []
    T = int(input())
    if 1 <= T <= 10:
        for i in range(T):
            N = int(input())
            neg_int = 0
            diff = []
            if 1 <= N <= 1000:
                energy_of_villains = [int(i) for i in input().split()]
                strength_of_players = [int(i) for i in input().split()]

            new_villains = list(sorted(energy_of_villains))
            new_players = list(sorted(strength_of_players))

            for x in range(0, len(new_players)):
                diff.append(new_players[x] - new_villains[x])

            while i < len(diff):
                if diff[i] < 0:
                    neg_int += 1
                i += 1
            if neg_int:
                out.append("LOSE")
            else:
                out.append("WIN")
    for i in range(len(out)):
        print(out[i])


main()
