class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}
        max_freq = 0
        max_window = 0
        R = 0
        L = 0

        while(R < len(s)):

            #We update the frequency of the current element
            freq[s[R]] = freq.get(s[R], 0) + 1
            #We then compute the max frequency overall
            max_freq = max(max_freq, freq[s[R]])

            #if that amount surpasses our maximum given
            while(R - L + 1 - max_freq > k):
                
                #we remove 1 occurance of that number
                freq[s[L]] -= 1
                #We contract the window
                L += 1


            #We compute the window, which we know is valid
            window = R - L + 1
            max_window = max(max_window, window)
            #We then try expanding it
            R += 1
        return max_window

