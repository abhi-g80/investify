from twilio.rest import Client


class SendText:
    def __init__(self, from_number: str, to_number: str) -> Client:
        self.client = Client()
        self.from_wsp_number = from_number
        self.to_wsp_number = to_number

    @property
    def from_wsp_number(self) -> str:
        return self._from_wsp_number

    @property
    def to_wsp_number(self) -> str:
        return self._to_wsp_number

    @from_wsp_number.setter
    def from_wsp_number(self, value: str) -> str:
        if value:
            self._from_wsp_number = "whatsapp:" + value
        else:
            raise ValueError("From phone number cannot be empty.")
        return self._from_wsp_number

    @to_wsp_number.setter
    def to_wsp_number(self, value: str) -> str:
        if value:
            self._to_wsp_number = "whatsapp:" + value
        else:
            raise ValueError("To phone number cannot be empty.")
        return self._to_wsp_number

    def send(self, message: str) -> None:
        """Wrapper to send text message on whatsapp.

        Args:
            message (str): Message to send.

        """
        self.client.messages.create(
            body=message, from_=self.from_wsp_number, to=self.to_wsp_number
        )
