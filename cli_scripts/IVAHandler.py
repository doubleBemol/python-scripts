class IVAHandler:
    """Simple class that can add or substract iva to prices.
    
    How to use: Import it to your script by using from IVAHandler import * (assuming the file is in the same directory), then just instantiate an object
    iva = IVAHandler() and use iva to performe your calculations.
    
    example:
    result = iva.price_without_iva(122.50)
    """

    def __init__(self):
        self._IVA_RATE = 0.16

    def price_without_iva(self, price_with_iva: float) -> float:
        """Given a price with the IVA already added, returns the price without it. The IVA rate is obtained from _IVA_RATE.

        Args:
            price_with_iva (float): The price

        Returns:
            float: A price without the IVA rate, i.e., the original price.
        """
        return price_with_iva / (1 + self._IVA_RATE)

    def price_with_iva(self, price_without_iva: float) -> float:
        """Given a price without the IVA, returns the price with the IVA. The IVA rate is obtained from _IVA_RATE.

        Args:
            price_without_iva (float): The price.

        Returns:
            float: A price with the IVA added.
        """
        return price_without_iva * self._IVA_RATE + price_without_iva

    @property
    def iva_rate(self) -> float:
        """Returns the internal IVA rate, so you can know what value is being used

        Returns:
            float: The current IVA rate.
        """
        return self._IVA_RATE

    @iva_rate.setter
    def iva_rate(self, new_iva_rate: float) -> None:
        """It allow to set a new IVA rate. The new value must be in a decimal format, if not, a convertion will be attempted.

        Args:
            new_iva_rate (float): The decimal value of the new IVA rate.

        Raises:
            TypeError: The entering value must be a decimal (float).
        """
        isFloat = isinstance(new_iva_rate, float)
        try:
            if not isFloat:
                raise TypeError("IVa rate must be provided in decimals")
            self._IVA_RATE = new_iva_rate
        except TypeError:
            try:
                new_iva_rate = new_iva_rate / 100
                self._IVA_RATE = new_iva_rate
                print("Value was converted to decimal form and saved correctly!")
            except:
                print("Something went wrong with the conversion. Nothing was assigned!")
