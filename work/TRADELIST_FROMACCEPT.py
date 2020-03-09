import os
import sys

# path0=r"C:\bwton\file"
# for root, dirs, files in os.walk(path0): 
# 	# print(root) #当前目录路径 
# 	# print(dirs) #当前路径下所有子目录 
# 	print(files) #当前路径下所有非目录子文件 
# 	print(files[1])

# 消费交易对账明细文件
fname = r'C:\bwton\file\TRADELIST_FROMACCEPT_C510820190200001_200226_01.dat' #需要解析的文件路径
count = 0
with open(fname, 'r', encoding='utf-8') as C:  # 打开文件
	
	lines = C.readlines()
	last_line = lines[-1]  # 取最后一行

	for C_line in lines:
		count = count + 1
		# print(count)
	
	path_check =last_line.split(",")
	if (int(path_check[1])) == count-1:
		print("#####文件行数校验完成#####")
	else:
	 	print("行数校验错误")

C.close()


# 仅解析文件首行进行验证
with open(fname, 'r', encoding='utf-8') as f:  # 打开文件
	lines = f.readlines()  # 读取所有行
	first_line = lines[0]  # 取第一行
	# last_line = lines[-1]  # 取最后一行
    # print('第一行为：'+ first_line)
    # print('文件' + fname + '最后一行为：' + last_line)
f.close()


path =first_line.split(",")
# print(path)
# print("#####开始解析文件#####")
print("#####该行有" + str(len(path)) + "个元素#####")
if len(path[0]) > 16:
	print("订单编号位数错误")
	exit()
if len(path[1]) > 16:
	print("行程单号位数错误")
	exit()
if len(path[2]) > 16:
	print("服务商移动应用ID长度错误")
	exit()
elif path[2][0] !="A":
	print("服务商移动应用ID编码错误")
	exit()
if len(path[19])  !=1:
	print("结算方式错误")
	exit()

def new_accept():
	with open('C:/Users/Administrator/Desktop/Analysis/消费交易对账明细文件解析.txt',"w",encoding='utf-8') as fs: #解析文件存储位置
		fs.write("订单编号:"+str(path[0]))
		fs.write('\n'+"行程单号:"+str(path[1]))
		fs.write('\n'+"服务商移动应用ID:"+str(path[2]))
		fs.write('\n'+"用户标识:"+str(path[3]))
		fs.write('\n'+"业务标识:"+str(path[4]))
		fs.write('\n'+"进站二维码凭证号:"+str(path[5]))
		fs.write('\n'+"进站线路号:"+str(path[6]))
		fs.write('\n'+"进站站点号:"+str(path[7]))
		fs.write('\n'+"进站时间:"+str(path[8]))
		fs.write('\n'+"进站确认类型:"+str(path[9]))
		fs.write('\n'+"出站二维码凭证号:"+str(path[10]))
		fs.write('\n'+"出站线路号:"+str(path[11]))
		fs.write('\n'+"出站站点号:"+str(path[12]))
		fs.write('\n'+"出站时间:"+str(path[13]))
		fs.write('\n'+"出站确认类型:"+str(path[14]))
		fs.write('\n'+"消费金额:"+str(path[15]))
		fs.write('\n'+"基础金额:"+str(path[16]))
		fs.write('\n'+"优惠金额:"+str(path[17]))
		fs.write('\n'+"扣罚金额:"+str(path[18]))
		fs.write('\n'+"结算方式:"+str(path[19]))
		fs.write('\n'+"结算票价:"+str(path[20]))
		fs.write('\n'+"结算类型:"+str(path[21]))
		fs.write('\n'+"消费扣款请求时间:"+str(path[22]))
		fs.write('\n'+"进站终端号:"+str(path[23]))
		fs.write('\n'+"出站终端号:"+str(path[24]))
	fs.close()
	print("#####解析文件结束#####")


def old_accept():
	with open('C:/Users/Administrator/Desktop/Analysis/消费交易对账明细文件解析.txt',"w",encoding='utf-8') as fs: #解析文件存储位置
		fs.write("订单编号:"+str(path[0]))
		fs.write('\n'+"行程单号:"+str(path[1]))
		fs.write('\n'+"服务商移动应用ID:"+str(path[2]))
		fs.write('\n'+"用户标识:"+str(path[3]))
		fs.write('\n'+"业务标识:"+str(path[4]))
		fs.write('\n'+"进站二维码凭证号:"+str(path[5]))
		fs.write('\n'+"进站线路号:"+str(path[6]))
		fs.write('\n'+"进站站点号:"+str(path[7]))
		fs.write('\n'+"进站时间:"+str(path[8]))
		fs.write('\n'+"进站确认类型:"+str(path[9]))
		fs.write('\n'+"出站二维码凭证号:"+str(path[10]))
		fs.write('\n'+"出站线路号:"+str(path[11]))
		fs.write('\n'+"出站站点号:"+str(path[12]))
		fs.write('\n'+"出站时间:"+str(path[13]))
		fs.write('\n'+"出站确认类型:"+str(path[14]))
		fs.write('\n'+"消费金额:"+str(path[15]))
		fs.write('\n'+"基础金额:"+str(path[16]))
		fs.write('\n'+"优惠金额:"+str(path[17]))
		fs.write('\n'+"扣罚金额:"+str(path[18]))
		fs.write('\n'+"结算方式:"+str(path[19]))
		fs.write('\n'+"结算票价:"+str(path[20]))
		fs.write('\n'+"结算类型:"+str(path[21]))
	fs.close()
	print("#####解析文件结束#####")

if len(path) == 25:
	new_accept()
elif len(path) ==22:
	old_accept()
else:
	print("元素个数错误"+"只有"+str(len(path))+"个")
