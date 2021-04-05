import openpyxl
import os
class ToolExcel:
    def __init__(self,path,sheetname):
        self.wb=openpyxl.load_workbook(path)
        self.sh=self.wb[sheetname]
    #返回title
    def read_title(self):
        title=[]
        for cell in list(self.sh.rows)[0]:
            title.append(cell.value)
        return title
    #返回所有数据
    def all_datas(self):
        data=[]
        for item in list(self.sh.rows)[1:]:
            content = []
            for cell in item:
                content.append(cell.value)
            res=dict(zip(self.read_title(),content))

            data.append(res)
        return data
    #关闭
    def close_wb(self):
        self.wb.close()

if __name__ == '__main__':
    file=os.path.join(os.path.dirname(os.path.abspath(__file__)),'data.xlsx')
    a=ToolExcel(file,"login")
    print(a.all_datas())
    a.close_wb()