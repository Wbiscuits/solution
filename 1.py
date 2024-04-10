# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n=len(source)
        m=len(target)
        j=ans=0
        while j<m:
            i=0
            k=j
            while i<n and k<m:
                if source[i]==target[k]:
                    k+=1
                i+=1
            if k==j:
                return -1
            j=k
            ans+=1
        return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    s = solution.shortestWay('xzyzy', 'xzyxz')
    print(s)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
