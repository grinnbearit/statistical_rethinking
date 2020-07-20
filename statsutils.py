def standardise(column):
    """
    returns a new column with the values standardised
    """
    return (column - column.mean())/column.std()


# https://ksachdeva.github.io/rethinking-tensorflow-probability/06_the_haunted_dag_and_the_causal_terror.html
def implied_conditional_independencies(dag):
    acc = []
    all_independencies = dag.get_all_independence_relationships()
    for s in all_independencies:
        if all(t[0] != s[0] or t[1] != s[1] or not t[2].issubset(s[2])
               for t in all_independencies if t != s):
            acc.append(s)
    return acc

# https://ksachdeva.github.io/rethinking-tensorflow-probability/06_the_haunted_dag_and_the_causal_terror.html
def adjustment_sets(dag, x, y, unobserved="U"):
    acc = []
    all_adjustment_sets = dag.get_all_backdoor_adjustment_sets(x, y)
    for s in all_adjustment_sets:
        if all(not t.issubset(s) for t in all_adjustment_sets if t != s):
            if s != {unobserved}:
                acc.append(s)
    return acc
