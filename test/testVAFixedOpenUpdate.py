from data.builder import builderVirtualAccount
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testVAFixedOpenUpdate:
    bodyVAFixedOpenUpdate = (
        builderVirtualAccount.BuildVAFixedOpenCustomerUpdate()
        .setCustomerId("")
        .setCustomerNm("")
        .setUpdateType("")
        .build()
    )

    response = ServiceNicepay.serviceVAFixedOpenUpdate(DataGenerator
                                                       .getVAFixedOpenUpdate(bodyVAFixedOpenUpdate
                                                                             .jsonVAFixedOpenCustomerUpdate()))
