# -*- coding: UTF-8 -*-
import xlwt as excel
import readJson


def write_row(sheet, rowIndex, item):
    sheet.write(rowIndex, 0, item["code"])
    sheet.write(rowIndex, 1, item["name"])
    sheet.write(rowIndex, 2, item["location"])


def create_a_sheet(workbook, sheetName):
    sheet = workbook.add_sheet(sheetName)
    sheet.col(0).width = 256 * 20
    sheet.col(1).width = 256 * 20
    sheet.col(2).width = 256 * 20
    # 添加标题
    sheet.write(0, 0, "编号")
    sheet.write(0, 1, "名称")
    sheet.write(0, 2, "地点")
    return sheet


def get_sheetName(items):
    return items[0]["location"]


def write_a_room_to_a_sheet(workbook, room):
    roomName = get_sheetName(room)
    sheet = create_a_sheet(workbook, roomName)
    for asset in room:
        # the 0th row is row title, so start from 1
        rowIndex = room.index(asset) + 1
        write_row(sheet, rowIndex, asset)


# handle room list assets
def handleRoomListAssets(workbook, roomsAssets):
    for room in roomsAssets:
        write_a_room_to_a_sheet(workbook, room)


def process(allAssets):
    # create output excel
    myWorkbook = excel.Workbook()

    handleRoomListAssets(myWorkbook, allAssets)

    # save to file
    myWorkbook.save("output.xls")


# def get_mock_data():
#     return [
#         [
#             {"code": "CBEX_7101_KZ_001", "name": "课桌", "location": "7101"},
#             {"code": "CBEX_7101_KZ_002", "name": "课桌", "location": "7101"},
#         ],
#         [
#             {"code": "CBEX_7102_DZ_001", "name": "凳子", "location": "7102"},
#             {"code": "CBEX_7102_DZ_002", "name": "凳子", "location": "7102"},
#         ],
#     ]

if __name__ == "__main__":
    allAssets = readJson.getDataSource()
    process(allAssets)
    print("写入成功")
