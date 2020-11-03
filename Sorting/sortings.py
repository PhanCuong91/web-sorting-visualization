from queue import Queue
class Sortings:
    def __init__(self):
        pass

    def selection_sort( array):
        n = len(array)
        print(array)
        all_steps_arr = []
        all_steps_arr.append(array[0:n])
        for i in range(n):
            m = i
            for j in range(i+1, n):
                if array[m] > array[j]:
                    m = j
            if m != i:
                tmp = array[i]
                array[i] = array[m]
                array[m] = tmp
                # print("arr",array)
                all_steps_arr.append(array[0:n])
                # print("all arr",all_steps_arr)
        return all_steps_arr

    