xdlinux 的project的页面
===

Install 
---
* 好吧....安装方法....
1. xdp.py 不要放到公开目录，放到一个安全的地方，当然必须在计算机里面。
2. 其他文件放在一个可以被访问的目录。
3. xdproject.html 这个是主页，如果需要可以修改名字，但是要记住修改xdp.py里面的相关的名字。
4. 然后修改xdp.py里面的路径为绝对路径。
5. 定时执行xdp.py 这个可以很随意，可以是crontab 或是由其他的程序调用，每次调用就会重新构造一边xdproject.html
* 这个安装过程，写的很随意。

基本思路:
---
这个问题划归成三个基本问题求解:

1. 获得页面
2. 正则处理，手动正则，这个对我来说比学习一个新的库更快，而且更自由
3. 生成新的页面，要求比较文艺，争取让大家喜欢上数学！

目录及文件简介：
---
* xdp.py        #核心程序
* project.html  #最终生成的html文件
* reference/     #存放编写程序的时候用到的资料
* cache/         #存放抓取来的页面
* data/          #存放生成的数据


一些问题：
---
* 这里思考再三选择直接处理文件，原因如下：
    1. 本人的编程习惯，自建buffer然后处理，就是习惯。
    2. 没有思考太多扩展的问题，因为这个只是一个练习。
    3. 写这个程序更大的目的是为了引导大家学习简明为第一位的。
    4. 本人写程序比较随心，而且思维模式简单，总想把不同的问题划归成基本问题求解。

* 好吧被说服了用beautifulsoup

TODO
---
* 信息的直接呈现，新的提交、Push等直接呈献在页面上
* 加入 Github API 模块
* 改进前端
* 与 IndexPlus 整合

PS: 脑子不太好使了，在这里记录一下吧：`git push -u origin master`
