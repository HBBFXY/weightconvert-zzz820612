   # WeightConvert.py
WeightStr = input().strip()

if WeightStr.lower().endswith('kg'):
    num_str = WeightStr[:-2]
    kg_value = eval(num_str)
    pd = kg_value * 2.2046
    # 截断到3位小数
    pd_truncated = int(pd * 1000) / 1000
    print("对应的英制重量为{:.3f}磅".format(pd_truncated))

elif 'pd' in WeightStr.lower():
    pd_index = WeightStr.lower().find('pd')
    num_str = WeightStr[:pd_index]
    pd_value = eval(num_str)
    kg = pd_value / 2.2046
    # 截断到3位小数
    kg_truncated = int(kg * 1000) / 1000
    print("对应的公制重量为{:.3f}公斤".format(kg_truncated))

else:
    print("输入格式错误")

  

