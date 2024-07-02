def average(*numbers):
    if not numbers:
        return 0
    
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    
    return average