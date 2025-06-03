#Lesson-12

#Task-1

import threading

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Thread function to find primes in a subrange
def find_primes_in_range(start, end, result):
    primes = []
    for number in range(start, end):
        if is_prime(number):
            primes.append(number)
    result.extend(primes)

# Main function to divide range and manage threads
def main(start, end, num_threads=4):
    thread_list = []
    results = []
    threads_results = [[] for _ in range(num_threads)]
    range_size = (end - start) // num_threads

    for i in range(num_threads):
        sub_start = start + i * range_size
        sub_end = start + (i + 1) * range_size if i != num_threads - 1 else end
        thread = threading.Thread(target=find_primes_in_range, args=(sub_start, sub_end, threads_results[i]))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    for partial_result in threads_results:
        results.extend(partial_result)

    results.sort()
    print(f"Prime numbers between {start} and {end}:")
    print(results)

# Example usage
if __name__ == "__main__":
    main(start=10, end=100, num_threads=4)

#Task-2
    import threading
from collections import Counter
import re

# Function to process a portion of lines and count words
def count_words(lines, partial_results, index):
    word_count = Counter()
    for line in lines:
        words = re.findall(r'\b\w+\b', line.lower())  # Extract words, case-insensitive
        word_count.update(words)
    partial_results[index] = word_count  # Store result in shared list

def main(filename, num_threads=4):
    # Step 1: Read all lines from the file
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Step 2: Split lines into chunks for each thread
    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    threads = []
    partial_results = [None] * num_threads  # Shared list to store results

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else total_lines
        thread_lines = lines[start:end]

        thread = threading.Thread(target=count_words, args=(thread_lines, partial_results, i))
        threads.append(thread)
        thread.start()

    # Step 3: Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Step 4: Merge all results
    final_count = Counter()
    for result in partial_results:
        final_count.update(result)

    # Step 5: Print summary
    for word, count in final_count.most_common(20):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main("large_text_file.txt", num_threads=4)

