from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0  # Where to write the compressed result
        read_index = 0  # Pointer to read through the input characters

        while read_index < len(chars):
            current_char = chars[read_index]  # Character being processed
            count = 0  # Count occurrences of the current character

            # Count the number of consecutive occurrences of current_char
            while read_index < len(chars) and chars[read_index] == current_char:
                read_index += 1
                count += 1

            # Write the character to the compression position
            chars[write_index] = current_char
            write_index += 1

            # If the count is greater than 1, write the count as individual digits
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        return write_index

print(Solution().compress(["a","a","b","b","c","c","c"]))
print(Solution().compress(["a"]))
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

# Faster code solution:

# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         prevChar = '!'
#         currCount = 0
#         idx = 0
#         for i in range(len(chars)):
#             if chars[i] != prevChar:
#                 if currCount > 1:
#                     chars[idx] = prevChar
#                     idx += 1
#                     for j in range(len(str(currCount))):
#                         chars[idx] = str(currCount)[j]
#                         idx += 1
#                 elif currCount == 1:
#                     chars[idx] = prevChar
#                     idx += 1
#                 prevChar = chars[i]
#                 currCount = 1
#             else:
#                 currCount += 1
#
#         if currCount > 1:
#             chars[idx] = prevChar
#             idx += 1
#             for j in range(len(str(currCount))):
#                 chars[idx] = str(currCount)[j]
#                 idx += 1
#             return idx
#         elif currCount == 1:
#             chars[idx] = prevChar
#             idx += 1
#
#         return idx