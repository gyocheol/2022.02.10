from xml.etree import ElementTree
import requests
import re

service_key = 'YBq6ApN0BcnCNI8xxOUQVegeDibpNcrfRSmK0oq8sdeRbhtM4H5J%2Fwt4MgTOjUNUlIfoocSou9BBsvFGNNDB%2Fg%3D%3D'
url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}'
print(url)

resp = requests.get(url)
# print(resp.text)

# url요청을 하면 서버에서 응답되는데 xml형태의 doc(문자열)이었다. 문자열을 가지고 parser tree 를 만들어 주는 식
tree = ElementTree.fromstring(resp.text)

for item in tree[1][0]:
    # print(item)

    # 구분 값 가져오기
    # gubun = item.find('gubun').text
    # print(gubun)

    if item.find('gubun').text == '합계':
        stdDay = re.sub(r'(\D)+', '', item.find('stdDay').text)
        # print(stdDay)
        stdDay = stdDay[2:4] + "/" + stdDay[6:8] + "/" + stdDay[6:8]
        # print(stdDay)
        incDec = item.find('incDec').text
        localOccCnt = item.find('localOccCnt').text
        overFlowCnt = item.find('overFlowCnt').text
        print(f'[{stdDay}]\n일일합계:{incDec}\n국내발생:{localOccCnt}\n해외발생:{overFlowCnt}')






