import json
from datetime import datetime


class dataGenerator:
    @staticmethod
    def getTransactionBody():
        headerMap = {"Content-Type": "Application/JSON"}
        bodyMap = {}
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
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

        # bodyMap[""]
