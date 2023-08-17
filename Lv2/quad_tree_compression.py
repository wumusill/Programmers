# 모든 원소 탐색
# 만약 첫 원소와 다른게 나온다면 분할 후 재귀 수행
# 끝까지 탐색을 마쳤다면 해당 원소 개수 += 1
def solution(arr): 
    answer = [0, 0]

    def recursion(arr):  
        first_element = None

        # 모든 원소 순회
        for i in range(len(arr)):
            for j in range(len(arr)):
                first_element = arr[0][0]
                # 첫 원소랑 탐색 중인 원소랑 다르다면 분할 후 재귀
                if arr[i][j] != first_element:
                    # 분할
                    arr1 = []
                    arr2 = []
                    arr3 = []
                    arr4 = []

                    k = len(arr) // 2

                    for i in range(len(arr)):
                        if i < k:
                            arr1.append(arr[i][:k])
                            arr2.append(arr[i][k:])
                        else:
                            arr3.append(arr[i][:k])
                            arr4.append(arr[i][k:])
                    # 재귀
                    recursion(arr1)
                    recursion(arr2)
                    recursion(arr3)
                    recursion(arr4)
                    return
        # 끝까지 원소 순회를 마쳤다면 = 모든 원소가 같은 숫자라면 개수 갱신
        answer[first_element] += 1

    # 재귀 실행      
    recursion(arr)
    
    return answer