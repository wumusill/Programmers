# Kruskal Algorithm

# 최소 비용으로 모든 노드들을 연결할 때 쓰는 그리디 알고리즘
# 간선의 개수는 무조건 (노드 - 1)

# 거리(비용)를 기준으로 오름차순 정렬 수행
# 정렬된 순서에 맞게 그래프에 포함
# 사이클을 형성하는 경우 간선을 포함하지 않음
# 사이클이 발생하는지의 여부는 Union-Find 알고리즘을 이용

# 부모를 찾아주는 함수
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 부모를 합치는 함수, 일반적으로 작은 값이 부모가 되게 함
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solution(n, costs):
    # 비용 순으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])
    answer = 0
    parent = [0] * (n + 1)

    # 각 노드에 대해 부모를 자기 자신으로 설정
    for i in range(1, n + 1):
        parent[i] = i

    # 모든 간선들 순회
    for a, b, c in costs:
        # 간선에 연결된 두 노드의 부모가 다르다면 연결해도 사이클을 형성하지 않는다는 뜻
        # 부모가 다르다면 부모를 합쳐 공통 부모를 두게 하고 비용 추가
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += c
    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))