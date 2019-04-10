#### 实现一个简单的xml解析器，解析此文件夹下的example.txt、并树状打印其内容。

#### 举个例子，输出格式可参考：
```
test-value:"main"
    a1-key1:"google1"-key2:"company1"
    name1-key1:"super1"-value:"cctv1"
    int1-value:666
    second
        a2-key1:"google2"-key2:"company2"
        name2-key1:"super2"-value:"cctv2"
        int2-value:777
    char1-value:"c"
```
#### 要求：务必自己实现xml文档解析功能，调用现成的xml库解析文档视为题目未完成。
#### 举三个错误示范的例子：
    JavaScript的xmlDoc=loadXMLDoc("example.txt");xmlDoc.getElementsByTagName("test");
    Python的import xml.etree.ElementTree
    使用C++的rapidxml库
#### 要求：务必自己实现xml文档解析功能，调用现成的xml库解析文档视为题目未完成。
