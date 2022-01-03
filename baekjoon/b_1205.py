def solution(answer, score_list):
    n, new_score, rank_limit = map(int, input().split())
    if n > 0:
        score_list = list(map(int, input().split()))
    else:
        # 이전기록이 없으면 내가 1등
        print(1)
        return
    ## 랭킹 리스트의 가장 낮은점수가 내 새로우 점수보다 작거나 같고, 최대 랭킹의 갯수가 가득 차있는경우
    if score_list[-1] >= new_score and rank_limit <= len(score_list):
        print(-1)
        return

    ## 스코어 리스트를 위에서부터 순차적으로 확인, 내 점수가 낮다면 answer을 늘려준다.
    for score in score_list:
        if score > new_score:
            answer += 1
            # if answer > rank_limit:
            #     print(-1)
            #     break
    print(answer)

if __name__ == '__main__':
    solution(1, [])
