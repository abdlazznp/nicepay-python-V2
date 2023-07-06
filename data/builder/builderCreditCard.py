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


class BuilderCreditCard:
    def __init__(self):
        self.payMethod = None
        self.instmntType = None
        self.instmntMon = None
        self.recurrOpt = None

    def setPayMethod(self, payMethod):
        self.payMethod = payMethod
        return self

    def setInstmntType(self, instmntType):
        self.instmntType = instmntType
        return self

    def setInstmntMon(self, instmntMon):
        self.instmntMon = instmntMon
        return self

    def setRecurrOpt(self, recurrOpt):
        self.recurrOpt = recurrOpt
        return self


class BuildCreditCard(BuilderCreditCard):
    def build(self):
        return CreditCard(
            self.payMethod,
            self.instmntType,
            self.instmntMon,
            self.recurrOpt
        )
