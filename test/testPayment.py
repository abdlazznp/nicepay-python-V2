from datetime import datetime

from data.builder import builderPayment
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testPayment:
    bodyPayment = (
        builderPayment.BuildPayment()
        .setTimestamp(datetime.now().strftime("%Y%m%d%H%M%S"))
        .setTxid("IONPAYTEST05202307271435343814")
        .setReferenceNo("OrdNo20230727143533")
        .setCardNo("")
        .setCardExpYymm("")
        .setCardCvv("")
        .setRecurringToken("")
        .setPreAuthToken("")
        .setAmt("10000")
        .build()
    )

    response = ServiceNicepay.servicePayment(DataGenerator.getPaymentBody(bodyPayment.dataPayment()))
