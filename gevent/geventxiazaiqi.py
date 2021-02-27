"""gevent下载器"""
from gevent import monkey
import gevent
from  urllib import request

#需要让gevent自动处理io事件
monkey.patch_all()


def myDownload(url):
	print('get : %s'%url)
	response = request.urlopen(url)
	data = response.read()
	print('从%s收到%d的数据'%(url,len(data)))
#生成协程对象
gevent.joinall([gevent.spawn(myDownload,"http://www.baidu.com"),gevent.spawn(myDownload,"http://www.sohu.com"),gevent.spawn(myDownload,"http://www.hao123.com")])