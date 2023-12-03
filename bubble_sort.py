vetor = [9, 5, 7, 2, 6, 1, 3, 0, 4, 8]
Implementar a função Bubble Sort:

python
Copy code
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

Chamar a função com o vetor dado:

python
Copy code
bubble_sort(vetor)
Verificar o vetor ordenado:

python
Copy code
print("Vetor Ordenado:", vetor)