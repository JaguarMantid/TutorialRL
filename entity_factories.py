import colour
from components import consumable
from components.ai import BaseAI, HostileEnemy
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

confusion_scroll = Item(char="~", colour=colour.scroll_confusion,
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

fireball_scroll = Item(char="~", colour=colour.scroll_fireball,
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)

health_potion = Item(char="!", colour=colour.potion_heal, name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
)

lightning_scroll = Item(char="~", colour=colour.scroll_lightning,
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)
