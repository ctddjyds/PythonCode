#模式匹配
import re #包含类似搜索、分割和替换等调用
matchG = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
t=matchG.group(1)
match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
