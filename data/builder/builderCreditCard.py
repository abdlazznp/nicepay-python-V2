class CreditCard:
    def __init__(self,
                 payMethod,
                 instmntType,
                 instmntMon,
                 recurrOpt
                 ):
        self.payMethod = payMethod
        self.instmntType = instmntType
        self.instmntMon = instmntMon
        self.recurrOpt = recurrOpt

    def jsonCreditCard(self):
        return ({
            "payMethod": self.payMethod,
            "instmntType": self.instmntType,
            "instmntMon": self.instmntMon,
            "recurrOpt": self.recurrOpt
        })
