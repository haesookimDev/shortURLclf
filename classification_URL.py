class shortURLsClassification():
    def __init__(self) -> None:
        self.shortURLList = ['Bit.ly', 'tinyurl.com' , 'bit.do', 'vvd.bz', 'url.kr', 'is.gd', 
        't2m.kr', '3.ly', 'rb.gy', 'reurl.kr', 'abit.ly', 'blow.pw', 
        'c11.kr', 'di.do', 'han.gl', 'koe.kr', 'lrl.kr', 'muz.so', 
        'adf.ly', 'ouo.io', 'adfoc.us']
        self.isDomain = False
        self.shortURL = False
        self.result = {}
    
    def clf_short_url(self, url):
        
        self.isDomain = self.check_url_domain(url)

        self.shortURL = self.isDomain
        self.result = {'isShort': self.shortURL, 'URL': url}

        return self.result

    def check_url_domain(self, url):

        # this part compares the URL with the domain of the URL Shortening service
        for URL in self.shortURLList:
            if URL in url:
                self.isDomain = True
                break
            else:
                continue
        return self.isDomain