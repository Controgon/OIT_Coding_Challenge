roman_conversion = {"I": "1", "V":"5", "X":"10", "L":"50", "C":"100", "D":"500", "M":"1000"}
decimal_conversion = {"1":"I", "5":"V", "10":"X", "50":"L", "100":"C", "500":"D", "1000":"M"}

def roman_converter(letters):
    nums = []
    """seperates letters"""
    for letter in letters:
        nums.append(roman_conversion[letter])
    return nums
    
          
def is_valid(nums):
    """checks rules"""
    prev = 0
    for num in nums:
        if int(num) == 10:
            if prev == 5:
                return False
        prev = int(num)
    return True
    
def math(nums):
    """adds/subtracts based on positions"""
    prev = 0
    total = 0
    if is_valid(nums):
        for num in nums:
            if prev < int(num):
                total -= prev * 2
                total += int(num)
            else:
                total += int(num)
            prev = int(num)
        return str(total) if total > 0 else "Invalid Number"
        



def decimal_converter(numbers):
    conversion = ""
    counter = 1
    nums = int(numbers)
    prev = 0
    while nums > 0:
        find = nums % 10
        for key in decimal_conversion:
            i = int(key)
            """checks if the number i need to find is an exact number in the dictionary"""
            if i == find * counter:
                roman = decimal_conversion[key]
                nums //= 10
                counter += 1
                prev = i
                conversion = roman + conversion
                break
            #checks for small subtraction
            elif int(prev) < find * counter and i > find * counter:
                for k in decimal_conversion:
                    if i - int(k) == find * counter:
                        roman = decimal_conversion[k] + decimal_conversion[key]
                        nums //= 10
                        counter += 1
                        prev = i
                        conversion = roman + conversion
                        break
                #checks how much addition is needed
                #my broken part, I needed to find a way to get this to not run if the one before it succeeded.
                    roman = decimal_conversion[str(prev)]
                    for k in decimal_conversion:
                        d = roman_conversion[decimal_conversion[k]]
                        if d[0] == "1":
                            temp = 1
                            while temp < 4:
                                if prev + (int(k) * temp) == find:
                                    for i in range(temp):
                                        roman += decimal_conversion[k]
                                    nums //= 10
                                    counter += 1
                                    prev = i
                                    conversion = roman + conversion
                                    break
                                temp += 1
    return conversion
        




def main():
    """I want to add all of the times that a pary of the number has been added or subtracted from. (5 - 1) + (50 - 10)"""
    while True:
        question = input("Enter Roman Numerals or Decimal Numbers:")
        if question.isalpha():
            nums = roman_converter(question.upper)
            print(math(nums))
            break
        elif question.isdigit():
            print(decimal_converter(question))
            break
        else:
            print("Sorry, input a Roman Numeral or a Decimal Number")
            
if __name__ == "__main__":
    main()