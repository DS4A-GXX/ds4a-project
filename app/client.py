import json
import logging
import urllib3
import base64


class ScoreClient:

    # CONFIGURA OS DADOS DE ACESSO AO SERVICO
    def __init__(self):

        url = "http://ec2-18-216-201-53.us-east-2.compute.amazonaws.com:8080"
        url = "http://localhost:8080"
        self._base_url = url + "/api/health/"
        username = "vital"
        password = "vital_e_sua_m0t0+queUniaoFeLiZ"
        credentials = b"vital:vital_e_sua_m0t0+queUniaoFeLiZ"
        print(type(credentials))
        base64string = base64.b64encode(credentials)
        self._headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Basic {base64string}",
        }
        self.http = urllib3.PoolManager()

    def get_score(self, data):
        url = f"score/"
        return self.callService(url, "POST", dictParams=data)

    def callService(self, url, method="GET", dictParams=""):
        urlToCall = self._base_url + url
        print(urlToCall)
        try:

            payload = json.dumps(dictParams).encode("utf-8")
            print(payload)
            resp = self.http.request(
                method=method, url=urlToCall, body=payload, headers=self._headers,
            )
            print(resp.data)
            print(resp.data.decode("utf-8"))
        except Exception as e:
            raise e


if __name__ == "__main__":
    client = ScoreClient()
    data = {"birthdate": "1983-03-24", "members": 5, "gender": "F", "income": "200-250"}
    print(client.get_score(data))
