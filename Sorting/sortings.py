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

    def insertion_sort(array):
        n = len(array)
        all_steps_arr = []
        all_id = []
        all_steps_arr.append(array[0:n])
        all_id.append([-1,-1])
        for i in range(1, n):
            # sort the next element to the exiting sorted array
            for j in range(i):
                all_steps_arr.append(array[0:n])
                all_id.append([i, j])
                # sort element: get next element and find suitable index in exiting sorted array
                # then delete next element  and insert it to the above index
                if array[i] < array[j]:
                    tmp = array[i]
                    array.pop(i)
                    array.insert(j, tmp)
                    break
        all_steps_arr.append(array[0:n])
        all_id.append([-1,-1])
        return [all_steps_arr, all_id]

    def merge_sort_s(array):
        n=len(array)
        all_steps_arr = []
        all_id = []
        all_steps_arr.append(array[0:n])
        all_id.append([-1,-1])
        Sortings.merge_sort(array, 0, n-1,all_steps_arr, all_id)
        all_steps_arr.append(array[0:n])
        all_id.append([-1,-1])
        return[all_steps_arr, all_id]

    def merge_sort(array, left, right, arr_step, arr_id):
        n=len(array)
        # split array
        if right - left >= 1:
            m = int((right - left)/2)
            # run merge_sort for first half of array
            Sortings.merge_sort(array, left, left+m, arr_step, arr_id)
            # run merge_sort for second half of array
            Sortings.merge_sort(array, left+m+1, right, arr_step, arr_id)
            # after run merge_sort, first and second shall be sorted
            # sort the first or second half of array
            i = left
            j = left + m+1
            tmp = []
            # 
            a = array[0:n]
            cnt = i
            a = array[0:n]
            arr_id.append([i, j])
            arr_step.append(a[0:n])
            while i <= left+m and j <= right:
                if array[i] >array[j]:
                    arr_id.append([i, j])
                    tmp.append(array[j])
                    a.pop(j)
                    a.insert(cnt, array[j])
                    arr_step.append(a[0:n])
                    j += 1
                else:
                    arr_id.append([i, j])
                    arr_step.append(a[0:n])
                    tmp.append(array[i])
                    i += 1
                cnt += 1
            while i <= left+m:
                arr_id.append([i, j-1])
                arr_step.append(a[0:n])
                tmp.append(array[i])
                i += 1

            while j <= right:
                arr_id.append([i-1, j])
                arr_step.append(a[0:n])
                tmp.append(array[j])
                j += 1
            array[left:right+1] = tmp

# a = Sortings()
# arr = [86,71,54,96,86]
# Sortings.merge_sort_s(arr)

    