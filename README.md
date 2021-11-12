# Small Property Right Housing Project

This repository contains the source code and data for the SPRH research project.

## Repo structure

```
├─data
|	└─main.csv
├─do
|	└─dofile_0730.do
└─src
	├─__init__.py
    ├─utils
    |	├─__init__.py
    |	├─geocode.py
    |	├─scraper.py
    |	└─visualization.py
    └─deprecated
    	├─__init__.py
    	├─getGeoCoding.py
    	├─getPOIs.py
    	├─getSPRH.py
    	├─getSchHsplocation.py
    	├─getSchools.py
    	├─get_comm_community.py
    	├─get_hospital_info.py
    	├─get_school_type.py
    	├─identify_attr.py
    	├─mercator_to_gps.py
    	└─mindistance.py
```

* **data**:
  * `main.csv`合并了所有搜集的变量，包含约2400套商品房和450套小产权房的单价和相关属性信息。
* **do**:
  * Stata do文件，对应文章中的几张图表。采用`asdoc`包直接输出结果。
* **src**:
  * 数据收集部分的Python源码。
  * `utils`文件夹包含几个可重用的函数：具体包括地理编码的`geocode`模块，网页爬取的`scraper`模块以及地图可视化的`visualization`模块。
  * `deprecated`文件夹包含早期编写的函数，不推荐使用，但可在其基础上修改。早期编写的模块硬编码过多，重用性较差；且存在命名规则混乱、说明文档不完整的问题。若考虑扩增新数据源，建议重新编写更灵活的新模块实现。

## Email Contact

Chengyu Wu (chengyu2{at}andrew.cmu.edu / chengyuwu8193{at}zju.edu.cn)