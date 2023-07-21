import hashlib

from util.utilLogging import Log

log = Log()


class MerchantToken:

    @staticmethod
    def getMerchantToken(timestamp, iMid, referenceNo, amt, merchantKey):
        data = f"{timestamp}{iMid}{referenceNo}{amt}{merchantKey}"
        merchantToken = hashlib.sha256(data.encode('utf-8')).hexdigest()
        log.info(f"util - Generated MerchantToken : {merchantToken}")
        return merchantToken

    @staticmethod
    def getMerchantTokenCancel(timestamp, iMid, tXid, amt, merchantKey):
        data = f"{timestamp}{iMid}{tXid}{amt}{merchantKey}"
        merchantToken = hashlib.sha256(data.encode('utf-8')).hexdigest()
        log.info(f"util - Generated MerchantToken : {merchantToken}")
        return merchantToken

    @staticmethod
    def getMerchantTokenPayoutRegistration(timestamp, iMid, amt, accountNo, merchantKey):
        data = f"{timestamp}{iMid}{amt}{accountNo}{merchantKey}"
        merchantToken = hashlib.sha256(data.encode('utf-8')).hexdigest()
        log.info(f"util - Generated MerchantToken : {merchantToken}")
        return merchantToken

    @staticmethod
    def getMerchantTokenPayoutApprove(timestamp, iMid, tXid, merchantKey):
        data = f"{timestamp}{iMid}{tXid}{merchantKey}"
        merchantToken = hashlib.sha256(data.encode('utf-8')).hexdigest()
        log.info(f"util - Generated MerchantToken : {merchantToken}")
        return merchantToken

    @staticmethod
    def getMerchantTokenPayoutReject(timestamp, iMid, tXid, merchantKey):
        data = f"{timestamp}{iMid}{tXid}{merchantKey}"
        merchantToken = hashlib.sha256(data.encode('utf-8')).hexdigest()
        log.info(f"util - Generated MerchantToken : {merchantToken}")
        return merchantToken

