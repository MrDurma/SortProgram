class SortValidator:
    def validate(list):
        """This function validates if numbers are sorted correctly"""
        n = len(list)
        for x in range(n-1):
            y = x + 1
            if (int(list[x]) > int(list[y])):
                return False
        return True
    
    def missing_number(raw_list, sorted_list):
        """This function checks if there are missing numbers"""
        sorted_list_copy = sorted_list.copy()
        for number in raw_list:
            if number not in sorted_list_copy:
                return True
            else:
                sorted_list_copy.remove(number)
        return False