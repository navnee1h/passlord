import os
import subprocess
from datetime import datetime
from itertools import product

class TextColors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    DARK_GREEN = "\033[32m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

ascii_art = """
\033[94m\033[1m         o  o   o  o\033[0m 
\033[94m\033[1m         |\\/ \\^/ \\/|\033[0m               \033[93m█▀▄ ▄▀▄ ▄▀▀ ▄▀▀ █   ▄▀▄ █▀▄ █▀▄\033[0m  
\033[94m\033[1m         |,-------.|\033[0m               \033[93m█▀  █▀█ ▄██ ▄██ █▄▄ ▀▄▀ █▀▄ █▄▀\033[0m          
\033[94m\033[1m       ,-.\033[93m(|)   (|)\033[94m\033[1m,-.\033[0m                                     \033[93mv1.0.0\033[0m
\033[94m\033[1m       \\_*._ ' '_.* _/\033[0m         \033[93m\033[1mAdvanced customizable wordlist generator
\033[94m\033[1m        /`-.`--' .-'\\\033[0m        ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━●\033[0m
\033[94m\033[1m   ,--./    `---'    \\,--.\033[0m   ┃   https://medium.com/@navnee1h            ┃
\033[94m\033[1m   \\   |(  )     (  )|   /\033[0m   ┃   https://www.linkedin.com/in/navnee1h    ┃
\033[94m\033[1m    \\  | ||       || |  /\033[0m    ┃   https://github.com/navnee1h/passlord    ┃
\033[94m\033[1m     \\ | /|\\     /|\\ | /\033[0m     ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━●\033[0m
\033[94m\033[1m     /  \\-._     _,-/  \\\033[0m      ✯ Edit rules.txt for personalized wordlist changes
\033[94m\033[1m    //| \\\\  `---'  // |\\\\\033[0m     ✯ Input details about your target 
\033[94m\033[1m   /,-.,-.\\       /,-.,-.\\\033[0m    ✯ Skip the question by hitting Enter
\033[94m\033[1m  o   o   o      o   o    o\033[0m
"""

def modify_word(word):
    #uppercase_word = word.upper()
    lowercase_word = word.lower()
    titlecase_word = word.title()
    return [lowercase_word, titlecase_word]
    
# Function to check for and remove duplicates in each array
def remove_duplicates(modified_array):
    seen = set()
    modified_array_no_duplicates = []
    
    for word_set in modified_array:
        unique_set = []
        for word in word_set:
            if word not in seen:
                seen.add(word)
                unique_set.append(word)
        modified_array_no_duplicates.append(unique_set)
    return modified_array_no_duplicates

# Function to generate combinations of modified names
def get_name_combinations(name):
    modified_name = []
    if name:
        modified_name = [modify_word(word) for word in name.split()]
    return remove_duplicates(modified_name)

# Function to generate combinations of all names
def generate_name_combinations():

    # Ask the user to input names
    first_name = input(f"{TextColors.BLUE}〘〙 First Name  : {TextColors.RESET}").strip()
    middle_name = input(f"{TextColors.BLUE}〘〙 Middle Name : {TextColors.RESET}").strip()
    last_name = input(f"{TextColors.BLUE}〘〙 Last Name   : {TextColors.RESET}").strip()
    nick_name = input(f"{TextColors.BLUE}〘〙 Nick Name   : {TextColors.RESET}").strip()
    other_name = input(f"{TextColors.BLUE}〘〙 Other Name  : {TextColors.RESET}").strip()
    
    firstname = get_name_combinations(first_name)
    global fname
    fname = [''.join(combination) for combination in product(*firstname)]
    
    middlename = get_name_combinations(middle_name)
    global mname
    mname = [''.join(combination) for combination in product(*middlename)]

    lastname = get_name_combinations(last_name)
    global lname
    lname = [''.join(combination) for combination in product(*lastname)]

    nickname = get_name_combinations(nick_name)
    global nname
    nname = [''.join(combination) for combination in product(*nickname)]

    othername = get_name_combinations(other_name)
    global oname
    oname = [''.join(combination) for combination in product(*othername)]
    

def modify_word(word):
    #uppercase_word = word.upper()
    lowercase_word = word.lower()
    titlecase_word = word.title()
    
    return [lowercase_word, titlecase_word]
    
# Function to check for and remove duplicates in each array
def remove_duplicates(modified_array):
    seen = set()
    modified_array_no_duplicates = []
    for word_set in modified_array:
        unique_set = []
        for word in word_set:
            if word not in seen:
                seen.add(word)
                unique_set.append(word)
        modified_array_no_duplicates.append(unique_set)
    return modified_array_no_duplicates

# Function to generate combinations of modified names
def get_name_combinations(name):
    modified_name = []
    if name:
        modified_name = [modify_word(word) for word in name.split()]
    return remove_duplicates(modified_name)

def generate_other_combinations():
    gf_name = input(f"{TextColors.BLUE}〘〙 Girl Friend : {TextColors.RESET}").strip()
    house_name = input(f"{TextColors.BLUE}〘〙 House Name  : {TextColors.RESET}").strip()
    pet_name = input(f"{TextColors.BLUE}〘〙 Pet Name    : {TextColors.RESET}").strip()
    company_name = input(f"{TextColors.BLUE}〘〙 Company Name: {TextColors.RESET}").strip()
    other_name = input(f"{TextColors.BLUE}〘〙 Other Name  : {TextColors.RESET}").strip()

    gfname = get_name_combinations(gf_name)
    global gf
    gf = [''.join(combination) for combination in product(*gfname)]

    hname = get_name_combinations(house_name)
    global house
    house = [''.join(combination) for combination in product(*hname)]

    pname = get_name_combinations(pet_name)
    global pet
    pet = [''.join(combination) for combination in product(*pname)]

    cname = get_name_combinations(company_name)
    global company
    company = [''.join(combination) for combination in product(*cname)]

    otname = get_name_combinations(other_name)
    global othername
    othername = [''.join(combination) for combination in product(*otname)]
    

dyear = []
dob = []

def generate_dob_combinations():
    def get_valid_date_input():
        while True:
            dob_input = input(f"{TextColors.BLUE}〘〙 DoB (DD MM YYYY): {TextColors.RESET}")
            if not dob_input:
                #skip dob entry
                return None
            try:
                dob_date = datetime.strptime(dob_input, '%d %m %Y').date()
                return dob_date
            except ValueError:
                print(f"{TextColors.RED}Invalid date format.{TextColors.RESET}")
                
    global dyear, dob
    dob_date = get_valid_date_input()
    
    if dob_date:
        dyear = [str(dob_date.year)]
        
        # Store various combinations of date of birth as strings
        dob = [
            dob_date.strftime("%d%m%Y"),  # 04082009
            #dob_date.strftime("%Y%m%d"), # 20090804
            #dob_date.strftime("%d%m%y"), # 040809
            #dob_date.strftime("%m%y"),   # 0809
            dob_date.strftime("%d"),      # 04
            dob_date.strftime("%m"),      # 08
            #dob_date.strftime("%d%m"),   # 0408
            str(dob_date.day)             # 4
        ]
        
        month = dob_date.month
        day = dob_date.day
        

ophn = []
phn = []

def generate_mob_combinations():
    global ophn, phn
    def phn_check():
    
        global ophn, phn
        def modify_digits(phone_number):
            return [
                #phone_number[:6],
                #phone_number[-6:],
                #phone_number[:5],
                #phone_number[-5:],
                phone_number[:4],
                phone_number[-4:],
                phone_number[:3],
                phone_number[-3:],
                phone_number[:2],
                phone_number[-2:]
            ]

        def get_valid_phone_number():
            while True:
                user_phone_number = input(f"{TextColors.BLUE}〘〙 Phn (10 digits) : ")
                # Check if the user pressed Enter to skip
                if not user_phone_number:
                    return None
                if user_phone_number.isdigit() and len(user_phone_number) == 10:
                    return user_phone_number
                else:
                    print(f"{TextColors.RED}Enter a valid 10-digit number.{TextColors.RESET}")
                    
        user_phone_number = get_valid_phone_number()
        if user_phone_number is None:
            return [], []
        ophn = [user_phone_number]
        
        # Save the first and last 6, 5, 4, 3, 2 digits in a single array
        phn = modify_digits(user_phone_number)
        return ophn, phn
    ophn, phn = phn_check()
    

def generate_all_combinations():                                                                 
    max_digits = 6
    combinations = []

    # Generate combinations of consecutive numbers
    for i in range(10):
        for j in range(1, min(max_digits, 10 - i)):
            num = ''.join(str(k % 10) for k in range(i, i + j + 1))
            combinations.append(num)

    return combinations

def print_all_generated(start_year, end_year):
    # Create an array of years
    global years,symbols,rnum1,rnum2
    years = [str(year) for year in range(start_year, end_year + 1)]

    # Create an array of symbols
    symbols = ['@', '_', '.']
    rnum1 = generate_all_combinations()
    additional_elements = ["7890", "8", "89", "890", "9", "90"]
    rnum2 = [ "11", "22", "33", "44", "55", "66", "77", "777", "88","888", "99",]
    rnum1.extend(additional_elements)
start_year = 1970
end_year = 2024


def combine_and_count(arr_pointers):
    lengths = [len(globals().get(pointer, [])) for pointer in arr_pointers]

    # Check if there are any empty arrays
    if 0 in lengths:
        return 0
    count = 1
    for length in lengths:
        count *= length
    return count


def combine_and_write(arr_pointers, output_file):
    # Check if there are any non-empty arrays to combine
    if any(not globals().get(pointer, []) for pointer in arr_pointers):
        return
    # Get all possible combinations of arrays
    import itertools
    combinations = [globals().get(pointer, []) for pointer in arr_pointers]
    all_combinations = list(itertools.product(*combinations))

    # Write each non-empty combination line by line, skipping combinations with empty arrays
    for combo in all_combinations:
        if all(combo_part for combo_part in combo):
            combined_result = ''.join(combo)
            output_file.write(combined_result + '\n')



def process_file():
    try:
        # Get the directory where the script is located
        script_directory = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the path to the patterns folder
        patterns_directory = os.path.join(script_directory, "patterns")
        
        # Construct the path to rules.txt in the patterns folder
        input_file_path = os.path.join(patterns_directory, "rules.txt")

        while True:
            # Prompt the user for the output file name
            output_file_name = input(f"{TextColors.BLUE}〘〙 Enter the output file name: {TextColors.RESET}").strip()
            if not output_file_name:
                print(f"{TextColors.RED}  ⭆  Output file name cannot be blank.{TextColors.RESET}")
            else:
                break

        # Combine the path and name to create the complete output file path
        global output_file_path
        output_file_path = os.path.join(os.getcwd(), output_file_name)

        with open(input_file_path, 'r') as file, open(output_file_path, 'w') as output_file:
            for line in file:
                # Assuming there's a function combine_and_write for processing and writing
                arr_pointers = line.strip().split("@")
                combine_and_write(arr_pointers, output_file)

    except FileNotFoundError:
        print(f"{TextColors.RED}  ⭆  File not found: {input_file_path}{TextColors.RESET}")
        exit()
    except Exception as e:
        print(f"{TextColors.RED}  ⭆  An error occurred: {e}{TextColors.RESET}")
        exit()



def update_file_and_print_line_count():
    with open(output_file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)

        unique_lines = set()  # Use a set to efficiently track unique lines
        for line in lines:
            stripped_line = line.strip()
            
            if len(stripped_line) >= 6 and stripped_line not in unique_lines:
                file.write(line)
                unique_lines.add(stripped_line)

        file.truncate()
        updated_line_count = len(unique_lines)
        print(f"{TextColors.BLUE}After deduping, {TextColors.RESET}{updated_line_count}{TextColors.BLUE} lines remain!{TextColors.RESET}")
        print(f"{TextColors.BLUE}Results written to {TextColors.RESET}{output_file_path}")



def check_file_existence(file_name):
    try:
        # Get the directory where the script is located
        script_directory = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the path to the patterns folder
        patterns_directory = os.path.join(script_directory, "patterns")
        
        # Construct the path to rules.txt in the patterns folder
        file_path = os.path.join(patterns_directory, file_name)

        if not os.path.isfile(file_path):
            print(f"{TextColors.RED} Error! {file_name} not found.{TextColors.RESET}")
            exit()

        # Read the contents of the input file
        with open(file_path, 'r') as input_file:
            # Read the content of the file without printing it
            content = input_file.read()
            # Do something with the content, if needed

    except Exception as e:
        print(f"{TextColors.RED} ⭆ An error occurred: {e}{TextColors.RESET}")
        exit()

# Call the function with the filename
file_name = "rules.txt"
check_file_existence(file_name)

def run_main_function():
    #file_to_check = "rules.txt"

    try:
        check_file_existence(file_name)
        while True:
            print(ascii_art)
            generate_name_combinations()
            generate_other_combinations()
            generate_dob_combinations()
            generate_mob_combinations()

            # Execute the functions after checking check_empty_arrays
            print_all_generated(start_year, end_year)
            process_file()
            update_file_and_print_line_count()
            break
    except KeyboardInterrupt:
        print(f"\n{TextColors.RED}\033[1m Exiting....\033[0m{TextColors.RESET}")
        # Additional cleanup or exit code can be added here if needed

if __name__ == "__main__":
    run_main_function()