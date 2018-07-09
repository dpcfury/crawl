import urllib2

str = "http://img.mukewang.com/57035ff200014b8a06000338-240-135.jpg"
str2="https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1479397771&di=27d0d343c2048212068e734489361ee4&src=http://img002.21cnimg.com/photos/album/20160326/m600/B920004B5414AE4C7D6F2BAB2966491E.jpeg"
str3 ="https://img1.doubanio.com/lpic/s29130957.jpg"
req= urllib2.urlopen(str3)
buff = req.read()
f =open("test3.jpg","wb")
f.write(buff)