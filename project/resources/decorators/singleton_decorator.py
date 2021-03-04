

def singleton(cls):

    instances = dict()

    def wrapper(*args, **kwags):
        if cls not in instances:
            instances[cls] = cls(*args, **kwags)

        return instances[cls]

    return wrapper
