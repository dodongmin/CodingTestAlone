def solution(tickets):
    answer = []

    visited = [0]*len(tickets)

    def dfs(airport, path):
        if len(path) == len(tickets)+1:
            answer.append(path)

        for i, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[i] == 0:
                visited[i] = 1
                dfs(ticket[1], path+[ticket[1]])
                visited[i] = 0

    dfs("ICN", ["ICN"])
    answer.sort()

    return answer[0]