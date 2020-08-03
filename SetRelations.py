import itertools

# The powerset of S is the set of all subsets of S
def PowerSet(S):
    if S == []:
        return [[]]

    rtnList = []
    rtnList.append([]) # empty set is subset of every set

    for i in range(1, len(S)+1):
        for j in list(itertools.combinations(S, i)):
            rtnList.append([j])

    return rtnList

# The cartesian product of sets A,B is the set of all ordered pairs...
def CartesianProduct(S, d):
    rtnList = []

    for i in S:
        for j in d:
            rtnList.append((i, j))

    return rtnList



# Relations between sets
def IsSetReflexive(S, Relation):
    for i in S:
        if not Relation(i, i):
            return False
    
    return True

def IsSetSymmetric(S, Relation):
    for i in S:
        for j in S:
            if not ((not Relation(i, j)) or Relation(j, i)):
                return False
    
    return True

def IsSetAntiSymmetric(S, Relation):
    for i in S:
        for j in S:
            if not(not (Relation(i, j) and Relation(j, i)) or i == j):
                return False

    return True

def IsSetTransitive(S, Relation):
    for i in S:
        for j in S:
            for k in S:
                if not (not(Relation(i, j) and Relation(j, k)) or Relation(i, k)):
                    return False

    return True



# Equivalence/partial order relations
def IsEquivalence(S, Relation):
    if IsSetReflexive(S, Relation) and IsSetSymmetric(S, Relation) and IsSetTransitive(S, Relation):
        return True

    return False

def IsPartialOrder(S, Relation):
    if IsSetReflexive(S, Relation) and IsSetAntiSymmetric(S, Relation) and IsSetTransitive(S, Relation):
        return True

    return False

