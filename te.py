import exifread
a = open(r'C:\Users\Administrator\Desktop\tr\微信图片_20220327202900.jpg','rb')
tags = exifread.process_file(a)
lat = tags.get('GPS GPSLatitudeRef')
print(lat)
