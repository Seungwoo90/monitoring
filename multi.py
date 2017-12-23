import bs4
import requests
import re
import time
import webbrowser
import glob
import random
import os
from playsound import playsound
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def make_href(get_html):
    get_href = []
    get_whole = []
    for a in get_html:
        each_href=[]
        each_whole=[]
        soup = bs4.BeautifulSoup(a, "html.parser")
        href = soup.find_all(href=re.compile("ArticleRead"), class_="m-tcol-c")

        for a in range(5):
            each_href.append(href[a].get("href"))
        for b in range(len(href)):
            each_whole.append(href[b].get("href"))

        get_href.append(each_href)
        get_whole.append(each_whole)

        href_list = [get_href, get_whole]
    return href_list

def returnNoMatches(new,old):
    a = set(new)
    b = set(old)
    return list(a-b)

def make_new_list(get_href, get_last_whole):
    new_list = []

    for i in range(6):
        each_diff = returnNoMatches(get_href[i], get_last_whole[i])
        new_list.append(each_diff)
    return new_list


dirpath = os.getcwd()
soundfiles = glob.glob(dirpath +"\lol\*.mp3")
get_last_whole=[]

print("\n\n오션 앤 앰파이어, 캐리비안의 해적, 주사위의 신은 chrome에서\n")
print("딜딜딜은 firefox에서\n")
print("아이어는 internet explorer에서\n")
print("프리징 익스텐션은 opera에서 실행됩니다.\n\n")

while True:
    alarm = int(input('\n알람 ON => 1, 알람 OFF => 0 입력 후 enter!: '))
    if alarm == 1:
        print("알람 ON\n")
        break
    if alarm == 0:
        print("알람 OFF\n")
        break

    else:
        print("\n올바른 값을 입력해주세요.\n")

print("모니터링 시작!\n\n")

count = 0
while (count!=20000):
    t0 =time.time()
    try:
        one_get = requests_retry_session().get('http://cafe.naver.com/ArticleList.nhn?search.clubid=28731730&search.boardtype=L', timeout=5)
    except Exception as x:
        print('It failed :(', x.__class__.__name__)
    else:
        print('one 갱신', one_get.status_code)
    finally:
        t1 = time.time()

        print('소요시간', t1 - t0, '초')


    t0 =time.time()
    try:

        potc_get = requests_retry_session().get('http://cafe.naver.com/ArticleList.nhn?search.clubid=28961712&search.boardtype=L', timeout=5)

    except Exception as x:
        print('It failed :(', x.__class__.__name__)
    else:
        print('potc 갱신', potc_get.status_code)
    finally:
        t1 = time.time()

        print('소요시간', t1 - t0, '초')


    t0 =time.time()
    try:
        god_get = requests_retry_session().get("http://cafe.naver.com/ArticleList.nhn?search.clubid=28019625&search.boardtype=L", timeout=5)

    except Exception as x:
        print('It failed :(', x.__class__.__name__)
    else:
        print('god 갱신', god_get.status_code)
    finally:
        t1 = time.time()

        print('소요시간', t1 - t0, '초')


    t0 =time.time()
    try:

        ddd_get = requests_retry_session().get('http://cafe.naver.com/ArticleList.nhn?search.clubid=28980826&search.boardtype=L', timeout=5)

    except Exception as x:
        print('It failed :(', x.__class__.__name__)
    else:
        print('ddd 갱신', ddd_get.status_code)
    finally:
        t1 = time.time()

        print('소요시간', t1 - t0, '초')


    t0 =time.time()
    try:

        ire_get = requests_retry_session().get("http://cafe.naver.com/ArticleList.nhn?search.clubid=28611439&search.boardtype=L", timeout=5)


    except Exception as x:
        print('It failed :(', x.__class__.__name__)
    else:
        print('ire 갱신', ire_get.status_code)
    finally:
        t1 = time.time()

        print('소요시간', t1 - t0, '초')

    t0 =time.time()
    try:

        freez_get = requests_retry_session().get("http://cafe.naver.com/ArticleList.nhn?search.clubid=29133177&search.boardtype=L", timeout=5)

    except Exception as x:
        print('It failed :(', x.__class__.__name__)
    else:
        print('freez 갱신', freez_get.status_code)
    finally:
        t1 = time.time()

        print('소요시간', t1 - t0, '초')


    get_requests = [one_get, potc_get, god_get, ddd_get, ire_get, freez_get]

    get_html = []

    for i in get_requests:
        get_html.append(i.text)


    get_href = make_href(get_html)[0]
    get_whole = make_href(get_html)[1]
    web = dict()

    if(count != 0):
        new_list = make_new_list(get_href, get_last_whole)
        w_count = 0
        for i in new_list:

                if (w_count == 0):
                    web['one'] = []
                    for j in i:
                        web['one'].append(j)

                if (w_count == 1):
                    web['potc'] = []
                    for j in i:
                        web['potc'].append(j)
                if (w_count == 2):
                    web['god'] = []
                    for j in i:
                        web['god'].append(j)
                if (w_count == 3):
                    web['ddd'] = []
                    for j in i:
                        web['ddd'].append(j)
                if (w_count == 4):
                    web['ire'] = []
                    for j in i:
                        web['ire'].append(j)
                if (w_count == 5):
                    web['freez'] = []
                    for j in i:
                        web['freez'].append(j)
                w_count +=1

        print (web)
        if (len(web['one'])+len(web['potc'])+len(web['god'])+len(web['ddd']) +len(web['ire']) + len(web['freez'])  >0):
            print("≤^오^≥ <=^오^=> ≤^오^≥ <=^오^=>\n\n")
            now = time.localtime()
            print("새로운 글 발견!! {}시 {}분 {}초\n".format(now.tm_hour ,now.tm_min, now.tm_sec))
            for j in web:

                if (j =='one' or j =='potc' or j =='god'):
                    if(j == 'one' and len(web['one'])>0):
                        print("오션 앤 엠파이어 {}개\n".format(len(web['one'])))
                    if(j == 'potc' and len(web['potc'])>0):
                        print("캐리비안의 해적  {}개\n".format(len(web['potc'])))
                    if(j == 'god' and len(web['god'])>0):
                        print("주사위의 신      {}개\n".format(len(web['god'])))
                    for k in web[j]:
                        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab("http://cafe.naver.com/"+k)
                if (j == 'ddd' and len(web['ddd'])>0):
                    print("딜딜딜          {}개\n".format(len(web['ddd'])))
                    for k in web[j]:
                        webbrowser.get("C:/Program Files/Mozilla Firefox/firefox.exe %s").open_new_tab("http://cafe.naver.com/"+k)
                if(j == 'ire' and len(web['ire'])>0):
                    print("아이어          {}개\n".format(len(web['ire'])))
                    for k in web[j]:
                        webbrowser.get("C:/Program Files/internet explorer/iexplore.exe %s").open("http://cafe.naver.com/"+k)
                        time.sleep(3)
                        break
                if(j =='freez' and len(web['freez'])>0):
                    print("프리징 익스텐션  {}개\n".format(len(web['freez'])))
                    for k in web[j]:
                        webbrowser.get("C:/Program Files/Opera/launcher.exe %s").open_new_tab("http://cafe.naver.com/"+k)

            if (len(soundfiles) != 0 and alarm == 1):
                a = random.choice(soundfiles)
                playsound(a)


    get_last_whole = get_whole
    count += 1
    print(count)
    time.sleep(5)
