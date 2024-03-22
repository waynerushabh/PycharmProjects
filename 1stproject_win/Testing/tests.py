# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
ip = [10, 5, 20, 1, 4]
[10, 15, 35, 36, 40]


def prob1(ip):
    res = []
    for x in range(len(ip)):
        res.append(sum(ip[:x + 1]))
    return res


ip1 = ["aa", "bb", "cc", "dd", "ee", "ff"]
ip2 = ["0", "1", "0", "2", "1", "3"]
["aa", "cc", "bb", "ee", "dd", "ff"]


def prob2(ip1, ip2):
    res = [(x, int(y)) for x, y in zip(ip1, ip2)]
    fin_res = sorted(res, key=lambda x: x[1])
    return [x[0] for x in fin_res]


def test_prob1():
    ip = [20, 5, 20, 1, 4]
    expected_op = [20, 25, 45, 46, 50]
    op = prob1(ip)
    assert expected_op == op, 'Actual result is not matching expected result in prob1'
    print('prob1 test passed')


def test_prob2():
    ip1 = ["aa", "bb", "cc", "dd", "ee", "ff"]
    ip2 = ["0", "1", "0", "0", "1", "3"]
    expected_op = ["aa", "cc", "dd", "bb", "ee", "ff"]
    op = prob2(ip1, ip2)
    assert expected_op == op, 'Actual result is not matching expected result in prob2'
    print('prob2 test passed')

import pandas as pd

df1 = pd.read_csv('csv_file_path1')
df2 = pd.read_csv('csv_file_path2')

df = pd.merge(df1, df2, how='inner,', on='id')
df.to_csv('final_csv_file_path', index=False)

