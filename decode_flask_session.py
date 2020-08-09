
def decode_flask_cookie(secret_key, cookie_str): # pass the SECRET_KEY, and COOKIE STRING VALUE ON BROWSER
    import hashlib
    from itsdangerous import URLSafeTimedSerializer
    from flask.sessions import TaggedJSONSerializer
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    return s.loads(cookie_str)


if __name__ == '__main__':
    print(decode_flask_cookie('gzTxzyKT8yWZvprygoxc5ALvoW3sXGOD','eyJ1c2VyIjpudWxsfQ.Xy7mtw.-PtvoNY9KwQP3D8ptIneuYRQQsU'))
