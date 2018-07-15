# -*-coding:utf-8-*-
# 给变量赋值为整型100
cars = 100
# 给变量赋值浮点型4.0
space_in_a_car = 4.0
# 整型
drivers = 30
# 整型
passengers = 90
# 减法运算
cars_not_driven = cars - drivers
# 变量等于另一个变量的值
cars_driven = drivers
# 整型和浮点型乘法运算，结果为浮点型
carpool_capacity = cars_driven * space_in_a_car
# 除法运算
average_passengers_per_car = passengers / cars_driven

print "there are",cars,"cars available."
print "there are only",drivers,"drivers available."
print "there will be",cars_not_driven,"empty cars today."
print "we can transport",carpool_capacity,"people today."
print "we have",passengers,"to carpool today."
print "we need to put about",average_passengers_per_car,"in each car."