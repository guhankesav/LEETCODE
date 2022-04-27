class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
	
        let = []
        dig = []
        heap = []
		
        for log in logs:
            res = log.split(' ')
            if res[1][0].isdigit():
                dig.append(log)
                continue
            cont = ' '.join(res[1:])
            iden = res[0]
            heapq.heappush(heap, (cont, iden))  # we will heapify by lexicographical order of content then identifier
        print(heap)
        for _ in range(len(heap)):
            cont, iden = heapq.heappop(heap)  # heappop gives the lexicographically smallest element
            let.append(iden + ' ' + cont)
        print(let)
        return let + dig