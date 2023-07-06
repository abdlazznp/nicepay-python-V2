import json

from config.apiClient import apiClient
from constants.constantsEndpoints import ConstantsEndpoints
from constants.constantsGeneral import ConstantsGeneral
from data.dataGenerator import dataGenerator
from util.utilLogging import Log

log = Log()
host = ConstantsGeneral.getSandboxBaseUrl()  # Environment


class ServiceNicepay:
    log.headers("Initialization")

    @staticmethod
    def serviceRequest(body):
        headers = dataGenerator.getTransactionHeader()
        endpoint = ConstantsEndpoints.registration()
        response = apiClient.send(host,
                                  headers,
                                  body,
                                  endpoint)

        a = json.dumps(response)
        log.info(a)
        return a

    @staticmethod
    def servicePayment(body):
        headers = dataGenerator.getTransactionHeader()
        endpoint = ConstantsEndpoints.payment()
        response = apiClient.send(host,
                                  headers,
                                  body,
                                  endpoint)

b = ServiceNicepay.serviceRequest(
    {
        "timeStamp": "20230706170732",
        "iMid": "TESTMPGS05",
        "payMethod": "01",
        "currency": "IDR",
        "amt": "10000",
        "merchantToken": "adf3724ca3a04eda31ebacbc7d16386c7197feadb6818ad0b46d8a2a4a7b111d",
        "referenceNo": "ordNo20230706170732",
        "goodsNm": "TESTING CREDIT CARD - BEDUL",
        "billingNm": "Hantu Kesorean",
        "billingPhone": "081288998899",
        "billingEmail": "abdul@example.com",
        "billingAddr": "Jln. Raya Kasablanka Kav.88",
        "billingCity": "South Jakarta",
        "billingState": "DKI Jakarta",
        "billingCountry": "Indonesia",
        "billingPostCd": "12800",
        "dbProcessUrl": "https://webhook.site/e15ef201-98a9-428c-85d4-a0c6458939c3",
        "userIP": "127.0.0.1",
        "instmntType": "1",
        "instmntMon": "1",
        "cartData": "{\"count\":\"2\",\"item\":[{\"goods_id\":\"BB12345678\",\"goods_detail\":\"BB12345678\",\"goods_name\":\"Pasar Modern\",\"goods_amt\":\"0\",\"goods_type\":\"Sembako\",\"goods_url\":\"http:\/\/merchant.com\/cellphones\/iphone5s_64g\",\"goods_quantity\":\"1\",\"goods_sellers_id\":\"SEL123\",\"goods_sellers_name\":\"Sellers 1\"},{\"goods_id\":\"BB12345678\",\"goods_detail\":\"BB12345678\",\"goods_name\":\"Pasar Modern\",\"goods_amt\":\"10000\",\"goods_type\":\"Sembako\",\"goods_url\":\"http:\/\/merchant.com\/cellphones\/iphone5s_64g\",\"goods_quantity\":\"1\",\"goods_sellers_id\":\"SEL123\",\"goods_sellers_name\":\"Sellers 1\"}]}",
        "recurrOpt": "1",
        "userLanguage": "en",
        "userAgent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    }
)
