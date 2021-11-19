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
export EMO_PLATFORM_API_ACCESS_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI0OGVjYTAwMC1hNTQxLTQ1OWUtOGJiMy00MmVhNjU2Njc0YjMiLCJpc3MiOiJwbGF0Zm9ybS1hcGkiLCJleHAiOjE2MzczMTEyMTQsInBsYW4iOiJmcmVlIiwiaWF0IjoxNjM3MzA3NjE0fQ.M25p1Pp8WG9vVHI0ZmnRpbT54XCQqVEn5Va17l7SsNSzOLH7nGXbkrmidXKtaXgJaQB7Koq25j_g5FUjWRNeAA"
export EMO_PLATFORM_API_REFRESH_TOKEN="f16868f3-e5f9-469a-88a8-bf274c50ec51"
```