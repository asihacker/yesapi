# yesapi
![](http://cdn7.okayapi.com/CEE4B8A091578B252AC4C92FB4E893C3_20190304213902_63f85e982adc8419feffd862e883581e.jpeg)

# yesapi-python-sdk
小白接口（YesApi.cn）Python SDK包

文档地址: http://api.okayapi.com/docs.php

用法：

    yes = YesApi(api_url='http://xxx.com', app_key='xxxx',
                 app_secret='xxxxx')
    params = {'s': 'App.Captcha.Create'}
    with open('yzm.jpeg', 'wb+') as f:
        rsp = yes.http_get(params=params)
        f.write(rsp.content)