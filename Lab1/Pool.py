import time


class Pool:
    def __init__(self, address, volume, max_number):
        self.address = address
        self.volume = volume
        self.max_number = max_number


def print_object(pool: Pool):
    print("Address: " + pool.address + ", water volume: " + str(pool.volume) + ", max number: " + str(pool.max_number))


def swap(list, i, min_index):
    tmp = list[i]
    list[i] = list[min_index]
    list[min_index] = tmp
    return list


def selection(path):
    file = open(path, "r")
    list = []
    for line in file:
        string = line
        str_list = string.split(",")
        pool = Pool(str_list[0], str_list[1], str_list[2])
        list.append(pool)

    file.close()

    n = len(list)
    comparing_times = 0
    change_times = 0
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if list[j].volume > list[min_index].volume:
                min_index = j
                comparing_times = comparing_times + 1
        list = swap(list, i, min_index)
        change_times = change_times + 1

    merge_time_start = time.process_time()

    merge_time_stop = time.process_time()

    print("Selection Sort")
    print("Change number:  " + str(change_times))
    print("Compare number:  " + str(comparing_times))
    print("Sorting time:  " + str((merge_time_stop - merge_time_start)))
    print("Result")
    for i in range(0, len(list)):
        print_object(list[i])


def merge_sort(pools_list):
    comparing_times = 0
    change_times = 0

    if len(pools_list) > 1:
        mid = len(pools_list) // 2
        lefthalf = pools_list[:mid]
        righthalf = pools_list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            comparing_times = comparing_times + 1
            if lefthalf[i].max_number > righthalf[j].max_number:
                change_times = change_times + 1
                pools_list[k] = lefthalf[i]
                i = i + 1
            else:
                change_times = change_times + 1
                pools_list[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            change_times = change_times + 1
            pools_list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            change_times = change_times + 1
            pools_list[k] = righthalf[j]
            j = j + 1
            k = k + 1


selection("file.cvs")

file = open("file.cvs", "r")
pools_list = []
for line in file:
    string = line
    str_list = string.split(",")
    pool = Pool(str_list[0], str_list[1], str_list[2])
    pools_list.append(pool)

merge_time_start = time.process_time()

merge_sort(pools_list)

merge_time_stop = time.process_time()

print("Merge Sort")
print("Sorting time:  " + str((merge_time_stop - merge_time_start)))
print("Result")
for i in range(0, len(pools_list)):
    print_object(pools_list[i])
