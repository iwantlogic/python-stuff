cache = {}
def addcache(func):
    def wrap(*params):
        global cache
        cache[f"{len(cache)}"]=func(*params)
        if func(*params) in cache:
            return cache[index(func(*params))]
        else:
            return func(*params)
    return wrap

@addcache
def exec2(a):
    exec(a)
exec2(input())
print(cache)
