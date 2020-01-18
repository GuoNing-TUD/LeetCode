class Solution(object):
    def lengthOfLongestSubstring(self, s):
        self.s=s
        dic={}#生成空字典
        oldCounter=0
        newCounter=0
        substring=''
        for letter in self.s:#先生成字典，初值都为0
            dic[letter]=0
        #print(dic)
        for letter in self.s:
            if dic.get(letter)==0:
                dic[letter]=1
                substring=substring+letter
                newCounter = newCounter +1
            else: #值为1,则比较newCounter和oldCounter,字典全部置0
                #找出当前letter在substring中的位置
                if len(substring)>oldCounter:
                 oldCounter=len(substring)
                strBegin = substring.find(letter)+1
                for char in substring[0:strBegin]:
                    dic[char]=0
                temp = ''
                for i in range(newCounter - strBegin):
                    temp = temp + substring[strBegin + i]
                substring = temp+letter
                newCounter=len(substring)
                dic[letter] = 1
        if len(substring) > oldCounter:
                oldCounter = len(substring)
        return oldCounter

if __name__ == '__main__':
 test0='bpfbhmipx'
 test1='abcabcbb'
 test3='dvdf'
 ss=Solution()
 ss.lengthOfLongestSubstring(test0)
 ss.lengthOfLongestSubstring(test1)
 ss.lengthOfLongestSubstring(test3)
