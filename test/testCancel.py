from constants.constantsGeneral import ConstantsGeneral
from data.builder import builderCancel
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testCancel:
    bodyCancel = (
        builderCancel.BuildCancel()
        .setPayMethod(ConstantsGeneral.getPayMethodVirtualAccount())
        .setTxid("NORMALTEST02202307140000112364")
        .setReferenceNo("OrdNo20230714000010")
        .setCancelType("1")
        .setCancelMsg("Testing Cancellation - n1tr0")
        .setAmt("10000")
        .build()
    )

    response = ServiceNicepay.serviceCancel(DataGenerator.getCancelBody(bodyCancel.jsonCancel()))
