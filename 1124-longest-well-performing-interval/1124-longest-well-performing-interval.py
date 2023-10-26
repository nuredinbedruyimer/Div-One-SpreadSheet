class Solution(object):
    def longestWPI(self, hours):
        def wellPerformLong(hours):
            tiring_days = 0
            m_days = 0
            hashmap = {}
            for right in range(len(hours)):
                if hours[right]>8:
                    tiring_days += 1 
                else:
                    tiring_days-=1

                if tiring_days>0:
                    m_days = max(m_days,right+1)
                if tiring_days not in hashmap:
                    hashmap[tiring_days]=right
                if tiring_days-1 in hashmap:
                    m_days = max(m_days,right-hashmap[tiring_days-1])
            return max(m_days,float('-inf'))
        return wellPerformLong(hours)


   
        