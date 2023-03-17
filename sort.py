import time
from sortValidator import SortValidator
from csvReader import CsvReader
from csvWriter import CsvWriter

class SortAlgorithm:
    def bubble_sort(raw_list):
        n = len(raw_list)
        for i in range(n):
            for j in range(n-1-i):
                y = j + 1
                if (raw_list[j] > raw_list[y]):
                    temp = raw_list[y]
                    raw_list[y] = raw_list[j]
                    raw_list[j] = temp

        return raw_list
    
    def selection_sort(raw_list):
        n = len(raw_list)
        for i in range(n-1):
            lowest_num = raw_list[i]
            for j in range(i, n+1): 
                if (j == n):
                    if (lowest_num == raw_list[i]):
                        continue
                    raw_list[position] = raw_list[i]
                    raw_list[i] = lowest_num
                    
                elif (lowest_num > raw_list[j]):
                    position = j
                    lowest_num = raw_list[j]

        return raw_list
    
    def insertion_sort(raw_list):
        n = len(raw_list)
        for i in range(n-1):
            if (raw_list[i] > raw_list[i+1]):
                temp_value = raw_list[i+1]
                raw_list[i+1] = raw_list[i]
                raw_list[i] = temp_value
                for j in range(i, 0, -1):
                    if (raw_list[j] < raw_list[j-1]):
                        temp_value = raw_list[j-1]
                        raw_list[j-1] = raw_list[j]
                        raw_list[j] = temp_value

        return raw_list

    def merge_sort(raw_list):
        if len(raw_list) <= 1:
            return raw_list

        # Divide the array into two halves
        mid = len(raw_list) // 2
        left_half = raw_list[:mid]
        right_half = raw_list[mid:]

        # Recursively sort each half
        left_half = SortAlgorithm.merge_sort(left_half)
        right_half = SortAlgorithm.merge_sort(right_half)

        # Merge the two sorted halves
        merged = []
        i = 0
        j = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                merged.append(left_half[i])
                i += 1
            else:
                merged.append(right_half[j])
                j += 1

        # Add any remaining elements from the left or right halves
        merged += left_half[i:]
        merged += right_half[j:]

        return merged
    
    def quick_sort(raw_list):
        return
            
def sortSelector(selected_alg):
    if(selected_alg == "1"):
        sorted_list = SortAlgorithm.bubble_sort(raw_list)
    elif(selected_alg == "2"):
        sorted_list = SortAlgorithm.selection_sort(raw_list)
    elif(selected_alg == "3"):
        sorted_list = SortAlgorithm.insertion_sort(raw_list)
    elif(selected_alg =="4"):
        sorted_list = SortAlgorithm.merge_sort(raw_list)
    else:
        raise ValueError("Enter a valid value.")
    return sorted_list

if __name__ == '__main__':
    csv_reader = CsvReader()
    raw_list = list(map(int, csv_reader.read_csv_file()))
    raw_list_copy = raw_list.copy()
    print("Select type of sorting algorythm")
    selected_alg = input("Available choices are: Bubble Sort(enter 1), Selection Sort(enter 2), Insertion Sort(enter 3), Merge Sort(enter 4): ")
    start = time.time()
    sorted_list = sortSelector(selected_alg)
    
    
    is_valid = SortValidator.validate(sorted_list)
    is_missing = SortValidator.missing_number(raw_list_copy, sorted_list)

    csv_filename = 'sortedNumbers.csv'
    csv_writer = CsvWriter(csv_filename)
    csv_writer.save_csv(sorted_list)
    end = time.time()


    #print(sorted_list)
    print("Sorting was successful:", is_valid)
    print("Any missing numbers: ", is_missing)
    print("Execution in seconds:", end - start)