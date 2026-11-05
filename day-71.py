
class Solution:
    def powerSet(self, s):
        result = []

        def generate(index, current):
            if index == len(s):
                result.append(current)
                return

            # Include current character
            generate(index + 1, current + s[index])

            # Exclude current character
            generate(index + 1, current)

        generate(0, "")

        return sorted(result)
