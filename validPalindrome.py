def is_palindrome(s):
  idx_start = 0
  idx_end = len(s) - 1
  if(len(s) <= 1):
    return True
  while idx_start <= idx_end:
    if s[idx_start] != s[idx_end]:
      return False
    idx_start +=1
    idx_end -=1

  return True

print(is_palindrome("abba"))