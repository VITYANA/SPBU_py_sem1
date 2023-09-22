if __name__ == "__main__":
    n = int(input("Введите число - предел для знаменателя: "))
    all_nums = []
    for i in range(1, n):
        check = True
        local_nums = []
        for j in range(i + 1, n + 1):
            for divider in range(2, n):
                if i % divider == 0 and j % divider == 0:
                    check = False
            if check == True and str(i) + "/" + str(j) not in all_nums:
                res = i / j
                all_nums.append([i, j, res])
    all_nums = sorted(all_nums, key=lambda x: x[2])
    for i in range(len(all_nums)):
        print(str(all_nums[i][0]) + "/" + str(all_nums[i][1]))
