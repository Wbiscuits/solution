class Solution:
    def parentheses(self, s: str):
        print(s)
        charStack = []  # 字符栈
        subStack = [] #下标栈
        length = len(s)
        ans_list = [' '] * length
        for i in range(length):
            if s[i] == '(':
                charStack.append(s[i])
                subStack.append(i)
            elif s[i] == ')':
                if len(charStack) ==0:
                    ans_list[i]='?'
                else:
                    charStack.pop()
                    subStack.pop()
        while len(charStack)!=0:
            sub=subStack[-1]
            ans_list[sub]='x'
            charStack.pop()
            subStack.pop()

        print(''.join(ans_list) )
if __name__ == '__main__':
    solution = Solution()
    solution.parentheses('))))UUUU((()')