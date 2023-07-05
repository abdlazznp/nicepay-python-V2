class ConstantsEndpoints:
    _REGISTRATION = "/nicepay/direct/v2/registration"
    _PAYMENT = "/nicepay/direct/v2/payment"
    _INQUIRY = "/nicepay/direct/v2/inquiry"
    _CANCEL = "/nicepay/direct/v2/cancel"

    @staticmethod
    def registration():
        return ConstantsEndpoints._REGISTRATION

    @staticmethod
    def payment():
        return ConstantsEndpoints._PAYMENT

    @staticmethod
    def inquiry():
        return ConstantsEndpoints._INQUIRY

    @staticmethod
    def cancel():
        return ConstantsEndpoints._CANCEL
