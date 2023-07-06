from constants.constantsGeneral import ConstantsGeneral
from data.builder import builderCreditCard
from util.utilLogging import Log

log = Log()

class testCreditCard:
    bodyCreditCard = (
        builderCreditCard.BuildCreditCard()
        .setPayMethod(ConstantsGeneral.getPayMethodCreditCard())
        .setRecurrOpt("1")
        .setInstmntMon("1")
        .setInstmntType("1")
        .build()
    )

