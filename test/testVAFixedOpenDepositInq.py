from data.builder import builderVirtualAccount
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testVAFixedOpenDepositInq:
    bodyVAFixedOpenDepositInq = (
        builderVirtualAccount.BuildVAFixedOpenDepositInq()
        .setVacctNo("")
        .setStartDt("")
        .setEndDt("")
        .build()
    )

    response = ServiceNicepay.serviceVAFixedOpenDepositInq(DataGenerator
                                                           .getVAFixedOpenDepositInq(bodyVAFixedOpenDepositInq
                                                                                     .jsonVAFixedOpenDepositInq()))
