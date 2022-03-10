score = 90
str1 = "張致誠"
count = 1
print("%s你的第 %d 次物理考試成績是 %d" % (str1,count,score)) # % = 變數系列區

#format()函數應用
score = 90
str1 = "張致誠"
count = 1
print("{}你的第 {} 次物理考試成績是 {}" .format(str1,count,score))


score = 90
str1 = "張致誠"
count = 1
formastr = "%s你的第 %d 次物理考試成績是 %d"
print(formastr % (str1,count,score))#可以用字串取代變數

#format()函數
score = 90
str1 = "張致誠"
count = 1
str2 = "{}你的第 {} 次物理考試成績是 {}"
print(str2.format(str1,count,score))
####################################################################

x = 100
print("100的16進位 = %x\n100的8進位 = %o" % (x,x))#格式化8,16進位運用

x = 10
print("整數%d \n浮點數%f \n字串%s" % (x,x,x))
y = 9.9
print("整數%d \n浮點數%f \n字串%s" % (y,y,y))

#精準控制格式化輸出位置

x = 100
print("x = /%6d/" % x)
y = 10.5
print("y = /%6.2f/" % y)
s = "Deep"
print("s=/%6s/" % s)
print("以下是保留空間不足的實例")
print("x=/%2d/" % x)
print("y=/%3.2f/" % y)
print("s=/%2s/" % s)

#格式化輸出出現正號

x = 10
print("x=/%+6d/" % x)
y = 10.5
print("y=/%+6.2f/" % y)

#格式化輸出向左對齊實例

x = 100
print("x=/%-6d/" % x)
y = 10.5
print("y=/%-6.2f/" % y)
s = "Deep"
print("s=/%-6s/" % s)

#應用

print("姓名  國文  英文  總分")
print("%3s  %5d  %4d  %4d" %("張XX", 99,99,198))
print("%3s  %4d  %4d  %4d" %("張X誠", 100,99,199))
print("%3s  %4d  %4d  %4d" %("張致X", 100,100,200))
print("%3s  %4d  %4d  %4d" %("X致誠", 90,90,180))


