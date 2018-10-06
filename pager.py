class Pagination(object):
    def __init__(self,totalCount,currentPage,perPageItemNum=10,maxPageNum=7):
        self.total_Count=totalCount
        #总个数
        try:
            v=int(currentPage)
            if v<=0:
                v=1
                self.current_Page=v
            else:
                self.current_Page=int(currentPage)
            #当前页,用户有可能输入的有误在此对当前页进行异常捕捉
        except Exception as e:
            self.current_Page=1
        self.per_Page_Item_Num=perPageItemNum
        #每页显示的行数
        self.max_Page_Num=maxPageNum
        #最多显示的页数
    def start(self):
        return (self.current_Page-1)*self.per_Page_Item_Num
    def end(self):
        return self.current_Page*self.per_Page_Item_Num
    @property#未添加的时候self.NumPage()进行条用，添加装饰器后直接self.NumPage就可以
    def NumPage(self):
        '''求总页数'''
        a,b=divmod(self.total_Count,self.per_Page_Item_Num)
        #用divmod方法对总个数和每页显示的行数进行取余数，返回两个值a,b
        #a是返回的页数，b是余数。如果b不等于0则说明页数需要+1
        if b==0:
            return a
        else:
            return a+1
    def page_num_rage(self):
        #对页数进行规则编写
        if self.NumPage<self.max_Page_Num:
            return range(1,self.NumPage)
        part=int(self.max_Page_Num)
        if(self.current_Page+part)>self.NumPage:
            return range(self.NumPage-self.max_Page_Num,self.NumPage+1)
        if self.current_Page-part>0:
            return range(self.current_Page,self.current_Page+part+1)
        else:
            return range(self.current_Page,self.current_Page+part+1)
    def page_str(self):
        #返回前端的数据直接可以通过模板语言进行渲染 
        page_list=[]
        if self.current_Page<=1:
            prev = "<li><a href='#'>上一页</a></li>"
        else:
            prev = "<li><a href='/index2.html?p=%s'>上一页</a></li>"%(self.current_Page-1)
        page_list.append(prev)
        for i in self.page_num_rage():
            if i==self.current_Page:
                temp = "<li class='active'><a href='/index2.html?p=%s'>%s</a></li>" % (i, i)
                page_list.append(temp)
            else:
                temp ="<li><a href='/index2.html?p=%s'>%s</a></li>"%(i,i)
                page_list.append(temp)
        if self.current_Page>=self.NumPage:
            next_Page = "<li><a href='#'>下一页</a></li>"
        else:
            next_Page = "<li><a href='/index2.html?p=%s'>下一页</a></li>" % (self.current_Page + 1)
        page_list.append(next_Page)
        return ''.join(page_list)
