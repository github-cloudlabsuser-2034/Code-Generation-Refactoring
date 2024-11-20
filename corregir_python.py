# A program that prompts the user for the number of elements to sum, takes those integers as input, and handles basic error cases.
   
MAX = 100

def calculate_sum(arr):
       result = 0
       for num in arr:
           result += num
       return result

def main():
    try:
        while True:
            n = int(input("Enter the number of elements to sum (1-100): "))
            if 1 <= n <= MAX:
                break
            else:
                print("Invalid input. Please provide a digit ranging from 1 to 100.")

        arr = []

        print(f"Enter {n} integers:")
        for _ in range(n):
            while True:
                try:
                    arr.append(int(input()))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        total = calculate_sum(arr)

        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        return

if __name__ == "__main__":
       main()