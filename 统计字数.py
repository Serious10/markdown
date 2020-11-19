# 整合代码，并输出
# 打开并读取文件
file = open('Walden.txt','r')
lines = file.readlines()
# 要把每行拆成单词
words = []
for line in lines:
    tmp_list = line.split(" ")
    for word in tmp_list:
        words.append(word.replace(',','').replace('.','').replace('"','').replace(':','').replace(';','').lower())
# 对words中每一个元素计算它出现的个数
# 把统计结果保存到字典中，字典的key是单词，value是单词出现的次数
word_count = {}
word_set = set(words)
for word in word_set:
    count_num = words.count(word)
    word_count[word] = count_num
word_count
# 对word_count字典进行排序，按照出现的次数进行降序排序
sorted(word_count.items(),key=lambda item:item[1],reverse=True)