def simulation_calculate(input = '1+2/3'):
    ''' 
    输入四则运算，得到最终的结果
    1. 对于加法运算 pop 栈中
    2. 对于减法运算 相反数pop 栈中
    3. 对于乘除运算 计算和栈顶的元算

    eg.  input = '1+2*3'
    '''
    stack = []
    n = len(input)
    preSign = '+' # 制定数字前面的数据
    temp_num = 0
    for i in range(n):
        if input[i].isdigit():
            temp_num = temp_num*10 + int(input[i])
        # 获得对应的数字
        if input[i] in '+-*/':
            # 说明数字结束，可以进行计算
            if preSign == '+':
                stack.push(temp_num)
        temp_num = 0
        preSign = input[i] # 据此来完成后续的计算方式
        