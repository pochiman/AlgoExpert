

# O(n * m) time | O(n * m) space - where n is the length of the
# first input array and m is the length of the second input array
def maxSubsequenceDotProduct(arrayOne, arrayTwo):
    maxDotProducts = initializeDotProducts(arrayOne, arrayTwo)
    for i in range(1, len(arrayOne) + 1):
        for j in range(1, len(arrayTwo) + 1):
            currentProduct = arrayOne[i - 1] * arrayTwo[j - 1]
            maxDotProducts[i][j] = max(
                currentProduct,
                maxDotProducts[i - 1][j - 1] + currentProduct,
                maxDotProducts[i - 1][j - 1],
                maxDotProducts[i - 1][j],
                maxDotProducts[i][j - 1],
            )
    return maxDotProducts[len(arrayOne)][len(arrayTwo)]


def initializeDotProducts(arrayOne, arrayTwo):
    dotProducts = [
        [float("-inf") for j in range(len(arrayTwo) + 1)] for i in range(len(arrayOne) + 1)
    ]
    return dotProducts
