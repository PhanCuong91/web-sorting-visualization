from queue import Queue
class Sortings:
    def __init__(self):
        pass

    def selection_sort( array):
        n = len(array)
        print(array)
        all_steps_arr = []
        all_id = []
        all_steps_arr.append(array[0:n])
        all_id.append([-1,-1])
        for i in range(n):
            m = i
            for j in range(i+1, n):
                all_steps_arr.append(array[0:n])
                all_id.append([m,j])
                if array[m] > array[j]:
                    m = j
            if m != i:
                tmp = array[i]
                array[i] = array[m]
                array[m] = tmp

        all_steps_arr.append(array[0:n])
        all_id.append([-1,-1])
        return [all_steps_arr, all_id]

    