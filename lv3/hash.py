import heapq


def solution(genres, plays):
    answer = []

    unique_genres = set(genres)
    genres_count = {genre: 0 for genre in unique_genres}
    songs_info = {}
    genre2song = {}

    for i in range(len(plays)):
        songs_info[i] = (plays[i], genres[i])

        if genres[i] not in genre2song.keys():
            genre2song[genres[i]] = [i]
        else:
            genre2song[genres[i]].append(i)
        genres_count[genres[i]] += plays[i]

    genres_count = dict(sorted(genres_count.items(), key=(lambda x: x[1]), reverse=True))
    songs_info = dict(sorted(songs_info.items(), key=(lambda x: x[1][0]), reverse=True))

    for genre in genres_count:
        heap = []
        for song in genre2song[genre]:
            heapq.heappush(heap, (-songs_info[song][0], song))
        for i in range(2):
            if len(heap) == 0:
                break
            answer.append(heapq.heappop(heap)[1])

    return answer
  
  
#   정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.10ms, 10.4MB)
# 테스트 6 〉	통과 (0.09ms, 10.4MB)
# 테스트 7 〉	통과 (0.06ms, 10.3MB)
# 테스트 8 〉	통과 (0.04ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.12ms, 10.3MB)
# 테스트 11 〉	통과 (0.03ms, 10.3MB)
# 테스트 12 〉	통과 (0.06ms, 10.3MB)
# 테스트 13 〉	통과 (0.10ms, 10.3MB)
# 테스트 14 〉	통과 (0.11ms, 10.3MB)
# 테스트 15 〉	통과 (0.02ms, 10.3MB)
