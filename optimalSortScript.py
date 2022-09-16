import sys       
import fileinput
import multiprocessing
words_list = []
for line in fileinput.input():
        words_list.append(line.replace("\n", "").lower())
                          
def merge_sort(inp):
    size = len(inp)
    if size > 1:
        middle = size // 2
        left_arr = inp[:middle]
        right_arr = inp[middle:]
 
        thread1 = multiprocessing.Process(target=merge_sort2, args=(left_arr,))
        thread2 = multiprocessing.Process(target=merge_sort2, args=(right_arr,))
        thread1.start()
        thread1.join()

        thread2.start()
        thread2.join()
        
        p = 0
        q = 0
        r = 0
        while p < len(left_arr) and q < len(right_arr):
            if left_arr[p] < right_arr[q]:
              inp[r] = left_arr[p]
              p += 1
            else:
                inp[r] = right_arr[q]
                q += 1
             
            r += 1
 
        
        while p < len(left_arr):
            inp[r] = left_arr[p]
            p += 1
            r += 1 

        while q < len(right_arr):
            inp[r]=right_arr[q]
            q += 1
            r += 1
def merge_sort2(inp):
    size = len(inp)
    if size > 1:
        middle = size // 2
        left_arr = inp[:middle]
        right_arr = inp[middle:]
 
        merge_sort2(left_arr)
        merge_sort2(right_arr)
        p = 0
        q = 0
        r = 0
        while p < len(left_arr) and q < len(right_arr):
            if left_arr[p] < right_arr[q]:
              inp[r] = left_arr[p]
              p += 1
            else:
                inp[r] = right_arr[q]
                q += 1
             
            r += 1
 
        
        while p < len(left_arr):
            inp[r] = left_arr[p]
            p += 1
            r += 1 

        while q < len(right_arr):
            inp[r]=right_arr[q]
            q += 1
            r += 1
            
merge_sort(words_list)
print(words_list)
