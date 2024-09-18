import time
import random

def get_texts_from_file():
    with open("text.txt", "r") as file:
        return file.readlines()

def calculate_wpm(start_time, end_time, user_input):
    total_time_minutes = (end_time - start_time) / 60
    word_count = len(user_input.split())
    return word_count / total_time_minutes if total_time_minutes > 0 else 0

def calculate_error_details(user_input, sample_text):
    errors = []
    min_length = min(len(user_input), len(sample_text))
    
    for index in range(min_length):
        if user_input[index] != sample_text[index]:
            errors.append((index, sample_text[index], user_input[index]))
    
    if len(user_input) < len(sample_text):
        for index in range(len(user_input), len(sample_text)):
            errors.append((index, sample_text[index], ''))

    if len(user_input) > len(sample_text):
        for index in range(len(sample_text), len(user_input)):
            errors.append((index, '', user_input[index]))
    
    return errors

def display_errors(errors, sample_text):
    for index, expected_char, user_char in errors:
        if expected_char:
            print(f"Position {index + 1}: Expected '{expected_char}', but got '{user_char}'")
        else:
            print(f"Position {index + 1}: Extra character '{user_char}'")

def typing_test():
    print("Typing Speed Test\n")
    texts = get_texts_from_file()
    number_of_lines = 3 # audjust it as you like
    
    if len(texts) < number_of_lines:
        print("Not enough lines in the file.")
        return
    
    sample_lines = random.sample(texts, number_of_lines)
    
    sample_text = ""
    for line in sample_lines:
        sample_text += line.strip()
    
    print(sample_text)
    input("\nPress Enter to start...")
    
    start_time = time.time()
    user_input = input("\nYour input: ").strip()
    end_time = time.time()
    
    wpm = calculate_wpm(start_time, end_time, user_input)
    error_details = calculate_error_details(user_input, sample_text)
    error_percentage = (len(error_details) / max(len(sample_text), 1)) * 100
    
    print(f"\nWords Per Minute (WPM): {wpm:.2f}")
    print(f"Error Percentage: {error_percentage:.2f}%")
    display_errors(error_details, sample_text)

typing_test()
