from datetime import datetime

from data.builder import builderCreditCard
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testCreditCardPayment:
    bodyCreditCardPayment = (
        builderCreditCard.BuildCreditCardPayment()
        .setTimestamp(datetime.now().strftime("%Y%m%d%H%M%S"))
        .setTxid("IONPAYTEST01202307271317573687")
        .setCardNo("5123450000000008")
        .setCardExpYymm("3901")
        .setCardCvv("100")
        .setReferenceNo("OrdNo20230727131755")
        .setAmt("10000")
        .build()
    )

    response = ServiceNicepay.servicePayment(DataGenerator.getPaymentBody(bodyCreditCardPayment.dataCreditCard()))

