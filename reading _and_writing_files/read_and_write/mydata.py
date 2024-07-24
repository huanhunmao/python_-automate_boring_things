import shelve

# 使用 dbm.dumb 类型的数据库
with shelve.open('mydata', flag='c', protocol=None, writeback=False, dbm_type='dbm.dumb') as shelfFile:
    cats = ['Zophie', 'Pooka', 'Simon']
    shelfFile['cats'] = cats
