#WeightConvert.py
WeightStr=input("")
if WeightStr[-2:].lower()=='kg':
  #输入公斤转化为磅
  pd=eval(WeightStr[0:-2])*2.2046
  print("对应的英制重量为{：.3f}磅".format(pd))
elif WeightStr[-2:].lower()=='pd':
  #输入为磅转化为公斤
  kg=eval(WeightStr[0:-2])/2.2046
  print("对应的公制单位为{:.3f}公斤".format(kg))
else:
  print("输入格式错误")
  10kg
  对应的英制重量为22.046磅
  10pd
  对应的公制单位为4.535公斤
  

  

