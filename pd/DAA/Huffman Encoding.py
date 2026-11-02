
import heapq

# Function to generate Huffman Codes
def huffman(chars, freq):
    heap = []

    for i in range(len(chars)):
        heapq.heappush(heap, (freq[i], chars[i]))

    while len(heap) > 1:
        f1, c1 = heapq.heappop(heap)
        f2, c2 = heapq.heappop(heap)

        heapq.heappush(heap, (f1 + f2, c1 + c2))

    codes = {}

    def generate(char, code):
        if len(char) == 1:
            codes[char] = code
            return

        mid = len(char) // 2
        generate(char[:mid], code + "0")
        generate(char[mid:], code + "1")

    generate(heap[0][1], "")

    return codes


# Main Program
print("===== HUFFMAN ENCODING =====")

n = int(input("Enter number of characters: "))

chars = []
freq = []

for i in range(n):
    ch = input("Enter character: ")
    f = int(input("Enter frequency: "))
    chars.append(ch)
    freq.append(f)

codes = huffman(chars, freq)

print("\nHuffman Codes:")
for ch in chars:
    print(ch, ":", codes[ch])
