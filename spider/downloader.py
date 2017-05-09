from urllib import request, parse


class Downloader(object):

    def download_json(self, url, data_string):
        if url is None or data_string is None:
            return None

        encode_data = parse.urlencode(data_string).encode()
        req = request.Request(url=url, data=encode_data)
        response = request.urlopen(req)

        if response.getcode() != 200:
            return None
        # print(type(response.read().decode()))
        return response.read().decode()

    def download_html(self, url):
        if url is None:
            return

        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0', }
        response = request.urlopen(request.Request(url=url, headers=head))
        if response.getcode() != 200:
            return None

        return response.read()
