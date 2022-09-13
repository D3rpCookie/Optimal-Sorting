import sys       
import fileinput
from threading import Thread
words_list = []
for line in fileinput.input(files ='wordlist.txt'):
        words_list.append(line.replace("\n", "").lower())
                          
def merge_sort(inp):
    size = len(inp)
    if size > 1:
        middle = size // 2
        left_arr = inp[:middle]
        right_arr = inp[middle:]
 
        thread1 = Thread(target=merge_sort, args=(left_arr,))
        thread2 = Thread(target=merge_sort, args=(right_arr,))
        thread1.start()
        thread1.join()

        thread2.start()
        thread2.join()
        
        p = 0
        q = 0
        r = 0
 
        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size and q < right_size:
            if left_arr[p] < right_arr[q]:
              inp[r] = left_arr[p]
              p += 1
            else:
                inp[r] = right_arr[q]
                q += 1
             
            r += 1
 
        
        while p < left_size:
            inp[r] = left_arr[p]
            p += 1
            r += 1

        while q < right_size:
            inp[r]=right_arr[q]
            q += 1
            r += 1
            
merge_sort(words_list)
print(words_list)
