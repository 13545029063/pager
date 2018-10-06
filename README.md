# pager
基于python的分页功能  
通过Pagination类进行调用   
参数：totalCount#总个数   currentPage#当前页   perPageItemNum=10#每页显示的行数默认值为10   maxPageNum=7最多显示的页数默认是7    
start():返回起始页面 type是int    
end():返回结束页面  可以在views.py下通过切片进行输出比如 data_list=[Pagination.star（）：Pagination.end（）]进行操作 因为data_list是一个list所以在前端可以通过for循环来进行输出内容比如：  
{% for i in data_list %}   
    <h4>{{ i }}</h4>   
{% endfor %}    
NumPage()：进行求算总页数     
page_num_rage（）：编写页面输出规则     
page_str():返回给前端的标签 可以在前端直接通过模板进行渲染输出{{ Pager_obj.page_str|safe}},如果需要更改css样式可以在page_str中给标签添加class属性   
