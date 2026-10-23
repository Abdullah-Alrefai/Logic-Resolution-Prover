# Logic Resolution Prover

Checks if a set of facts (a knowledge base) proves a statement, using propositional resolution.

The facts are written as clauses. For example, `{"~P", "Q"}` means "P implies Q". The program adds the opposite of the statement and keeps combining clauses. If it reaches a contradiction, the statement is proven.

It runs three test cases and prints whether each statement is proven and how many steps it took.

## Run it

No packages needed.

```bash
python main.py
```
