class CreditCard:
    def __init__(self,
                 payMethod,
                 instmntType,
                 instmntMon,
                 recurrOpt,
                 amt
                 ):
        self.payMethod = payMethod
        self.instmntType = instmntType
        self.instmntMon = instmntMon
        self.recurrOpt = recurrOpt
        self.amt = amt

    def jsonCreditCard(self):
        return ({
            "payMethod": self.payMethod,
            "instmntType": self.instmntType,
            "instmntMon": self.instmntMon,
            "recurrOpt": self.recurrOpt,
            "amt": self.amt
        })


class BuilderCreditCard:
    def __init__(self):
        self.payMethod = None
        self.instmntType = None
        self.instmntMon = None
        self.recurrOpt = None
        self.amt = None

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

    def setAmt(self, amt):
        self.amt = amt
        return self


class BuildCreditCard(BuilderCreditCard):
    def build(self):
        return CreditCard(
            self.payMethod,
            self.instmntType,
            self.instmntMon,
            self.recurrOpt,
            self.amt
        )


class CreditCardPayment:
    def __init__(self,
                 tXid,
                 cardNo,
                 cardExpYymm,
                 cardCvv):
        self.tXid = tXid
        self.cardNo = cardNo
        self.cardExpYymm = cardExpYymm
        self.cardCvv = cardCvv

    def dataCreditCard(self):
        return f"{self.tXid}&{self.cardNo}&{self.cardExpYymm}&{self.cardCvv}"


class BuilderCreditCardPayment:
    def __init__(self):
        self.tXid = None
        self.cardNo = None
        self.cardExpYymm = None
        self.cardCvv = None

    def setTxid(self, tXid):
        self.tXid = tXid
        return self

    def setCardNo(self, cardNo):
        self.cardNo = cardNo
        return self

    def setCardExpYymm(self, cardExpYymm):
        self.cardExpYymm = cardExpYymm
        return self

    def setCardCvv(self, cardCvv):
        self.cardCvv = cardCvv
        return self


class BuildCreditCardPayment(BuilderCreditCardPayment):
    def build(self):
        return CreditCardPayment(
            self.tXid,
            self.cardNo,
            self.cardExpYymm,
            self.cardCvv
        )
