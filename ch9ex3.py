read_file = open('D:\\TEST\\test.txt')
text = read_file.read()
write_file = open('D:\\TEST\\testcopy.txt','w')
write_file.write(text)
write_file.close()




