
import heapq

def huffman(freq):
    heap = [[f, [ch, ""]] for ch, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for x in left[1:]:
            x[1] = "0" + x[1]

        for x in right[1:]:
            x[1] = "1" + x[1]

        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    return sorted(heap[0][1:])

freq = {'A': 5, 'B': 9, 'C': 12, 'D': 13}

print("Huffman Codes:")
print(huffman(freq))
