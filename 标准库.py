# import reprlib
# s=reprlib.repr(set('supercalifragilisticexpialidocious'))
# print(s)
#
# import pprint
# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
#     'yellow'], 'blue']]]
#
# pprint.pprint(t, width=30)
# print(t)

# import textwrap
# doc = """The wrap() method is just like fill() except that it returns
# a list of strings instead of one big string with newlines to separate
# the wrapped lines."""
#
# print(textwrap.fill(doc, width=40))
#
# from string import Template
# t = Template('${village}folk send $$10 to $cause.')
# c=t.substitute(village='Nottingham', cause='the ditch fund')
# print(c)
#
# t = Template('Return the $item to $owner.')
# d = dict(item='unladen swallow')
#
# # print(t.substitute(d))
# print(t.safe_substitute(d))

#
# import threading, zipfile
#
# class AsyncZip(threading.Thread):
#     def __init__(self, infile, outfile):
#         threading.Thread.__init__(self)
#         self.infile = infile
#         self.outfile = outfile
#
#     def run(self):
#         f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
#         f.write(self.infile)
#         f.close()
#         print('Finished background zip of:', self.infile)
#
# background = AsyncZip('mydata.txt', 'myarchive.zip')
# background.start()
# print('The main program continues to run in foreground.')
#
# background.join()    # 等待后台任务结束
# print('Main program waited until background was done.')

# import logging
# logging.debug('Debugging information')
# logging.info('Informational message')
# logging.warning('Warning:config file %s not found', 'server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')
#
# from array import array
# a = array('H', [4000, 10, 700, 22222])
# print(sum(a))
# print(a[1:3])
#
# from collections import deque
# d = deque(["task1", "task2", "task3"])
# d.append("task4")
# print("Handling", d.popleft())
#
# import bisect
# scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
# bisect.insort(scores, (600, 'ruby'))
# print(scores)
#
# from heapq import heapify, heappop, heappush
# data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# heapify(data)                      # 将列表重新调整为堆顺序
# print(data)
# heappush(data, -5)                 # 添加一个新条目
# print(data)
#   # 获取三个最小的条目
# print([heappop(data) for i in range(3)])

from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)

round(.70 * 1.05, 2)

print(Decimal(0.1)+Decimal(0.2))
print(Decimal('1.00') % Decimal('.10'))
print(1%0.1)
print(0.1+0.2)
