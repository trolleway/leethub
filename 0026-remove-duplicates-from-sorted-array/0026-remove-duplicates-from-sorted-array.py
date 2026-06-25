class Solution:
    def removeDuplicates(self, nums):
        if not nums:  # Handle empty list case
            return 0

        j = 0  # Pointer for the position of unique elements
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1  # Move to the next position for unique element
                nums[j] = nums[i]  # Assign the unique element

        return j + 1  # Return the length of the list with unique elements




"""
0,0,1,1,1,2,2,3,3,4
приводим к виду где дубликаты заменены на н
    !
0,n,1,1,1,2,2,3,3,4
    ^
цикл пока
ц2+=1
есле c1 is digit and [c2]==[c1]: [ц2]==none
else с1=с2
         
ц1=0
ц2=1
цикл пока 
если хц2ъ!=хц1ъ: ц2+=1
если хц2ъ=хц1ъ и ц2!=ц1: хц2ъ=н
инесли хц2ъ!=хц1ъ: ц1+=1
        !  
0,1,2,3,4,n,n,n,n,n
                  ^                
цикл 1 двигаем маркер 1 пока он не попадёт на н
цикл 2 двигаем маркер 2 начиная с позиции маркера 1, пока он не попадёт на цифру
своп значений под маркерами. к+=1
есле маркер2 на последнем элементе - конец
повтор цикла 1

"""