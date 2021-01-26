import colour
from components import consumable, equippable
from components.ai import BaseAI, HostileEnemy
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item


player = Actor(char="@", colour=colour.player, name="Player",
    ai_cls=BaseAI, equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26), level=Level(level_up_base=200),
)

orc = Actor(char="o", colour=colour.orc, name="Orc", ai_cls=HostileEnemy,
    equipment=Equipment(), fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0), level=Level(xp_given=35),
)

troll = Actor(char="T", colour=colour.troll, name="Troll", ai_cls=HostileEnemy,
    equipment=Equipment(), fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0), level=Level(xp_given=100),
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

dagger = Item(char="/", colour=colour.weapon, name="Dagger",
    equippable=equippable.Dagger()
)

sword = Item(char="/", colour=colour.weapon, name="Sword",
             equippable=equippable.Sword()
)

leather_armour = Item(char="[", colour=colour.armour, name="Leather Armour",
    equippable=equippable.LeatherArmour(),
)

chain_mail = Item(char="[", colour=colour.armour, name="Chain Mail",
    equippable=equippable.ChainMail()
)
