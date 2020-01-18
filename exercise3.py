class Solution(object):
    def lengthOfLongestSubstring(self, s):
        self.s=s
        dic={}#生成空字典
        oldCounter=0
        newCounter=0
        flag=0
        substring=''
        for letter in self.s:#先生成字典，初值都为0
            dic[letter]=0
           # print(dic)

        for letter in self.s:
            if dic.get(letter)==0:
                flag=0
                dic[letter]=1
                substring=substring+letter
                newCounter = newCounter +1
            else: #值为1,则比较newCounter和oldCounter,字典全部置0
                #找出当前letter在substring中的位置
                substring
                for ll in self.s:
                    dic[ll] = 0
                flag=1
                if newCounter > oldCounter:#<=都可以不变
                    oldCounter=newCounter
                newCounter=1
                dic[letter] = 1
        if flag==0 and  newCounter > oldCounter:#一直没遇到重复的
            #<=都可以不变
             oldCounter=newCounter
        return oldCounter

if __name__ == '__main__':
 test0='abccdfgggggg'
 print(test0[4])
 test1=''
 test0=test1+'a'
 print(test0)

 #ss=Solution()
 #ss.lengthOfLongestSubstring(test0)
 #ss.lengthOfLongestSubstring(test1)