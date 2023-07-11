import json

from service.serviceNicepay import ServiceNicepay


class testCreditCardPayment:
    item = {"timeStamp":"20230711103852",
            "tXid":"TESTMPGS0501202307111039049035",
            "cardNo":"5123450000000008",
            "cardExpYymm":"3901",
            "cardCvv": "100",
            "merchantToken":"1c86fa7c4c7a53d76668e6792bd6dd7ac732cbcbd4cdafa7b6d2eb440b29e0ae",
            "callBackUrl":"https://www.nicepay.co.id/IONPAY_CLIENT/paymentResult.jsp"}

    response = ServiceNicepay.servicePayment(item)

testCreditCardPayment()
