# `xlsxwriter`作图

## 前言

安装请参考[PyPI官网:https://pypi.org/](https://pypi.org/)

对已做数据进行制图

```python
import xlsxwriter

workbook = xlsxwriter.Workbook("demo2.xlsx")

work_sheet = workbook.add_worksheet("消费记录")

##数据样式
#加粗 红色字体 字体大小20
format_dic = {
    "bold":True,
    "font_color":"#DC143C",
    "font_size":20
}
text_format = workbook.add_format(format_dic)
##数据写入
#头部写入
header = ["门票总额","旅途总费用","购物消费","年消费总额"]
for col in range(len(header)):
    work_sheet.write(0,col,header[col],text_format)
#数据写入
data = [742.6,4399,1298]
data.append(sum(data))

for col in range(len(data)):
    work_sheet.write_number(1,col,data[col])

#设置列宽
work_sheet.set_column(0,len(header),20)

workbook.close()
```

## 制图

### 柱状图实现

```python
#categories 横坐标数据
#values	具体数据
#0,0,0,2	代表从（第1行，第1列）到（第1行，第3列）
#1,0,1,2	代表从（第2行，第1列）到（第2行，第3列）
chart1.add_series({
    "categories":["消费记录",0,0,0,2 ],
    "values":["消费记录",1,0,1,2 ]
})
#标题title
chart1.set_title({"name":"消费记录柱状图"})
#图例legend
chart1.set_legend({"none":True})
#插入位置
work_sheet.insert_chart(row=3,col=0,chart=chart1)
```

### 饼状图实现

```python
chart2 = workbook.add_chart({'type':'pie'})

chart2.add_series({
    "categories":["消费记录",0,0,0,3 ],
    "values":["消费记录",1,0,1,2 ]
})
chart2.set_title({"name":"消费记录柱状图"})
work_sheet.insert_chart(row=3,col=5,chart=chart2)
```

