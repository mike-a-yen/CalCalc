import argparse
import requests
import xml.etree.ElementTree as ET


def make_query(query):
    base = 'http://api.wolframalpha.com/v2/query?'
    params = {'input':query,'appid':'UAGAWR-3X6Y8W777Q'}
    response = requests.get(base,params=params)
    return response.content

def calculate(query):
    xmlparser = ET.XMLParser(encoding="utf-8")
    tree = ET.fromstring(make_query(query),parser=xmlparser)
    for pod in tree.findall('pod'):
        if pod.attrib.get('id') == 'Result':
            sub = pod.find('subpod')
            result = sub.find('plaintext').text
            return result
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('s', type=str)

    args = parser.parse_args()
    query = args.s

    print(calculate(query))

