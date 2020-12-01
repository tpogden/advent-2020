def bs(arr, val, lo=0, hi=None):
    """Binary search for val in arr."""
    if hi is None:
        hi = len(arr)
    if lo >= hi:
        return None
    m = (hi+lo)//2
    if arr[m] == val:
        return m
    if arr[m] > val:
        return bs(arr, val, lo=0, hi=m)
    else:
        return bs(arr, val, lo=m+1, hi=hi)
