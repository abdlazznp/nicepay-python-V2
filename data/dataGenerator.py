import json
from datetime import datetime

from constants.constantsGeneral import ConstantsGeneral
from util.utilLogging import Log
from util.utilMerchantToken import MerchantToken

log = Log()


class DataGenerator:

    @staticmethod
    def getTransactionHeader():
        headerMap = {"Content-Type": "Application/JSON"}
        return headerMap

    @staticmethod
    def getTransactionBody(body, cartData):
        bodyMap = {}
        log.info(body)
        a = json.dumps(body)
        dataBody = json.loads(a)
        amt = dataBody["amt"]
        b = json.dumps(cartData, indent=None, separators=(',', ':'))
        cartData = b.replace('"', '\"')
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        referenceNo = "OrdNo" + timestamp

        iMid = ConstantsGeneral.getImid()
        merchantKey = ConstantsGeneral.getMerchantKey()
        merchantToken = MerchantToken.getMerchantToken(timestamp, iMid, referenceNo, amt, merchantKey)
        currency = ConstantsGeneral.getCurrency()
        dbProcessUrl = ConstantsGeneral.getDbProcessUrl()

        bodyMap["timeStamp"] = timestamp
        bodyMap["iMid"] = iMid
        bodyMap["referenceNo"] = referenceNo
        bodyMap["billingNm"] = "John Doe"
        bodyMap["billingPhone"] = "08123456789"
        bodyMap["billingEmail"] = "john.doe@example.com"
        bodyMap["billingAddr"] = "Jln. Raya Casablanca Kav.88"
        bodyMap["billingCity"] = "South Jakarta"
        bodyMap["billingState"] = "DKI Jakarta"
        bodyMap["billingCountry"] = "Indonesia"
        bodyMap["billingPostCd"] = "10200"
        bodyMap["deliveryNm"] = "Merchant's Name"
        bodyMap["deliveryPhone"] = "08123456789"
        bodyMap["deliveryAddr"] = "Jln. Dr. Saharjo No.88"
        bodyMap["deliveryCity"] = "South Jakarta"
        bodyMap["deliveryState"] = "DKI Jakarta"
        bodyMap["deliveryCountry"] = "Indonesia"
        bodyMap["deliveryPostCd"] = "10202"
        bodyMap["goodsNm"] = "TESTING PY V2"
        bodyMap["description"] = "This is testing transaction CC - n1tr0"
        bodyMap["dbProcessUrl"] = dbProcessUrl
        bodyMap["cartData"] = cartData
        bodyMap["currency"] = currency
        bodyMap["merchantToken"] = merchantToken
        bodyMap.update(body)
        log.headers(bodyMap)
        # c = json.loads(a)
        # d = json.dumps(bodyMap)
        # e = json.loads(d)
        # mergeData = e.copy()
        # mergeData.update(c)
        # log.info(mergeData)

        # return json.dumps(mergeData)
        return bodyMap
