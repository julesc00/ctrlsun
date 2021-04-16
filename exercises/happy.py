
class Solution(object):
    """
    Determine if an entered number is happy:
        1. Define if n is equal to 1 return True.
        2. Define if n is in set visited return False.
        3. Format n accordingly.
    """

    def is_happy(self, n):
        return self.solve(n, {})

    def solve(self, n, visited):
        if n == 1:
            return True
        if n in visited:
            return False
        visited[n] = 1
        n = str(n)
        my_l = list(n)
        my_l = list(map(int, my_l))
        temp = 0

        for i in my_l:
            temp += (i**2)

        return self.solve(temp, visited)


ob1 = Solution()
op = ob1.is_happy(2)
print(f"Is Happy: {op}")
