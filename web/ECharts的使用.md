# ECharts的简单使用

ECharts是JS作图的文件

## 源

[官网:https://echarts.apache.org/zh/](https://echarts.apache.org/zh/)

[下载地址：https://echarts.apache.org/zh/download.html](https://echarts.apache.org/zh/download.html)

## 使用

html页面引入

+ 本地引入：

  ```html
  <script type="text/javascript" charset="utf-8" src="static/js/echarts.min.js"></script>
  ```

+ 第三方引入：

  ```html
  https://cdn.jsdelivr.net/npm/echarts@5.0.1/dist/echarts.min.js
  ```

  

通过[官网实例](https://echarts.apache.org/examples/zh/index.html)拉入简单的数据

```html
option = {
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [150, 230, 224, 218, 135, 147, 260],
        type: 'line'
    }]
};
```

页面展示，**body**中嵌入以下内容

```html
<div id="test_wrap" style="min-height: 400px;">
	123123
</div>
<script type="text/javascript">
    var chart = echarts.init(document.getElementById("test_wrap"));
    var option = {
    	xAxis: {
        	type: 'category',
        	data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    	},
    	yAxis: {
        	type: 'value'
    	},
    	series: [{
        	data: [150, 230, 224, 218, 135, 147, 260],
        	type: 'line'
    	}]
	};
    chart.setOption(option);
</script>
```

## 扩展

### 标题title

title组件用于渲染图表的标题，含主标题、副标题两部分

title组件支持配置位置、文本样式、链接模式等

### 提示框tooltip

当鼠标悬停再图表的某点或坐标轴的某个值上时，以浮层的方式展示该点数据信息的组件。提示框内提示的信息还可以通过格式化函数动态指定

### 图例legend

图例是图表的辅助视觉引导组件，用以解释说明图表中各数据序列的含义及图表中数据的筛选

### 工具栏toolbox

图表操作工具栏，内置导出图片、数据视图、动态图表类型切换、数据区域缩放、重置五种工具，但不支持自定义扩展

### 坐标系组件

不同的图表要使用特定的坐标系才能完成渲染

+ 直角坐标系：通过grid、xAxis、yAxis组件实现
+ 极坐标系：通过polar、angleAxis、radiusAxis组件实现
+ 地图坐标系：通过geo组件实现
+ 平行坐标系：通过parallelAxis、parallel组件实现
+ 日历坐标系：通过calendar组件实现
+ 雷达坐标系：通过radar组件实现

### 具体使用

```html
<script type="text/javascript">	
	var option = {
            title: {
                text: "echarts主标题",
                subtext: "副标题"
            },
            tooltip: {
                trigger: "axis"
            },
            toolbox: {
                show: true,
                feature: {
                    dataView: {},//数据视图 可以编辑
                    restore: {},//还原
                    saveAsImage: {},//保存图片
                    magicType: { type: ['line', 'bar'] },//切换折线图和柱状图
                    dataZoom: {}//区域放大
                }
            },
            xAxis: {
                type: 'category',
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            },
            yAxis: {
                type: 'value'
            },
            series: [{
                data: [120, 200, 150, 80, 70, 110, 130],
                type: 'bar',
                showBackground: true,
                backgroundStyle: {
                    color: 'rgba(180, 180, 180, 0.2)'
                }
            }]
        };
</script>
```



