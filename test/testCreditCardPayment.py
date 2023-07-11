from datetime import datetime

from data.builder import builderCreditCard
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testCreditCardPayment:
    bodyCreditCardPayment = (
        builderCreditCard.BuildCreditCardPayment()
        .setTimestamp(datetime.now().strftime("%Y%m%d%H%M%S"))
        .setTxid("IONPAYTEST01202307120246040632")
        .setCardNo("5123450000000008")
        .setCardExpYymm("3901")
        .setCardCvv("100")
        .setMerchantToken("")
        .setReferenceNo("OrdNo20230712024603")
        .setAmt("10000")
        .build()
    )
    # item = {
    #     "timeStamp": "20230712022730",
    #     "tXid": "IONPAYTEST01202307120227210627",
    #     "cardNo": "5123450000000008",
    #     "cardExpYymm": "3901",
    #     "cardCvv": "100",
    #     "merchantToken": "e08fa540d1f1ce0709f1202933618194b0f0d3e2773d31ce40c0b872748c6617",
    #     "callBackUrl": "https://www.nicepay.co.id/IONPAY_CLIENT/paymentResult.jsp"
    # }

    response = ServiceNicepay.servicePayment(DataGenerator.getPaymentBody(bodyCreditCardPayment.dataCreditCard()))

    # response = ServiceNicepay.servicePayment(item)

# testCreditCardPayment()
