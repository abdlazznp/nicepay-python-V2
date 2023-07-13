class CreditCard:
    def __init__(self,
                 payMethod,
                 instmntType,
                 instmntMon,
                 recurrOpt,
                 amt):
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
                 timestamp,
                 tXid,
                 cardNo,
                 cardExpYymm,
                 cardCvv,
                 merchantToken,
                 referenceNo,
                 amt):
        self.timestamp = timestamp
        self.tXid = tXid
        self.cardNo = cardNo
        self.cardExpYymm = cardExpYymm
        self.cardCvv = cardCvv
        self.merchantToken = merchantToken
        self.referenceNo = referenceNo
        self.amt = amt

    def dataCreditCard(self):
        return ({
            "timeStamp": self.timestamp,
            "tXid": self.tXid,
            "cardNo": self.cardNo,
            "cardExpYymm": self.cardExpYymm,
            "cardCvv": self.cardCvv,
            "merchantToken": self.merchantToken,
            "referenceNo": self.referenceNo,
            "amt": self.amt
        })


class BuilderCreditCardPayment:
    def __init__(self):
        self.timestamp = None
        self.tXid = None
        self.cardNo = None
        self.cardExpYymm = None
        self.cardCvv = None
        self.merchantToken = None
        self.referenceNo = None
        self.amt = None

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp
        return self

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

    def setMerchantToken(self, merchantToken):
        self.merchantToken = merchantToken
        return self

    def setReferenceNo(self, referenceNo):
        self.referenceNo = referenceNo
        return self

    def setAmt(self, amt):
        self.amt = amt
        return self


class BuildCreditCardPayment(BuilderCreditCardPayment):
    def build(self):
        return CreditCardPayment(
            self.timestamp,
            self.tXid,
            self.cardNo,
            self.cardExpYymm,
            self.cardCvv,
            self.merchantToken,
            self.referenceNo,
            self.amt
        )
