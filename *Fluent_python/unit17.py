import os
import time
import sys
import requests

POP20_CC = ('CN IN US ID BR PK NG BR RU JP'
            'MX PH VN ET EG IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'

dest_dir = 'downloads'

def save_flag(img,filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path,'wb') as fp:
        fp.write(img)

def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL,cc=cc.lower())
    resp = requests.get(url)
    return resp.content

def show(text):
    print(text,end=' ')
    sys.stdout.flush()

def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')

    return len(cc_list)

def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    mag = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count,elapsed))

if __name__ == '__main__':
    main(download_many)


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):

    workers = min(MAX_WORKERS,len(cc_list))

    with futures.ThreadPoolExecutor(workers) as executor:

        res = executor.map(download_one,sorted(cc_list))

    return len(list(res))


def download_many(cc_list):
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one,cc)
            to_do.append(future)
            msg = 'Scheduled for {} {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
    return len(results)


def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = requests.get(url)
    if resp.status_code != 200:
        resp.raise_for_status
    return resp.content


def download_one(cc, base_url, verbose=False):
    try:
        image = get_flag(base_url, cc)
    except requests.exceptions.HTTPError as exc:
        res = exc.request
        if res.status_code == 404:
            status = HTTPStatus.not_found
            msg = 'not found'
        else:
            raise
    else:
        save_flag(image, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'OK'

    if verbose:
        print(cc, msg)

    return Result(status, cc)


def download_many(cc_list, base_url, verbose, max_req):
    counter = collections.Counter()
    with futures.ThreadPoolExecutor(max_workers = concur_req) as executor:
        to_do_map = {}
        for cc in sorted(cc_list):
            future = executor.submit(download_one,cc,base_url,verbose))
            to_do_map[future] = cc
        done_iter = futures.as_completed(to_do_map)
        if not verbose:
            done_iter = tqdm.tqdm(done_iter, total=len(cc_list))
        for future in done_iter:
            try:
                res = future.result()
            except requests.exceptions.HTTPError as exc:
                error_msg = 'HTTP {res.status_code} - {res.reason}'
                error_msg = error_mag.format(res=exc.response)
            except requests.ConnectionError as exc:
                error_msg = 'Connection error'
            else:
                error_msg = ''
                status = res.status

            if error_msg:
                status = HTTPStatus.error
            counter[status] += 1
            if verbose and error_msg:
                cc = to_do_map[future]
                print('{} did status\'s{}'.format(cc, status))
