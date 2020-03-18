class Solution:
    def charMapping( s1: str, s2: str) -> bool:
        map = [-1]*256
        if len(s1)!=len(s2):
            return False
        boolmap = [-1] * 256
        for i in range(len(s1)):
            if map[ord(s1[i])] == -1: 
                if boolmap[ord(s2[i])] == True: 
                    return False
                boolmap[ord(s2[i])] = True
                map[ord(s1[i])] = s2[i] 
            elif map[ord(s1[i])] != s2[i]: 
                return False
        return True
