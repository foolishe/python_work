import collections
from concurrent import futures

import requests
import tqdm

def download_many(cc_list,baseurl,werbose,concur_req):
    counter = collections.Counter()
    with futures.ThreadPoolExecutor(max_workers=concur_req) as executor:
        to_do_map = {}
        for cc in sorted(cc_list):
            future = executor.submit(download_one,cc,base_url,verbose)
            to_do_map[future] = cc
        done_iter = futures.as_completed(to_do_map)
        if not verbose:
            done_iter = tqdm.tqdm(done_iter,total=len(cc_list))
        for future in done_iter:
            try:
                res = future.result()
            except requests.exceptions.HttpError as exc:
                error_msg = 'HTTP {res.status_code} - {res.reason}'
                error_msg = error_msg.format(res=exc.response)
            except requests.exceptions.ConnectionError as exc:
                error_msg = 'Connection error'
            else:
                error_msg = ''
                status = res.status


            if error_msg:
                status = HTTPStatus.error
            conter[status] += 1
            if verbose and error_msg:
                cc = to_do_map[future]
                print('***Error for {}: {}'.format(cc,error_msg))
        return counter

if __name__ == '__main__':
    main(download_many,.....)
