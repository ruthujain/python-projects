import pyqrcode
data='https://github.com/ruthujain'
img=pyqrcode.create(data)
img.png('ruthuGithub.png',scale=8)