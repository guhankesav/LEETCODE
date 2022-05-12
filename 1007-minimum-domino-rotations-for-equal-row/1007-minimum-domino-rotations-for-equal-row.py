class Solution:
	def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

		frequency_tops = {1:0,2:0,3:0,4:0,5:0,6:0}

		for i in tops:
			if i not in frequency_tops:
				frequency_tops[i] = 1
			else:
				frequency_tops[i] = frequency_tops[i] + 1

		frequency_bottoms = {1:0,2:0,3:0,4:0,5:0,6:0}

		for i in bottoms:
			if i not in frequency_bottoms:
				frequency_bottoms[i] = 1
			else:
				frequency_bottoms[i] = frequency_bottoms[i] + 1

		swap_number = 0

		for i in range(1,7):
			if frequency_tops[i] + frequency_bottoms[i] >= len(tops):
				swap_number = i

		if swap_number == 0:
			return -1

		min_num1 = len(tops)-frequency_tops[swap_number]
		min_num2 = len(bottoms)-frequency_bottoms[swap_number]


		for i in range(len(tops)):
			if swap_number not in [tops[i],bottoms[i]]:
				return -1

		return min(min_num1,min_num2)