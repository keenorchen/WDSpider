from urllib import request
import json
from bs4 import BeautifulSoup


class Parser(object):
    def parse_json(self, string):
        if string is None or string == '':
            return

        data_list = json.loads(string)
        return data_list

    def parse_html(self, data):
        if data is None:
            return

        soup = BeautifulSoup(data, "lxml")
        data_list = []
        title_nodes = soup.find('thead', id='platdatahd').tr.find_all('th', class_=self.not_operation)
        titles = []
        for node in title_nodes:
            titles.append(node.get_text())
        data_list.append(titles)

        item_nodes = soup.find('table', id='platdata').tbody.find_all('tr')
        for item in item_nodes:
            items = []
            for node in item.find_all('td', class_=self.not_operation):
                items.append(node.get_text(strip=True))
            data_list.append(items)
        return data_list

    def not_operation(self, css_class):
        return css_class != 'operation'
