# Quart-Compress

[![Version](https://img.shields.io/pypi/v/quart-compress.svg)](https://pypi.python.org/pypi/quart-compress)
[![Build Status](https://travis-ci.org/AceFire6/quart-compress.svg?branch=master)](https://travis-ci.org/AceFire6/quart-compress)
[![Coverage Status](https://coveralls.io/repos/github/AceFire6/quart-compress/badge.svg?branch=master)](https://coveralls.io/github/AceFire6/quart-compress?branch=master)
[![License](https://img.shields.io/pypi/l/quart-compress.svg)](https://github.com/AceFire6/quart-compress/blob/master/LICENSE.txt)

Quart-Compress allows you to easily compress your [Quart](https://pgjones.gitlab.io/quart/) application's responses with gzip.

The preferred solution is to have a server (like [Nginx](http://wiki.nginx.org/Main)) automatically compress the static files for you. If you don't have that option Quart-Compress will solve the problem for you.


## How it works

Quart-Compress both adds the various headers required for a compressed response and gzips the response data. This makes serving gzip compressed static files extremely easy.

Internally, every time a request is made the extension will check if it matches one of the compressible MIME types and will automatically attach the appropriate headers.


## Installation

If you use pip then installation is simply:

```shell
$ pip install quart-compress
```

or, if you want the latest github version:

```shell
$ pip install git+git://github.com/AceFire6/quart-compress.git
```

## Using Quart-Compress

Quart-Compress is incredibly simple to use. In order to start gzip'ing your Quart application's assets, the first thing to do is let Quart-Compress know about your [`quart.Quart`](https://pgjones.gitlab.io/quart/source/quart.app.html#quart.app.Quart) application object.

```python
from quart import Quart
from quart_compress import Compress

app = Quart(__name__)
Compress(app)
```

In many cases, however, one cannot expect a Quart instance to be ready at import time, and a common pattern is to return a Quart instance from within a function only after other configuration details have been taken care of. In these cases, Quart-Compress provides a simple function, `quart_compress.Compress.init_app`, which takes your application as an argument.

```python
from quart import Quart
from quart_compress import Compress

compress = Compress()

def start_app():
    app = Quart(__name__)
    compress.init_app(app)
    return app
```

In terms of automatically compressing your assets using gzip, passing your [`quart.Quart`](https://pgjones.gitlab.io/quart/source/quart.app.html#quart.app.Quart) object to the `quart_compress.Compress` object is all that needs to be done.


## Options

Within your Quart application's settings you can provide the following settings to control the behavior of Quart-Compress. None of the settings are required.

| Option | Description | Default |
| ------ | ----------- | ------- |
| `COMPRESS_MIMETYPES` | Set the list of mimetypes to compress here. | `[`<br>`'text/html',`<br>`'text/css',`<br>`'text/xml',`<br>`'application/json',`<br>`'application/javascript'`<br>`]` |
| `COMPRESS_LEVEL` | Specifies the gzip compression level. | `6` |
| `COMPRESS_MIN_SIZE` | Specifies the minimum file size threshold for compressing files. | `500` |
| `COMPRESS_CACHE_KEY` | Specifies the cache key method for lookup/storage of response data. | `None` |
| `COMPRESS_CACHE_BACKEND` | Specified the backend for storing the cached response data. | `None` |
| `COMPRESS_REGISTER` | Specifies if compression should be automatically registered. | `True` |
