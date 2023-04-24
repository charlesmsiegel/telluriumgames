import random

# from secrets import choice

ABILITIES = [
    "archery",
    "athletics",
    "awareness",
    "brawl",
    "bureaucracy",
    "craft",
    "dodge",
    "integrity",
    "investigation",
    "larceny",
    "linguistics",
    "lore",
    "martial_arts",
    "medicine",
    "melee",
    "occult",
    "performance",
    "presence",
    "resistance",
    "ride",
    "sail",
    "socialize",
    "stealth",
    "survival",
    "thrown",
    "war",
]


class RandomName:
    def __call__(self):
        return self.prompt()

    def prompt(self):
        return ""

    def random_add(self, option_list, option, probability):
        if random.random() < probability:
            option_list.append(option)


class ExaltedName(RandomName):
    """
    Based on Exalted Name Generator: https://orteil.dashnet.org/randomgen/?gen=idbeAjts
    """

    def absnegative(self, plural=False):
        choice = random.choice(
            [
                (random.choice(["Rage", "Anger"]), "Angers"),
                ("Annihilation", "Ends"),
                ("Ash", "Ashes"),
                ("Bitterness", "Fears"),
                ("Cries", "Cries"),
                ("Dance", "Dances"),
                ("Despair", "Despairs"),
                ("Dishonor", "Dishonors"),
                ("Doubt", "Doubts"),
                ("Dust", "Ashes"),
                ("Ennui", "Tears"),
                ("Envy", "Envies"),
                (random.choice(["Fear", "Fear", "Horror"]), "Horrors"),
                ("Gathering", "Gatherings"),
                ("Gloom", "Palls"),
                ("Grief", "Griefs"),
                ("Hate", "Hates"),
                ("Illusion", "Illusions"),
                ("Intonation", "Intonations"),
                ("Lament", "Laments"),
                ("Laughter", "Laughs"),
                ("Loss", "Losses"),
                ("Machination", "Machinations"),
                ("Mirage", "Mirages"),
                ("Misery", "Miseries"),
                ("Murder", "Murders"),
                ("Nightmare", "Nightmares"),
                ("Oblivion", "Voids"),
                ("Pain", "Pains"),
                ("Plague", "Plagues"),
                ("Plot", "Plots"),
                ("Procession", "Processions"),
                ("Punishment", "Punishments"),
                ("Regret", "Regrets"),
                ("Repose", "Silences"),
                ("Ritual", "Rituals"),
                ("Sacrifice", "Sacrifices"),
                (random.choice(["Sadness", "Sorrow"]), "Sorrows"),
                ("Screams", "Screams"),
                ("Tears", "Tears"),
                ("Travail", "Travail"),
                ("Tyranny", "Tyrants"),
                ("Vanity", "Vanities"),
                (random.choice(["Poison", "Venom"]), "Venoms"),
                ("Woe", "Woes"),
                ("Wrath", "Wraths"),
            ]
        )
        if plural:
            return choice[1]
        return choice[0]

    def abspositive(self, plural=False):
        options = [
            ("Cascades", "Cascades"),
            ("Celebration", "Celebrations"),
            ("Ceremony", "Ceremonies"),
            ("Chanting", "Chants"),
            ("Contemplation", "Meditations"),
            ("Dance", "Dances"),
            ("Dream", "Dreams"),
            ("Facet", "Facets"),
            ("Fortune", "Fortunes"),
            ("Gathering", "Gatherings"),
            ("Glory", "Glories"),
            ("Grace", "Graces"),
            ("Honor", "Honors"),
            ("Hope", "Hopes"),
            ("Intonation", "Intonations"),
            ("Joy", "Joys"),
            ("Laughter", "Laughs"),
            ("Light", "Lights"),
            ("Mandala", "Mandalas"),
            ("Melody", "Melodies"),
            ("Mercy", "Mercies"),
            ("Miracle", "Miracles"),
            ("Mirror", "Mirrors"),
            ("Moment", "Moments"),
            ("Passion", "Passions"),
            ("Peace", "Gifts"),
            ("Poetry", "Poems"),
            ("Procession", "Processions"),
            ("Reflection", "Reflections"),
            ("Reward", "Rewards"),
            ("Ritual", "Rituals"),
            ("Sacrifice", "Sacrifices"),
            ("Song", "Songs"),
            ("Splendor", "Splendors"),
            ("Stillness", "Dreams"),
            ("Triumph", "Triumphs"),
            ("Virtue", "Virtues"),
            ("Vows", "Vows"),
            ("Wisdom", "Wisdoms"),
            ("Wonder", "Wonders"),
        ]
        choice = random.choice(options)
        if plural:
            return choice[1]
        return choice[0]

    def anatomy(self, plural=False):
        options = [
            ("Bile", "Humors"),
            ("Blood", "Veins"),
            ("Breath", "Breaths"),
            (random.choice(["Claw", "Talon"]), "Claws"),
            (random.choice(["Eye", "Eyes"]), "Eyes"),
            ("Face", "Eyes"),
            ("Fang", "Fangs"),
            ("Finger", "Fingers"),
            ("Fist", "Fists"),
            ("Foot", "Feet"),
            ("Hair", "Hands"),
            ("Hand", "Hands"),
            ("Heart", "Hearts"),
            ("Heartbeat", "Heartbeats"),
            ("Mind", "Thoughts"),
            ("Silhouette", "Silhouettes"),
            ("Soul", "Souls"),
            (random.choice(["Skin", "Arm"]), "Arms"),
            ("Tooth", "Teeth"),
            ("Voice", "Voices"),
            (
                random.choice(["Wing", "Wing", "Wing", "Pinion", "Feather", "Plume"]),
                "Wings",
            ),
        ]
        if random.random() < 0.6:
            options.append(("Hoof", "Hooves"))
        if random.random() < 0.75:
            options.append(("Stance", "Stances"))
        if random.random() < 0.75:
            options.append(("Tail", "Tails"))
        choice = random.choice(options)
        if plural:
            return choice[1]
        return choice[0]

    def animal(self, plural=False):
        options = [
            ("Aardvark", "Aardvarks"),
            ("Addax", "Addaxes"),
            ("Adzebill", "Adzebills"),
            (random.choice(["Agouti", "Paca"]), "Pacas"),
            ("Albatross", "Albatrosses"),
            ("Alligator", "Alligators"),
            ("Angler-lizard", "Angler-lizards"),
            ("Anole", "Anoles"),
            ("Antbird", "Antbirds"),
            ("Anteater", "Anteaters"),
            (
                random.choice(["Ape", "Chimpanzee", "Bonobo", "Gorilla", "Orangutan"]),
                "Apes",
            ),
            ("Armadillo", "Armadillos"),
            (random.choice(["Auk", "Auk", "Puffin"]), "Auks"),
            ("Aurochs", "Aurochs"),
            (random.choice(["Austrech", "Austrech", "Ostrich"]), "Austreches"),
            ("Avocet", "Avocets"),
            ("Aye-Aye", "Aye-Aye"),
            ("Babbler", "Babblers"),
            (random.choice(["Baboon", "Baboon", "Mandrill"]), "Baboons"),
            (random.choice(["Badger", "Badger", "Ratel"]), "Badgers"),
            ("Bandicoot", "Bandicoots"),
            ("Barracuda", "Barracudas"),
            ("Basilisc", "Basiliscs"),
            ("Bat", "Bats"),
            ("Bear", "Bears"),
            ("Beast", "Beasts"),
            ("Beaver", "Beavers"),
            ("Bee", "Bees"),
            (random.choice(["Beetle", "Scarab"]), "Beetles"),
            ("Bellbird", "Bellbirds"),
            ("Betta", "Bettas"),
            ("Bettong", "Bettongs"),
            ("Bilby", "Bilbies"),
            ("Bird", "Birds"),
            (random.choice(["Bittern", "Egret"]), "Egrets"),
            (random.choice(["Boar", "Sow"]), "Boars"),
            ("Boar-Seal", "Boar-Seals"),
            ("Bowerbird", "Bowerbirds"),
            ("Buffalo", "Buffalo"),
            ("Bull", "Bulls"),
            ("Bunting", "Buntings"),
            ("Bunyip", "Bunyip"),
            ("Burrow-lok", "Burrow-loks"),
            ("Bushdog", "Bushdogs"),
            ("Bustard", "Bustards"),
            ("Butterfly", "Butterflies"),
            ("Buzzard", "Buzzards"),
            ("Caecilian", "Caeclians"),
            ("Caiman", "Caimans"),
            ("Camel", "Camels"),
            ("Capybara", "Capybaras"),
            ("Caracal", "Caracals"),
            (random.choice(["Caribou", "Reindeer"]), "Reindeer"),
            ("Carp", "Carp"),
            ("Cassowary", "Cassowaries"),
            ("Catfish", "Catfish"),
            (random.choice(["Cavy", "Coney"]), "Cavies"),
            ("Centipede", "Centipedes"),
            ("Cheetah", "Cheetahs"),
            ("Chevrotain", "Chevrotains"),
            ("Chinchilla", "Chinchillas"),
            ("Chipmunk", "Chipmunks"),
            ("Chiru", "Chiru"),
            ("Chital", "Chital"),
            ("Ciclid", "Ciclids"),
            ("Clawstrider", "Clawstriders"),
            (random.choice(["Coati", "Coati", "Coatimundi"]), "Coatis"),
            ("Cobra", "Cobras"),
            ("Cockatoo", "Cockatoos"),
            ("Cockatrice", "Cockatrices"),
            ("Coelacanth", "Coelacanths"),
            ("Colugo", "Colugos"),
            ("Condor", "Condors"),
            (random.choice(["Coot", "Crake", "Moorhen"]), "Crakes"),
            ("Cormorant", "Cormorants"),
            (random.choice(["Cougar", "Puma"]), "Cougars"),
            ("Crab", "Crabs"),
            ("Crane", "Cranes"),
            ("Crayfish", "Crayfish"),
            ("Cricket", "Crickets"),
            ("Crocodile", "Crocodiles"),
            ("Crossbill", "Crossbills"),
            (random.choice(["Crow", "Raven"]), "Crows"),
            ("Cuckoo", "Cuckoos"),
            ("Currasow", "Currasows"),
            ("Curlew", "Curlews"),
            ("Cuttlefish", "Cuttlefish"),
            (random.choice(["Dace", "Chub"]), "Daces"),
            ("Deer", "Deer"),
            ("Devil", "Devils"),
            ("Dhole", "Dholes"),
            ("Dinosaur", "Dinosaurs"),
            ("Dodo", "Dodos"),
            ("Dog", "Dogs"),
            ("Dolphin", "Dolphins"),
            ("Dormouse", "Dormice"),
            ("Dove", "Doves"),
            ("Dragon", "Dragons"),
            ("Dragonfly", "Dragonflies"),
            ("Duck", "Ducks"),
            ("Dugong", "Dugongs"),
            ("Duiker", "Duikers"),
            ("Dunnart", "Dunnarts"),
            (random.choice(["Eagle", "Eagle", "Caracara", "Erne"]), "Eagles"),
            ("Echidna", "Echidnas"),
            ("Eel", "Eels"),
            ("Eider", "Eiders"),
            ("Eland", "Elands"),
            ("Elephant", "Elephants"),
            ("Elephant-bird", "Elephant-birds"),
            ("Emu", "Emus"),
            (
                random.choice(
                    ["Falcon", "Falcon", "Kestrel", "Gyrfalcon", "Peregrine"]
                ),
                "Falcons",
            ),
            ("Fantail", "Fantails"),
            (
                random.choice(["Ferret", "Weasel", "Stoat", "Ermine", "Polecat"]),
                "Ferrets",
            ),
            ("Finch", "Finches"),
            ("Finfoot", "Finfoots"),
            ("Fire-ant", "Fire-ants"),
            ("Fish", "Fish"),
            ("Flamingo", "Flamingos"),
            ("Flowerpecker", "Flowerpeckers"),
            ("Flufftail", "Flufftails"),
            ("Flycatcher", "Flycatchers"),
            ("Four-wing", "Four-wings"),
            (random.choice(["Fox", "Fox", "Fennec", "Zorro"]), "Foxes"),
            ("Francolin", "Francolins"),
            ("Frigatebird", "Frigatebirds"),
            ("Frilled-lizard", "Frilled-lizards"),
            ("Frog", "Frogs"),
            (random.choice(["Gallinule", "Swamphen"]), "Swamphens"),
            (random.choice(["Gannet", "Gannet", "Booby"]), "Gannets"),
            ("Gara", "Gara-fish"),
            (random.choice(["Gavial", "Gharial"]), "Gavials"),
            ("Gazelle", "Gazelles"),
            ("Gecko", "Geckos"),
            (random.choice(["Genet", "Civet"]), "Civets"),
            ("Gerenuk", "Gerenuks"),
            ("Ghost", "Ghosts"),
            ("Gibbon", "Gibbons"),
            ("Giraffe", "Giraffes"),
            ("Glider", "Gliders"),
            ("Goat", "Goats"),
            ("Goose", "Geese"),
            ("Gopher", "Gophers"),
            (random.choice(["Goral", "Serow"]), "Gorals"),
            ("Grasscutter", "Grasscutters"),
            ("Grasshopper", "Grasshoppers"),
            ("Gravehound", "Gravehounds"),
            ("Great-terror", "Great-terror"),
            ("Grebe", "Grebes"),
            ("Grosbeak", "Grosbeaks"),
            ("Grouse", "Grouses"),
            ("Grunion", "Grunions"),
            ("Gryphon", "Gryphons"),
            ("Grysbok", "Grysbok"),
            ("Guan", "Guans"),
            (random.choice(["Guanaco", "Vicuña"]), "Guanacos"),
            ("Guenon", "Guenons"),
            (random.choice(["Guillemot", "Murre", "Auk"]), "Guillemots"),
            ("Guineafowl", "Guineafowl"),
            ("Gull", "Gulls"),
            ("Guppy", "Guppies"),
            (random.choice(["Hamster", "Gerbil"]), "Hamsters"),
            ("Hare", "Hares"),
            ("Harpy", "Harpies"),
            ("Hartebeest", "Hartebeests"),
            ("Hatra", "Hatras"),
            (random.choice(["Hawk", "Hawk", "Azor"]), "Hawks"),
            ("Hedgehog", "Hedgehogs"),
            ("Hellboar", "Hellboars"),
            (random.choice(["Hen", "Rooster"]), "Hens"),
            (random.choice(["Heron", "Egret"]), "Herons"),
            ("Herring", "Herrings"),
            ("Hippo", "Hippos"),
            ("Hoatzin", "Hoatzins"),
            ("Honeycreeper", "Honeycreepers"),
            ("Honeyeater", "Honeyeaters"),
            ("Hoopoe", "Hoopoes"),
            ("Hornbill", "Hornbills"),
            (
                random.choice(
                    ["Horse", "Horse", "Pony", "Donkey", "Tarpan", "Mare", "Stallion"]
                ),
                "Horses",
            ),
            ("Hound", "Hounds"),
            ("Hummingbird", "Hummingbirds"),
            (random.choice(["Hutia", "Coypu"]), "Hutias"),
            ("Hybroc", "Hybrocs"),
            (random.choice(["Hyena", "Hyena", "Crocuta"]), "Hyenas"),
            ("Hyrax", "Hyraxes"),
            (random.choice(["Ibex", "Tahr"]), "Ibexes"),
            ("Ibis", "Ibises"),
            ("Ice-fisher", "Ice-fishers"),
            ("Ichneumon", "Ichneumons"),
            ("Iguana", "Iguanas"),
            ("Impala", "Impalas"),
            ("Indri", "Indris"),
            ("Jaçana", "Jaçanas"),
            ("Jackal", "Jackals"),
            ("Jaeger", "Jaegers"),
            ("Jaguar", "Jaguars"),
            ("Jaguarundi", "Jaguarundis"),
            ("Jay", "Jays"),
            ("Jellyfish", "Jellyfish"),
            ("Jerboa", "Jerboas"),
            ("Kangaroo", "Kangaroos"),
            ("Kermeus", "Karmeus"),
            ("Kingfisher", "Kingfishers"),
            ("Kinkajou", "Kinkajous"),
            ("Kirin", "Kirin"),
            ("Kite", "Kites"),
            ("Kiwi", "Kiwis"),
            ("Knifetooth", "Knifetooths"),
            ("Koala", "Koalas"),
            ("Koi", "Koi"),
            ("Krait", "Kraits"),
            ("Kraken", "Krakens"),
            ("Kudu", "Kudus"),
            ("Langur", "Langurs"),
            (random.choice(["Lapwing", "Plover"]), "Lapwings"),
            ("Lark", "Larks"),
            (random.choice(["Lechwe", "Waterbuck", "Reedbuck"]), "Lechwes"),
            (random.choice(["Lemming", "Vole"]), "Voles"),
            ("Lemur", "Lemurs"),
            (random.choice(["Leopard", "Leopard", "Pard"]), "Leopards"),
            ("Linsang", "Linsangs"),
            ("Lion", "Lions"),
            ("Lizard", "Lizards"),
            ("Llama", "Llamas"),
            ("Lobster", "Lobsters"),
            ("Locust", "Locusts"),
            (random.choice(["Loon", "Diver"]), "Divers"),
            (random.choice(["Loris", "Galago"]), "Galagos"),
            (random.choice(["Lory", "Lorikeet"]), "Lorikeets"),
            ("Lyrebird", "Lyrebirds"),
            ("Lynx", "Lynxes"),
            ("Macaque", "Macaques"),
            ("Macaw", "Macaws"),
            ("Magpie", "Magpies"),
            ("Mamba", "Mambas"),
            ("Mammoth", "Mammoths"),
            ("Manatee", "Manatees"),
            ("Mangabey", "Mangabeys"),
            ("Mantis", "Mantises"),
            ("Mare", "Mares"),
            ("Marlin", "Marlins"),
            (random.choice(["Marmoset", "Tamarin"]), "Marmosets"),
            ("Marmot", "Marmots"),
            (random.choice(["Marten", "Sable", "Fisher"]), "Sables"),
            ("Mastodon", "Mastodons"),
            ("Megapode", "Megapodes"),
            ("Merganser", "Mergansers"),
            ("Mihirung", "Mihirungs"),
            ("Minnow", "Minnows"),
            (random.choice(["Mink", "Polecat"]), "Polecats"),
            ("Moa", "Moas"),
            ("Moa-nalo", "Moa-nalo"),
            ("Mockingbird", "Mockingbirds"),
            ("Mole", "Moles"),
            ("Mole-rat", "Mole-rats"),
            ("Monal", "Monals"),
            (random.choice(["Mongoose", "Mongoose", "Meerkat"]), "Mongooses"),
            ("Monitor", "Monitors"),
            ("Monkey", "Monkeys"),
            ("Moonrat", "Moonrats"),
            ("Moose", "Moose"),
            ("Mospid", "Mospids"),
            ("Moth", "Moths"),
            ("Motmot", "Motmots"),
            ("Mouse", "Mice"),
            ("Mousebird", "Mousebirds"),
            ("Muntjac", "Muntjacs"),
            ("Muskox", "Muskoxen"),
            ("Muskrat", "Muskrats"),
            ("Mynah", "Mynahs"),
            ("Naga", "Naga"),
            ("Ñandu", "Ñanduces"),
            (random.choice(["Narwhal", "Narwhal", "Beluga"]), "Narwhales"),
            ("Nautilus", "Nautiluses"),
            ("Needlefish", "Needlefish"),
            ("Ngoubou", "Ngoubous"),
            ("Nightingale", "Nightingales"),
            ("Nightjar", "Nightjars"),
            ("Numbat", "Numbats"),
            (random.choice(["Ocelot", "Margay"]), "Ocelots"),
            ("Octopus", "Octopi"),
            ("Oilbird", "Oilbird"),
            ("Okapi", "Okapis"),
            ("Omen-dog", "Omen-dogs"),
            (random.choice(["Onager", "Kulan"]), "Onagers"),
            ("Oriole", "Orioles"),
            ("Oryx", "Oryxes"),
            ("Otter", "Otters"),
            ("Owl", "Owls"),
            ("Ox", "Oxen"),
            ("Ox-dragon", "Ox-dragons"),
            ("Panda", "Pandas"),
            ("Pangolin", "Pangolins"),
            (random.choice(["Parrot", "Parakeet"]), "Parrots"),
            ("Partridge", "Partridges"),
            (random.choice(["Peacock", "Peahen"]), "Peafowl"),
            ("Peccary", "Peccaries"),
            ("Pelican", "Pelicans"),
            ("Perch", "Perches"),
            ("Pestletail", "Pestletails"),
            (random.choice(["Petrel", "Petrel", "Storm-petrel"]), "Petrels"),
            ("Phalanger", "Phalangers"),
            ("Phalarope", "Phalaropes"),
            ("Pheasant", "Pheasants"),
            ("Phoenix", "Phoenixes"),
            ("Pigeon", "Pigeons"),
            ("Pika", "Pikas"),
            ("Piranha", "Piranhas"),
            ("Pitta", "Pittas"),
            ("Platypus", "Platypi"),
            ("Pochard", "Pochards"),
            ("Porcupine", "Porcupines"),
            ("Porpoise", "Porpoise"),
            (random.choice(["Possum", "Opossum"]), "Possums"),
            ("Pratincole", "Pratincoles"),
            ("Pronghorn", "Pronghorns"),
            ("Pudu", "Pudu-deer"),
            (random.choice(["Python", "Boa", "Anaconda"]), "Pythons"),
            ("Quail", "Quails"),
            ("Quokka", "Quokkas"),
            ("Quoll", "Quolls"),
            ("Quoll-Lion", "Quoll-Lion"),
            ("Rabbit", "Rabbits"),
            ("Raccoon", "Raccoons"),
            ("Rail", "Rails"),
            (random.choice(["Rainshark", "Fogshark"]), "Rainsharks"),
            (random.choice(["Raiton", "Raven"]), "Raitons"),
            ("Raptor", "Raptors"),
            ("Raptor-cat", "Raptor-cats"),
            ("Rat", "Rats"),
            ("Rattlesnake", "Rattlesnakes"),
            ("Rhebok", "Rheboks"),
            ("Rhino", "Rhinos"),
            ("River-dragon", "River-dragon"),
            ("Robin", "Robins"),
            ("Roc", "Rocs"),
            ("Rodent", "Rodents"),
            ("Roller", "Rollers"),
            ("Sabretooth", "Sabretooths"),
            ("Saiga", "Saiga"),
            (
                random.choice(
                    [
                        "Salamander",
                        "Salamander",
                        "Salamander",
                        "Newt",
                        "Newt",
                        "Axolotl",
                    ]
                ),
                "Salamanders",
            ),
            ("Salmon", "Salmon"),
            ("Sandgrouse", "Sandgrouse"),
            ("Sandpiper", "Sandpipers"),
            ("Sand-swimmer", "Sand-swimmer"),
            ("Sardine", "Sardines"),
            ("Scorpion", "Scorpions"),
            ("Scythefoot", "Scythefoots"),
            ("Seal", "Seals"),
            ("Seacow", "Seacows"),
            ("Sea-dragon", "Sea-dragons"),
            ("Sea-elk", "Sea-elks"),
            ("Seahorse", "Seahorses"),
            ("Sealion", "Sealions"),
            ("Sea-snake", "Sea-snake"),
            ("Sengi", "Sengis"),
            ("Serpent", "Serpents"),
            ("Serval", "Servals"),
            (random.choice(["Shark", "Shark", "Dogfish"]), "Sharks"),
            ("Shearwater", "Shearwaters"),
            ("Shelduck", "Shelducks"),
            ("Sheldgoose", "Sheldgoose"),
            ("Shrew", "Shrews"),
            ("Shrike", "Shrikes"),
            ("Siaka", "Siakas"),
            ("Siege-lizard", "Siege-lizards"),
            ("Sitatunga", "Sitatungas"),
            ("Sivathere", "Sivatheres"),
            ("Skink", "Skinks"),
            ("Skunk", "Skunks"),
            ("Sloth", "Sloths"),
            ("Snail", "Snails"),
            ("Snake", "Snakes"),
            (random.choice(["Snipe", "Woodcock"]), "Woodcocks"),
            ("Snowcock", "Snowcocks"),
            ("Solenodon", "Solenodons"),
            ("Souslik", "Sousliks"),
            ("Sparrow", "Sparrows"),
            ("Spiny-rat", "Spiny-rats"),
            ("Spider", "Spiders"),
            ("Spoonbill", "Spoonbills"),
            ("Squid", "Squid"),
            ("Squirrel", "Squirrels"),
            ("Stag", "Stags"),
            ("Hart", "Harts"),
            ("Stalker", "Stalkers"),
            ("Stallion", "Stallions"),
            ("Starfish", "Starfish"),
            ("Starling", "Starlings"),
            ("Stork", "Storks"),
            ("Strix", "Striges"),
            ("Sturgeon", "Sturgeon"),
            ("Sunbird", "Sunbirds"),
            ("Sungrebe", "Sungrebes"),
            ("Swallow", "Swallows"),
            ("Swamp-dragon", "Swamp-dragons"),
            ("Swan", "Swans"),
            ("Swordfish", "Swordfish"),
            ("Taipan", "Taipans"),
            ("Tanager", "Tanagers"),
            ("Tanuki", "Tanuki"),
            ("Tapir", "Tapirs"),
            ("Tarantula", "Tarantulas"),
            ("Tarsier", "Tarsiers"),
            ("Tekahe", "Tekahes"),
            ("Teratorn", "Teratorns"),
            ("Tern", "Terns"),
            ("Thrush", "Thrushes"),
            ("Thylacine", "Thylacines"),
            ("Tiger", "Tigers"),
            ("Tinamu", "Tinamus"),
            ("Titmouse", "Titmice"),
            ("Toad", "Toads"),
            ("Tortoise", "Tortoises"),
            ("Toucan", "Toucans"),
            ("Treecreeper", "Treecreepers"),
            ("Treedragon", "Treedragon"),
            ("Tree-pard", "Tree-pards"),
            ("Treepie", "Treepies"),
            ("Tree-singer", "Tree-singers"),
            ("Tree-strider", "Tree-striders"),
            ("Tropicbird", "Tropicbirds"),
            (random.choice(["Trout", "Whitefish"]), "Trout"),
            ("Trumpeter", "Trumpeters"),
            ("Tuatara", "Tuataras"),
            ("Tuna", "Tuna"),
            ("Turaco", "Turacos"),
            ("Turkey", "Turkeys"),
            (random.choice(["Turtle", "Turtle", "Terrapin"]), "Turtles"),
            ("Unicorn", "Unicorns"),
            ("Urvogel", "Urvogels"),
            (random.choice(["Viper", "Adder", "Asp"]), "Vipers"),
            ("Vireo", "Vireos"),
            ("Vulture", "Vultures"),
            ("Wagtail", "Wagtails"),
            ("Wallaby", "Wallabies"),
            ("Walleye", "Walleye"),
            ("Walrus", "Walruses"),
            (random.choice(["Wapiti", "Elk"]), "Elk"),
            ("Warbler", "Warblers"),
            ("Warhawk", "Warhawk"),
            ("Warthog", "Warthogs"),
            (random.choice(["Wasp", "Hornet"]), "Wasps"),
            ("Weaverbird", "Weaverbirds"),
            (random.choice(["Whale", "Whale", "Orca", "Cachalot"]), "Whales"),
            ("Whimbrel", "Whimbrels"),
            ("White-eye", "White-eyes"),
            ("Wildcat", "Wildcats"),
            ("Wildebeest", "Wildebeests"),
            (random.choice(["Wisent", "Bison", "Bison"]), "Wisents"),
            ("Wolf", "Wolves"),
            ("Wolf-spider", "Wolf-spiders"),
            ("Wolverine", "Wolverines"),
            ("Wombat", "Wombats"),
            ("Woodhoopoe", "Woodhoopoe"),
            ("Woodpecker", "Woodpeckers"),
            ("Woodstar", "Woodstars"),
            ("Wren", "Wrens"),
            ("Whydah", "Whydahs"),
            ("Yak", "Yaks"),
            ("Yeddim", "Yeddims"),
            ("Yeti", "Yetis"),
            (random.choice(["Zebra", "Zebra", "Quagga"]), "Zebras"),
            ("Zoril", "Zorils"),
        ]
        choice = random.choice(options)
        if plural:
            return choice[1]
        return choice[0]

    def building(self, plural=False):
        options = [
            ("Banner", "Banners"),
            ("Bastion", "Bastions"),
            ("Bridge", "Bridges"),
            ("Bulwark", "Bulwarks"),
            ("Cairn", "Cairns"),
            ("Castle", "Castles"),
            ("Citadel", "Citadels"),
            ("Cromlech", "Cromlechs"),
            ("Dolmen", "Dolmens"),
            ("Edifice", "Edifices"),
            ("Facade", "Facades"),
            ("Fastness", "Fastnesses"),
            ("Fortress", "Fortresses"),
            ("Gate", "Gates"),
            ("Henge", "Henges"),
            ("House", "Houses"),
            ("Huaca", "Huacas"),
            ("Kiva", "Kivas"),
            ("Kraal", "Kraals"),
            ("Kwoon", "Kwoon"),
            ("Labyrinth", "Labyrinths"),
            ("Longhouse", "Longhouses"),
            ("Menhir", "Menhirs"),
            ("Monastery", "Monasteries"),
            ("Monolith", "Monoliths"),
            ("Monument", "Monuments"),
            ("Mound", "Mounds"),
            ("Obelisk", "Obelisks"),
            ("Pagoda", "Pagodas"),
            ("Palace", "Palaces"),
            ("Pavillion", "Pavillions"),
            ("Pillar", "Pillars"),
            ("Plaza", "Plazas"),
            ("Prison", "Prisons"),
            ("Pyramid", "Pyramids"),
            ("Redoubt", "Redoubts"),
            ("Refuge", "Refuges"),
            ("Ruin", "Ruins"),
            ("Shrine", "Shrines"),
            ("Spire", "Spires"),
            ("Stele", "Steles"),
            ("Stronghold", "Strongholds"),
            ("Temple", "Temples"),
            ("Terrace", "Terraces"),
            ("Tomb", "Tombs"),
            ("Tower", "Towers"),
            ("Vault", "Vaults"),
            ("Wall", "Walls"),
            ("Wigwam", "Wigwams"),
            ("Yurt", "Yurts"),
            ("Ziggurat", "Ziggurats"),
        ]
        if random.random() < 0.5:
            options.append(("Village", "Village"))
        if random.random() < 0.75:
            options.append(("Catacomb", "Catacombs"))
        if random.random() < 0.5:
            options.append(("Kingdom", "Kingdoms"))
        choice = random.choice(options)
        if plural:
            return choice[1]
        return choice[0]

    def celestial(self, plural=False):
        options = [
            ("Aurora", "Auroras"),
            ("Cloud", "Clouds"),
            ("Comet", "Comets"),
            ("Constellation", "Constellations"),
            ("Dawn", "Dawns"),
            ("Day", "Days"),
            ("Dusk", "Dusks"),
            ("Evening", "Evenings"),
            ("Heavens", "Heavens"),
            ("Moon", "Moons"),
            ("Moonlight", "Moons"),
            (random.choice(["Moonrise", "Moonset"]), "Moonrises"),
            ("Morning", "Mornings"),
            ("Night", "Nights"),
            ("Rainbow", "Rainbows"),
            ("Sky", "Skies"),
            ("Star", "Stars"),
            ("Sun", "Suns"),
            ("Sunlight", "Suns"),
            ("Sunrise", "Sunrises"),
            ("Sunset", "Sunsets"),
        ]
        if random.random() < 0.75:
            options.append(("Meteor", "Meteors"))
        if random.random() < 0.2:
            options.append(("Nova", "Novas"))
        if random.random() < 0.5:
            options.append(("Planet", "Planets"))
        choice = random.choice(options)
        if plural:
            return choice[1]
        return choice[0]

    def color(self):
        options = [
            "Amber",
            "Argent",
            "Ashen",
            "Azure",
            "Black",
            "Blue",
            random.choice(["Brilliant", "Bright"]),
            "Brown",
            "Cerulean",
            "Crimson",
            "Cyan",
            "Dark",
            "Earthen",
            "Ebon",
            "Emerald",
            "Flaxen",
            "Golden",
            "Green",
            "Grey",
            "Indigo",
            random.choice(
                ["Iridescent", "Iridescent", "Pearlescent", "Chatoyant", "Prismatic"]
            ),
            "Magenta",
            "Maroon",
            "Painted",
            random.choice(["Pale", "Pallid"]),
            "Purple",
            "Rainbow",
            "Red",
            "Saffron",
            "Scarlet",
            "Shadowy",
            random.choice(["Shining", "Shimmering", "Glittering"]),
            "Silver",
            "Sooty",
            "Tawny",
            "Teal",
            "Turquoise",
            "Vermillion",
            "Vert",
            "Violet",
            "White",
            "Yellow",
        ]
        if random.random() < 0.5:
            options.append("Beige")
        if random.random() < 0.6:
            options.append("Orange")
        return random.choice(options)

    def condition(self):
        options = [
            "Auspicious",
            "Baleful",
            "Beautiful",
            "Blessed",
            "Blind",
            "Bright",
            "Celestial",
            "Cheerful",
            "Cheerless",
            "Colloquial",
            "Cursed",
            "Diminished",
            "Dire",
            "Empty",
            "Enduring",
            "Excellent",
            "Fair",
            "Festive",
            "Fine",
            random.choice(["Flaming", "Blazing"]),
            "Flawless",
            "Forsaken",
            "Grim",
            "Harmonious",
            "Harsh",
            "Heavenly",
            "Hidden",
            "Icy",
            "Illimitable",
            "Invisible",
            "Keen",
            random.choice(["Little", "Small"]),
            "Lively",
            random.choice(["Loathly", "Loathsome"]),
            "Lost",
            "Lovely",
            random.choice(["Lucky", "Fortunate"]),
            "Mad",
            "Masked",
            "Naked",
            "Noisy",
            "Peaceful",
            "Perfect",
            "Precious",
            "Prosperous",
            "Pure",
            "Quiet",
            "Secret",
            "Serene",
            "Sharpened",
            "Silent",
            random.choice(["Sleeping", "Sleeping", "Sleepy"]),
            "Sour",
            "Splendid",
            "Strange",
            "Subtle",
            "Tall",
            "Towering",
            "Unlamented",
            random.choice(["Unlucky", "Luckless"]),
            "Wan",
            "Whispering",
            "Wild",
        ]
        if random.random() < 0.75:
            options.append("High")
        if random.random() < 0.75:
            options.append("Low")
        if random.random() < 0.75:
            options.append("Weirded")
        if random.random() < 0.75:
            options.append("Young")
        return random.choice(options)

    def emonegative(self):
        return random.choice(
            [
                "Bitter",
                "Blasphemous",
                "Careless",
                "Cautious",
                random.choice(["Cruel", "Cruel", "Malicious"]),
                "Cynical",
                "Deceitful",
                random.choice(["Discordant", "Discordant", "Disharmonious"]),
                "Drunken",
                "Envious",
                "Erring",
                "Foolish",
                "Furious",
                "Grieving",
                "Grievous",
                "Grinning",
                random.choice(
                    ["Hardhearted", "Coldhearted", "Heartless", "Flinthearted"]
                ),
                "Hateful",
                "Hopeless",
                "Hungry",
                "Impecunious",
                "Impious",
                "Impulsive",
                "Indecisive",
                "Irascible",
                "Irritable",
                "Merciless",
                "Mirthless",
                "Naive",
                "Poisonous",
                "Profligate",
                "Questioning",
                "Rancorous",
                "Rebellious",
                "Reluctant",
                "Ravenous",
                "Reckless",
                random.choice(["Relentless", "Unrelenting"]),
                "Restless",
                "Sad",
                "Savage",
                "Sorrowful",
                "Stubborn",
                "Suspicious",
                "Unbending",
                "Uncaring",
                random.choice(["Unfortunate", "Hapless"]),
                "Unrepentant",
                "Unwilling",
                "Vehement",
                random.choice(["Vengeful", "Avenging"]),
                "Venomous",
                "Weary",
                "Weeping",
                "Wicked",
                "Willful",
                "Wrathful",
                "Zealous",
            ]
        )

    def emopositive(self):
        options = [
            "Amicable",
            "Ardorous",
            "Bounteous",
            "Caring",
            "Celibate",
            "Clever",
            random.choice(["Courageous", "Brave"]),
            "Considerate",
            "Courteous",
            "Curious",
            "Decisive",
            "Determined",
            "Dutiful",
            "Eager",
            "Elder",
            "Exultant",
            "Faithful",
            "Fell",
            random.choice(["Ferocious", "Fierce", "Vicious"]),
            "Fortunate",
            "Frugal",
            "Generous",
            "Gentle",
            "Glad",
            "Gracious",
            "Grateful",
            "Hale",
            "Hearty",
            "Honest",
            "Honorable",
            "Hopeful",
            "Humble",
            "Intrepid",
            "Joyous",
            random.choice(["Jubilant", "Jovial"]),
            "Just",
            "Knowing",
            "Laughing",
            "Loving",
            "Loyal",
            "Magnanimous",
            "Meditating",
            "Merciful",
            "Mirthful",
            "Openhanded",
            random.choice(["Openhearted", "Warmhearted"]),
            random.choice(["Persistent", "Perseverant"]),
            "Pious",
            "Principled",
            "Prudent",
            "Resourceful",
            "Resting",
            "Righteous",
            random.choice(["Sagacious", "Sagacious", "Erudite"]),
            "Satiated",
            "Sensuous",
            "Smiling",
            "Stern",
            "Sweet",
            "Temperate",
            "Thoughtful",
            "True",
            "Unbowed",
            "Unhesitant",
            random.choice(["Unstained", "Unstained", "Unstained", "Stainless"]),
            "Valiant",
            "Valorous",
            "Virtuous",
            "Well-Spoken",
            "Wise",
            random.choice(["Witty", "Sharp-Witted"]),
        ]
        if random.random() < 0.75:
            options.append(random.choice(["Beneficent", "Benevolent"]))
        if random.random() < 0.75:
            options.append("Compassionate")
        if random.random() < 0.75:
            options.append("Understanding")
        return random.choice(options)

    def transitive(self):
        return random.choice(
            [
                "Adoring",
                "Anticipating",
                "Awaiting",
                "Bearing",
                "Breaking",
                "Cleaving",
                "Consuming",
                "Crushing",
                "Defending",
                "Defiling",
                "Destroying",
                "Devouring",
                "Embracing",
                "Esteeming",
                "Forging",
                "Glorifying",
                "Guarding",
                "Holding",
                "Honoring",
                "Kissing",
                "Loathing",
                "Loving",
                "Piercing",
                "Pondering",
                "Praising",
                "Protecting",
                "Raising",
                "Rectifying",
                "Scorning",
                "Sealing",
                "Seeking",
                "Smashing",
                "Smiting",
                "Stealing",
                "Sundering",
                "Tearing",
                "Treasuring",
                "Upholding",
                "Warding",
                "Watching",
                "Worshipping",
            ]
        )

    def heroic(self):
        return random.choice(
            [
                "Battleworn",
                "Brazen",
                random.choice(["Dreadful", "Terrible"]),
                "Foremost",
                "Glorious",
                "Great",
                random.choice(["Honored", "Lauded"]),
                "Imperious",
                "Incomparable",
                "Invincible",
                "Marvellous",
                "Mighty",
                "Noble",
                "Peerless",
                "Proud",
                "Regal",
                "Stalwart",
                "Strong",
                random.choice(["Triumphal", "Triumphant"]),
                random.choice(["Unconquered", "Unconquerable"]),
                random.choice(["Undaunted", "Dauntless"]),
                "Undefeated",
                "Victorious",
            ]
        )

    def item(self, plural=False):
        options = [
            ("Armor", "Mail"),
            ("Arrow", "Arrows"),
            ("Axe", "Axes"),
            ("Bell", "Bells"),
            ("Blade", "Blades"),
            (random.choice(["Boat", "Canoe"]), "Boats"),
            ("Candle", "Candles"),
            ("Chain", "Chains"),
            ("Cloak", "Cloaks"),
            ("Coin", "Coins"),
            ("Collar", "Collars"),
            ("Drum", "Drums"),
            ("Falchion", "Falchion"),
            ("Fist", "Fists"),
            ("Flute", "Flutes"),
            (random.choice(["Garland", "Chaplet"]), "Garlands"),
            ("Gauntlet", "Gauntlets"),
            ("Goblet", "Goblets"),
            ("Gong", "Gongs"),
            ("Hammer", "Hammers"),
            ("Harp", "Harps"),
            ("Helm", "Helms"),
            ("Horn", "Horns"),
            ("Jewel", "Jewels"),
            ("Knife", "Knives"),
            ("Light", "Lights"),
            ("Lute", "Lutes"),
            ("Mask", "Masks"),
            ("Net", "Nets"),
            ("Pendant", "Pendants"),
            ("Parliament", "Parliaments"),
            ("Puppet", "Puppets"),
            ("Quill", "Quills"),
            ("Quiver", "Quiver"),
            ("Ring", "Rings"),
            ("Robe", "Robes"),
            ("Rope", "Ropes"),
            (random.choice(["Shackle", "Manacle"]), "Shackles"),
            ("Shell", "Shells"),
            ("Shield", "Shields"),
            ("Ship", "Ships"),
            ("Spear", "Spears"),
            ("Staff", "Staves"),
            (random.choice(["Sword", "Dagger"]), "Swords"),
            ("Talisman", "Talismans"),
            ("Veil", "Veils"),
            ("Wheel", "Wheels"),
            ("Zither", "Zithers"),
        ]
        if random.random() < 0.6:
            options.append(("Basket", "Baskets"))
        if random.random() < 0.6:
            options.append(("Bowl", "Bowls"))
        if random.random() < 0.75:
            options.append(("Canopy", "Canopies"))
        if random.random() < 0.75:
            options.append(("Cloth", "Cloths"))
        if random.random() < 0.6:
            options.append(("Cup", "Cups"))
        if random.random() < 0.75:
            options.append(("Gem", "Gems"))
        if random.random() < 0.6:
            options.append(("Hourglass", "Hourglasses"))
        if random.random() < 0.75:
            options.append(("Instrument", "Instruments"))
        if random.random() < 0.25:
            options.append((random.choice(["Scroll", "Book"]), "Scrolls"))
        if random.random() < 0.75:
            options.append(("Seat", "Seats"))
        if random.random() < 0.6:
            options.append(("Vessel", "Vessels"))
        choice = random.choice(options)
        if plural:
            return choice[1]
        return choice[0]

    def location(self, plural=False):
        options = [
            ("Archipelago", "Archipelago"),
            ("Cavern", "Caverns"),
            ("Chase", "Chases"),
            (random.choice(["City", "Town", "Village"]), "Cities"),
            ("Coast", "Coasts"),
            ("Copse", "Copses"),
            ("Crossroads", "Crossroads"),
            ("Dell", "Dell"),
            ("Delta", "Delta"),
            (random.choice(["Depths", "Depths", "Deep"]), "Deeps"),
            ("Desert", "Deserts"),
            ("East", "East"),
            (random.choice(["Erg", "Graben"]), "Ergs"),
            ("Forest", "Forests"),
            (random.choice(["Grove", "Grove", "Copse", "Glade"]), "Groves"),
            ("Harbor", "Harbors"),
            ("Hills", "Hills"),
            (random.choice(["Islands", "Isles", "Isle"]), "Isles"),
            ("Marches", "Marches"),
            ("Marsh", "Marshes"),
            ("Meadow", "Meadows"),
            ("Mesa", "Mesas"),
            (
                random.choice(
                    ["Mountains", "Mountain", "Mountain", "Mountain", "Omphalos"]
                ),
                "Mountains",
            ),
            ("North", "North"),
            ("Northeast", "Northeast"),
            ("Northwest", "Northwest"),
            ("Plain", "Plains"),
            ("Plateau", "Plateaus"),
            ("River", "Rivers"),
            ("Road", "Roads"),
            ("Savannah", "Savannahs"),
            (random.choice(["Seas", "Sea", "Sea", "Ocean"]), "Seas"),
            ("Season", "Seasons"),
            (random.choice(["Shore", "Prairie"]), "Shores"),
            ("Steppe", "Steppes"),
            ("South", "South"),
            ("Southeast", "Southeast"),
            ("Southwest", "Southwest"),
            (random.choice(["Swamp", "Bayou"]), "Swamps"),
            ("Taiga", "Taigas"),
            ("Tundra", "Tundras"),
            ("Valley", "Valleys"),
            ("Wasteland", "Wastes"),
            ("Waves", "Waves"),
            ("West", "West"),
            ("Wold", "Wolds"),
            (random.choice(["Woodland", "Woods"]), "Woods"),
        ]

        if random.random() < 0.5:
            options.append((random.choice(["Bog", "Fen", "Muskeg"]), "Bogs"))
        if random.random() < 0.75:
            options.append(("Bosque", "Bosques"))
        if random.random() < 0.7:
            options.append(("Canyon", "Canyons"))
        if random.random() < 0.8:
            options.append(("Heavens", "Heavens"))
        if random.random() < 0.6:
            options.append(("Karst", "Karst"))
        if random.random() < 0.6:
            options.append(("Land", "Lands"))
        if random.random() < 0.8:
            options.append(("Underworld", "Shadowlands"))
        choice = random.choice(options)
        if plural:
            return choice[1]
        return choice[0]

    def mineral(self):
        options = [
            "Agate",
            "Amethyst",
            "Basalt",
            "Bloodstone",
            "Brass",
            "Bronze",
            "Calcite",
            "Chalcedony",
            "Clay",
            "Coral",
            "Copper",
            "Crystal",
            "Flint",
            "Granite",
            "Hematite",
            "Iron",
            "Jasper",
            "Metal",
            "Obsidian",
            "Onyx",
            "Ore",
            "Pumice",
            "Pyrite",
            "Quartz",
            "Rust",
            "Sandstone",
            "Salt",
            "Stone",
            "Tigereye",
            "Tin",
            "Turquoise",
            "Verdigris",
        ]
        if random.random() < 0.7:
            options.append("Glass")
        if random.random() < 0.6:
            options.append("Steel")
        return random.choice(options)

    def movement(self):
        return random.choice(
            [
                "Ascending",
                "Darting",
                "Descending",
                "Falling",
                "Faring",
                "Flickering",
                "Flowing",
                "Fluttering",
                "Leaping",
                "Plummeting",
                "Questing",
                "Racing",
                "Rapid",
                "Rising",
                "Roaming",
                "Running",
                "Soaring",
                "Standing",
                "Still",
                "Striding",
                "Swift",
                "Swimming",
                "Unfettered",
                "Wandering",
            ]
        )

    def natural(self):
        options = [self.nature(), self.nature()]
        if random.random() < 0.5:
            options.append(self.tree())
        return random.choice(options)

    def naturalplural(self):
        options = [self.nature(plural=True), self.nature(plural=True)]
        if random.random() < 0.25:
            options.append(self.tree(plural=True))
        return random.choice(options)

    def nature(self, plural=False):
        options = [
            ("Arroyo", "Arroyos"),
            ("Blossom", "Blossoms"),
            (
                self.tree() + " " + random.choice(["Blossom", "Flower", "Nectar"]),
                "Blossoms",
            ),
            ("Boulder", "Boulders"),
            ("Breeze", "Breezes"),
            ("Brook", "Brooks"),
            ("Caldera", "Calderas"),
            ("Canyon", "Canyons"),
            ("Cavern", "Caverns"),
            ("Cliff", "Cliffs"),
            ("Crag", "Crags"),
            ("Creek", "Creeks"),
            ("Dawn", "Dawns"),
            ("Dew", "Dewdrops"),
            ("Dune", "Dunes"),
            ("Erg", "Ergs"),
            ("Ember", "Embers"),
            ("Fern", "Ferns"),
            (random.choice(["Fire", "Flame"]), "Flames"),
            ("Flower", "Flowers"),
            ("Fog", "Clouds"),
            ("Forest", "Forests"),
            ("Garden", "Gardens"),
            ("Glacier", "Glaciers"),
            ("Grain", "Grains"),
            ("Grass", "Grasses"),
            ("Hill", "Hills"),
            ("Horizon", "Horizons"),
            ("Ice", "Icicles"),
            ("Isle", "Islands"),
            (random.choice(["Kelp", "Seawrack"]), "Kelps"),
            ("Leaf", "Leaves"),
            ("Lightning", "Thunderbolts"),
            ("Lily", "Lilies"),
            ("Lotus", "Lotuses"),
            ("Mangrove", "Mangroves"),
            (random.choice(["Meadow", "Field"]), "Meadows"),
            ("Midnight", "Nights"),
            ("Mist", "Mists"),
            ("Monsoon", "Monsoons"),
            ("Mountain", "Mountains"),
            ("Moss", "Mosses"),
            ("Mushroom", "Mushrooms"),
            ("Orchard", "Orchards"),
            ("Orchid", "Orchids"),
            ("Paradise", "Paradises"),
            ("Petal", "Petals"),
            (random.choice(["Pollen", "Honey"]), "Fruits"),
            ("Prairie", "Prairies"),
            ("Rain", "Rains"),
            ("Ravine", "Ravines"),
            ("Reed", "Reeds"),
            ("River", "Rivers"),
            ("Rose", "Roses"),
            (random.choice(["Sea", "Ocean"]), "Seas"),
            (random.choice(["Sky", "Sky", "Skies"]), "Skies"),
            ("Smoke", "Fires"),
            ("Snow", "Snows"),
            ("Song", "Songs"),
            ("Spring", "Springs"),
            ("Stone", "Stones"),
            ("Storm", "Storms"),
            ("Stream", "Streams"),
            ("Tarn", "Tarns"),
            ("Tempest", "Tempests"),
            ("Thunder", "Thunders"),
            ("Tide", "Tides"),
            ("Tor", "Tors"),
            ("Tsunami", "Tsunamis"),
            ("Tussock", "Tussocks"),
            ("Typhoon", "Typhoons"),
            ("Volcano", "Volcanoes"),
            ("Water", "Waters"),
            ("Waterfall", "Waterfalls"),
            ("Wave", "Waves"),
            ("Wind", "Winds"),
            ("Wood", "Woods"),
            ("Zephyr", "Zephyrs"),
        ]
        choice = random.choice(options)
        if plural:
            return choice[1]
        return choice[0]

    def number(self):
        options = [
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            random.choice(["Twelve", "One Dozen"]),
            "Fifteen",
            random.choice(["Twenty", "One Score"]),
            "Many",
        ]
        if random.random() < 0.9:
            options.append("One Hundred")
        if random.random() < 0.6:
            options.append("One Thousand")
        if random.random() < 0.25:
            options.append("Ten Thousand")
        return random.choice(options)

    def ordinal(self):
        options = [
            "First",
            "Second",
            "Third",
            "Fourth",
            "Fifth",
            "Sixth",
            "Seventh",
            "Eighth",
            "Ninth",
            "Tenth",
            "Twentieth",
            "Final",
            "Last",
        ]
        if random.random() < 0.9:
            options.append("Eleventh")
        if random.random() < 0.9:
            options.append("Twelfth")
        if random.random() < 0.6:
            options.append("Thirteenth")
        if random.random() < 0.9:
            options.append("One-Hundredth")
        if random.random() < 0.6:
            options.append("One-Thousandth")
        if random.random() < 0.25:
            options.append("Ten-Thousandth")
        if random.random() < 0.5:
            options.append("Number One")
        if random.random() < 0.25:
            options.append("Number Ten")
        return random.choice(options)

    def person(self):
        return random.choice(
            [
                "Architect",
                "Artisan",
                "Assassin",
                "Boatswain",
                "Bodhisattva",
                "Builder",
                "Bureaucrat",
                "Carpenter",
                "Champion",
                "Chandler",
                "Chanter",
                "Cobbler",
                "Conquerer",
                "Corsair",
                "Counselor",
                "Dancer",
                "Executioner",
                "Farmer",
                "Fisher",
                "Gardener",
                "Guardian",
                "Guru",
                "Hero",
                random.choice(["Rider", "Rider", "Horseman", "Horsewoman"]),
                "Hunter",
                "Killer",
                "Knight",
                random.choice(["Lady", "Lord"]),
                "Lover",
                random.choice(["Maiden", "Master"]),
                "Mason",
                "Messenger",
                "Monk",
                "Musician",
                "Nomad",
                "Potter",
                "Priest",
                random.choice(["Prince", "Princess"]),
                "Rishi",
                "Runner",
                "Sage",
                "Sailor",
                "Savant",
                "Scholar",
                "Scribe",
                "Shaman",
                "Shepherd",
                "Shipwright",
                "Sifu",
                "Singer",
                "Smith",
                "Soldier",
                "Tailor",
                "Tanner",
                "Tyrant",
                "Veteran",
                "Wainwright",
                "Warrior",
                "Weaver",
                "Wheelwright",
                "Youth",
            ]
        )

    def precious(self):
        options = [
            "Alabaster",
            random.choice(["Amber", "Amber", "Copal"]),
            "Aquamarine",
            "Azurite",
            "Beryl",
            "Carnelian",
            "Chrysoberyl",
            "Chrysocolla",
            "Citrine",
            "Coral",
            "Diamond",
            "Diorite",
            "Emerald",
            "Garnet",
            "Gemstone",
            "Glass",
            "Gold",
            "Ivory",
            "Jadesteel",
            "Jet",
            "Jewel",
            "Lapis",
            "Malachite",
            "Marble",
            "Nephrite",
            "Opal",
            random.choice(["Pearl", "Pearl", "Pearl", "Nacre"]),
            "Peridot",
            "Platinum",
            "Pyrope",
            "Rhodochrosite",
            "Ruby",
            "Sapphire",
            "Silver",
            "Spinel",
            "Steel",
            "Sunstone",
            "Topaz",
            "Tourmaline",
            "Zircon",
        ]
        if random.random() < 0.3:
            options.append("Adamant")
        if random.random() < 0.75:
            options.append("Feathersteel")
        if random.random() < 0.75:
            options.append("Firesteel")
        if random.random() < 0.1:
            options.append("Gossamer")
        if random.random() < 0.75:
            options.append("Jade")
        if random.random() < 0.5:
            options.append("Moonsilver")
        if random.random() < 0.75:
            options.append("Moonstone")
        if random.random() < 0.5:
            options.append("Orichalcum")
        if random.random() < 0.3:
            options.append("Soulsteel")
        if random.random() < 0.3:
            options.append("Starmetal")
        if random.random() < 0.75:
            options.append("Tumbaga")
        return random.choice(options)

    def relation(self):
        options = [
            "Acolyte",
            "Ally",
            "Brother",
            "Child",
            "Chumyo",
            "Client",
            "Daimyo",
            "Daughter",
            "Disciple",
            "Exarch",
            "Father",
            "Lady",
            "Liege",
            "Lord",
            "Master",
            "Mother",
            "Patron",
            random.choice(["Scion", "Heir"]),
            "Serf",
            "Servant",
            "Sifu",
            "Sister",
            random.choice(["Slave", "Thrall"]),
            "Son",
            "Squire",
            "Student",
            "Vassal",
        ]
        if random.random() < 0.5:
            options.append("Odalisque")
        return random.choice(options)

    def title(self):
        return random.choice(
            [
                "Admiral",
                random.choice(["Baron", "Baroness"]),
                random.choice(["Brother", "Sister"]),
                "Caliph",
                "Captain",
                random.choice(
                    [
                        "Chumyo",
                        "Chuzei",
                        "Haizei",
                        "Kazei",
                        "Sazei",
                        "Shozei",
                        "Sochei",
                        "Taimyo",
                        "Taizei",
                    ]
                ),
                "Commander",
                "Daimyo",
                random.choice(["Duke", "Duchess"]),
                "Elder",
                random.choice(["Fanglord", "Scalelord", "Talonlord", "Winglord"]),
                random.choice(["Father", "Mother"]),
                "General",
                "Guru",
                "Lady",
                "Lieutenant",
                "Lord",
                "Magistrate",
                "Master",
                random.choice(["Prince", "Princess"]),
                "Rishi",
                "Sifu",
                "Sultan",
                random.choice(["Warlord", "Warlady"]),
            ]
        )

    def tree(self, plural=False):
        options = [
            ("Acacia", "Acacias"),
            ("Ailanthus", "Ailanthus-trees"),
            ("Alder", "Alders"),
            ("Almond", "Almond-trees"),
            ("Apple", "Apple-trees"),
            ("Ashoka", "Ashoka-trees"),
            (random.choice(["Poplar", "Aspen"]), "Poplars"),
            ("Balsa", "Balsas"),
            ("Bamboo", "Bamboo"),
            ("Banyan", "Banyans"),
            ("Baobob", "Baobobs"),
            ("Beech", "Beeches"),
            ("Birch", "Birches"),
            ("Buckeye", "Buckeyes"),
            (random.choice(["Cactus", "Saguaro"]), "Cacti"),
            ("Cashew", "Cashew-trees"),
            ("Cassia", "Cassias"),
            ("Catalpa", "Catalpas"),
            ("Cedar", "Cedars"),
            ("Ceiba", "Ceibas"),
            ("Cherry", "Cherry-trees"),
            ("Chestnut", "Chestnut-trees"),
            ("Citron", "Citron-trees"),
            ("Coffee-tree", "Coffee-trees"),
            ("Cycad", "Cycads"),
            ("Cypress", "Cypresses"),
            ("Ebony", "Ebonies"),
            ("Elm", "Elms"),
            ("Fig", "Fig-trees"),
            ("Fir", "Firs"),
            ("Ginkgo", "Ginkgos"),
            ("Guava", "Guava-trees"),
            ("Gum-tree", "Gum-trees"),
            ("Henna", "Henna-trees"),
            ("Hickory", "Hickories"),
            ("Holly", "Hollies"),
            ("Hornbeam", "Hornbeams"),
            ("Iroko", "Iroko-trees"),
            ("Ironwood", "Ironwoods"),
            ("Jacaranda", "Jacarandas"),
            ("Jasmine", "Jasmines"),
            ("Jujube", "Jujube-trees"),
            ("Kapok", "Kapoks"),
            ("Kauri", "Kauri-pines"),
            ("Kigelia", "Kigelia-trees"),
            ("Laburnum", "Laburnums"),
            ("Lancewood", "Lancewoods"),
            ("Laurel", "Laurels"),
            ("Lilac", "Lilacs"),
            ("Linden", "Lindens"),
            ("Locust", "Locust-trees"),
            ("Lychee", "Lychee-trees"),
            ("Magnolia", "Magnolias"),
            ("Mahogany", "Mahoganies"),
            ("Mango", "Mango-trees"),
            ("Mangosteen", "Mangosteens"),
            ("Mangrove", "Mangroves"),
            ("Manilkara", "Manilkara-trees"),
            ("Maple", "Maples"),
            ("Marula", "Marula-trees"),
            ("Medlar", "Medlar-trees"),
            ("Mesquite", "Mesquites"),
            ("Milkwood", "Milkwoods"),
            ("Mimosa", "Mimosas"),
            ("Moringa", "Moringas"),
            ("Myrtle", "Myrtles"),
            ("Neem", "Neem-trees"),
            ("Oak", "Oaks"),
            ("Oleaster", "Oleasters"),
            ("Olive", "Olive-trees"),
            ("Palm", "Palms"),
            ("Palmetto", "Palmettos"),
            ("Palmyra", "Palmyra-trees"),
            ("Pandan", "Pandan-trees"),
            ("Papaya", "Papaya-trees"),
            ("Paperbark", "Paperbarks"),
            ("Peach", "Peach-trees"),
            ("Persea", "Persea-trees"),
            ("Pine", "Pines"),
            ("Plum", "Plum-trees"),
            ("Plumyew", "Plumyews"),
            ("Podocarp", "Podocarp-pines"),
            ("Quandong", "Quandong-trees"),
            ("Rambutan", "Rambutan-trees"),
            ("Redwood", "Redwoods"),
            ("Rose", "Roses"),
            ("Rosewood", "Rosewoods"),
            (random.choice(["Rowan", "Whitebeam"]), "Rowans"),
            ("Sakaki", "Sakaki-trees"),
            ("Sandalwood", "Sandalwoods"),
            ("Shea", "Shea-trees"),
            ("Siris", "Siris-trees"),
            ("Soursop", "Soursop-trees"),
            ("Spruce", "Spruces"),
            ("Sumac", "Sumacs"),
            ("Sycamore", "Sycamores"),
            (random.choice(["Tamarack", "Larch"]), "Larches"),
            ("Tamarind", "Tamarind-trees"),
            ("Tamarisk", "Tamarisks"),
            ("Tea-tree", "Tea-trees"),
            ("Teak", "Teaks"),
            ("Thorn", "Thorn-trees"),
            ("Totara", "Totaras"),
            ("Tupelo", "Tupelos"),
            ("Wattle", "Wattle-trees"),
            ("Willow", "Willows"),
            ("Yellowwood", "Yellowwoods"),
            ("Yew", "Yews"),
        ]
        if random.random() < 0.75:
            options.append(("Flame-tree", "Flame-trees"))
        choice = random.choice(options)
        if plural:
            return choice[1]
        return choice[0]

    def adjective(self):
        return random.choice(
            [
                self.color(),
                self.condition(),
                self.emonegative(),
                self.emopositive(),
                self.heroic(),
                self.mineral(),
                self.nature(),
                self.movement(),
                self.precious(),
            ]
        )

    def noun(self):
        options = [
            random.choice([self.absnegative(), self.abspositive()]),
            self.anatomy(),
            self.animal(),
            self.building(),
            self.celestial(),
            self.item(),
            self.mineral(),
            self.natural(),
            self.precious(),
        ]
        if random.random() < 0.75:
            options.append(self.relation())
        return random.choice(options)

    def nounbasic(self):
        options = [
            self.animal(),
            self.celestial(),
            self.mineral(),
            self.natural(),
        ]
        if random.random() < 0.6:
            options.append(random.choice([self.absnegative(), self.abspositive()]))
        if random.random() < 0.5:
            options.append(self.anatomy())
        if random.random() < 0.75:
            options.append(self.item())
        if random.random() < 0.75:
            options.append(self.precious())
        return random.choice(options)

    def nounnumber(self):
        options = [
            random.choice(
                [self.absnegative(plural=True), self.abspositive(plural=True)]
            ),
            self.animal(plural=True),
            self.building(plural=True),
            self.celestial(plural=True),
            self.item(plural=True),
            self.naturalplural(),
        ]
        if random.random() < 0.75:
            options.append(self.anatomy(plural=True))
        return random.choice(options)

    def conjunctive(self):
        return random.choice(
            [
                f"{self.animal()} and {self.celestial()} {random.choice([self.person(), self.relation()])}",
                f"{random.choice([self.absnegative(), self.abspositive()])} and {self.mineral()} {self.person()}",
                f"{self.anatomy()} of the {random.choice([self.animal(), self.animal(), self.animal(), self.animal(plural=True)])} and the {random.choice([self.location(), self.location(), self.location(), self.location(plural=True)])}",
                f"{self.precious()} and {self.mineral()} {random.choice([self.person(), self.relation()])}",
                f"{self.relation()} of "
                + random.choice(
                    [
                        f"{self.mineral()} and {self.precious()}",
                        f"{self.precious()} and {self.mineral()}",
                    ]
                ),
                f"{self.condition()} {random.choice([self.absnegative(), self.abspositive()])} and {self.natural()} {self.anatomy()} {self.person()}",
                f"{random.choice([self.absnegative(), self.abspositive()])} of the {random.choice([self.location(), self.location(), self.location(), self.location(plural=True)])}",
                f"{random.choice([self.animal(), self.item()])} of the "
                + random.choice(
                    [
                        self.celestial(),
                        random.choice(
                            [
                                self.location(),
                                self.location(),
                                self.location(),
                                self.location(plural=True),
                            ]
                        ),
                    ]
                ),
            ]
        )

    def misc(self):
        options = [
            f"{random.choice([self.emopositive(), self.emopositive(), self.emopositive(), self.condition()])} {self.item()}-{self.transitive()} {random.choice([self.person(), self.relation()])}",
            f"{self.item()}-{self.transitive()} {self.precious()} {random.choice([self.person(), self.relation()])}",
            f"{self.adjective()} {random.choice([self.relation(), self.relation(), self.person(), self.title()])} of {random.choice([self.absnegative(), self.abspositive()])}",
            f"{random.choice([self.animal(), self.celestial(), self.natural(), self.mineral()])} the {self.adjective()}",
        ]
        s = self.title()
        s += " "
        s += random.choice(
            [
                random.choice(
                    [
                        self.animal(),
                        self.animal(),
                        self.natural(),
                        self.natural(),
                        self.mineral(),
                        self.precious(),
                        self.celestial(),
                        self.item(),
                    ]
                ),
                f"{self.adjective()} {self.nounbasic()}",
                f"{self.adjective()} {self.nounbasic()}",
            ]
        )
        options.append(s)
        if random.random() < 0.9:
            s = f"{self.heroic()} {self.precious()} {self.animal()} {self.relation()} of the {self.condition()} {random.choice([self.location(), self.location(), self.location(), self.location(plural=True)])}"
            options.append(s)
        return random.choice(options)

    def numbered(self):
        options = [
            f"{self.number()} {self.nounnumber()}",
            f"{self.number()} {self.nounnumber()}",
            f"{self.number()} {self.adjective()} {self.nounnumber()}",
            f"The {self.ordinal()} {self.person()} of the {self.celestial()}",
            f"The {self.ordinal()} {self.person()}",
        ]
        if random.random() < 0.9:
            options.append(
                f"{random.choice([self.emopositive(), self.emopositive(), self.emopositive(), self.condition()])} {self.ordinal()} {self.relation()} of the {random.choice([self.location(), self.location(), self.location(), self.location(plural=True)])}"
            )
        return random.choice(options)

    def prompt(self):
        options = [
            random.choice(
                [
                    self.animal(),
                    self.animal(),
                    self.natural(),
                    self.natural(),
                    self.mineral(),
                    self.precious(),
                    self.celestial(),
                    self.item(),
                ]
            ),
            f"{self.adjective()} {self.nounbasic()}",
            f"{self.adjective()} {self.nounbasic()}",
            f"{self.adjective()} {self.nounbasic()}",
            f"{random.choice([self.natural(), self.celestial(), self.mineral(), self.item(), random.choice([self.absnegative(), self.abspositive()])])}-{self.transitive()} {self.person()}",
            f"{self.adjective()} {self.noun()} {random.choice([self.relation(), self.relation(), self.person(), self.person(), self.person(), self.animal()])}",
            self.numbered(),
        ]
        if random.random() < 0.9:
            options.append(self.conjunctive())
        if random.random() < 0.6:
            options.append(
                f"{self.nounbasic()} {random.choice([self.celestial(), self.item(), self.natural(), self.anatomy()])} {self.person()}"
            )
        if random.random() < 0.6:
            s = random.choice(
                [
                    self.emopositive(),
                    self.emonegative(),
                    self.heroic(),
                    self.heroic(),
                    self.color(),
                    self.condition(),
                ]
            )
            s += " "
            s += random.choice(
                [
                    f"{random.choice([self.precious(), self.mineral()])} {random.choice([self.item(), self.item(), self.natural(), self.anatomy(), self.animal()])}",
                    f"{self.animal()} {self.anatomy()}",
                ]
            )
            s += " "
            s += random.choice(
                [self.person(), self.person(), self.person(), self.relation()]
            )
            options.append(s)
        if random.random() < 0.6:
            options.append(
                f"{random.choice([self.color(), self.precious()])} {random.choice([self.anatomy(), self.person()])} of the {random.choice([self.celestial(), self.natural(), self.animal(), self.celestial(plural=True), self.naturalplural(), self.animal(plural=True)])}"
            )
        if random.random() < 0.6:
            s = random.choice(
                [self.animal(), self.person(), self.relation(), self.relation()]
            )
            s += " of the "
            s += random.choice(
                [
                    f"{random.choice([self.celestial(), self.heroic(), self.color(), self.condition()])} {random.choice([self.building(), self.anatomy(), self.location()])}",
                    f"{random.choice([self.emopositive(), self.emonegative(), self.color(), self.condition()])} {random.choice([self.celestial(), self.celestial(), self.anatomy()])}",
                ]
            )
            options.append(s)
        if random.random() < 0.25:
            options.append(
                f"{random.choice([self.heroic(), self.movement()])} {random.choice([self.animal(), self.item()])} of the {random.choice([self.emonegative(), self.emopositive(), self.condition()])} {random.choice([random.choice([self.building(), self.building(), self.building(), self.building(plural=True)]), random.choice([self.location(), self.location(), self.location(), self.location(plural=True)]), self.natural()])}"
            )
        if random.random() < 0.25:
            options.append(self.misc())
        return random.choice(options)


class DragonKingName(RandomName):
    """
    Based on Dragon King Name Generator: https://orteil.dashnet.org/randomgen/?gen=LwePLTEY
    """

    def first(self):
        return random.choice(
            [
                "A",
                "A",
                "E",
                "O",
                "Ch" + self.vv(),
                "H" + self.vv(),
                "Hl" + self.vv(),
                "Hr" + self.vv(),
                "K" + self.vv(),
                "Khr" + self.vv(),
                "Kl" + self.vv(),
                "R" + self.vv(),
                "R" + self.vv(),
                "R" + self.vv(),
                "R" + self.vv(),
                "Sc" + self.vv(),
                "Sh" + self.vv(),
                "Ss" + self.vv(),
                "Th" + self.vv(),
                "V" + self.vv(),
            ]
        )

    def second(self):
        options = [
            "j",
            "l",
            "l",
            "m",
            "nth",
            "r",
            "th",
            "th",
        ]
        self.random_add(options, "d", 0.5)
        self.random_add(options, "k", 0.5)
        self.random_add(options, "km", 0.5)
        self.random_add(options, "lch", 0.5)
        self.random_add(options, "n", 0.5)
        self.random_add(options, "nz", 0.5)
        self.random_add(options, "r", 0.5)
        self.random_add(options, "s", 0.5)
        self.random_add(options, "ssh", 0.5)
        self.random_add(options, "t", 0.5)
        self.random_add(options, "x", 0.5)
        self.random_add(options, "y", 0.5)
        self.random_add(options, "zth", 0.5)
        return random.choice(options)

    def vv(self):
        options = [
            "a",
            "a",
            "a",
            "e",
            "e",
            "i",
            "o",
        ]
        self.random_add(options, "aa", 0.6)
        self.random_add(options, "ai", 0.2)
        self.random_add(options, "e", 0.2)
        self.random_add(options, "i", 0.6)
        self.random_add(options, "o", 0.2)
        self.random_add(options, "u", 0.2)
        self.random_add(options, "ya", 0.3)
        return random.choice(options)

    def endcons(self):
        options = [
            "k",
            "k",
            "k",
            "k",
            "n",
            "r",
            "s",
            "ss",
            "th",
        ]
        self.random_add(options, "d", 0.5)
        self.random_add(options, "k", 0.5)
        self.random_add(options, "l", 0.5)
        self.random_add(options, "s", 0.5)
        return random.choice(options)

    def endvow(self):
        return random.choice(["a", "a", "a", "é", "i", "u",])

    def name(self):
        options = [
            f"{self.first()}{self.second()}{self.vv()}{self.endcons()}",
            f"{self.first()}{self.second()}{self.vv()}{self.second()}{self.vv()}{self.endcons()}",
        ]
        self.random_add(options, f"{self.first()}{self.endcons()}", 0.46)
        self.random_add(options, f"{self.first()}{self.second()}{self.endcons()}", 0.27)
        self.random_add(
            options,
            f"{self.first()}{self.second()}{self.vv()}{self.second()}{self.endcons()}",
            0.27,
        )

    def prompt(self):
        options = [self.name()]
        self.random_add(options, f"{self.name()}'{self.name()}", 0.04)
        return random.choice(options)


class InfernalName(RandomName):
    """
    Based on Infernal Name Harmony Test: https://orteil.dashnet.org/randomgen/?gen=EcFUJXMw
    """


class OldRealmName(RandomName):
    """
    Based on Old Realm Name Generator: https://orteil.dashnet.org/randomgen/?gen=FaifGb1M    
    """


class ScarletDynastyName(RandomName):
    """
    Based on Scarley Dynasty Name Generator: https://orteil.dashnet.org/randomgen/?gen=AYsfB34A
    """


def dynast_name():
    first_syllable_options = [
        "A",
        "A",
        "A",
        "A",
        "A",
        "A",
        "A",
        "A",
        "An'",
        "Ba",
        "Ba",
        "Ba",
        "Bae",
        "Be",
        "Be",
        "Be",
        "Bha",
        "Bhu",
        "Bi",
        "Bo",
        "Bu",
        "Ca",
        "Ca",
        "Ca",
        "Ca",
        "Ca",
        "Cai",
        "Ce",
        "Cha",
        "Che",
        "Che",
        "Chi",
        "Chi",
        "Cho",
        "Chu",
        "Co",
        "Cu",
        "Cy",
        "Da",
        "Da",
        "Da",
        "De",
        "De",
        "De",
        "De",
        "Di",
        "Do",
        "Dro",
        "Du",
        "E",
        "E",
        "E",
        "E",
        "E",
        "Fa",
        "Fe",
        "Fe",
        "Fe",
        "Fi",
        "Fo",
        "Fu",
        "Ga",
        "Ga",
        "Ge",
        "Gi",
        "Go",
        "Gu",
        "Ha",
        "Ha",
        "He",
        "Hi",
        "Ho",
        "How",
        "Hu",
        "I",
        "I",
        "I",
        "I",
        "Ja",
        "Ja",
        "Je",
        "Jo",
        "Ka",
        "Ka",
        "Kai",
        "Ke",
        "Ke",
        "Ke",
        "Ki",
        "Ko",
        "Ku",
        "La",
        "La",
        "Le",
        "Le",
        "Li",
        "Lo",
        "Lo",
        "Lu",
        "Ma",
        "Ma",
        "Ma",
        "Ma",
        "Ma",
        "Ma",
        "Ma",
        "Ma",
        "Me",
        "Me",
        "Mi",
        "Mi",
        "Mne",
        "Mo",
        "Moi",
        "Mu",
        "My",
        "Na",
        "Na",
        "Na",
        "Ne",
        "Ne",
        "Ne",
        "Ni",
        "No",
        "No",
        "Nu",
        "O",
        "O",
        "O",
        "Pa",
        "Pe",
        "Pi",
        "Po",
        "Po",
        "Pu",
        "R'",
        "Ra",
        "Ra",
        "Ra",
        "Re",
        "Ri",
        "Ro",
        "Ro",
        "Ru",
        "Sa",
        "Sa",
        "Sa",
        "Se",
        "Se",
        "Shu",
        "Si",
        "Si",
        "So",
        "So",
        "Su",
        "Sza",
        "Ta",
        "Ta",
        "Ta",
        "Ta",
        "Tai",
        "Te",
        "Ti",
        "Ti",
        "To",
        "Tu",
        "Ty",
        "U",
        "U",
        "U",
        "V'",
        "Va",
        "Ve",
        "Ve",
        "Vo",
        "Wa",
        "We",
        "Wi",
        "Wo",
        "Wu",
        "Ya",
        "Ye",
        "Yi",
        "Yo",
        "Yu",
    ]

    mid_syllable_options = [
        "ba",
        "ba",
        "ba",
        "be",
        "bi",
        "bo",
        "bu",
        "cha",
        "che",
        "che",
        "chi",
        "cho",
        "chu",
        "da",
        "da",
        "de",
        "di",
        "di",
        "do",
        "du",
        "fa",
        "fa",
        "fe",
        "fi",
        "fo",
        "fu",
        "ga",
        "ga",
        "ga",
        "ga",
        "ge",
        "ge",
        "gi",
        "gne",
        "go",
        "gu",
        "gu",
        "gwe",
        "ha",
        "ha",
        "he",
        "hi",
        "ho",
        "hu",
        "ja",
        "ja",
        "ka",
        "ka",
        "ke",
        "kga",
        "ki",
        "ko",
        "ko",
        "ko",
        "ku",
        "ku",
        "la",
        "la",
        "la",
        "la",
        "la",
        "la",
        "le",
        "li",
        "li",
        "li",
        "llo",
        "lo",
        "lo",
        "lu",
        "ma",
        "ma",
        "ma",
        "ma",
        "ma",
        "ma",
        "mbu",
        "me",
        "me",
        "me",
        "mi",
        "mi",
        "mi",
        "mo",
        "mo",
        "mu",
        "mu",
        "na",
        "na",
        "na",
        "na",
        "na",
        "nchi",
        "nda",
        "nda",
        "ne",
        "no",
        "no",
        "no",
        "nte",
        "nte",
        "nu",
        "pa",
        "pe",
        "pi",
        "po",
        "pu",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "rde",
        "re",
        "ri",
        "ri",
        "ri",
        "ri",
        "ri",
        "ro",
        "ro",
        "ru",
        "ru",
        "ru",
        "sa",
        "sa",
        "se",
        "se",
        "si",
        "so",
        "su",
        "su",
        "ta",
        "ta",
        "ta",
        "ta",
        "ta",
        "te",
        "ti",
        "ti",
        "to",
        "to",
        "tu",
        "u",
        "va",
        "vi",
        "vi",
        "wa",
        "we",
        "wi",
        "wo",
        "wu",
        "xa",
        "xe",
        "xi",
        "xo",
        "xu",
        "ya",
        "ye",
        "yi",
        "yo",
        "yu",
        "ze",
        "zo",
    ]

    last_syllable_options = [
        "a",
        "al",
        "as",
        "ba",
        "ba",
        "ban",
        "be",
        "bi",
        "bnor",
        "bo",
        "bok",
        "bor",
        "bos",
        "bu",
        "cek",
        "cel",
        "cha",
        "che",
        "chet",
        "chi",
        "cho",
        "chu",
        "cot",
        "cus",
        "da",
        "da",
        "da",
        "da",
        "da",
        "daal",
        "darn",
        "de",
        "den",
        "di",
        "do",
        "do",
        "du",
        "dus",
        "er",
        "fa",
        "fe",
        "fi",
        "fo",
        "fu",
        "ga",
        "gan",
        "gath",
        "ge",
        "gel",
        "ger",
        "gi",
        "gnin",
        "go",
        "gu",
        "gus",
        "ha",
        "ham",
        "hav",
        "he",
        "he",
        "hi",
        "ho",
        "hor",
        "hu",
        "i",
        "ja",
        "jah",
        "jai",
        "jak",
        "jip",
        "juf",
        "ka",
        "ka",
        "kai",
        "kan",
        "kar",
        "ke",
        "ki",
        "kim",
        "ko",
        "ko",
        "ko",
        "ku",
        "ku",
        "ku",
        "la",
        "la",
        "la",
        "la",
        "lac",
        "lan",
        "lan",
        "lar",
        "lco",
        "le",
        "led",
        "lel",
        "len",
        "li",
        "lin",
        "lin",
        "lin",
        "lin",
        "lin",
        "lin",
        "lin",
        "lis",
        "lis",
        "lis",
        "lit",
        "lki",
        "llens",
        "lles",
        "llon",
        "lo",
        "lon",
        "lor",
        "lsi",
        "lu",
        "lut",
        "lva",
        "ma",
        "ma",
        "ma",
        "ma",
        "mam",
        "me",
        "me",
        "mi",
        "mi",
        "mo",
        "mo",
        "mo",
        "mol",
        "mon",
        "mu",
        "mu",
        "na",
        "na",
        "na",
        "na",
        "na",
        "nan",
        "nault",
        "ne",
        "neef",
        "nga",
        "ni",
        "ni",
        "nic",
        "nis",
        "nism",
        "no",
        "no",
        "now",
        "nryu",
        "ntis",
        "nua",
        "pa",
        "pal",
        "pe",
        "pel",
        "pel",
        "per",
        "pet",
        "phin",
        "pi",
        "po",
        "pu",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "ra",
        "rah",
        "rahd",
        "ral",
        "ral",
        "ran",
        "rar",
        "ras",
        "ras",
        "ras",
        "rdus",
        "re",
        "rek",
        "rel",
        "rel",
        "ren",
        "req",
        "resh",
        "ret",
        "rgus",
        "ri",
        "ri",
        "ri",
        "rid",
        "rik",
        "rin",
        "rin",
        "ris",
        "ris",
        "ris",
        "ris",
        "rnis",
        "ro",
        "ro",
        "ro",
        "roc",
        "ron",
        "ros",
        "row",
        "rren",
        "rro",
        "rrun",
        "rsa",
        "ru",
        "ru",
        "ruk",
        "sa",
        "sa",
        "sa",
        "sai",
        "sal",
        "se",
        "sel",
        "set",
        "sha",
        "si",
        "sil",
        "ska",
        "so",
        "sque",
        "su",
        "sus",
        "ta",
        "ta",
        "ta",
        "ta",
        "ta",
        "tal",
        "tar",
        "te",
        "ten",
        "ten",
        "thak",
        "threm",
        "ti",
        "tis",
        "to",
        "tod",
        "tro",
        "tu",
        "tus",
        "va",
        "va",
        "vah",
        "val",
        "var",
        "ve",
        "ves",
        "wa",
        "we",
        "wi",
        "wit",
        "wo",
        "wu",
        "xa",
        "xe",
        "xi",
        "xin",
        "xo",
        "xu",
        "ya",
        "ya",
        "ye",
        "yi",
        "yo",
        "yu",
        "za",
        "zath",
        "zir",
        "zon",
        "zzer",
    ]

    first_options = [
        "B",
        "B",
        "B",
        "B",
        "Bh",
        "C",
        "C",
        "C",
        "C",
        "Ch",
        "Ch",
        "Ch",
        "D",
        "D",
        "D",
        "D",
        "D",
        "Dr",
        "F",
        "F",
        "F",
        "G",
        "G",
        "G",
        "H",
        "H",
        "H",
        "J",
        "J",
        "K",
        "K",
        "K",
        "K",
        "L",
        "L",
        "L",
        "L",
        "M",
        "M",
        "M",
        "M",
        "M",
        "M",
        "M",
        "Mn",
        "N",
        "N",
        "N",
        "N",
        "P",
        "P",
        "R",
        "R",
        "R",
        "R",
        "S",
        "S",
        "S",
        "S",
        "S",
        "Sz",
        "T",
        "T",
        "T",
        "T",
        "T",
        "V",
        "V",
        "W",
        "W",
        "Y",
        "Y",
    ]

    vv_options = [
        "a",
        "a",
        "e",
        "e",
        "i",
        "i",
        "o",
        "o",
        "u",
        "u",
        "ey",
        "iou",
        "oi",
        "y",
    ]

    end_options = [
        "c",
        "d",
        "f",
        "k",
        "k",
        "l",
        "l",
        "l",
        "l",
        "lt",
        "m",
        "n",
        "n",
        "n",
        "n",
        "n",
        "n",
        "nd",
        "ns",
        "p",
        "q",
        "r",
        "r",
        "r",
        "r",
        "rn",
        "s",
        "s",
        "s",
        "s",
        "s",
        "sh",
        "sm",
        "t",
        "t",
        "th",
        "v",
        "a",
        "e",
        "i",
    ]

    schema_options = ["1ve", "fl", "fl", "fml", "fml", "fmml"]

    schema = random.choice(schema_options)

    if schema == "1ve":
        first = random.choice(first_options)
        vv = random.choice(vv_options)
        end = random.choice(end_options)
        name = first + vv + end
    else:
        num_ms = schema.count("m")
        f = random.choice(first_syllable_options)
        l = random.choice(last_syllable_options)
        m = [random.choice(mid_syllable_options) for _ in range(num_ms)]
        m = "".join(m)
        name = f + m + l
    return name


def old_realm_name():
    fv = [
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "ē",
        "ea",
        "ei",
        "ēi",
        "eu",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "ī",
        "ia",
        "iā",
        "ie",
        "iē",
        "io",
        "iō",
        "iu",
    ]
    bv = [
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "ā",
        "ae",
        "ai",
        "āi",
        "ao",
        "aō",
        "au",
        "o",
        "o",
        "o",
        "o",
        "o",
        "ō",
        "u",
        "u",
        "u",
        "u",
        "u",
        "ū",
        "ua",
        "ui",
        "uo",
    ]
    fbv = [
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "ā",
        "ae",
        "ai",
        "āi",
        "ao",
        "aō",
        "au",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "ē",
        "ea",
        "ei",
        "ēi",
        "eu",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "ī",
        "ia",
        "iā",
        "ie",
        "iē",
        "io",
        "iō",
        "iu",
    ]
    brv = [
        "o",
        "o",
        "o",
        "o",
        "o",
        "ō",
        "u",
        "u",
        "u",
        "u",
        "u",
        "ū",
        "ua",
        "ui",
        "uo",
    ]
    vv = [
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "ā",
        "ae",
        "ai",
        "āi",
        "ao",
        "aō",
        "au",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "ē",
        "ea",
        "ei",
        "ēi",
        "eu",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "ī",
        "ia",
        "iā",
        "ie",
        "iē",
        "io",
        "iō",
        "iu",
        "o",
        "o",
        "o",
        "o",
        "o",
        "ō",
        "u",
        "u",
        "u",
        "u",
        "u",
        "ū",
        "ua",
        "ui",
        "uo",
    ]
    firstcons = [
        "B" + random.choice(vv),
        "B" + random.choice(vv),
        "Br" + random.choice(vv),
        "Ch" + random.choice(fv),
        "Ch" + random.choice(fv),
        "J" + random.choice(bv),
        "J" + random.choice(bv),
        "D" + random.choice(vv),
        "D" + random.choice(vv),
        "D" + random.choice(vv),
        "F" + random.choice(vv),
        "F" + random.choice(vv),
        "Fr" + random.choice(vv),
        "G" + random.choice(vv),
        "G" + random.choice(vv),
        "G" + random.choice(vv),
        "Gr" + random.choice(vv),
        "H" + random.choice(vv),
        "H" + random.choice(vv),
        "H" + random.choice(vv),
        "Hr" + random.choice(vv),
        "K" + random.choice(vv),
        "K" + random.choice(vv),
        "K" + random.choice(vv),
        "K" + random.choice(vv),
        "Kl" + random.choice(vv),
        "Kr" + random.choice(vv),
        "X" + random.choice(vv),
        "L" + random.choice(vv),
        "L" + random.choice(vv),
        "L" + random.choice(vv),
        "M" + random.choice(vv),
        "M" + random.choice(vv),
        "M" + random.choice(vv),
        "M" + random.choice(vv),
        "N" + random.choice(vv),
        "N" + random.choice(vv),
        "N" + random.choice(vv),
        "P" + random.choice(vv),
        "Pl" + random.choice(vv),
        "Pr" + random.choice(vv),
        "R" + random.choice(vv),
        "R" + random.choice(vv),
        "S" + random.choice(vv),
        "S" + random.choice(vv),
        "S" + random.choice(vv),
        "S" + random.choice(vv),
        "S" + random.choice(vv),
        "S" + random.choice(vv),
        "Sk" + random.choice(vv),
        "Sp" + random.choice(vv),
        "St" + random.choice(vv),
        "Sh" + random.choice(vv),
        "Sh" + random.choice(vv),
        "Shr" + random.choice(vv),
        "T" + random.choice(vv),
        "T" + random.choice(vv),
        "T" + random.choice(vv),
        "Tr" + random.choice(vv),
        "Th" + random.choice(vv),
        "Tl" + random.choice(vv),
        "Tz" + random.choice(vv),
        "V" + random.choice(fbv),
        "V" + random.choice(fbv),
        "W" + random.choice(brv),
        "Y" + random.choice(vv),
        "Y" + random.choice(vv),
        "Y" + random.choice(vv),
        "Z" + random.choice(vv),
        "Z" + random.choice(vv),
    ]
    firstvow = [
        "A",
        "A",
        "A ",
        "A",
        "Ā",
        "Ae",
        "Ai",
        "Āi",
        "Ao",
        "Au",
        "E",
        "Ē",
        "Ea",
        "Ei",
        "Eu",
        "I",
        "I",
        "Ī",
        "Ia",
        "Ie",
        "O",
        "O",
        "Ō",
        "Oa",
        "U",
        "U",
        "Ū",
        "Ua",
    ]
    first = [
        random.choice(firstcons),
        random.choice(firstcons),
        random.choice(firstcons),
        random.choice(firstcons),
        random.choice(firstcons),
        random.choice(firstvow),
    ]
    second = [
        "b"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "b"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "br"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "ch" + random.choice(fv),
        "j" + random.choice(bv),
        "j" + random.choice(bv),
        "d"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "d"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "d"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "dr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "dv" + random.choice(fbv),
        "dw" + random.choice(brv),
        "f"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "fr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "g"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "g"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "g"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "gr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "h"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "h"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "hr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "k"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "k"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "k"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "k"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "k"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "kl"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "kr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "x"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "x"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "l"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "l"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "l"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "l"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "l"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "l"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lk"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "ll"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lm"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lp"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lt"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lv" + random.choice(fbv),
        "lw" + random.choice(brv),
        "lz"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "m"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "m"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "m"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "m"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "m"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "m"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "mb"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "mf"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "mm"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "my"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "n"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "n"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "n"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "n"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "n"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "n"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "n"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nd"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nd"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nj"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nm"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nn"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nt"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nth"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nv" + random.choice(fbv),
        "nw" + random.choice(brv),
        "ny"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nz"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "ng"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nk"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "p"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "pl"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "pr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rd"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rg"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rj"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rk"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rl"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rm"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rn"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rs"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rt"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rth"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rv" + random.choice(fbv),
        "rw" + random.choice(brv),
        "rz"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "s"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "s"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "s"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "sk"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "sn"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "sp"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "ss"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "st"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "sh"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "sh"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "shr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "ssh"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "sht"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "t"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "t"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "t"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "t"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "tr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "th"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "thr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "tl"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "tz"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "v" + random.choice(fbv),
        "v" + random.choice(fbv),
        "w" + random.choice(brv),
        "y"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "y"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "z"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "z"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
    ]
    end = [
        "d",
        "k",
        "l",
        "l",
        "m",
        "n",
        "n",
        "n",
        "n",
        "n",
        "n",
        "ng",
        "p",
        "r",
        "r",
        "s",
        "s",
        "sh",
        "t",
        "th",
        "z",
    ]

    name1 = [
        "".join(
            [
                random.choice(first),
                random.choice(["", random.choice(end), random.choice(end)]),
            ]
        )
    ]
    name2 = [
        "".join([random.choice(first), random.choice(second)]),
        "".join([random.choice(first), random.choice(second), random.choice(end)]),
        " ".join(
            [
                "-".join(
                    [
                        random.choice(name1),
                        "".join([random.choice(name1), random.choice(name1)]),
                        "".join([random.choice(name1), random.choice(name1)]),
                    ]
                ),
                random.choice(name1),
            ]
        ),
    ]
    name3 = [
        "".join([random.choice(first), random.choice(second), random.choice(second)]),
        "".join(
            [
                random.choice(first),
                random.choice(second),
                random.choice(second),
                random.choice(end),
            ]
        ),
        random.choice(["-", "-", " "]).join(
            [random.choice(name1), random.choice(name1), random.choice(name1),]
        ),
        random.choice(["-", "-", " "]).join(
            [
                random.choice(name1),
                "".join(
                    [
                        random.choice(first),
                        random.choice(second),
                        random.choice(["", random.choice(end)]),
                    ]
                ),
            ]
        ),
        random.choice(["-", "-", " "]).join(
            [
                "".join(
                    [
                        random.choice(first),
                        random.choice(second),
                        random.choice(["", random.choice(end)]),
                    ]
                ),
                random.choice(name1),
            ]
        ),
    ]
    name4 = [
        "".join(
            [
                random.choice(first),
                random.choice(second),
                random.choice(second),
                random.choice(second),
            ]
        ),
        "".join(
            [
                random.choice(first),
                random.choice(second),
                random.choice(second),
                random.choice(second),
                random.choice(end),
            ]
        ),
        random.choice(
            [
                random.choice(["-", " "]).join(
                    [
                        "".join(
                            [
                                random.choice(first),
                                random.choice(second),
                                random.choice(["", random.choice(end)]),
                            ]
                        ),
                        "".join(
                            [
                                random.choice(first),
                                random.choice(second),
                                random.choice(["", random.choice(end)]),
                            ]
                        ),
                    ]
                ),
                " ".join(
                    [
                        random.choice(name2),
                        "".join(
                            [
                                random.choice(first),
                                random.choice(second),
                                random.choice(["", random.choice(end)]),
                            ]
                        ),
                    ]
                ),
            ]
        ),
        random.choice(["-", "-", " "]).join(
            [
                random.choice(name1),
                "".join(
                    [
                        random.choice(first),
                        random.choice(second),
                        random.choice(second),
                        random.choice(["", random.choice(end)]),
                    ]
                ),
            ]
        ),
        random.choice(["-", " ", " "]).join(
            [
                "".join(
                    [
                        random.choice(first),
                        random.choice(second),
                        random.choice(second),
                        random.choice(["", random.choice(end)]),
                    ]
                ),
                random.choice(name1),
            ]
        ),
    ]
    name5 = [
        "".join(
            [
                random.choice(first),
                random.choice(second),
                random.choice(second),
                random.choice(second),
                random.choice(second),
                random.choice(["", random.choice(end)]),
            ]
        ),
        " ".join(
            [
                random.choice(
                    [
                        "".join(
                            [
                                random.choice(first),
                                random.choice(second),
                                random.choice(["", random.choice(end)]),
                                "-",
                                random.choice(first),
                                random.choice(second),
                                random.choice(second),
                                random.choice(["", random.choice(end)]),
                            ]
                        ),
                        "".join(
                            [
                                random.choice(first),
                                random.choice(second),
                                random.choice(["", random.choice(end)]),
                                "-",
                                random.choice(first),
                                random.choice(second),
                                random.choice(second),
                                random.choice(["", random.choice(end)]),
                            ]
                        ),
                        "".join(
                            [
                                random.choice(first),
                                random.choice(second),
                                random.choice(["", random.choice(end)]),
                            ]
                        ),
                    ]
                ),
                "".join(
                    [
                        random.choice(first),
                        random.choice(second),
                        random.choice(second),
                        random.choice(["", random.choice(end)]),
                    ]
                ),
            ]
        ),
        " ".join(
            [
                "-".join(
                    [
                        "".join(
                            [
                                random.choice(first),
                                random.choice(second),
                                random.choice(second),
                                random.choice(["", random.choice(end)]),
                            ]
                        ),
                        random.choice(
                            [
                                "".join(
                                    [
                                        random.choice(first),
                                        random.choice(second),
                                        random.choice(["", random.choice(end)]),
                                    ]
                                ),
                                "".join(
                                    [
                                        random.choice(first),
                                        random.choice(second),
                                        random.choice(second),
                                        random.choice(["", random.choice(end)]),
                                    ]
                                ),
                            ]
                        ),
                        random.choice(
                            [
                                "".join(
                                    [
                                        random.choice(first),
                                        random.choice(second),
                                        random.choice(["", random.choice(end)]),
                                    ]
                                ),
                                "".join(
                                    [
                                        random.choice(first),
                                        random.choice(second),
                                        random.choice(second),
                                        random.choice(["", random.choice(end)]),
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),
                "".join(
                    [
                        random.choice(first),
                        random.choice(second),
                        random.choice(["", random.choice(end)]),
                    ]
                ),
            ]
        ),
    ]

    prompt = [
        random.choice(name1),
        random.choice(name2),
        random.choice(name2),
        random.choice(name2),
        random.choice(name2),
        random.choice(name3),
        random.choice(name3),
        random.choice(name3),
        random.choice(name3),
        random.choice(name3),
        random.choice(name4),
        random.choice(name4),
        random.choice(name5),
        "".join(
            [
                random.choice(first),
                random.choice(second),
                random.choice(second),
                random.choice(end),
                " ",
                random.choice(first),
                random.choice(second),
                random.choice(second),
                random.choice(end),
            ]
        ),
    ]
    return random.choice(prompt)


def infernal_name():
    vv = [
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "ā",
        "ae",
        "ai",
        "āi",
        "ao",
        "aō",
        "au",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "ē",
        "ea",
        "eo",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "ī",
        "ia",
        "ie",
        "io",
        "iē",
        "iu",
        "o",
        "o",
        "o",
        "o",
        "ō",
        "oa",
        "oi",
        "u",
        "u",
        "u",
        "ū",
    ]
    fv = [
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "ē",
        "ea",
        "eo",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "ī",
        "ia",
        "ie",
        "io",
        "iē",
        "iu    ",
    ]
    bv = [
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "ā",
        "ae",
        "ai",
        "āi",
        "ao",
        "aō",
        "au",
        "o",
        "o",
        "o",
        "o",
        "ō",
        "oa",
        "oi",
        "u",
        "u",
        "u",
        "ū",
    ]
    hmv = [
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "e",
        "ē",
        "ea",
        "eo",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "i",
        "ī",
        "ia",
        "ie",
        "io",
        "iē",
        "iu",
        "o",
        "o",
        "o",
        "o",
        "ō",
        "oa",
        "oi",
        "u",
        "u",
        "u",
        "ū",
    ]
    av = [
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "a",
        "ā",
        "ae",
        "ai",
        "āi",
        "ao",
        "aō",
        "au",
    ]
    firstvow = [
        "A",
        "A",
        "A",
        "A",
        "E",
        "E",
        "E",
        "I",
        "I",
        "I",
        "O",
        "U",
        "Ā",
        "Ē",
        "Ī",
        "Ō",
        "Ū",
        "Ae",
        "Ai",
        "Āi",
        "Ao",
        "Au",
        "Ea",
        "Eo",
        "Ia",
        "Ie",
        "Oa",
    ]
    firstcons = [
        "B" + random.choice(vv),
        "B" + random.choice(vv),
        "B" + random.choice(vv),
        "Br" + random.choice(vv),
        random.choice(["Ch" + random.choice(fv), "J" + random.choice(bv)]),
        random.choice(["Ch" + random.choice(fv), "J" + random.choice(bv)]),
        "D" + random.choice(vv),
        "D" + random.choice(vv),
        "D" + random.choice(vv),
        "F" + random.choice(vv),
        "F" + random.choice(vv),
        "G" + random.choice(vv),
        "G" + random.choice(vv),
        "Gl" + random.choice(vv),
        "Gr" + random.choice(vv),
        "H" + random.choice(vv),
        "H" + random.choice(vv),
        "Hr" + random.choice(vv),
        "K" + random.choice(vv),
        "K" + random.choice(vv),
        "K" + random.choice(vv),
        "K" + random.choice(vv),
        "K" + random.choice(vv),
        "K" + random.choice(vv),
        "Kr" + random.choice(vv),
        "X" + random.choice(vv),
        "L" + random.choice(vv),
        "L" + random.choice(vv),
        "M" + random.choice(vv),
        "M" + random.choice(vv),
        "M" + random.choice(vv),
        "M" + random.choice(vv),
        "N" + random.choice(vv),
        "N" + random.choice(vv),
        "N" + random.choice(vv),
        "P" + random.choice(vv),
        "P" + random.choice(vv),
        "R" + random.choice(vv),
        "S" + random.choice(vv),
        "S" + random.choice(vv),
        "S" + random.choice(vv),
        "S" + random.choice(vv),
        "S" + random.choice(vv),
        "S" + random.choice(vv),
        "Sk" + random.choice(vv),
        "Sh" + random.choice(vv),
        "St" + random.choice(vv),
        "T" + random.choice(vv),
        "T" + random.choice(vv),
        "Th" + random.choice(vv),
        "Tl" + random.choice(vv),
        "Tz" + random.choice(vv),
        "V" + random.choice(hmv),
        random.choice(["V" + random.choice(hmv), "W" + random.choice(av)]),
        "Y" + random.choice(vv),
        "Y" + random.choice(vv),
        "Z" + random.choice(vv),
    ]
    first = [
        random.choice(firstcons),
        random.choice(firstcons),
        random.choice(firstcons),
        random.choice(firstcons),
        random.choice(firstcons),
        random.choice(firstcons),
        random.choice(firstcons),
        random.choice(firstcons),
        random.choice(firstvow),
        random.choice(firstvow),
        random.choice(firstvow),
    ]
    second = [
        "b"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "bk"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "br"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "bt"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "ch" + random.choice(fv),
        "j" + random.choice(bv),
        "d"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "d"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "dk"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "dp"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "dr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "f"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "fr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "g"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "g"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "g"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "gl"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "gp"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "gr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "gt"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "h"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "hr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "k"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "k"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "kk"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "kr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "kt"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "qu"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "x"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "l"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "l"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "l"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "l"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "l"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lf"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lg"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lk"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "ll"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lm"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lsh"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lt"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "lv" + random.choice(hmv),
        "lw" + random.choice(av),
        "ly"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "m"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "m"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "m"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "m"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "m"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "mb"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "md"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "mf"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "mg"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "mm"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "my"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "n"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "n"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "n"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "n"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nb"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nd"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "n'g"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nh"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nj"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nn"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nsh"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nt"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nth"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nv" + random.choice(hmv),
        "nw" + random.choice(av),
        "ny"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nz"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "ng"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "ngb"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "ngd"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "nk"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "p"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "pp"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "r"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rd"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rg"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rj"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rk"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rl"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rm"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rn"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rs"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "rv" + random.choice(hmv),
        "rw" + random.choice(av),
        "rz"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "s"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "s"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "sk"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "ss"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "sh"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "ssh"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "sht"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "t"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "t"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "tr"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "tt"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "th"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "tl"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "tz"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "v" + random.choice(hmv),
        "w" + random.choice(av),
        "y"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "z"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
        "z"
        + random.choice(
            [random.choice(vv), random.choice(vv), random.choice(vv), random.choice(vv)]
        ),
    ]
    end = [
        "d",
        "k",
        "l",
        "l",
        "m",
        "n",
        "n",
        "n",
        "n",
        "n",
        "ng",
        "p",
        "r",
        "r",
        "s",
        "s",
        "s",
        "s",
        "sh",
        "t",
        "th",
        "z",
    ]
    name1 = [
        random.choice(first),
        "".join([random.choice(first), random.choice(end)]),
    ]
    name2 = [
        "".join([random.choice(first), random.choice(second)]),
        "".join([random.choice(first), random.choice(second), random.choice(end)]),
        "".join(
            [
                random.choice(first),
                random.choice(["", random.choice(end)]),
                "'",
                random.choice(first),
                random.choice(["", random.choice(end)]),
            ]
        ),
    ]
    name3 = [
        "".join([random.choice(first), random.choice(second), random.choice(second)]),
        "".join(
            [
                random.choice(first),
                random.choice(second),
                random.choice(second),
                random.choice(end),
            ]
        ),
        random.choice(
            [
                "".join(
                    [
                        random.choice(first),
                        random.choice(second),
                        random.choice(["", random.choice(end)]),
                        "-",
                        random.choice(first),
                        random.choice(["", random.choice(end)]),
                    ]
                ),
                "".join(
                    [
                        random.choice(first),
                        random.choice(["", random.choice(end)]),
                        "-",
                        random.choice(first),
                        random.choice(second),
                        random.choice(["", random.choice(end)]),
                    ]
                ),
            ]
        ),
    ]
    name4 = [
        "".join(
            [
                random.choice(first),
                random.choice(second),
                random.choice(second),
                random.choice(second),
            ]
        ),
        "".join(
            [
                random.choice(first),
                random.choice(second),
                random.choice(second),
                random.choice(second),
                random.choice(end),
            ]
        ),
        "".join(
            [
                random.choice(first),
                random.choice(second),
                random.choice(["", random.choice(end)]),
                "-",
                random.choice(first),
                random.choice(second),
                random.choice(["", random.choice(end)]),
            ]
        ),
    ]
    name5 = [
        "".join(
            [
                random.choice(first),
                random.choice(second),
                random.choice(second),
                random.choice(second),
                random.choice(second),
                random.choice(["", random.choice(end)]),
            ]
        ),
        "".join(
            [
                random.choice(first),
                random.choice(second),
                random.choice(["", random.choice(end)]),
                "-",
                random.choice(first),
                random.choice(second),
                random.choice(second),
                random.choice(["", random.choice(end)]),
            ]
        ),
        "".join(
            [
                random.choice(first),
                random.choice(second),
                random.choice(second),
                random.choice(["", random.choice(end)]),
                "-",
                random.choice(first),
                random.choice(second),
                random.choice(["", random.choice(end)]),
            ]
        ),
    ]

    prompt = [
        random.choice(name1),
        random.choice(name2),
        random.choice(name2),
        random.choice(name2),
        random.choice(name3),
        random.choice(name3),
        random.choice(name3),
        random.choice(name3),
        random.choice(name3),
        random.choice(name3),
        random.choice(name4),
        random.choice(name4),
        random.choice(name5),
    ]
    return random.choice(prompt)
