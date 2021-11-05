# emo_body_temp
   emo&konashiの作例emo体温管理用リポジトリ
## Using PyPl
```bash
# Python 3.7+ required
pip3 install emo-platform-api-sdk
```
## Setting api tokens

You can see access token & refresh token from dashboard in [this page](https://platform-api.bocco.me/dashboard/login) after login.

Then, set those tokens as environment variables.

```bash
export EMO_PLATFORM_API_ACCESS_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI0OGVjYTAwMC1hNTQxLTQ1OWUtOGJiMy00MmVhNjU2Njc0YjMiLCJpc3MiOiJwbGF0Zm9ybS1hcGkiLCJleHAiOjE2MzQ4ODc4NDksInBsYW4iOiJmcmVlIiwiaWF0IjoxNjM0ODg0MjQ5fQ.gC9xvnVw0JsVg_Cl06FRtXD6akROQ_9Gt9b7uHi3EO8XzgnGD7ou8mOBTHDJwUkaJC414AvRo1ndpaMxi_A3GA"
export EMO_PLATFORM_API_REFRESH_TOKEN="13d6fecb-00fc-405a-af22-62ff30a944ca"
```