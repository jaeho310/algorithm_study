class Beak2606:
    graph = {}
    def __init__(self) -> None:
        pass

    def input_data(self):
        cnt = int(input())
        for i in range(cnt):
            self.graph[i+1] = set()
        link_cnt = int(input())
        for _ in range(link_cnt):
            a, b = map(int,input().split())
            self.graph[a].add(b)
            self.graph[b].add(a)
    
    def solution(self):
        need_visit = []
        visited = []

        # 1번 컴퓨터에서 시작
        need_visit.append(1)

        while need_visit:
            current_node = need_visit.pop(0)
            if current_node not in visited:
                visited.append(current_node)
                if current_node in self.graph.keys():
                    need_visit.extend(self.graph[current_node])

        print(len(visited) - 1)
        
        

if __name__ == "__main__":
    beak = Beak2606()
    beak.input_data()
    beak.solution()
