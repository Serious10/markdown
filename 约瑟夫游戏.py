
def circle(x,y,z):
    """
    用于做约瑟夫环的游戏函数
    Input:
    x:总共玩的人数
    y:玩到几淘汰
    z:剩余几个人

    Output:
    返回List的计算结果
    """
    List = list(range(1,x+1))
    index = 0
    while List:
        temp = List.pop(0)
        index += 1
        if index == y:
            index = 0
            continue
        List.append(temp)
        if len(List)==z:
            print(List)
            break
    return List