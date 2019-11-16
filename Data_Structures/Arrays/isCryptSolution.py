
def isCryptSolution(crypt, solution):
    dic = {ord(c): d for c, d in solution}
    *v, = map(lambda x: x.translate(dic), crypt)
    return not any(x != "0" and x.startswith("0") for x in v) and \
        int(v[0]) + int(v[1]) == int(v[2])

# solution 2
def isCryptSolution(crypt, solution):
    table = str.maketrans(dict(solution))
    t = tuple(s.translate(table) for s in crypt)
    zeroes = any(s[0] == '0' for s in t if len(s) > 1)
    return not zeroes and int(t[0]) + int(t[1]) == int(t[2])
