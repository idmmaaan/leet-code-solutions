class Solution:

    def intToRoman(self, num: int) -> str:

        if num < 1 :
            return 'Please provide positive number.'
        
        list_num = list(str(num))
        roman_nums = []
        order = 0
        for val in reversed(list_num):
            order+=1
            roman_nums.append(self.resolve_roman_number(order, int(val)))

        return "".join(roman_nums[::-1])
            
    
    def resolve_roman_number(self, order: int, num: int) -> str:
        if order == 1 :
            if num == 9:
                return "IX"
            elif num > 5:
                return "V" + ("I" * (num - 5))
            elif num == 5:
                return "V"
            elif num == 4:
                return "IV"
            elif num < 4:
                return num * "I"
            else: return ''
        elif order == 2 :
            if num == 9:
                return "XC"
            elif num > 5:
                return "L" + ("X" * (num - 5))
            elif num == 5:
                return "L"
            elif num == 4:
                return "XL"
            elif num < 4:
                return num * "X"
            else: return ''
        elif order == 3 :
            if num == 9:
                return "CM"
            elif num > 5:
                return "D" + ("C" * (num - 5))
            elif num == 5:
                return "D"
            elif num == 4:
                return "CD"
            elif num < 4:
                return num * "C"
            else: return ''
        elif order == 4 :
            return num * "M"
        else: return ''