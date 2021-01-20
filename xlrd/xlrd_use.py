import xlrd

#打开excel
book = xlrd.open_workbook("day_01.xls")
print("总页数：{0}；页名称列表{1}；book的第一个工作表{2}"
      .format(book.nsheets,
             book.sheet_names(),
             book.sheet_by_index(0)))
#获取总页数
book.nsheets
#获取页名称列表
book.sheet_names()
#获取book中的第一个工作表
sh = book.sheet_by_index(0)
print("当前工作表名称：{0}；工作表总行数：{1}；工作表总列数：{2}"
      .format(sh.name,
              sh.nrows,
              sh.ncols))
print("第一行第一列A1：{0}".format(sh.cell_value(rowx=0,colx=0)))
#快捷键ctrl+d 快速复制一行
print("第一行第一列B1：{0}".format(sh.cell_value(rowx=0,colx=1)))
#获取工作表名称
sh.name
#获取工作表总行数
sh.nrows
#获取工作表总列数
sh.ncols
#获取单元格数据函数
#sh.cell_value()
#打印每一行的值
#----------------
#打印每一行的值
#注释快捷键 ctrl+/
# for rowx in range(sh.nrows):
#     print("第{0}行".format(rowx+1),end="")
#     for cols in range(sh.ncols):
#         print(" 第{0}列：{1}"\
#               .format(cols+1,sh.cell_value(rowx=rowx,colx=cols)))
#-------------------
for rowx in range(sh.nrows):
    #tmp_row_val = sh.row(rowx)
    tmp_row_val = sh.row_values(rowx)
    tmp_date = ''
    if rowx >= 1:
        tmp_date = xlrd.xldate_as_datetime(tmp_row_val[3],0).strftime("%Y-%m-%d")
        tmp_row_val[3] = tmp_date
    #脚下留心 时间格式转化，目前打印时间【43860.0】对应【2020/1/30】
    print(tmp_row_val)





