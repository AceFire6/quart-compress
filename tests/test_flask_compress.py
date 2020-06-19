import os

import pytest
from quart import Quart, render_template

from quart_compress import Compress


class TestDefaults:
    def setup(self):
        self.app = Quart(__name__)
        self.app.testing = True

        Compress(self.app)

    def test_mimetypes_default(self):
        """ Tests COMPRESS_MIMETYPES default value is correctly set. """
        defaults = [
            "text/html",
            "text/css",
            "text/xml",
            "application/json",
            "application/javascript",
        ]
        assert self.app.config["COMPRESS_MIMETYPES"] == defaults

    def test_level_default(self):
        """ Tests COMPRESS_LEVEL default value is correctly set. """
        assert self.app.config["COMPRESS_LEVEL"] == 6

    def test_min_size_default(self):
        """ Tests COMPRESS_MIN_SIZE default value is correctly set. """
        assert self.app.config["COMPRESS_MIN_SIZE"] == 500

    def test_algorithm_default(self):
        """ Tests COMPRESS_ALGORITHM default value is correctly set. """
        assert self.app.config["COMPRESS_ALGORITHM"] == "gzip"


class TestInit:
    def setup(self):
        self.app = Quart(__name__)
        self.app.testing = True

    def test_constructor_init(self):
        Compress(self.app)

    def test_delayed_init(self):
        compress = Compress()
        compress.init_app(self.app)


class TestUrls:
    def setup(self):
        self.app = Quart(__name__)
        self.app.testing = True

        small_path = os.path.join(os.getcwd(), "tests", "templates", "small.html")

        large_path = os.path.join(os.getcwd(), "tests", "templates", "large.html")

        self.small_size = os.path.getsize(small_path) - 1
        self.large_size = os.path.getsize(large_path) - 1

        Compress(self.app)

        @self.app.route("/small/")
        async def small():
            return await render_template("small.html")

        @self.app.route("/large/")
        async def large():
            return await render_template("large.html")

    async def client_get(self, ufs):
        client = self.app.test_client()
        response = await client.get(ufs, headers=[("Accept-Encoding", "gzip")])

        assert response.status_code == 200

        return response

    @pytest.mark.asyncio
    async def test_br_algorithm(self):
        client = self.app.test_client()
        headers = [("Accept-Encoding", "br")]

        response = await client.options("/small/", headers=headers)
        assert response.status_code == 200

        response = await client.options("/large/", headers=headers)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_compress_level(self):
        """ Tests COMPRESS_LEVEL correctly affects response data. """
        self.app.config["COMPRESS_LEVEL"] = 1

        response = await self.client_get("/large/")
        data = await response.get_data()

        response1_size = len(data)

        self.app.config["COMPRESS_LEVEL"] = 6

        response = await self.client_get("/large/")
        data = await response.get_data()

        response6_size = len(data)

        assert response1_size != response6_size

    @pytest.mark.asyncio
    async def test_compress_min_size(self):
        """ Tests COMPRESS_MIN_SIZE correctly affects response data. """
        small_response = await self.client_get("/small/")
        small_response_data = await small_response.get_data()

        assert self.small_size == len(small_response_data)

        large_response = await self.client_get("/large/")
        large_response_data = await large_response.get_data()

        assert self.large_size != len(large_response_data)

    @pytest.mark.asyncio
    async def test_mimetype_mismatch(self):
        """ Tests if mimetype not in COMPRESS_MIMETYPES. """
        response = await self.client_get("/static/1.png")

        assert response.mimetype == "image/png"

    @pytest.mark.asyncio
    async def test_content_length_options(self):
        client = self.app.test_client()

        headers = [("Accept-Encoding", "gzip")]
        response = await client.options("/small/", headers=headers)

        assert response.status_code == 200
