import time,os,re,random
def d1():
	lo = open('offku.txt', 'r')
	pi = lo.readlines()
	pp = open('du.txt', 'w')
	for a in pi:
		if a != '\n':
			jo = a.split('\t')
			pp.write('<tr>')
			for b in jo:
				if b != '\n' and b !='':
					if '\n' in b:
						pp.write('<td>'+ b.replace('\n','') +'</td>')
					else:
						pp.write('<td>'+ b +'</td>')
			pp.write('</tr>\n')
	pp.close()
	lo.close()

def d2():
	n = 1
	lo = open('ja.txt', 'r')
	pi = lo.read()
	jj = re.findall(r'.*?\d [A-Z]\s?[ⅠⅡⅢ]',pi,re.S)
	print(len(jj),jj)
	li = open('曳引.txt','w')
	for a in jj:
		li.write(str(n) + ' ')
		n += 1
		while a[0] == ' ' or a[0] == '\n':
			a = a[1:]
		yy1 = re.compile(r'^(.*?)[\s\n]?([\u4E00-\u9FFF].*?)([/A-Z].*?)([\u4E00-\u9FFF△☆a].*)(\d) ([A-Z])\s?([ⅠⅡⅢ])', re.S)
		yy0 = re.findall(yy1, a)
		for b in yy0[0]:
			b = b.replace('\n', '')
			while a[0] == ' ':
				a = a[1:]
			while a[-1] == ' ':
				a = a[:-1]
			if b == yy0[0][0]:
				if b[:2] == '1.':
					li.write(b + ' ' + '使用管理')
				elif b[:2] == '2.':
					li.write(b + ' ' + '电气系统')
				elif b[:2] == '3.':
					li.write(b + ' ' + '曳引系统')
				elif b[:2] == '4.':
					li.write(b + ' ' + '导向系统')
				elif b[:2] == '5.':
					li.write(b + ' ' + '轿厢系统')
				elif b[:2] == '6.':
					li.write(b + ' ' + '门系统')
				elif b[:2] == '7.':
					li.write(b + ' ' + '重量平衡系统')
				elif b[:2] == '8.':
					li.write(b + ' ' + '安全保护系统')
				elif b[:2] == '9.':
					li.write(b + ' ' + '机房与井道土建')
				elif b[:2] == '10':
					li.write(b + ' ' + '试验与功能测试')
				elif b[:2] == '11':
					li.write(b + ' ' + '液压电梯试验与功能测试')
			else:
				li.write(' ' + b)
		li.write('\n')
		# print(re.findall(yy4, a), a.replace('\n', ''))
		# yy4 = re.compile(r'^(.*?[\s\n][\u4E00-\u9FFF].*?)[/A-Z]',re.S)
		# print(re.findall(yy4, a), a.replace('\n', ''))
		# print(re.findall(r'^.*?[\s\n]',a,re.S),a.replace('\n',''))
		# yy1 = re.compile(r'^.*?[\s\n].*?([/A-Z].*?)[\u4E00-\u9FFF]',re.S)
		# print(re.findall(yy1, a), a.replace('\n', ''))
		# yy2 = re.compile(r'^.*?[\s\n].*?[/A-Z].*?([\u4E00-\u9FFF△☆a].*)\d [A-Z]\s?[ⅠⅡⅢ]$',re.S)
		# print(re.findall(yy2, a), a.replace('\n', ''))
		# yy3 = re.compile(r'.*?(\d) ([A-Z])\s?([ⅠⅡⅢ])',re.S)
		# print(re.findall(yy3, a), a.replace('\n', ''))
		# li.write('\n')
	li.close()
	lo.close()
def d3():
	n = 1
	lo = open('yeya.txt', 'r')
	pi = lo.read()
	jj = re.findall(r'.*?\d [A-Z]\s?[ⅠⅡⅢ]',pi,re.S)
	li = open('液压.txt','w')
	for a in jj:
		li.write(str(n) + ' ')
		n += 1
		while a[0] == ' ' or a[0] == '\n':
			a = a[1:]
		yy1 = re.compile(r'^(.*?)[\s\n]?([\u4E00-\u9FFF].*?)([/A-Z].*?)([\u4E00-\u9FFF△☆a].*)(\d) ([A-Z])\s?([ⅠⅡⅢ])', re.S)
		yy0 = re.findall(yy1, a)
		for b in yy0[0]:
			b = b.replace('\n', '')
			while a[0] == ' ':
				a = a[1:]
			while a[-1] == ' ':
				a = a[:-1]
			if b == yy0[0][0]:
				if b[:2] == '1.':
					li.write(b + ' ' + '使用管理')
				elif b[:2] == '2.':
					li.write(b + ' ' + '电气系统')
				elif b[:2] == '3.':
					li.write(b + ' ' + '曳引系统')
				elif b[:2] == '4.':
					li.write(b + ' ' + '导向系统')
				elif b[:2] == '5.':
					li.write(b + ' ' + '轿厢系统')
				elif b[:2] == '6.':
					li.write(b + ' ' + '门系统')
				elif b[:2] == '7.':
					li.write(b + ' ' + '重量平衡系统')
				elif b[:2] == '8.':
					li.write(b + ' ' + '安全保护系统')
				elif b[:2] == '9.':
					li.write(b + ' ' + '机房与井道土建')
				elif b[:2] == '10':
					li.write(b + ' ' + '试验与功能测试')
				elif b[:2] == '11':
					li.write(b + ' ' + '液压电梯试验与功能测试')
			else:
				li.write(' ' + b)
		li.write('\n')
		# print(re.findall(yy4, a), a.replace('\n', ''))
		# yy4 = re.compile(r'^(.*?[\s\n][\u4E00-\u9FFF].*?)[/A-Z]',re.S)
		# print(re.findall(yy4, a), a.replace('\n', ''))
		# print(re.findall(r'^.*?[\s\n]',a,re.S),a.replace('\n',''))
		# yy1 = re.compile(r'^.*?[\s\n].*?([/A-Z].*?)[\u4E00-\u9FFF]',re.S)
		# print(re.findall(yy1, a), a.replace('\n', ''))
		# yy2 = re.compile(r'^.*?[\s\n].*?[/A-Z].*?([\u4E00-\u9FFF△☆a].*)\d [A-Z]\s?[ⅠⅡⅢ]$',re.S)
		# print(re.findall(yy2, a), a.replace('\n', ''))
		# yy3 = re.compile(r'.*?(\d) ([A-Z])\s?([ⅠⅡⅢ])',re.S)
		# print(re.findall(yy3, a), a.replace('\n', ''))
		# li.write('\n')
	li.close()
	lo.close()
def d4():
	n = 1
	lo = open('futi.txt', 'r')
	pi = lo.read()
	jj = re.findall(r'.*?\d [A-Z]\s?[ⅠⅡⅢ]',pi,re.S)
	print(len(jj),jj)
	li = open('自动扶梯.txt','w')
	for a in jj:
		li.write(str(n) + ' ')
		n += 1
		while a[0] == ' ' or a[0] == '\n':
			a = a[1:]
		yy1 = re.compile(r'^(.*?)[\s\n]?([\u4E00-\u9FFF].*?)([/A-Z].*?)([\u4E00-\u9FFF△☆a].*)(\d) ([A-Z])\s?([ⅠⅡⅢ])', re.S)
		yy0 = re.findall(yy1, a)
		for b in yy0[0]:
			b = b.replace('\n', '')
			while b[0] == ' ':
				b = b[1:]
			while a[-1] == ' ':
				b = b[:-1]
			if b == yy0[0][0]:
				if b[:2] == '1.':
					li.write(b + ' ' + '使用管理')
				elif b[:2] == '2.':
					li.write(b + ' ' + '电气系统')
				elif b[:2] == '3.':
					li.write(b + ' ' + '驱动装置系统')
				elif b[:2] == '4.':
					li.write(b + ' ' + '支撑结构和围板')
				elif b[:2] == '5.':
					li.write(b + ' ' + '梯级（踏板或胶带）系统')
				elif b[:2] == '6.':
					li.write(b + ' ' + '扶手装置')
				elif b[:2] == '7.':
					li.write(b + ' ' + '扶手带系统')
				elif b[:2] == '8.':
					li.write(b + ' ' + '出入口系统')
				elif b[:2] == '9.':
					li.write(b + ' ' + '机房、驱动站和转向站')
				elif b[:2] == '10':
					li.write(b + ' ' + '试验与功能测试')
			else:
				li.write(' ' + b)
		li.write('\n')
		# print(re.findall(yy4, a), a.replace('\n', ''))
		# yy4 = re.compile(r'^(.*?[\s\n][\u4E00-\u9FFF].*?)[/A-Z]',re.S)
		# print(re.findall(yy4, a), a.replace('\n', ''))
		# print(re.findall(r'^.*?[\s\n]',a,re.S),a.replace('\n',''))
		# yy1 = re.compile(r'^.*?[\s\n].*?([/A-Z].*?)[\u4E00-\u9FFF]',re.S)
		# print(re.findall(yy1, a), a.replace('\n', ''))
		# yy2 = re.compile(r'^.*?[\s\n].*?[/A-Z].*?([\u4E00-\u9FFF△☆a].*)\d [A-Z]\s?[ⅠⅡⅢ]$',re.S)
		# print(re.findall(yy2, a), a.replace('\n', ''))
		# yy3 = re.compile(r'.*?(\d) ([A-Z])\s?([ⅠⅡⅢ])',re.S)
		# print(re.findall(yy3, a), a.replace('\n', ''))
		# li.write('\n')
	li.close()
	lo.close()

d4()
d2()
d3()



