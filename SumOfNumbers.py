#lecture 5 homework
def sum_of_elements(numbers, ignore_negative=False):
    if ignore_negative:
        numbers = [num for num in numbers if num >= 0]
    return sum(numbers)
    
def main():
    
    u_input = input("Enter numbers separated by spaces: ")
    input_numbers = u_input.split()
    numbers = list(map(int, input_numbers))

    ignore_negative_input = input("Do you want to ignore negative numbers? (yes or no): ")
    ignore_negative = ignore_negative_input.lower() == 'yes'

    total_sum = sum_of_elements(numbers, ignore_negative)
    print("Sum:", total_sum)
    
if __name__ == "main":
    main()