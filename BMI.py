h1=eval(input('hight:'))
w1=eval(input('weight:'))
bmi=w1/(h1*h1)
if bmi<18.5:
    print('国际、国内瘦')
elif 18.5<=bmi<24:
    print('国际、国内标准')
elif 24<=bmi<25:
    print('国际正常、国内偏胖')
elif 25<=bmi<28:
    print('国际、国内偏胖')
elif 28<=bmi<30:
    print('国际偏胖、国内肥胖')
else:
    print('国际国内肥胖')
