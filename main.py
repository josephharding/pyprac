

import re
import random


def run():
    num = raw_input("please enter a number:\n")
    number = int(num)
    print("you entered: {}".format(number + 1))
    if number % 2 == 0:
        print("this is even")
    else:
        print("this is odd")


def reverse_str(input_str):
    parts = re.split("\s+", input_str)
    #parts = input_str.split("\w")
    parts.reverse()
    output_str = " ".join(parts)
    return output_str

def comp():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    # one liner to return only the even elements
    b = [x for x in a if x % 2 == 0]
    print(b)

# 1 1 2 3 5 8
def fib(num):
    output = [0, 1]
    count = 0 
    while count < num and num > 0:
        output.append(output[count] + output[count + 1])
        count = count + 1
   
    output.pop(0)
    print(output)


# return the elements that are common between the lists
def overlap(a, b):
    # first way
    result = [x for x in set(a) if x in set(b)]
    print(result)

    # assume sorted, faster way
    common = []
    a_p = 0
    b_p = 0
    done = False
    while not done:
        if a[a_p] < b[b_p]:
            a_p = a_p + 1
        elif a[a_p] == b[b_p] and a[a_p] not in common:
            common.append(a[a_p])
        else:
            b_p = b_p + 1

        if a_p == len(a) or b_p == len(b):
            done = True

    print(common)


# find the pairs of elements from a and b that sum to target
def find_sums(a, b, target):
    # first sort the two lists
    a.sort()
    b.sort()

    match = []
    a_p = 0
    b_p = len(b) - 1
    while a_p < b_p:
        summed = a[a_p] + b[b_p]
        if summed == target:
            match.append([a[a_p], b[b_p]])
        elif summed > target:
            b_p = b_p - 1
        else:
            a_p = a_p + 1

    print(match)


def get_digits(input_int):
    result = []
    while input_int > 10:
        result.append(input_int % 10)
        input_int = input_int / 10
    
    result.append(input_int)
    result.reverse()
    return result


def cows_n_bulls():
    random_int = random.randint(1000, 9999)
    random_int_str = str(random_int)
    running = True
    while running:
        guess = int(raw_input("please enter a number:\n"))
        if guess >= 1000 and guess <= 9999:
            # challenge is accessing the digit in each place
            guest_str = str(guess)
            cow = 0
            bull = 0
            for idx, char in enumerate(guest_str):
                if char == random_int_str[idx]:
                    cow = cow + 1
                else:
                    bull = bull + 1
            
            print("{c} cows, {b} bulls".format(c=cow, b=bull))
            if(cow == 4):
                running = False

        else:
            print("try again")


def get_all_even(start, end):
    for elem in range(start, end):
        if elem % 2 == 0:
            print(elem)


def fast_all_even(start, end):
    nums = range(start, end)
    idx = 0
    while idx < len(nums):
        if nums[idx] % 2 != 0:
            idx = idx + 1 

        print(nums[idx])
        idx = idx + 2


def write_to_file(content):
    with open("/tmp/myfile", 'w') as fh:
        fh.write(content)


def joe_gen():
    for x in range(3):
        yield x


def play_with_generators():
    joe_g = joe_gen()
    print(next(joe_g))
    print(next(joe_g))
    print(next(joe_g))


def word_count(in_str):
    in_str_list = re.split("\W", in_str)
    in_str_dict = {}
    for word in in_str_list:
        if word in in_str_dict:
            in_str_dict[word] += 1
        else:
            in_str_dict[word] = 1

    print(in_str_dict)


def is_isogram(word):
    word_set = set()
    for char in word:
        if char in word_set:
            return False
        
        word_set.add(char)

    return True


def is_palin(word):
    a = 0
    b = len(word) - 1
    while a < b:
        if word[a] != word[b]:
            return False
        a += 1
        b -= 1

    return True


def gen_number_word(num_int):
    print("=======input number: {n}".format(n=num_int))
    num_to_words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens_to_words = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_to_words = ["", "", "twenty", "thirty", "fourty", "fifity", "sixty", "seventy", "eighty", "ninety"]
    # 3000 => three thousand
    # 3001 => three thousand one
    # 3333 => three thousand three hundrend thirty three
    words = []
    # consume number starting from smallest to largest word
    while num_int > 0:
        bite = 0
        if len(str(num_int)) > 4:
            bite = 3
        elif len(str(num_int)) > 3:
            bite = 2
        elif len(str(num_int)) > 2:
            bite = 3

        current = int(str(num_int)[:2])
        num_int = int(str(num_int)[2:])

        print(current)
        # these are all the unique ways to say 0 - 99, above that you take what you got and add a hundred, thousand, million, billion, etc
        if current >= 20:
            digit = current / 10
            words.append(tens_to_words[digit]) 

        elif current >= 10:
            digit = current % 10
            words.append(teens_to_words[digit]) 
  
        elif current > 0:
            words.append(num_to_words[current]) 

        count = len(str(num_int))
        if count == 2:
            words.append("hundred")
        elif count == 3:
            words.append("thousand")


        print(num_int)


    print(words)


if __name__ == '__main__':
    #print(reverse_str("hello world, my name is joe"))
    #overlap([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    #find_sums([3, 4, 7, 6, 8], [2, 4, 0, 2, 5], 8)
    #cows_n_bulls()
    #print(get_digits(4566))
    #fast_all_even(-3, 13)
    #write_to_file("joe harding")
    #play_with_generators()
    #word_count("the grey fox is a dog is a grey dog my dog not grey")
    #print(is_isogram("apple"))
    #print(is_palin("racecar"))
    gen_number_word(870)

