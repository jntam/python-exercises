def love_meet(bob, alice):
    return set(bob) & set(alice)


def affair_meet(bob, alice, silvester):
    as_ = [x for x in alice if x in silvester]
    as_b = [y for y in as_ if y not in bob]
    return set(as_b)
