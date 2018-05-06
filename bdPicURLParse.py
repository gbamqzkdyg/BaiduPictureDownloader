import urllib.parse

def bdParse(rawURL):
	dic ={'w': "a", 'k': "b", 'v': "c", '1': "d", 'j': "e", 'u': "f", '2': "g", 'i': "h", 't': "i", '3': "j", 'h': "k", 's': "l", '-': '-',
		'4': "m", 'g': "n", '5': "o", 'r': "p", 'q': "q", '6': "r", 'f': "s", 'p': "t", '7': "u", 'e': "v", 'o': "w", '8': "1", 'd': "2", 
		'n': "3", '9': "4", 'c': "5", 'm': "6", '0': "7", 'b': "8", 'l': "9", 'a': "0"} 
	rawURL = rawURL.replace('_z2C$q', ":").replace('_z&e3B', ".").replace('AzdH3F', "/")
	charList = list(rawURL.lower())
	url = ''
	for char in charList:
		url += dic[char] if char in dic else char
	return url
	
def parseChinese(string):
	return urllib.parse.quote(string)

if __name__ == '__main__':
	print(bdParse('ippr_z2C$qAzdH3FAzdH3Fvg_z&e3Bp5s7gw_z&e3Bv54AzdH3F1r5ssf_t4w2jfAzdH3Fda8mAzdH3Fa0AzdH3FamAzdH3Fa8jvl9ba-a09v-9mj1-b80a-mwu0b0d18j8w_xnaa_z&e3B3r2'))