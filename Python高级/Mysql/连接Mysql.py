import pymysql

def main():
    #创建连接
    conn = pymysql.connect(host='192.168.1.251',port=3306,user='root',password='xx',database='jing_dong',charset='utf8')

    #获得Cursor对象
    cs = conn.cursor()

    #执行select语句，并返回受影响的行数，查询一条数据
    cs.execute('select id,name from goods where id>=4')



    print(cs.fetchall())

    #关闭Cursor对象
    cs.close()
    conn.close()
if __name__ == "__main__":
    main()