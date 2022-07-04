Day=0.51*24.00
Month=Day*30.00
Twenty_Servers_per_day=Day*20
Twenty_Servers_per_month=Twenty_Servers_per_day*30
Day_operate_one_server=918/Day

print('Cost to operate one server per day ${:.2f}.'.format(Day))
print('Cost to operate one server per Month ${:.2f}.'.format(Month))
print('cost to operate twenty servers per day ${:.2f}.'.format(Twenty_Servers_per_day))
print('cost to operate twenty servers per month ${:.2f}.'.format(Twenty_Servers_per_month))
print('one server can be operated {}days with $918'.format(Day_operate_one_server))
