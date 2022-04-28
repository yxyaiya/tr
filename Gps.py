import exifread
import json
import requests
import jsonpath
def process_img(path):
    '''
    这个函数用来处理图片 并返回图片的 经纬度、拍摄时间信息
    :return: 返回图片信息 是一个字典
    '''
    f = open(path, 'rb')
    tags = exifread.process_file(f)
    info = {
        # 注意 这里获得到的是值 需要使用 values方法
        'Image DateTime(拍摄时间)': tags.get('Image DateTime', '0').values,
        'GPS GPSLatitudeRef(纬度标志)': tags.get('GPS GPSLatitudeRef', '0').values,
        'GPS GPSLatitude(纬度)': tags.get('GPS GPSLatitude', '0').values,
        'GPS GPSLongitudeRef(经度标志)': tags.get('GPS GPSLongitudeRef', '0').values,
        'GPS GPSLongitude(经度)': tags.get('GPS GPSLongitude', '0').values
    }
    return info
def get_info(lat, lng):
    '''
     注意 网站的经纬度接口格式是 h.mmsssssss
    :param lat:  纬度
    :param lng:  经度
    :return: 返回地址信息
    '''
    url = r'http://www.gpsspg.com/apis/maps/geo/?output=json&lat={}&lng={}&type=0' \
          r'&callback=jQuery110209178036150146593_1559380618496&_=1559380618502'.format(lat, lng)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Referer': 'http://www.gpsspg.com/iframe/maps/baidu_181109.htm?mapi=1',
        'Host': 'www.gpsspg.com',
    }
    r = requests.get(url, headers=headers)
    # 返回的是一个json字符串文本 使用 r.json()方法 转化为python字典
    info = r.json()
    # 使用jsonpath 查找地址信息
    address = jsonpath.jsonpath(info, '$..address')[0]
    return address
def process_num(x):
    '''
    处理经纬度 将其转化为 xx.xxxxxx格式
    注意列表中的每一个元素 是 <class 'exifread.utils.Ratio'>
    由于最后一个是 10243/2000 这样的格式 需要手动将其处理 其余的使用 .num 方法就能获得到值
    :param x: 传入的经度和纬度
    :return: 处理好了经纬度
    '''
    # 处理列表中最后一个元素
    x_last = eval(str(x[-1]))
    #  转化
    new_x = x[0].num + x[1].num / 60 + x_last / 3600

    return '{:.13f}'.format(new_x)
def main():
    img_path = r'C:\Users\Administrator\Desktop\tr\2.jpg'
def process_img(path):
    '''
    这个函数用来处理图片 并返回图片的 经纬度、拍摄时间信息
    :return: 返回图片信息 是一个字典
    '''
    f = open(path, 'rb')
    tags = exifread.process_file(f)
    info = {
        # 注意 这里获得到的是值 需要使用 values方法
        'Image DateTime(拍摄时间)': tags.get('Image DateTime', '0').values,
        'GPS GPSLatitudeRef(纬度标志)': tags.get('GPS GPSLatitudeRef', '0').values,
        'GPS GPSLatitude(纬度)': tags.get('GPS GPSLatitude', '0').values,
        'GPS GPSLongitudeRef(经度标志)': tags.get('GPS GPSLongitudeRef', '0').values,
        'GPS GPSLongitude(经度)': tags.get('GPS GPSLongitude', '0').values
    }
    return info
def get_info(lat, lng):
    '''
     注意 网站的经纬度接口格式是 h.mmsssssss
    :param lat:  纬度
    :param lng:  经度
    :return: 返回地址信息
    '''
    url = r'http://www.gpsspg.com/apis/maps/geo/?output=json&lat={}&lng={}&type=0' \
          r'&callback=jQuery110209178036150146593_1559380618496&_=1559380618502'.format(lat, lng)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Referer': 'http://www.gpsspg.com/iframe/maps/baidu_181109.htm?mapi=1',
        'Host': 'www.gpsspg.com',
    }
    r = requests.get(url, headers=headers)
    # 返回的是一个json字符串文本 使用 r.json()方法 转化为python字典
    info = r.json()
    # 使用jsonpath 查找地址信息
    address = jsonpath.jsonpath(info, '$..address')[0]
    return address
def process_num(x):
    '''
    处理经纬度 将其转化为 xx.xxxxxx格式
    注意列表中的每一个元素 是 <class 'exifread.utils.Ratio'>
    由于最后一个是 10243/2000 这样的格式 需要手动将其处理 其余的使用 .num 方法就能获得到值
    :param x: 传入的经度和纬度
    :return: 处理好了经纬度
    '''
    # 处理列表中最后一个元素
    x_last = eval(str(x[-1]))
    #  转化
    new_x = x[0].num + x[1].num / 60 + x_last / 3600

    return '{:.13f}'.format(new_x)
def main():
    img_path = r'C:\Users\Administrator\Desktop\tr\1.jpg'
    info_dict = process_img(img_path)
    lat = info_dict.get('GPS GPSLatitude(纬度)')
    lng = info_dict.get('GPS GPSLongitude(经度)')
    address = get_info(lat=process_num(lat), lng=process_num(lng))

    print('拍摄时间: {},GPS位置:纬度{}{},经度{}{}'.format(info_dict.get('Image DateTime(拍摄时间)'),
                                                 info_dict.get('GPS GPSLatitudeRef(纬度标志)'),
                                                 process_num(lat),
                                                 info_dict.get('GPS GPSLongitudeRef(经度标志)'),
                                                 process_num(lng),
                                                 ))
    print('具体位置: {}'.format(address))
    info_dict = process_img(img_path)
    lat = info_dict.get('GPS GPSLatitude(纬度)')
    lng = info_dict.get('GPS GPSLongitude(经度)')
    address = get_info(lat=process_num(lat), lng=process_num(lng))

    print('拍摄时间: {},GPS位置:纬度{}{},经度{}{}'.format(info_dict.get('Image DateTime(拍摄时间)'),
                                                 info_dict.get('GPS GPSLatitudeRef(纬度标志)'),
                                                 process_num(lat),
                                                 info_dict.get('GPS GPSLongitudeRef(经度标志)'),
                                                 process_num(lng),
                                                 ))
    print('具体位置: {}'.format(address))





