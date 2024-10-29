from module_2_5 import result1


def calculate(*args):
    total_sum = 0
    for arg in args:
        if isinstance(arg,(list,tuple, set)):
                  total_sum += calculate(*args)
        elif isinstance(arg, dict):
             total_sum += calculate(*arg.items())
        elif isinstance(arg, str):
            total_sum += len(arg)
        elif isinstance(arg,(int,float)):
            total_sum += arg

    return(total_sum)








