import web
import xlrd

# 路由配置
urls = (
    '/', 'index',
    '/index', 'index'
)
app = web.application(urls, globals())
render = web.template.render("templates/")

class index:
    def GET(self):
        work_book = xlrd.open_workbook("static/homework.xlsx")
        # 柱状图
        work_sheet_1 = work_book.sheet_by_index(0)
        sales_data = {
            "category":work_sheet_1.row_values(0),
            "data":work_sheet_1.row_values(1),
        }
        # print(work_sheet_1.row_values(0))
        # 饼状图
        work_sheet_2 = work_book.sheet_by_index(1)
        source_data = []
        source_title = work_sheet_2.row_values(3)
        source_value = work_sheet_2.row_values(4)
        for idx in range(len(source_title)):
            tmp_data={
                "name":source_title[idx],
                "value":source_value[idx]
            }
            source_data.append(tmp_data)
        source_stat_data = []
        source_stat_title = work_sheet_2.row_values(0,0,3)
        source_stat_value = work_sheet_2.row_values(1,0,3)
        for idx in range(len(source_stat_title)):
            tmp_data = {
                "name": source_stat_title[idx],
                "value": source_stat_value[idx]
            }
            source_stat_data.append(tmp_data)
        source_all_title = source_stat_title + source_title
        # 漏斗图
        work_sheet_3 = work_book.sheet_by_index(2)
        clue_title = work_sheet_3.row_values(0,0,4)
        clue_value = work_sheet_3.row_values(1,0,4)
        clue_data = []
        for idx in range(len(clue_title)):
            tmp_data={
                "name":clue_title[idx],
                "value":clue_value[idx]
            }
            clue_data.append(tmp_data)
        print(sales_data)
        print(source_data)
        print(source_all_title)
        print(source_stat_data)
        print(clue_data)
        print(clue_title)
        return render.index(sales_data = sales_data,
                           source_data = source_data,
                           source_all_title = source_all_title,
                           source_stat_data = source_stat_data,
                           clue_data = clue_data,
                           clue_title = clue_title
                           )


if __name__ == "__main__":
    app.run()
