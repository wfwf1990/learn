import pymysql

class JD(object):
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.1.251', port=3306, user='root', password='xx',database='jing_dong', charset='utf8')
        self.cs = self.conn.cursor()

    def __del__(self):
        self.cs.close()
        self.conn.close()

    def print_menu(self):
        print("1:查询所有品牌信息")
        print("2:查询所有供应商信息")
        print("3:输入商品查询价格")
        print("4:插入供应商信息")
        return input("请输入你要的选项:")

    def execute_sql(self,sql):
        self.cs.execute(sql)
        for temp in self.cs.fetchall():
            print(temp)

    def query_all_brands(self):
        sql = "select name from goods_brands"
        self.execute_sql(sql)


    def query_all_cates(self):
        sql = "select name from goods_cates"
        self.execute_sql(sql)

    def query_goods_price(self):
        name = input("请输入你要查询的商品:")
        #sql = """select name,price from goods where cate_id = (select id from goods_cates where name = '%s')""" %name
        sql = """select name,price from goods where name = '%s'""" %name
        #' or 1=1 or 1='  如果输入 ，就是sql注入了
        print(sql)
        self.execute_sql(sql)

    def insert_brands(self):
        name = input("请输入供应商名称:")
        sql = """insert into goods_brands (name) values('%s')""" %name
        print(sql)
        self.cs.execute(sql)
        self.conn.commit()

def main():
    while True:
        jd = JD()
        num = jd.print_menu()
        if num == "1":
            jd.query_all_brands()
        elif num == "2":
            jd.query_all_cates()
        elif num == "3":
            jd.query_goods_price()
        elif num == "4":
            jd.insert_brands()
        else:
            print("请输入正确的选项...")

if __name__ == "__main__":
    main()