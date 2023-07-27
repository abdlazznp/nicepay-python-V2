from datetime import datetime

from data.builder import builderEwallet
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testEwalletPayment:
    bodyEwalletPayment = (
        builderEwallet.BuildEwalletPayment()
        .setTimestamp(datetime.now().strftime("%Y%m%d%H%M%S"))
        .setTxid("IONPAYTEST05202307271349353728")
        .setReferenceNo("OrdNo20230727134935")
        .setAmt("10000")
        .build()
    )

    response = ServiceNicepay.servicePayment(DataGenerator.getPaymentBody(bodyEwalletPayment.dataEwallet()))
