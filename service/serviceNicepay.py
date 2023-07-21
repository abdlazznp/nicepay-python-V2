import json

from config.apiClient import apiClient
from constants.constantsEndpoints import ConstantsEndpoints
from constants.constantsGeneral import ConstantsGeneral
from data.dataGenerator import DataGenerator
from util.utilLogging import Log

log = Log()
host = ConstantsGeneral.getSandboxBaseUrl()  # Environment


class ServiceNicepay:
    log.headers("Initialization")

    @staticmethod
    def serviceRequest(body):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ConstantsEndpoints.registration()
        data = apiClient.send(host,
                              headers,
                              body,
                              endpoint)

        response = json.dumps(data)
        log.info("Headers : " + json.dumps(headers))
        log.info("Request Data : " + json.dumps(body))
        log.info("Response Data : " + json.dumps(data))
        return response

    @staticmethod
    def servicePayment(data):
        endpoint = ConstantsEndpoints.payment()
        response = apiClient.get(host,
                                 data,
                                 endpoint)
        # a = json.dumps(response)
        log.info("Request Data : " + json.dumps(data))
        log.info("Response Data : " + json.dumps(response))
        # log.info(response)
        return response

    @staticmethod
    def serviceCancel(data):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ConstantsEndpoints.cancel()
        response = apiClient.send(host,
                                  headers,
                                  data,
                                  endpoint)
        # a = json.dumps(response)
        log.info("Headers : " + json.dumps(headers))
        log.info("Request Data : " + json.dumps(data))
        log.info("Response Data : " + json.dumps(response))
        # log.info(response)
        return response

    @staticmethod
    def serviceInquiry(data):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ConstantsEndpoints.inquiry()
        response = apiClient.send(host,
                                  headers,
                                  data,
                                  endpoint)
        log.info("Headers : " + json.dumps(headers))
        log.info("Request Data : " + json.dumps(data))
        log.info("Response Data : " + json.dumps(response))


    @staticmethod
    def servicePayoutReg(data):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ConstantsEndpoints.payoutRegistration()
        response = apiClient.send(host,
                                  headers,
                                  data,
                                  endpoint)
        log.info("Headers : " + json.dumps(headers))
        log.info("Request Data : " + json.dumps(data))
        log.info("Response Data : " + json.dumps(response))

    @staticmethod
    def servicePayoutApprove(data):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ConstantsEndpoints.payoutApprove()
        response = apiClient.send(host,
                                  headers,
                                  data,
                                  endpoint)
        log.info("Headers : " + json.dumps(headers))
        log.info("Request Data : " + json.dumps(data))
        log.info("Response Data : " + json.dumps(response))

    @staticmethod
    def servicePayoutReject(data):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ConstantsEndpoints.payoutReject()
        response = apiClient.send(host,
                                  headers,
                                  data,
                                  endpoint)
        log.info("Headers : " + json.dumps(headers))
        log.info("Request Data : " + json.dumps(data))
        log.info("Response Data : " + json.dumps(response))

    @staticmethod
    def servicePayoutInquiry(data):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ""
        response = apiClient.send(host,
                                  headers,
                                  data,
                                  endpoint)
        log.info("Headers : " + json.dumps(headers))
        log.info("Request Data : " + json.dumps(data))
        log.info("Response Data : " + json.dumps(response))

    @staticmethod
    def servicePayoutCancel(data):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ""
        response = apiClient.send(host,
                                  headers,
                                  data,
                                  endpoint)
        log.info("Headers : " + json.dumps(headers))
        log.info("Request Data : " + json.dumps(data))
        log.info("Response Data : " + json.dumps(response))

    @staticmethod
    def servicePayoutBalanceInquiry(data):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ""
        response = apiClient.send(host,
                                  headers,
                                  data,
                                  endpoint)
        log.info("Headers : " + json.dumps(headers))
        log.info("Request Data : " + json.dumps(data))
        log.info("Response Data : " + json.dumps(response))

    @staticmethod
    def servicePayoutTransHistInq(data):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ""
        response = apiClient.send(host,
                                  headers,
                                  data,
                                  endpoint)
        log.info("Headers : " + json.dumps(headers))
        log.info("Request Data : " + json.dumps(data))
        log.info("Response Data : " + json.dumps(response))

    @staticmethod
    def serviceVAFixedOpenRegist(data):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ""
        response = apiClient.send(host,
                                  headers,
                                  data,
                                  endpoint)
        log.info("Headers : " + json.dumps(headers))
        log.info("Request Data : " + json.dumps(data))
        log.info("Response Data : " + json.dumps(response))
