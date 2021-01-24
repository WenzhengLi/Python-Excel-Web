# 使用`xlsxwriter`来写入Excel文件

安装请参考[PyPI官网:https://pypi.org/](https://pypi.org/)

## 使用方法

### 新建Excel

```python
import xlsxwriter
#创建Excel 名称为demo.xlsx
workbook = xlsxwriter.Workbook("demo.xlsx")

workbook.close()
```

### 创建Sheet

```python
#创建Sheet 名称为demo
worksheet = workbook.add_worksheet("demo")
```

### 设置宽度

```python
#第0行第0列宽度为40
worksheet.set_column(0,0,40)
```

### \#字体添加样式

```python
#加粗 红色字体 字体大小20
format_dic = {
    "bold":True,
    "font_color":"#DC143C",
    "font_size":20
}
text_format = workbook.add_format(format_dic)
```

### 写入

第一列写入`姓名`

```python
#第0行第0列内容为【Name】样式为 加粗，红色，大小20
worksheet.write(0,0,"姓名",text_format)
worksheet.write(1,0,"张三")
worksheet.write(2,0,"李四")
```

第二列写入`日期`,日期需要添加字符样式

```python
#设置字符样式
format_dic['num_format'] = "yyyy-mm-dd HH:MM:SS"
date_format = workbook.add_format(format_dic)
#第二列表头
worksheet.write(0,1,"时间",text_format)
#第2行第2列内容
date_time = datetime.datetime.strptime("2013-01-03","%Y-%m-%d")
worksheet.write_datetime(1,1,date_time,date_format)
#第3行第2列内容
worksheet.write_datetime(2,1,datetime.datetime.now(),date_format)
```

### 具体实现代码

```python
import xlsxwriter
import datetime

workbook = xlsxwriter.Workbook("demo.xlsx")
#创建Sheet 名称为demo
worksheet = workbook.add_worksheet("demo")
#第0行第0列宽度为40
worksheet.set_column(0,0,40)
#字体添加样式
format_dic = {
    "bold":True,
    "font_color":"#DC143C",
    "font_size":20
}
text_format = workbook.add_format(format_dic)
#第一列------------------------------------------------
#第0行第0列内容为【Name】样式为 加粗，红色，大小20
worksheet.write(0,0,"姓名",text_format)
worksheet.write(1,0,"张三")
worksheet.write(2,0,"李四")
#第二列------------------------------------------------
#第0行第1列宽度为80
worksheet.set_column(0,1,40)
format_dic['num_format'] = "yyyy-mm-dd HH:MM:SS"

date_format = workbook.add_format(format_dic)

worksheet.write(0,1,"时间",text_format)
date_time = datetime.datetime.strptime("2013-01-03","%Y-%m-%d")
worksheet.write_datetime(1,1,date_time,date_format)

worksheet.write_datetime(2,1,datetime.datetime.now(),date_format)

workbook.close()
```
