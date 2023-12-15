from typing import TypeVar

from raffaelo.interfaces.providers.interface import iCBP

ProviderType = TypeVar("ProviderType", bound=iCBP)
