# -*- coding: UTF-8 -*-
import xlwt as excel
import readJson


def write_row(sheet, rowIndex, item):
    sheet.write(rowIndex, 0, item["code"])
    sheet.write(rowIndex, 1, item["name"])
    sheet.write(rowIndex, 2, item["location"])


def write_excel(items):
    # 创建Excel工作薄
    myWorkbook = excel.Workbook()

    # 添加Excel工作表
    sheetName = get_locationName(items)
    workSheet = create_sheet(myWorkbook, sheetName)

    # 写入内容
    for item in items:
        rowIndex = items.index(item) + 1  # 第0行已经写成标题了
        write_row(workSheet, rowIndex, item)

    # 保存到文件
    # myWorkbook.save("output.xls")
    myWorkbook.save("output.xlsx")


def create_sheet(workbook, sheetName):
    sheet = workbook.add_sheet(sheetName)
    sheet.col(0).width = 256 * 20
    sheet.col(1).width = 256 * 20
    sheet.col(2).width = 256 * 20
    # 添加标题
    sheet.write(0, 0, "编号")
    sheet.write(0, 1, "名称")
    sheet.write(0, 2, "地点")
    return sheet


def get_locationName(items):
    return items[0]["location"]


if __name__ == "__main__":
    # 提取数据
    items = readJson.getDataSource()
    # 写入Excel
    write_excel(items)
    print("写入成功")
