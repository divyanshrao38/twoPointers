def twoSum( numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                
def twoSumOptimized( numbers: list[int], target: int) -> list[int]:
        high = len(numbers) - 1
        low = 0
        while low < high:
            if numbers[low] + numbers[high] == target:
                return [low+1, high+1]
            elif numbers[low] + numbers[high] < target:
                low += 1
            else:
                high -= 1
print(twoSum([2,7,11,15], 9))
print(twoSumOptimized([2,7,11,15], 9))