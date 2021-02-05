import random
import copy

def init(n, max_nmr, min_nmr):
    """
    """
    one_dimensional = [122, 153, 101, 105, 123, 405, 909]
    # two_dimensional = [ [x, [None for x in range(n-1)]] for x in range(10) ]
    two_dimensional = [ [x, []] for x in range(10) ]

    return one_dimensional, two_dimensional


def sorter(to_sort, bucket, tiental, slice_at):

    new_list = []

    for i in to_sort:
        if i < tiental:
            bucket[0][0].append(i)
        elif slice_at == 1:
            unit = int(str(i)[-1:])
            bucket[unit][1].append(i)
        else:
            unit = int(str(i)[-(slice_at):-(slice_at - 1)])
            bucket[unit][1].append(i)
    
    for x in range(0, 10):
        new_list.extend(bucket[x][1])
    # print(new_list)
    return new_list
        

def bucket_sort():


    to_sort, bucket = init(7, 7, 7)

    clean_bucket = bucket
    tiental = 1
    slice_at = 1
    max_tiental = len(str(max(to_sort)))

    for i in range(0, max_tiental):
        print(clean_bucket)
        to_sort = sorter(to_sort, bucket, tiental, slice_at)
        

        tiental *= 10
        slice_at += 1
    

bucket_sort()