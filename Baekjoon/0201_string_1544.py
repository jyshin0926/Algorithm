n = int(input())    # 입력할 단어 갯수 입력
word_list = []      # 모든 단어 담을 리스트
cnt = 0
for i in range(n):
    word = list(input())
    word_list.append(word)      # 단어리스트 담기
    visited = [False] * len(word_list)      # 방문 여부 따질 리스트 형성
for i in range(len(word_list)):     # 같은 단어가 있는지 검사
    if visited[i]:              # 방문 처리된 같은 단어가 있었다면 무시
        continue
    check = list(word_list[i])      # 현재 단어를 미리 저장
    visited[i] = True               # 현재 단어를 방문 처리
    k = i+1
    for j in range(len(check)):     # 현재 단어의 스펠링
        check = check + [check[0]]  # 맨 앞을 뒤로 붙이고
        del check[0]                # 그 후 맨 앞 스펠링 제거    # 현재 찾을 단어를 시계 방향으로 회전
        for k in range(len(word_list)):     # 현재 다음 단어 탐색
            if check == word_list[k]:       # 같은 단어이면
                visited[k] = True           # 방문 처리
    cnt += 1           # 단어 갯수 증가
print(cnt)
