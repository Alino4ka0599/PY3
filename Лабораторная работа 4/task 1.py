from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # Начальные значения
    dp[1][1] = 1
    for i in range(2, n+1):
        dp[i][1] = 1
    for j in range(2, m+1):
        dp[1][j] = 1
    
    # Заполнение таблицы с помощью динамического программирования
    for i in range(2, n+1):
        for j in range(2, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]
    
    return dp

if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
