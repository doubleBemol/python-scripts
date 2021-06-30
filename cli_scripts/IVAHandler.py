class PriceTaxHelper:
    """Simple class that can add or substract TAX to prices.

    How to use: Import it to your script by using:
    from PriceTaxHelper import * (assuming the file is in the same directory), 

    Then just instantiate an object:
    tax = PriceTaxHelper() 

    And use tax to performe your calculations.

    Example:
    result = tax.price_without_tax(122.50)
    """

    def __init__(self):
        self._TAX_RATE = 0.16

    def price_without_tax(self, price_with_tax: float) -> float:
        """Given a price with the TAX already added, returns the price without it. The TAX rate is obtained from _TAX_RATE.

        Args:
            price_with_tax (float): The price

        Returns:
            float: A price without the TAX rate, i.e., the original price.
        """
        return price_with_tax / (1 + self._TAX_RATE)

    def price_with_tax(self, price_without_tax: float) -> float:
        """Given a price without the TAX, returns the price with the TAX. The TAX rate is obtained from _TAX_RATE.

        Args:
            price_without_tax (float): The price.

        Returns:
            float: A price with the TAX added.
        """
        return price_without_tax * self._IVA_RATE + price_without_tax

    @property
    def tax_rate(self) -> float:
        """Returns the internal TAX rate, so you can know what value is being used

        Returns:
            float: The current TAX rate.
        """
        return self._TAX_RATE

    @tax_rate.setter
    def tax_rate(self, new_tax_rate: float) -> None:
        """It allow to set a new TAX rate. The new value must be in a decimal format, if not, a convertion will be attempted.

        Args:
            new_tax_rate (float): The decimal value of the new TAX rate.

        Raises:
            TypeError: The entering value must be a decimal (float).
        """
        isFloat = isinstance(new_tax_rate, float)
        try:
            if not isFloat:
                raise TypeError("TAX rate must be provided in decimals")
            self._TAX_RATE = new_tax_rate
        except TypeError:
            try:
                new_tax_rate = new_tax_rate / 100
                self._TAX_RATE = new_tax_rate
                print("Value was converted to decimal form and saved correctly!")
            except:
                print("Something went wrong with the conversion. Nothing was assigned!")
