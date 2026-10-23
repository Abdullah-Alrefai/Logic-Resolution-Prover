from itertools import combinations


def negate(literal):
    """Return the opposite literal: "Z" -> "~Z", "~Z" -> "Z"."""
    if literal.startswith("~"):
        return literal[1:]
    return "~" + literal


def resolve(c1, c2):
    """Return all resolvent clauses of clauses c1 and c2."""
    resolvents = set()
    for literal in c1:
        if negate(literal) in c2:
            resolvent = (c1 - {literal}) | (c2 - {negate(literal)})
            resolvents.add(frozenset(resolvent))
    return resolvents


def resolution_with_steps(kb, query):
    """Run resolution by refutation. Returns (entailed, number of resolution steps).

    A resolution step is one call of resolve() on one pair of clauses.
    """
    clauses = {frozenset(c) for c in kb}
    clauses.add(frozenset({negate(query)}))
    steps = 0

    while True:
        new = set()
        # Sorted so the step count is the same on every run
        for c1, c2 in combinations(sorted(clauses, key=sorted), 2):
            steps += 1
            resolvents = resolve(c1, c2)
            if frozenset() in resolvents:
                return True, steps
            new |= resolvents
        if new <= clauses:
            return False, steps
        clauses |= new


def pl_resolution(kb, query) -> bool:
    """
    Determine whether kb entails query
    using propositional resolution.

    Parameters:
        kb: A collection of clauses in CNF.
        query: A propositional symbol.

    Returns:
        True if kb entails query.
        False otherwise.
    """
    return resolution_with_steps(kb, query)[0]


if __name__ == "__main__":
    tests = [
        ("Task 3 KB, query Z", [
            {"~X", "Z"},
            {"~J", "~K", "X"},
            {"~C", "~J", "K"},
            {"~D", "~X", "J"},
            {"~D", "~C", "J"},
            {"D"},
            {"C"},
        ], "Z"),
        ("Test 2 (entailed), query Q", [
            {"P"},
            {"~P", "Q"},
        ], "Q"),
        ("Test 3 (not entailed), query P", [
            {"P", "Q"},
        ], "P"),
    ]

    for name, kb, query in tests:
        result = pl_resolution(kb, query)
        steps = resolution_with_steps(kb, query)[1]
        print(f"{name}: {result} ({steps} resolution steps)")
