from constants.constantsGeneral import ConstantsGeneral
from data.builder import builderCartData, builderConvenienceStore
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testConvenienceStore:
    amt = 10000
    itemCartData = {
        "goods_id": "BB12345678",
        "goods_detail": "BB12345678",
        "goods_name": "Pasar Modern",
        "goods_amt": amt,
        "goods_type": "Sembako",
        "goods_url": "https://merchant.com/cellphones/iphone5s_64g",
        "goods_quantity": "1",
        "goods_sellers_id": "SEL123",
        "goods_sellers_name": "Sellers 1"
    }

    bodyCartData = (
        builderCartData.BuildCartData()
        .setCount("1")
        .setItem(itemCartData)
        .build()
    )

    bodyConvenienceStore = (
        builderConvenienceStore.BuildConvenienceStore()
        .setPayMethod(ConstantsGeneral.getPayMethodConvenienceStore())
        .setMitraCd("ALMA")
        .setPayValidDt("")
        .setPayValidTm("")
        .setMerFixAcctId("")
        .setAmt(amt)
        .build()
    )

    response = ServiceNicepay.serviceRequest(DataGenerator.getTransactionBody(bodyConvenienceStore.jsonConvenienceStore(),
                                                                              bodyCartData.jsonCartData()))
