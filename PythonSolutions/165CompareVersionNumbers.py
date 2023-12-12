version1 = "0.1"
version2 = "1.0"

pos1, pos2 = 0, 0
sum1, sum2 = 0, 0

while pos1 < len(version1)-1 or pos2 < len(version2)-1:
    if version1[pos1] == '.' and version2[pos2] == '.':
        if sum1 > sum2:
            print (1)
        elif sum1 < sum2:
            print (-1)
        else:
            if pos1 >= len(version1) - 1 or pos2 >= len(version2) - 1:
                print (0)
            pos1 += 1
            pos2 += 1
            sum1, sum2 = 0, 0
    if version1[pos1] != '.' and pos1 < len(version1)-1:
        sum1 = (sum1 * 10) + ord(version1[pos1]) - 48
        pos1 += 1
    if version2[pos2] != '.' and pos2 < len(version2)-1:
        sum2 = (sum2 * 10) + ord(version2[pos2]) - 48
        pos2 += 1
print (0)