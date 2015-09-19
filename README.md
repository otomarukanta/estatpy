# estatpy
estatpy is a simple wrapper to access e-stat API.
<http://www.e-stat.go.jp/api/>

# Usage
```
# please set your appid
df = StatsData(appid).read(stats_data_id='0003045948')
print(df)
```

```
           $ @cat01  @cat02    @tab  @time @unit
           0      16761    建設業   19歳以下  給与所得者数  2013年     人
           1       5985    建設業   19歳以下  給与所得者数  2012年     人
           2       4900    建設業   19歳以下  給与所得者数  2011年     人
           3      11628    建設業   19歳以下  給与所得者数  2010年     人
           4      11172    建設業   19歳以下  給与所得者数  2009年     人
           5       8156    建設業   19歳以下  給与所得者数  2008年     人
           6     129482    建設業  20～24歳  給与所得者数  2013年     人
           7     112304    建設業  20～24歳  給与所得者数  2012年     人
           8     109844    建設業  20～24歳  給与所得者数  2011年     人
           9     122647    建設業  20～24歳  給与所得者数  2010年     人
           10    100088    建設業  20～24歳  給与所得者数  2009年     人
           11    114733    建設業  20～24歳  給与所得者数  2008年     人
           12    255294    建設業  25～29歳  給与所得者数  2013年     人
           13    229779    建設業  25～29歳  給与所得者数  2012年     人
           14    273844    建設業  25～29歳  給与所得者数  2011年     人
           15    268499    建設業  25～29歳  給与所得者数  2010年     人
           16    238791    建設業  25～29歳  給与所得者数  2009年     人
           17    261963    建設業  25～29歳  給与所得者数  2008年     人
           18    334164    建設業  30～34歳  給与所得者数  2013年     人
           19    344804    建設業  30～34歳  給与所得者数  2012年     人
           20    372615    建設業  30～34歳  給与所得者数  2011年     人
           21    373956    建設業  30～34歳  給与所得者数  2010年     人
           22    409716    建設業  30～34歳  給与所得者数  2009年     人
           23    444159    建設業  30～34歳  給与所得者数  2008年     人
           24    519672    建設業  35～39歳  給与所得者数  2013年     人
           25    504084    建設業  35～39歳  給与所得者数  2012年     人
           26    527228    建設業  35～39歳  給与所得者数  2011年     人
           27    487129    建設業  35～39歳  給与所得者数  2010年     人
           28    468492    建設業  35～39歳  給与所得者数  2009年     人
           29    509349    建設業  35～39歳  給与所得者数  2008年     人
           ...      ...    ...     ...     ...    ...   ...
```

# Credit
「このサービスは、政府統計総合窓口(e-Stat)のAPI機能を使用していますが、サービスの内容は国によって保証されたものではありません。」