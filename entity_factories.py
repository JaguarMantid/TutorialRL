import colour
from components.ai import BaseAI, HostileEnemy
from components.consumable import HealingConsumable
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Actor, Item


player = Actor(char="@", colour=colour.player, name="Player",
    ai_cls=BaseAI, fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=26),
)

orc = Actor(char="o", colour=colour.orc, name="Orc", ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
)

troll = Actor(char="T", colour=colour.troll, name="Troll", ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
    inventory=Inventory(capacity=0),
)

health_potion = Item(char="!", colour=colour.item, name="Health Potion",
    consumable=HealingConsumable(amount=4),
)
