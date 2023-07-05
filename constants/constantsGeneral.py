class ConstantsGeneral:
    _SANDBOX_BASE_URL = "https://dev.nicepay.co.id"
    _STAGING_BASE_URL = "https://staging.nicepay.co.id"
    _PRODUCTION_BASE_URL = "https://www.nicepay.co.id"
    _I_MID = "IONPAYTEST"
    _MERCHANT_KEY = ""
    _PAY_METHOD_CREDIT_CARD = "01"
    _PAY_METHOD_VIRTUAL_ACCOUNT = "02"
    _PAY_METHOD_CONVENIENCE_STORE = "03"
    _PAY_METHOD_DIRECT_DEBIT = "04"
    _PAY_METHOD_E_WALLET = "05"
    _PAY_METHOD_PAYLOAN = "06"
    _PAY_METHOD_PAYOUT = "07"
    _PAY_METHOD_QRIS = "08"
    _PAY_METHOD_GPN = "09"


    @staticmethod
    def getSandboxBaseUrl():
        return ConstantsGeneral._SANDBOX_BASE_URL

    @staticmethod
    def getStagingBaseUrl():
        return ConstantsGeneral._STAGING_BASE_URL

    @staticmethod
    def getProductionBaseUrl():
        return ConstantsGeneral._PRODUCTION_BASE_URL

    @staticmethod
    def getImid():
        return ConstantsGeneral._I_MID

    @staticmethod
    def getMerchantKey():
        return ConstantsGeneral._MERCHANT_KEY
