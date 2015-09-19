import urllib.parse
import urllib.request
import json
import pandas as pd


class StatsData(object):
    """stat data class"""

    def __init__(self, appid, lang="J"):
        self.appid = appid
        self.lang = lang
        self.url = 'http://api.e-stat.go.jp/rest/2.0/app/json/getStatsData'

    def read(self, stats_data_id=None, start_position=None, limit=None,
             meta_get_flg=None, cnt_get_flg=None, **ex_query):

        # set parameters
        common_query = {
                'appId': self.appid,
                'lang': self.lang,
                }

        query = {
                'statsDataId': stats_data_id,
                'startPosition': start_position,
                'limit': limit,
                'metaGetFlg': meta_get_flg,
                'cntGetFlg': cnt_get_flg
                }

        query.update(common_query)
        query.update(ex_query)

        query = {k: v for k, v in query.items() if v is not None}

        url = self.url + '?' + urllib.parse.urlencode(query)

        # get stats data
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode('utf-8'))

        # change json data to DataFrame on pandas
        stats = data['GET_STATS_DATA']['STATISTICAL_DATA']
        class_inf = stats['CLASS_INF']['CLASS_OBJ']
        data_inf = stats['DATA_INF']['VALUE']

        labels = dict()
        for class_info in class_inf:
            for class_obj in class_info['CLASS']:
                key = ('@' + class_info['@id'], class_obj['@code'])
                labels[key] = class_obj['@name']

        df = pd.DataFrame(data_inf)

        for k, v in labels.items():
            column, code = k
            df[column][df[column] == code] = v

        return df
