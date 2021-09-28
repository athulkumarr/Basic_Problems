
  def minWindow(self, s: str, t: str) -> str:

      if s == "" or t == "":                          # If any one string is empty, return null 
          return ""

      dict_t = {i:t.count(i) for i in t}              # contains the count of each character in t
      l, r = 0, 0                                     # left and right end of the window
      window = {}                                     
      required = len(dict_t.keys())                   # no of unique characters to be present
      formed = 0                                      # no of characters obtained so far in the current sliding window
      ans = float("inf"), None, None                  # a tuple with window size, start and end of the window

      while r < len(s):
          ch = s[r]
          window[ch] = window.get(ch, 0) + 1
          if ch in t and window[ch] == dict_t[ch]:    # if we have obtained enough number of this character
              formed += 1
          while l<=r and formed == required:          # try to contract the window by incrementing l
              ch = s[l]
              if r-l+1 < ans[0]:
                  ans = (r-l+1, l, r)
              window[ch] -= 1
              if ch in t and window[ch] < dict_t[ch]: # if we have removed a required character
                  formed -= 1
              l = l + 1

          r += 1                                      # expanding the window by incrementing r

      if ans[0] > len(s):
          return ""
      return s[ans[1]:ans[2]+1]
