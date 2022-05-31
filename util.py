import sys


def format_arg(a, kw):
    str_list = []
    for v in a: str_list.append(str(v))
    if kw: str_list.append(f"**{kw}")
    return ", ".join(str_list)


def logcall(fun):
    """Log calls to the decorated function each time one begins"""
    def wrap(*a, **kw):
        print(f"{fun.__name__}({format_arg(a, kw)})")
        result = fun(*a, **kw)
        return result
    return wrap


def logboth(fun):
    """Log beginning and end of calls to the decorated function"""
    def wrap(*a, **kw):
        print(f"{fun.__name__}({format_arg(a, kw)}) begin")
        result = fun(*a, **kw)
        print(f"{fun.__name__} end")
        return result
    return wrap


def repeat(fun, sleep, duration, ending_message):
    """
    Refactored code which runs the `fun` function a number of times proportional to duration
    (10 times duration to be precise)
    - sleep is the function to use to perform sleep. It is passed `.1` each time
    - ending_message is printed at the end
    """
    for k in range(int(duration)):
        print(k, end=" ")
        sys.stdout.flush()
        for m in [0] * 10:
            fun()
            sleep(.1)
    print(int(duration), end=" ")
    sys.stdout.flush()
    for m in [0] * (int(10 * duration) % 10):
        fun()
        sleep(.1)
    print(ending_message)
    sys.stdout.flush()


def remove_common_prefix(*list_list):
    """
    Given any number of lists, identify what part is common to all of them at the begnning, and return
    a list of lists (in the same order) where this common part has been removed.
    """
    common = 0
    for k, elemList in enumerate(zip(*list_list)):
        elem, *rest = elemList
        if any(elem != e for e in rest):
            break
        common = k + 1
    result_list = [li[common:] for li in list_list]
    return result_list
