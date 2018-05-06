import requests
import os
import bdPicURLParse as p

PREFIX = 9

def count(name, total, stateLabel):
	current = len(os.listdir('pictures/' + name))
	if(current >= total):
		stateLabel['text'] = '下载完成！'
	else:
		stateLabel['text'] = '当前下载进度为：' + str(current / total *100) +'%'
		timer = threading.Timer(3.0, count, [name, total, stateLabel])
		timer.start()


def getParas(pn):
	pn = int(pn) + 30
	gsm = hex(pn)[2: ]
	return (str(pn), gsm)
	
def generateURL(generalName, pn, gsm):
	return ('http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=' 
		+ generalName + '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=' + generalName + '&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn='
		+ pn +'&rn=30&gsm=' + gsm + '&1525113364454')
		
def generateHeader(generalName):
	data = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Connection': 'keep-alive',
		'Cookie': 'BDqhfp=pokemon%26%26NaN-1undefined%26%260%26%261; BAIDUID=A637E0677CF3322B07E1195A238804C5:FG=1; BIDUPSID=A637E0677CF3322B07E1195A238804C5; PSTM=1507021395; BDUSS=dMa0s4dVVzOWtNOHRsYWd3NlhPVlFvSHQ1N3VmRWxJSGtjQzJSQzloVk8tdjVaTUFBQUFBJCQAAAAAAAAAAAEAAACWWWcAZ2JhbXF6a2R5ZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE5t11lObddZc1; pgv_pvi=6650045440; cflag=15%3A3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1436_21081_26184_20929; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=7; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; __lnkrntdmcvrd=-1; indexPageSugList=%5B%22pokemon%22%2C%22%E5%AE%8B%E5%AE%B6%E4%B8%89%E8%83%9E%E8%83%8E%20%E8%A1%A8%E6%83%85%E5%8C%85%22%2C%22%E7%88%B8%E7%88%B8%E5%8E%BB%E5%93%AA%E5%84%BF%20%E8%A1%A8%E6%83%85%E5%8C%85%22%5D; cleanHistoryStatus=0',
		'Host': 'image.baidu.com',
		'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1525113281603_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=' + generalName,
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
	}
	return data
	
extensions = ['png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG']

def getSource(url, generalName):
	data = generateHeader(generalName)
	r = requests.post(url, headers = data)
	html = r.text
	return html, html.find('objURL"')

def updateHTML(html, position, picURL):
	html = html[position + PREFIX + len(picURL): ]
	return html, html.find('objURL"')
	
def getPicURL(html, position):
	picURL = p.bdParse(html[position + PREFIX : position + 500].split('"')[0].replace('\/','/'))
	return picURL, picURL.split('.')[-1]
	
def getPic(name,picURL, current, extension):
	try:
		pic = requests.get(picURL, timeout = 3).content
		if(len(pic) >= 20480):
			with open('pictures/' + name + '/' + name + '%d'%current + '.' + extension, 'wb') as f:
				f.write(pic)
			print('#%d:\t%s'%(current,picURL))
			current += 1
	except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout, requests.exceptions.TooManyRedirects):
		pass
	return current
	
def updateSource(pn, generalName):
	(pn, gsm) = getParas(pn)
	url = generateURL(generalName, pn, gsm)
	return getSource(url, generalName) 

def createDir(name):
	if not os.path.exists('pictures'):
		os.mkdir('pictures')
	if not os.path.exists('pictures/' + name):
		os.mkdir('pictures/' + name)

def download(name = '梅西', total = 20):
	createDir(name)
	generalName = p.parseChinese(name)
	(pn, gsm) = getParas(0)
	url = generateURL(generalName, pn, gsm)
	(html, position) = getSource(url, generalName) 
	current = 1
	while current <= total:
		while position != -1 and current <= total:
			(picURL, extension) = getPicURL(html, position)
			if(extension in extensions):
				current = getPic(name, picURL, current, extension)
			(html, position) = updateHTML(html, position, picURL)
		(html, position) = updateSource(pn,generalName)

if __name__ == '__main__':
	download('梅西', 15)