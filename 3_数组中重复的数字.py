def duplication_in_array_1(numbers):
	"""
	题目一 找出数组中重复的数字
	原地修改数组
	时间O(n), 空间O(1)
	:type numbers: List[int]
	:rtype: int
	"""
	if not isinstance(numbers, list) or len(numbers) <= 0:
		return False, None

	for num in numbers:
		if not isinstance(num, int) or num >= len(numbers) or num < 0:
			return False, None

	i = 0

	while i < len(numbers):
		if numbers[i] != i:
			if numbers[i] == numbers[numbers[i]]:
				return True, numbers[i]
			temp = numbers[numbers[i]]	
			numbers[numbers[i]] = numbers[i]
			numbers[i] = temp
		else:
			i += 1

	return False, None


def duplication_in_array_2(numbers):
	"""
	题目二 找出数组中重复的数字
	时间O(n), 空间O(n)
	:type numbers: List[int]
	:rtype: bool, int
	"""
	if not isinstance(numbers, list) or len(numbers) <= 0:
		return False, None
	
	l = [None] * len(numbers)

	for num in numbers:
		if not isinstance(num, int) or num < 1 or num >= len(numbers):
			return False, None
		if l[num] == num:
			return True, num
		l[num] = num

	return False, None


def duplication_in_array_3(numbers):
	"""
	题目三 不修改数组找出重复的数字
	时间O(nlogn), 空间O(1)
	用时间换空间
	:param numbers: List[int]
	:return: int
	"""
	def count_range(numbers, start, end):
		"""
		:param numbers: List[int]
		:param start: int
		:param end: int
		:return: int
		"""
		if numbers is None:
			return 0
		
		count = 0
		for num in numbers:
			if start <= num <= end:
				count += 1
		return count

	if not isinstance(numbers, list) or len(numbers) < 1:
		return -1
	
	length = len(numbers)
	start = 1
	end = length - 1
	while end > start:
		mid = (start + end) // 2
		count = count_range(numbers, start, mid)
		if end > start:
			if count > (mid - start + 1):
				end = mid
			else:
				start = mid + 1
		
	return end


if __name__ == "__main__":
	print(duplication_in_array_1([2, 3, 1, 2, 5, 3, 0]))
	print(duplication_in_array_1([2, 1, 0]))
	print(duplication_in_array_3([2, 3, 1, 2, 5, 3]))
	print(duplication_in_array_3([2, 1, 1]))
	print(duplication_in_array_3([2, 3, 5, 4, 3, 2, 6, 7]))
