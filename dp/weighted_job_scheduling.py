def max_profit(jobs):
    n = len(jobs)
    sorted(jobs, key = lambda job: job[1])
    profit = [0]*n
    profit[0] = jobs[0][2]

    for i in range(1, n):
        p = jobs[i][2]
        last_job = -1
        for j in range(i):
            if jobs[j][1] <= jobs[i][0]:
                last_job = j

        if last_job != -1:
            p += profit[last_job]

        profit[i] = max(profit[i-1], p)

    return profit[n-1]


if __name__=='__main__':
    jobs = [[3, 10, 20], [1, 2, 50], [6, 19, 100], [2, 100, 200]]
    print max_profit(jobs)
