n = int(raw_input())
nums = map(int, raw_input().split())    
print sorted(list(set(nums)))[-2]