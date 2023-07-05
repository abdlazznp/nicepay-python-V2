import hashlib
from datetime import datetime


class MerchantToken:

    @staticmethod
    def getMerchantToken(timestamp, iMid, referenceNo, amt, merchantKey):
        data = f"{timestamp}{iMid}{referenceNo}{amt}{merchantKey}"
        merchantToken = hashlib.sha256(data.encode('utf-8')).hexdigest()
        return merchantToken


    @staticmethod
    def getMerchantTokenCancel(timestamp, iMid, tXid, amt, merchantKey):
        data = f"{timestamp}{iMid}{tXid}{amt}{merchantKey}"
        merchantToken = hashlib.sha256(data.encode('utf-8')).hexdigest()
        return merchantToken


a = MerchantToken.getMerchantToken(datetime.now().strftime("%Y%m%d%H%M%S"), "NORMALTEST",
                                   ("OrdNo" + datetime.now().strftime("%Y%m%d%H%M%S")), "10000",
                                   "33F49GnCMS1mFYlGXisbUDzVf2ATWCl9k3R++d5hDd3Frmuos/XLx8XhXpe+LDYAbpGKZYSwtlyyLOtS/8aD7A==")
print(a)
