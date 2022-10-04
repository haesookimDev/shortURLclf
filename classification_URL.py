class shortURLsClassification():
    def __init__(self) -> None:
        self.shortURLList = ['adfoc.us/', 'vvd.bz/', 'me2.kr/', '3.ly/', 'rb.gy/', 'adf.ly/', 'na.to/', 'nic.do/', 'koe.kr/', 'safeds.tk/', 
        'Bit.ly/', 'gourl.kr/', 'twr.kr/', 'hana.icu/', 'han.gl/', 'bit.do/', 'gg.gg/', 'lrl.kr/', 'mlnl.me/', 'blow.pw/', 'star.net/', 
        'asq.kr/', 'tinyurl.com/', 'abit.ly/', 'c11.kr/', 'di.do/', 'ouo.io/', 'wiv.kr/', 'url.sg/', 'vot.kr/', 'muz.so/', 't.ly/', 't2m.kr/', 
        'reurl.kr/', 'flic.kr/', 'url.kr/', 'vo.la/', 'fw.sg/', 't.co/', 'is.gd/', 'zrr.kr/', 'wo.to/']
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
                self.isDomain = False
                continue
        return self.isDomain