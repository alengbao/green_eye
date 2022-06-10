def 求斐波那契n项值(n: int):
    if n <= 0:
        raise Exception('参数应为正整数')
    if n == 1 or n == 2:
        return 1
    return 求斐波那契n项值(n-1) + 求斐波那契n项值(n-2)


call = 求斐波那契n项值
