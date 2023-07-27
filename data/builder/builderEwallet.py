class Ewallet:
    def __init__(self,
                 payMethod,
                 mitraCd,
                 userIp,
                 amt):
        self.payMethod = payMethod
        self.mitraCd = mitraCd
        self.userIp = userIp
        self.amt = amt

    def jsonEwallet(self):
        return ({
            "payMethod": self.payMethod,
            "mitraCd": self.mitraCd,
            "userIP": self.userIp,
            "amt": self.amt
        })


class BuilderEwallet:
    def __init__(self):
        self.payMethod = None
        self.mitraCd = None
        self.userIp = None
        self.amt = None

    def setPayMethod(self, payMethod):
        self.payMethod = payMethod
        return self

    def setMitraCd(self, mitraCd):
        self.mitraCd = mitraCd
        return self

    def setUserIp(self, userIp):
        self.userIp = userIp
        return self

    def setAmt(self, amt):
        self.amt = amt
        return self


class BuildEwallet(BuilderEwallet):
    def build(self):
        return Ewallet(
            self.payMethod,
            self.mitraCd,
            self.userIp,
            self.amt
        )


class EwalletPayment:
    def __init__(self,
                 timestamp,
                 tXid,
                 referenceNo,
                 amt):
        self.timestamp = timestamp
        self.tXid = tXid
        self.referenceNo = referenceNo
        self.amt = amt

    def dataEwallet(self):
        return ({
            "timeStamp": self.timestamp,
            "tXid": self.tXid,
            "referenceNo": self.referenceNo,
            "amt": self.amt
        })


class BuilderEwalletPayment:
    def __init__(self):
        self.timestamp = None
        self.tXid = None
        self.referenceNo = None
        self.amt = None

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp
        return self

    def setTxid(self, tXid):
        self.tXid = tXid
        return self

    def setReferenceNo(self, referenceNo):
        self.referenceNo = referenceNo
        return self

    def setAmt(self, amt):
        self.amt = amt
        return self


class BuildEwalletPayment(BuilderEwalletPayment):
    def build(self):
        return EwalletPayment(
            self.timestamp,
            self.tXid,
            self.referenceNo,
            self.amt
        )
