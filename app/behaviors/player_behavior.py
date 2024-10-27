import random
from abc import ABC, abstractmethod


class PlayerBehavior(ABC):
    @abstractmethod
    def should_buy_property(self, player, property):
        pass


class ImpulsiveBehavior:
    def should_buy_property(self, player, property):
        # Comportamento impulsivo: compra qualquer propriedade cair
        return True


class DemandingBehavior:
    def should_buy_property(self, player, property):
        # Comportamento exigente: só compra se o aluguel for maior que 50
        return property.rent > 50


class CautiousBehavior:
    def should_buy_property(self, player, property):
        # Comportamento cauteloso: compra se, após a compra, ainda tiver um saldo de pelo menos 80
        return player.balance - property.cost >= 80


class RandomBehavior:
    def should_buy_property(self, player, property):
        # Comportamento aleatório: decide aleatoriamente comprar ou não
        return random.choice([True, False])
