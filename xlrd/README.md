# 使用`xlrd`来读取Excel文件

# 使用方法

## 打开excel

```python
book = xlrd.open_workbook("day_01.xls")
```

## 获取总页数

```python
book.nsheets
```

## 获取book中的第一个工作表

```python
book.sheet_names()
```

## 获取工作表名称

```python
sh.name
```

## 获取工作表总行数，总列数

```python
#获取工作表总行数
sh.nrows
#获取工作表总列数
sh.ncols
```

## 获取单元格数据函数

```python
sh.cell_value(rowx=rowx,colx=cols)
```

## 打印每一行的值

```python
# for rowx in range(sh.nrows):
#     print("第{0}行".format(rowx+1),end="")
#     for cols in range(sh.ncols):
#         print(" 第{0}列：{1}"\
#               .format(cols+1,sh.cell_value(rowx=rowx,colx=cols)))
```

# 脚下留心

## 时间格式转化

打印时间`43860.0`对应`2020/1/30`

```python
for rowx in range(sh.nrows):
    tmp_row_val = sh.row_values(rowx)
    tmp_date = ''
    #注意表头不是时间类型
    if rowx >= 1:
        tmp_date = xlrd.xldate_as_datetime(tmp_row_val[3],0).strftime("%Y-%m-%d")
        tmp_row_val[3] = tmp_date
    print(tmp_row_val)
```

# 具体实现代码及Excel

```


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
```

| 景点名称             | 景点特色                                                     | 门票金额 | 出行日期  | 旅途费用 | 购物消费 |
| -------------------- | ------------------------------------------------------------ | -------- | --------- | -------- | -------- |
| 广州融创雪世界       | 国内滑雪场首条探险步道，集趣味、娱乐、拓展功能为一体，在高空、速度、力量、毅力等元素的挑战中，感受感官上的刺激和闯关成功的成就感。 | 145      | 2020/1/30 | 550      | 299      |
| 广州长隆旅游度假区   | 长隆旅游度假区(AAAAA景区)，长隆国际大马戏拥有全球首创实景式马戏舞台，为你打造令人惊叹的视听盛宴 | 69       | 2020/5/1  | 850      | 60       |
| 南沙百万葵园         | 以迷人的北海道七彩花田、浪漫的普罗旺斯薰之恋、热情的英伦玫瑰苑、缤纷的七彩天鹅鲜花地以及神奇的万朵鲜花天上飘等等不同亮点组合而成，真所谓花花世界，美景无敌。 | 69       | 2020/5/2  | 0        | 100      |
| 广州塔               | 广州塔别具匠心地在428米及433.2米高度处分设白云和星空主题观光大厅，全透明钢化夹胶玻璃构造的悬空走廊，带来前所未有的凌空观景刺激感受 | 147      | 2020/5/3  | 0        | 160      |
| 广州正佳极地海洋世界 | 正佳极地海洋世界坐落于广州天河核心商圈正佳广场，总建筑面积超58000平方米，拥有共500种超30000只极地海洋动物，是座室内空中极地海洋馆。 | 80       | 2020/10/1 | 2999     | 99       |
| 宝墨园               | 满园樱色，樱园一带以小日樱花为主，收集了早樱、晚樱和垂枝樱等共6种10余个佳品的樱花，花色丰富，绚丽多彩，枝、干多异且花期不同。 | 41       | 2020/10/2 | 0        | 0        |
| 广东科学中心         | 本展馆展示了人类千百年来的梦想--翱翔蓝天，挣脱了地球引力，实现了千百年来的梦想。以环保为主题，岭南特色为背景，以生动有趣的形式将美丽的大自然全景式地展现在观众面前。 | 42       | 2020/10/3 | 0        | 80       |
| 珠江夜游             | 宽大的空间在悠和的灯光映衬下，尤如置身于五星级殿堂。出游时播放江面景观的室内视频，即使下雨，亦可在室内观赏珠江两岸的景色。 | 47.5     | 2020/10/4 | 0        | 0        |
| 岭南印象园           | 岭南乡土风情和民俗文化，悠长的青云巷、古朴的趟栊门、精致的满洲窗，小溪蜿蜒，池塘清澈，处处散发着岭南水乡的韵味。 | 47.1     | 2020/10/5 | 0        | 500      |
| 增城白水寨风景名胜区 | 全国仅见的精品海船木栈道。在白水寨漫步古朴的海船木栈道登山观瀑，看流水潺潺、听瀑布轰鸣，倍感诗意。 | 55       | 2020/10/6 | 0        | 0        |