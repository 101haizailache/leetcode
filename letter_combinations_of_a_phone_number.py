'''题目描述：
给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
例：
输入："23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''


def lettertophonumber(digits):
    conversion = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits) == 0:
        return []
    product = ['']
    for k in digits:
        product = [i + j for i in product for j in conversion[k]]
    return product