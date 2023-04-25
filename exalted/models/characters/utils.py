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

    def first(self):
        options = [
            self.firstcons(),
            self.firstcons(),
            self.firstcons(),
            self.firstcons(),
            self.firstcons(),
            self.firstcons(),
            self.firstcons(),
            self.firstvow(),
            self.firstvow(),
            self.firstvow(),
        ]
        self.random_add(options, self.firstcons(), 0.7)
        self.random_add(options, self.firstvow(), 0.7)
        return random.choice(options)

    def firstvow(self, v=False):
        options = [
            ("A", "a"),
            ("A", "a"),
            ("A", "a"),
            ("A", "a"),
            ("E", "e"),
            ("E", "e"),
            ("I", "i"),
            ("I", "i"),
            ("O", "o"),
            ("U", "u"),
        ]
        self.random_add(options, ("E", "e"), 0.50)
        self.random_add(options, ("I", "i"), 0.50)
        self.random_add(options, ("Ā", "a"), 0.50)
        self.random_add(options, ("Ē", "e"), 0.10)
        self.random_add(options, ("Ī", "i"), 0.10)
        self.random_add(options, ("Ō", "o"), 0.10)
        self.random_add(options, ("Ū", "u"), 0.05)
        self.random_add(options, ("Ae", "e"), 0.50)
        self.random_add(options, ("Ai", "i"), 0.15)
        self.random_add(options, ("Āi", "i"), 0.15)
        self.random_add(options, ("Ao", "o"), 0.10)
        self.random_add(options, ("Au", "u"), 0.50)
        self.random_add(options, ("Ea", "a"), 0.10)
        self.random_add(options, ("Eo", "o"), 0.10)
        self.random_add(options, ("Ia", "a"), 0.10)
        self.random_add(options, ("Ie", "e"), 0.50)
        self.random_add(options, ("Oa", "a"), 0.10)
        choice = random.choice(options)
        if v:
            return choice[1]
        return choice[0]

    def firstcons(self):
        options = [
            f"B{self.vv()}",
            f"B{self.vv()}",
            f"B{self.vv()}",
            random.choice(["Ch" + self.fv(), "J" + self.bv()]),
            f"D{self.vv()}",
            f"D{self.vv()}",
            f"D{self.vv()}",
            f"F{self.vv()}",
            f"G{self.vv()}",
            f"G{self.vv()}",
            f"H{self.vv()}",
            f"K{self.vv()}",
            f"K{self.vv()}",
            f"K{self.vv()}",
            f"K{self.vv()}",
            f"K{self.vv()}",
            f"K{self.vv()}",
            f"L{self.vv()}",
            f"M{self.vv()}",
            f"M{self.vv()}",
            f"M{self.vv()}",
            f"M{self.vv()}",
            f"N{self.vv()}",
            f"N{self.vv()}",
            f"N{self.vv()}",
            f"P{self.vv()}",
            f"P{self.vv()}",
            f"R{self.vv()}",
            f"S{self.vv()}",
            f"S{self.vv()}",
            f"S{self.vv()}",
            f"S{self.vv()}",
            f"S{self.vv()}",
            f"S{self.vv()}",
            f"T{self.vv()}",
            f"V{self.hmv()}",
            f"Y{self.vv()}",
            f"Y{self.vv()}",
        ]
        self.random_add(
            options, random.choice(["Ch" + self.fv(), "J" + self.bv()]), 0.50
        )
        self.random_add(options, f"Br{self.vv()}", 0.50)
        self.random_add(options, f"F{self.vv()}", 0.50)
        self.random_add(options, f"Gl{self.vv()}", 0.50)
        self.random_add(options, f"Gr{self.vv()}", 0.15)
        self.random_add(options, f"H{self.vv()}", 0.50)
        self.random_add(options, f"Hr{self.vv()}", 0.50)
        self.random_add(options, f"Kr{self.vv()}", 0.50)
        self.random_add(options, f"X{self.vv()}", 0.15)
        self.random_add(options, f"L{self.vv()}", 0.50)
        self.random_add(options, f"Sk{self.vv()}", 0.10)
        self.random_add(options, f"Sh{self.vv()}", 0.50)
        self.random_add(options, f"St{self.vv()}", 0.10)
        self.random_add(options, f"T{self.vv()}", 0.50)
        self.random_add(options, f"Th{self.vv()}", 0.15)
        self.random_add(options, f"Tl{self.vv()}", 0.15)
        self.random_add(options, f"Tz{self.vv()}", 0.15)
        self.random_add(
            options, random.choice(["V" + self.hmv(), "W" + self.av()]), 0.50
        )
        self.random_add(options, f"Z{self.vv()}", 0.50)
        return random.choice(options)

    """
$2nd
d[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
d[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
g[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
g[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
k[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
k[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
l[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
l[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
l[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
l[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
l[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
ll[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
m[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
m[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
m[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
m[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
n[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
n[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
n[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
n[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
nd[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
nt[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
s[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
t[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
t[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
v[hmv]
z[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]]
b[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
bk[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
br[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
bt[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
ch[fv] {30%}
j[bv] {30%}
dk[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
dp[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
dr[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
f[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {80%}
fr[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
g[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {60%}
gl[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {15%}
gp[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
gr[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
gt[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
h[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
hr[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {15%}
kk[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
kr[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
kt[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
qu[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
x[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
lf[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
lg[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
lk[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {60%}
lm[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {60%}
lr[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
lsh[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
lt[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
lv[hmv] {60%}
lw[av] {10%}
ly[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
m[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {60%}
mb[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {60%}
md[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
mf[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
mg[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
mm[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
my[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
nb[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
n'g[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
nh[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
nj[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
nn[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
nsh[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
nth[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
nv[hmv] {30%}
nw[av] {10%}
ny[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {15%}
nz[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {60%}
ng[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
ngb[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
ngd[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
nk[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
p[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {60%}
pp[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
rd[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
rg[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {15%}
rj[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
rk[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
rl[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
rm[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
rn[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
rr[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {15%}
rs[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {80%}
rv[hmv] {30%}
rw[av] {10%}
rz[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
s[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {60%}
sk[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {60%}
ss[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
sh[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {60%}
ssh[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {10%}
sht[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {60%}
tr[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
tt[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
th[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {15%}
tl[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {15%}
tz[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {30%}
w[av] {30%}
y[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {80%}
z[[vv]|[vv]|[vv]|[vv,as v]|[vv,as v]] {20%}

$vv
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
i {v:i}
i {v:i}
i {v:i}
i {v:i}
i {v:i}
i {v:i}
i {v:i}
ia {v:a}
o {v:o}
o {v:o}
o {v:o}
o {v:o}
u {v:u}
u {v:u}
u {v:u}
ā {v:a}{15%}
ae {v:e}{15%}
ai {v:i}{50%}
āi {v:i}{50%}
ao {v:o}{15%}
aō {v:o}{5%}
au {v:u}{30%}
ē {v:e}{15%}
ea {v:a}{44%}
eo {v:o}{44%}
ī {v:i}{15%}
ie {v:e}{60%}
io {v:o}{60%}
iē {v:e}{5%}
iu {v:u}{15%}
ō {v:o}{15%}
oa {v:a}{5%}
oi {v:i}{15%}
ū {v:u}{5%}

$fv
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
i {v:i}
i {v:i}
i {v:i}
i {v:i}
i {v:i}
i {v:i}
i {v:i}
ia {v:a}
ē {v:e}{15%}
ea {v:a}{44%}
eo {v:o}{44%}
ī {v:i}{15%}
ie {v:e}{60%}
io {v:o}{60%}
iē {v:e}{5%}
iu {v:u}{15%}

$bv
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
o {v:o}
o {v:o}
o {v:o}
o {v:o}
u {v:u}
u {v:u}
u {v:u}
ā {v:a}{15%}
ae {v:e}{15%}
ai {v:i}{50%}
āi {v:i}{50%}
ao {v:o}{15%}
aō {v:o}{5%}
au {v:u}{30%}
ō {v:o}{15%}
oa {v:a}{5%}
oi {v:i}{15%}
ū {v:u}{5%}

$hmv
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
e {v:e}
i {v:i}
i {v:i}
i {v:i}
i {v:i}
i {v:i}
i {v:i}
i {v:i}
ia {v:a}
o {v:o}
o {v:o}
o {v:o}
o {v:o}
u {v:u}
u {v:u}
u {v:u}
ē {v:e}{15%}
ea {v:a}{44%}
eo {v:o}{44%}
ī {v:i}{15%}
ie {v:e}{60%}
io {v:o}{60%}
iē {v:e}{5%}
iu {v:u}{15%}
ō {v:o}{15%}
oa {v:a}{5%}
oi {v:i}{15%}
ū {v:u}{5%}

$av
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
a {v:a}
ā {v:a}{15%}
ae {v:e}{15%}
ai {v:i}{50%}
āi {v:i}{50%}
ao {v:o}{15%}
aō {v:o}{5%}
au {v:u}{30%}

$end
l
l
n
n
n
n
n
r
r
s
s
s
s
d {40%}
k {60%}
m {60%}
ng {15%}
p {15%}
sh {30%}
t {60%}
th {40%}
z {15%}

$name1
[1st]
[1st][end]

$name2
[1st][2nd]
[1st][2nd][end]
[1st][|[end]]'[1st][|[end]] {12%}

$name3
[1st][2nd][2nd]
[1st][2nd][2nd][end]
[[1st][2nd][|[end]]-[1st][|[end]]|[1st][|[end]]-[1st][2nd][|[end]]] {5%}

$name4
[1st][2nd][2nd][2nd]
[1st][2nd][2nd][2nd][end]
[1st][2nd][|[end]]-[1st][2nd][|[end]] {20%}

$name5
[1st][2nd][2nd][2nd][2nd][|[end]]
[1st][2nd][|[end]]-[1st][2nd][2nd][|[end]]
[1st][2nd][2nd][|[end]]-[1st][2nd][|[end]] {5%}
    """

    def prompt(self):
        options = [
            self.name2(),
            self.name2(),
            self.name3(),
            self.name3(),
            self.name3(),
            self.name3(),
            self.name3(),
            self.name4(),
        ]
        self.random_add(options, self.name1(), 0.15)
        self.random_add(options, self.name2(), 0.54)
        self.random_add(options, self.name3(), 0.52)
        self.random_add(options, self.name4(), 0.64)
        self.random_add(options, self.name5(), 0.15)
        return random.choice(options)


class OldRealmName(RandomName):
    """
    Based on Old Realm Name Generator: https://orteil.dashnet.org/randomgen/?gen=FaifGb1M    
    """

    def first(self):
        options = [
            self.firstcons(),
            self.firstcons(),
            self.firstcons(),
            self.firstcons(),
            self.firstvow(),
        ]
        self.random_add(options, self.firstcons(), 0.77)
        return random.choice(options)

    def firstvow(self, v=False):
        options = [
            ("A", "a"),
            ("A", "a"),
            ("A", "a"),
            ("I", "i"),
            ("O", "o"),
            ("U", "u"),
        ]
        self.random_add(options, ("A", "a"), 0.50)
        self.random_add(options, ("Ā", "a"), 0.10)
        self.random_add(options, ("Ae", "e"), 0.10)
        self.random_add(options, ("Ai", "i"), 0.20)
        self.random_add(options, ("Āi", "i"), 0.20)
        self.random_add(options, ("Ao", "o"), 0.10)
        self.random_add(options, ("Au", "u"), 0.20)
        self.random_add(options, ("E", "e"), 0.90)
        self.random_add(options, ("Ē", "e"), 0.02)
        self.random_add(options, ("Ea", "a"), 0.10)
        self.random_add(options, ("Ei", "i"), 0.10)
        self.random_add(options, ("Eu", "u"), 0.01)
        self.random_add(options, ("I", "i"), 0.30)
        self.random_add(options, ("Ī", "i"), 0.06)
        self.random_add(options, ("Ia", "a"), 0.10)
        self.random_add(options, ("Ie", "e"), 0.02)
        self.random_add(options, ("O", "o"), 0.60)
        self.random_add(options, ("Ō", "o"), 0.08)
        self.random_add(options, ("Oa", "a"), 0.20)
        self.random_add(options, ("U", "u"), 0.40)
        self.random_add(options, ("Ū", "u"), 0.06)
        self.random_add(options, ("Ua", "a"), 0.03)
        choice = random.choice(options)
        if v:
            return choice[1]
        return choice[0]

    def firstcons(self):
        options = [
"B" + self.vv(),
"Ch" + self.fv(),
"J" + self.bv(),
"D" + self.vv(),
"D" + self.vv(),
"F" + self.vv(),
"G" + self.vv(),
"G" + self.vv(),
"H" + self.vv(),
"H" + self.vv(),
"K" + self.vv(),
"K" + self.vv(),
"K" + self.vv(),
"L" + self.vv(),
"L" + self.vv(),
"M" + self.vv(),
"M" + self.vv(),
"M" + self.vv(),
"N" + self.vv(),
"N" + self.vv(),
"R" + self.vv(),
"S" + self.vv(),
"S" + self.vv(),
"S" + self.vv(),
"S" + self.vv(),
"S" + self.vv(),
"Sh" + self.vv(),
"T" + self.vv(),
"T" + self.vv(),
"V" + self.fbv(),
"Y" + self.vv(),
"Y" + self.vv(),
"Z" + self.vv(),
        ]
        self.random_add(options, "B" + self.vv(), 0.80)
        self.random_add(options, "Br" + self.vv(), 0.10)
        self.random_add(options, "Ch" + self.fv(), 0.10)
        self.random_add(options, "J" + self.bv(), 0.80)
        self.random_add(options, "D" + self.vv(), 0.20)
        self.random_add(options, "F" + self.vv(), 0.20)
        self.random_add(options, "Fr" + self.vv(), 0.20)
        self.random_add(options, "G" + self.vv(), 0.20)
        self.random_add(options, "Gr" + self.vv(), 0.40)
        self.random_add(options, "H" + self.vv(), 0.90)
        self.random_add(options, "Hr" + self.vv(), 0.10)
        self.random_add(options, "K" + self.vv(), 0.90)
        self.random_add(options, "Kl" + self.vv(), 0.20)
        self.random_add(options, "Kr" + self.vv(), 0.40)
        self.random_add(options, "X" + self.vv(), 0.90)
        self.random_add(options, "L" + self.vv(), 0.20)
        self.random_add(options, "M" + self.vv(), 0.60)
        self.random_add(options, "N" + self.vv(), 0.80)
        self.random_add(options, "P" + self.vv(), 0.90)
        self.random_add(options, "Pl" + self.vv(), 0.10)
        self.random_add(options, "Pr" + self.vv(), 0.40)
        self.random_add(options, "R" + self.vv(), 0.80)
        self.random_add(options, "S" + self.vv(), 0.30)
        self.random_add(options, "Sk" + self.vv(), 0.20)
        self.random_add(options, "Sp" + self.vv(), 0.10)
        self.random_add(options, "St" + self.vv(), 0.20)
        self.random_add(options, "Sh" + self.vv(), 0.90)
        self.random_add(options, "Shr" + self.vv(), 0.10)
        self.random_add(options, "T" + self.vv(), 0.90)
        self.random_add(options, "Tr" + self.vv(), 0.30)
        self.random_add(options, "Th" + self.vv(), 0.60)
        self.random_add(options, "Tl" + self.vv(), 0.20)
        self.random_add(options, "Tz" + self.vv(), 0.40)
        self.random_add(options, "V" + self.fbv(), 0.10)
        self.random_add(options, "W" + self.brv(), 0.60)
        self.random_add(options, "Y" + self.vv(), 0.30)
        self.random_add(options, "Z" + self.vv(), 0.10)
        return random.choice(options)

    """
$2nd
b[[vv]|[vv]|[vv]|[vv,as v]]
j[bv]
d[[vv]|[vv]|[vv]|[vv,as v]]
d[[vv]|[vv]|[vv]|[vv,as v]]
g[[vv]|[vv]|[vv]|[vv,as v]]
g[[vv]|[vv]|[vv]|[vv,as v]]
h[[vv]|[vv]|[vv]|[vv,as v]]
k[[vv]|[vv]|[vv]|[vv,as v]]
k[[vv]|[vv]|[vv]|[vv,as v]]
k[[vv]|[vv]|[vv]|[vv,as v]]
k[[vv]|[vv]|[vv]|[vv,as v]]
x[[vv]|[vv]|[vv]|[vv,as v]]
l[[vv]|[vv]|[vv]|[vv,as v]]
l[[vv]|[vv]|[vv]|[vv,as v]]
l[[vv]|[vv]|[vv]|[vv,as v]]
l[[vv]|[vv]|[vv]|[vv,as v]]
l[[vv]|[vv]|[vv]|[vv,as v]]
ll[[vv]|[vv]|[vv]|[vv,as v]]
m[[vv]|[vv]|[vv]|[vv,as v]]
m[[vv]|[vv]|[vv]|[vv,as v]]
m[[vv]|[vv]|[vv]|[vv,as v]]
m[[vv]|[vv]|[vv]|[vv,as v]]
m[[vv]|[vv]|[vv]|[vv,as v]]
n[[vv]|[vv]|[vv]|[vv,as v]]
n[[vv]|[vv]|[vv]|[vv,as v]]
n[[vv]|[vv]|[vv]|[vv,as v]]
n[[vv]|[vv]|[vv]|[vv,as v]]
n[[vv]|[vv]|[vv]|[vv,as v]]
n[[vv]|[vv]|[vv]|[vv,as v]]
nd[[vv]|[vv]|[vv]|[vv,as v]]
p[[vv]|[vv]|[vv]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]]
r[[vv]|[vv]|[vv]|[vv,as v]]
s[[vv]|[vv]|[vv]|[vv,as v]]
s[[vv]|[vv]|[vv]|[vv,as v]]
s[[vv]|[vv]|[vv]|[vv,as v]]
sh[[vv]|[vv]|[vv]|[vv,as v]]
t[[vv]|[vv]|[vv]|[vv,as v]]
t[[vv]|[vv]|[vv]|[vv,as v]]
t[[vv]|[vv]|[vv]|[vv,as v]]
v[fbv]
y[[vv]|[vv]|[vv]|[vv,as v]]
z[[vv]|[vv]|[vv]|[vv,as v]]
b[[vv]|[vv]|[vv]|[vv,as v]] {50%}
br[[vv]|[vv]|[vv]|[vv,as v]] {20%}
ch[fv] {70%}
j[bv] {20%}
d[[vv]|[vv]|[vv]|[vv,as v]] {50%}
dr[[vv]|[vv]|[vv]|[vv,as v]] {30%}
dv[fbv] {30%}
dw[brv] {2%}
f[[vv]|[vv]|[vv]|[vv,as v]] {80%}
fr[[vv]|[vv]|[vv]|[vv,as v]] {20%}
g[[vv]|[vv]|[vv]|[vv,as v]] {20%}
gr[[vv]|[vv]|[vv]|[vv,as v]] {50%}
h[[vv]|[vv]|[vv]|[vv,as v]] {10%}
hr[[vv]|[vv]|[vv]|[vv,as v]] {20%}
k[[vv]|[vv]|[vv]|[vv,as v]] {20%}
kl[[vv]|[vv]|[vv]|[vv,as v]] {30%}
kr[[vv]|[vv]|[vv]|[vv,as v]] {30%}
x[[vv]|[vv]|[vv]|[vv,as v]] {40%}
l[[vv]|[vv]|[vv]|[vv,as v]] {80%}
lk[[vv]|[vv]|[vv]|[vv,as v]] {50%}
lm[[vv]|[vv]|[vv]|[vv,as v]] {40%}
lp[[vv]|[vv]|[vv]|[vv,as v]] {30%}
lr[[vv]|[vv]|[vv]|[vv,as v]] {30%}
lt[[vv]|[vv]|[vv]|[vv,as v]] {20%}
lv[fbv] {30%}
lw[brv] {10%}
lz[[vv]|[vv]|[vv]|[vv,as v]] {30%}
m[[vv]|[vv]|[vv]|[vv,as v]] {10%}
mb[[vv]|[vv]|[vv]|[vv,as v]] {40%}
mf[[vv]|[vv]|[vv]|[vv,as v]] {40%}
mm[[vv]|[vv]|[vv]|[vv,as v]] {10%}
my[[vv]|[vv]|[vv]|[vv,as v]] {10%}
n[[vv]|[vv]|[vv]|[vv,as v]] {30%}
nd[[vv]|[vv]|[vv]|[vv,as v]] {10%}
nj[[vv]|[vv]|[vv]|[vv,as v]] {40%}
nm[[vv]|[vv]|[vv]|[vv,as v]] {30%}
nn[[vv]|[vv]|[vv]|[vv,as v]] {40%}
nt[[vv]|[vv]|[vv]|[vv,as v]] {50%}
nth[[vv]|[vv]|[vv]|[vv,as v]] {10%}
nv[fbv] {20%}
nw[brv] {10%}
ny[[vv]|[vv]|[vv]|[vv,as v]] {20%}
nz[[vv]|[vv]|[vv]|[vv,as v]] {40%}
ng[[vv]|[vv]|[vv]|[vv,as v]] {20%}
nk[[vv]|[vv]|[vv]|[vv,as v]] {20%}
pl[[vv]|[vv]|[vv]|[vv,as v]] {5%}
pr[[vv]|[vv]|[vv]|[vv,as v]] {20%}
r[[vv]|[vv]|[vv]|[vv,as v]] {20%}
rd[[vv]|[vv]|[vv]|[vv,as v]] {30%}
rg[[vv]|[vv]|[vv]|[vv,as v]] {40%}
rj[[vv]|[vv]|[vv]|[vv,as v]] {10%}
rk[[vv]|[vv]|[vv]|[vv,as v]] {60%}
rl[[vv]|[vv]|[vv]|[vv,as v]] {20%}
rm[[vv]|[vv]|[vv]|[vv,as v]] {60%}
rn[[vv]|[vv]|[vv]|[vv,as v]] {20%}
rr[[vv]|[vv]|[vv]|[vv,as v]] {50%}
rs[[vv]|[vv]|[vv]|[vv,as v]] {30%}
rt[[vv]|[vv]|[vv]|[vv,as v]] {10%}
rth[[vv]|[vv]|[vv]|[vv,as v]] {20%}
rv[fbv] {60%}
rw[brv] {4%}
rz[[vv]|[vv]|[vv]|[vv,as v]] {20%}
sk[[vv]|[vv]|[vv]|[vv,as v]] {10%}
sn[[vv]|[vv]|[vv]|[vv,as v]] {20%}
sp[[vv]|[vv]|[vv]|[vv,as v]] {5%}
ss[[vv]|[vv]|[vv]|[vv,as v]] {30%}
st[[vv]|[vv]|[vv]|[vv,as v]] {60%}
sh[[vv]|[vv]|[vv]|[vv,as v]] {70%}
shr[[vv]|[vv]|[vv]|[vv,as v]] {40%}
ssh[[vv]|[vv]|[vv]|[vv,as v]] {10%}
sht[[vv]|[vv]|[vv]|[vv,as v]] {20%}
t[[vv]|[vv]|[vv]|[vv,as v]] {20%}
tr[[vv]|[vv]|[vv]|[vv,as v]] {30%}
th[[vv]|[vv]|[vv]|[vv,as v]] {80%}
thr[[vv]|[vv]|[vv]|[vv,as v]] {20%}
tl[[vv]|[vv]|[vv]|[vv,as v]] {30%}
tz[[vv]|[vv]|[vv]|[vv,as v]] {30%}
v[fbv] {50%}
w[brv] {5%}
y[[vv]|[vv]|[vv]|[vv,as v]] {60%}
z[[vv]|[vv]|[vv]|[vv,as v]] {40%}

"""
    def vv(self, v=False):
        """
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        e {v:e}
        e {v:e}
        e {v:e}
        e {v:e}
        e {v:e}
        e {v:e}
        e {v:e}
        i {v:i}
        i {v:i}
        i {v:i}
        i {v:i}
        i {v:i}
        i {v:i}
        i {v:i}
        o {v:o}
        o {v:o}
        o {v:o}
        o {v:o}
        o {v:o}
        u {v:u}
        u {v:u}
        u {v:u}
        u {v:u}
        a {v:a}{89%}
        ā {v:a}{41%}
        ae {v:e}{11%}
        ai {v:i}{44%}
        āi {v:i}{48%}
        ao {v:o}{19%}
        aō {v:o}{4%}
        au {v:u}{11%}
        e {v:e}{74%}
        ē {v:e}{11%}
        ea {v:a}{11%}
        ei {v:i}{7%}
        ēi {v:i}{4%}
        eu {v:u}{7%}
        i {v:i}{22%}
        ī {v:i}{26%}
        ia {v:a}{59%}
        iā {v:a}{4%}
        ie {v:e}{19%}
        iē {v:e}{4%}
        io {v:o}{30%}
        iō {v:o}{4%}
        iu {v:u}{7%}
        ō {v:o}{22%}
        u {v:u}{59%}
        ū {v:u}{15%}
        ua {v:a}{22%}
        ui {v:i}{7%}
        uo {v:o}{20%}
        """
        options = [
            
        ]
        choice = random.choice(options)
        if v:
            return choice[1]
        return choice[0]

    def fv(self, v=False):
        """
        $fv
        e {v:e}
        e {v:e}
        e {v:e}
        e {v:e}
        e {v:e}
        e {v:e}
        e {v:e}
        i {v:i}
        i {v:i}
        i {v:i}
        i {v:i}
        i {v:i}
        i {v:i}
        i {v:i}
        e {v:e}{74%}
        ē {v:e}{11%}
        ea {v:a}{11%}
        ei {v:i}{7%}
        ēi {v:i}{4%}
        eu {v:u}{7%}
        i {v:i}{22%}
        ī {v:i}{26%}
        ia {v:a}{59%}
        iā {v:a}{4%}
        ie {v:e}{19%}
        iē {v:e}{4%}
        io {v:o}{30%}
        iō {v:o}{4%}
        iu {v:u}{7%}
        """
        options = [
            
        ]
        choice = random.choice(options)
        if v:
            return choice[1]
        return choice[0]
    def bv(self, v=False):
        """
        $bv
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        o {v:o}
        o {v:o}
        o {v:o}
        o {v:o}
        o {v:o}
        u {v:u}
        u {v:u}
        u {v:u}
        u {v:u}
        a {v:a}{89%}
        ā {v:a}{41%}
        ae {v:e}{11%}
        ai {v:i}{44%}
        āi {v:i}{48%}
        ao {v:o}{19%}
        aō {v:o}{4%}
        au {v:u}{11%}
        ō {v:o}{22%}
        u {v:u}{59%}
        ū {v:u}{15%}
        ua {v:a}{22%}
        ui {v:i}{7%}
        uo {v:o}{20%}
        """
        options = [
            
        ]
        choice = random.choice(options)
        if v:
            return choice[1]
        return choice[0]

    def fbv(self, v=False):
        """
        $fbv
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        a {v:a}
        e {v:e}
        e {v:e}
        e {v:e}
        e {v:e}
        e {v:e}
        e {v:e}
        e {v:e}
        i {v:i}
        i {v:i}
        i {v:i}
        i {v:i}
        i {v:i}
        i {v:i}
        i {v:i}
        a {v:a}{89%}
        ā {v:a}{41%}
        ae {v:e}{11%}
        ai {v:i}{44%}
        āi {v:i}{48%}
        ao {v:o}{19%}
        aō {v:o}{4%}
        au {v:u}{11%}
        e {v:e}{74%}
        ē {v:e}{11%}
        ea {v:a}{11%}
        ei {v:i}{7%}
        ēi {v:i}{4%}
        eu {v:u}{7%}
        i {v:i}{22%}
        ī {v:i}{26%}
        ia {v:a}{59%}
        iā {v:a}{4%}
        ie {v:e}{19%}
        iē {v:e}{4%}
        io {v:o}{30%}
        iō {v:o}{4%}
        iu {v:u}{7%}
        """
        options = [
            
        ]
        choice = random.choice(options)
        if v:
            return choice[1]
        return choice[0]

    def brv(self, v=False):
        """
        o {v:o}
        o {v:o}
        o {v:o}
        o {v:o}
        o {v:o}
        u {v:u}
        u {v:u}
        u {v:u}
        u {v:u}
        ō {v:o}{22%}
        u {v:u}{59%}
        ū {v:u}{15%}
        ua {v:a}{22%}
        ui {v:i}{7%}
        uo {v:o}{20%}
        """
        options = [
            
        ]
        choice = random.choice(options)
        if v:
            return choice[1]
        return choice[0]
    
    def end(self):
        options = [
"k",
"l",
"n",
"n",
"n",
"n",
"n",
"r",
"s",
"s",
            
        ]
        self.random_add(options, "", 0.44)
        self.random_add(options, "d", 0.24)
        self.random_add(options, "l", 0.14)
        self.random_add(options, "m", 0.62)
        self.random_add(options, "n", 0.19)
        self.random_add(options, "ng", 0.57)
        self.random_add(options, "p", 0.10)
        self.random_add(options, "r", 0.19)
        self.random_add(options, "sh", 0.29)
        self.random_add(options, "t", 0.33)
        self.random_add(options, "th", 0.81)
        self.random_add(options, "z", 0.24)
        return random.choice(options)

    def name1(self):
        return self.first() + random.choice("", self.end(), self.end())

    def name2(self):
        options = [
            f"{self.first()}{self.second()}",
            f"{self.first()}{self.second()}{self.end()}",
        ]
        self.random_add(
            options,
            random.choice(
                [
                    f"{self.name1()}-{self.name1()}",
                    f"{self.name1()}-{self.name1()}",
                    f"{self.name1()} {self.name1()}",
                ]
            ),
            0.36,
        )
        return random.choice(options)

    def name3(self):
        options = [
            f"{self.first()}{self.second()}{self.second()}",
            f"{self.first()}{self.second()}{self.second()}{self.end()}",
        ]
        self.random_add(
            options,
            random.choice(
                [
                    f"{self.name1()}-{self.name1()}-{self.name1()}",
                    f"{self.name1()}-{self.name1()}-{self.name1()}",
                    f"{self.name1()} {self.name1()} {self.name1()}",
                ]
            ),
            0.06,
        )
        self.random_add(
            options,
            random.choice(
                [
                    f"{self.name1()}-{self.first()}{self.second()}"
                    + random.choice(["", self.end()]),
                    f"{self.name1()}-{self.first()}{self.second()}"
                    + random.choice(["", self.end()]),
                    f"{self.name1()} {self.first()}{self.second()}"
                    + random.choice(self.end()),
                ]
            ),
            0.09,
        )
        self.random_add(
            options,
            random.choice(
                [
                    f"{self.first()}{self.second()}"
                    + random.choice(["", self.end()])
                    + f"-{self.name1()}",
                    f"{self.name1()}-{self.first()}{self.second()}"
                    + random.choice(["", self.end()])
                    + f"-{self.name1()}",
                    f"{self.name1()} {self.first()}{self.second()}"
                    + random.choice(self.end())
                    + f" {self.name1()}",
                ]
            ),
            0.17,
        )
        return random.choice(options)

    def name4(self):
        options = [
            f"{self.first()}{self.second()}{self.second()}{self.second()}",
            f"{self.first()}{self.second()}{self.second()}{self.second()}{self.end()}",
        ]
        self.random_add(
            options,
            random.choice(
                [
                    self.first()
                    + self.second()
                    + random.choice(["", self.end()])
                    + "-"
                    + self.first()
                    + self.second()
                    + random.choice(["", self.end()]),
                    self.first()
                    + self.second()
                    + random.choice(["", self.end()])
                    + " "
                    + self.first()
                    + self.second()
                    + random.choice(["", self.end()]),
                    self.first()
                    + self.second()
                    + random.choice(["", self.end()])
                    + " "
                    + self.first()
                    + self.second()
                    + random.choice(["", self.end()]),
                ]
            ),
            0.86,
        )
        self.random_add(
            options,
            random.choice(
                [
                    self.name1()
                    + "-"
                    + self.first()
                    + self.second()
                    + self.second()
                    + random.choice(["", self.end()]),
                    self.name1()
                    + "-"
                    + self.first()
                    + self.second()
                    + self.second()
                    + random.choice(["", self.end()]),
                    self.name1()
                    + " "
                    + self.first()
                    + self.second()
                    + self.second()
                    + random.choice(["", self.end()]),
                ]
            ),
            0.14,
        )
        self.random_add(
            options,
            random.choice(
                [
                    self.first()
                    + self.second()
                    + self.second()
                    + random.choice(["", self.end()])
                    + "-"
                    + self.name1(),
                    self.first()
                    + self.second()
                    + self.second()
                    + random.choice(["", self.end()])
                    + " "
                    + self.name1(),
                    self.first()
                    + self.second()
                    + self.second()
                    + random.choice(["", self.end()])
                    + " "
                    + self.name1(),
                ]
            ),
            0.09,
        )
        return random.choice(options)

    def name5(self):
        options = [
            self.first()
            + self.second()
            + random.choice(["", self.end()])
            + "-"
            + self.first()
            + self.second()
            + self.second()
            + random.choice(["", self.end()]),
            self.first()
            + self.second()
            + random.choice(["", self.end()])
            + "-"
            + self.first()
            + self.second()
            + self.second()
            + random.choice(["", self.end()]),
            self.first()
            + self.second()
            + random.choice(["", self.end()])
            + " "
            + self.first()
            + self.second()
            + self.second()
            + random.choice(["", self.end()]),
        ]

        self.random_add(
            options,
            f"{self.first()}{self.second()}{self.second()}{self.second()}{self.second()}{random.choice(['', self.end()])}",
            0.67,
        )
        self.random_add(
            options,
            random.choice(
                [
                    self.first()
                    + self.second()
                    + self.second()
                    + random.choice(["", self.end()])
                    + "-"
                    + self.first()
                    + self.second()
                    + random.choice(["", self.end()]),
                    self.first()
                    + self.second()
                    + self.second()
                    + random.choice(["", self.end()])
                    + "-"
                    + self.first()
                    + self.second()
                    + random.choice(["", self.end()]),
                    self.first()
                    + self.second()
                    + self.second()
                    + random.choice(["", self.end()])
                    + " "
                    + self.first()
                    + self.second()
                    + random.choice(["", self.end()]),
                ]
            ),
            0.50,
        )
        return random.choice(options)

    def prompt(self):
        options = [
            self.name2(),
            self.name2(),
            self.name2(),
            self.name3(),
            self.name3(),
            self.name3(),
            self.name3(),
            self.name4(),
        ]
        self.random_add(options, self.name1(), 0.33)
        self.random_add(options, self.name2(), 0.82)
        self.random_add(options, self.name3(), 0.22)
        self.random_add(options, self.name4(), 0.33)
        self.random_add(options, self.name5(), 0.27)
        self.random_add(
            options,
            f"{self.first()}{self.second()}{self.second}{random.choice(['', self.end()])} {self.first()}{self.second()}{self.second}{random.choice(['', self.end()])}",
            0.02,
        )
        return random.choice(options)


class ScarletDynastyName(RandomName):
    """
    Based on Scarley Dynasty Name Generator: https://orteil.dashnet.org/randomgen/?gen=AYsfB34A
    """

    def house(self):
        return random.choice(
            [
                "Cathak",
                "Cathak Cacek",
                "Cathak Garel",
                "Cynis",
                f"Cynis {random.choice(['', 'Belar', 'Belar', 'Denovah'])}",
                f"Cynis {random.choice(['Falen', 'Wisel'])}",
                "Iselsi",
                f"Iselsi {random.choice(['Enuma', 'Saraban'])}",
                "Ledaal",
                "Ledaal Catala",
                "Ledaal Kebok",
                "Mnemon",
                "Mnemon Caras",
                "Mnemon Darow",
                "Nellens",
                "Nellens",
                "Peleps",
                f"Peleps {random.choice(['', 'Danic', 'Nalin'])}",
                f"Peleps {random.choice(['Kaizoku', 'Najalin'])}",
                "Ragara",
                "Ragara Calel",
                "Ragara Soras",
                "Sesus",
                f"Sesus {random.choice(['Alon', 'Chenow', 'Denerid', 'Kajak', 'Magel'])}",
                f"Sesus {random.choice(['Alon', 'Chenow', 'Denerid', 'Kajak', 'Magel'])}",
                "Tepet",
                f"Tepet {random.choice(['Berel', 'Marek', 'Nerigus', 'Tilis', 'Vergus'])}",
                f"Tepet {random.choice(['Berel', 'Deramol', 'Marek', 'Nerigus', 'Tilis', 'Vergus'])}",
            ]
        )

    def firstsyl(self):
        options = [
            "A",
            "A",
            "A",
            "A",
            "A",
            "A",
            "A",
            "A",
            "Ba",
            "Ba",
            "Be",
            "Be",
            "Ca",
            "Ca",
            "Ca",
            "Ca",
            "Che",
            "Chi",
            "Cho",
            "Co",
            "Cy",
            "Da",
            "Da",
            "Da",
            "De",
            "De",
            "De",
            "De",
            "Di",
            "Du",
            "E",
            "E",
            "E",
            "E",
            "Fa",
            "Fe",
            "Fe",
            "Ga",
            "Ge",
            "Gu",
            "Ha",
            "Ha",
            "He",
            "Ho",
            "I",
            "I",
            "I",
            "I",
            "Ja",
            "Ja",
            "Je",
            "Ka",
            "Ka",
            "Ke",
            "Ke",
            "Ke",
            "Ki",
            "La",
            "La",
            "Le",
            "Le",
            "Li",
            "Lo",
            "Lu",
            "Ma",
            "Ma",
            "Ma",
            "Ma",
            "Ma",
            "Ma",
            "Ma",
            "Me",
            "Mi",
            "Mi",
            "Mo",
            "My",
            "Na",
            "Na",
            "Ne",
            "Ne",
            "No",
            "No",
            "O",
            "O",
            "O",
            "Pa",
            "Pe",
            "Pi",
            "Po",
            "Ra",
            "Ra",
            "Ra",
            "Ri",
            "Ro",
            "Sa",
            "Sa",
            "Se",
            "Se",
            "Shu",
            "Si",
            "So",
            "Su",
            "Ta",
            "Ta",
            "Ta",
            "Ta",
            "Te",
            "Ti",
            "Ti",
            "To",
            "Tu",
            "U",
            "U",
            "U",
            "Va",
            "Ve",
            "Vo",
            "Wi",
            "Ya",
            "Yo",
        ]
        self.random_app(options, "An'", 0.5)
        self.random_app(options, "Ba", 0.5)
        self.random_app(options, "Bae", 0.5)
        self.random_app(options, "Be", 0.5)
        self.random_app(options, "Bha", 0.5)
        self.random_app(options, "Bhu", 0.5)
        self.random_app(options, "Bi", 0.5)
        self.random_app(options, "Bo", 0.5)
        self.random_app(options, "Bu", 0.5)
        self.random_app(options, "Ca", 0.5)
        self.random_app(options, "Cai", 0.5)
        self.random_app(options, "Ce", 0.5)
        self.random_app(options, "Cha", 0.5)
        self.random_app(options, "Che", 0.5)
        self.random_app(options, "Chu", 0.5)
        self.random_app(options, "Cu", 0.5)
        self.random_app(options, "Do", 0.5)
        self.random_app(options, "Dro", 0.5)
        self.random_app(options, "E", 0.5)
        self.random_app(options, "Fe", 0.5)
        self.random_app(options, "Fi", 0.5)
        self.random_app(options, "Fo", 0.5)
        self.random_app(options, "Fu", 0.5)
        self.random_app(options, "Ga", 0.5)
        self.random_app(options, "Gi", 0.5)
        self.random_app(options, "Go", 0.5)
        self.random_app(options, "Hi", 0.5)
        self.random_app(options, "How", 0.1)
        self.random_app(options, "Hu", 0.5)
        self.random_app(options, "Jo", 0.5)
        self.random_app(options, "Kai", 0.5)
        self.random_app(options, "Ko", 0.5)
        self.random_app(options, "Ku", 0.5)
        self.random_app(options, "Lo", 0.5)
        self.random_app(options, "Ma", 0.5)
        self.random_app(options, "Me", 0.5)
        self.random_app(options, "Mne", 0.5)
        self.random_app(options, "Moi", 0.5)
        self.random_app(options, "Mu", 0.5)
        self.random_app(options, "Na", 0.5)
        self.random_app(options, "Ne", 0.5)
        self.random_app(options, "Ni", 0.5)
        self.random_app(options, "Nu", 0.5)
        self.random_app(options, "Po", 0.5)
        self.random_app(options, "Pu", 0.5)
        self.random_app(options, "R'", 0.5)
        self.random_app(options, "Re", 0.5)
        self.random_app(options, "Ro", 0.5)
        self.random_app(options, "Ru", 0.5)
        self.random_app(options, "Sa", 0.5)
        self.random_app(options, "Si", 0.5)
        self.random_app(options, "So", 0.5)
        self.random_app(options, "Sza", 0.5)
        self.random_app(options, "Tai", 0.5)
        self.random_app(options, "Ty", 0.5)
        self.random_app(options, "V'", 0.5)
        self.random_app(options, "Ve", 0.5)
        self.random_app(options, "Wa", 0.5)
        self.random_app(options, "We", 0.5)
        self.random_app(options, "Wo", 0.5)
        self.random_app(options, "Wu", 0.5)
        self.random_app(options, "Ye", 0.5)
        self.random_app(options, "Yi", 0.5)
        self.random_app(options, "Yu", 0.5)
        return random.choice(options)

    def midsyl(self):
        return random.choice(
            [
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
        )

    def lastsyl(self):
        return random.choice(
            [
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
        )

    def first(self):
        options = [
            "B"
            "B"
            "B"
            "C"
            "C"
            "C"
            "C"
            "Ch"
            "Ch"
            "D"
            "D"
            "D"
            "D"
            "F"
            "F"
            "G"
            "G"
            "H"
            "H"
            "J"
            "K"
            "K"
            "K"
            "L"
            "L"
            "L"
            "L"
            "M"
            "M"
            "M"
            "M"
            "M"
            "M"
            "N"
            "N"
            "N"
            "N"
            "P"
            "P"
            "R"
            "R"
            "R"
            "S"
            "S"
            "S"
            "S"
            "T"
            "T"
            "T"
            "T"
            "T"
            "V"
            "W"
            "Y"
        ]
        self.random_add(options, "B", 0.50)
        self.random_add(options, "Bh", 0.50)
        self.random_add(options, "Ch", 0.25)
        self.random_add(options, "D", 0.50)
        self.random_add(options, "Dr", 0.25)
        self.random_add(options, "F", 0.50)
        self.random_add(options, "G", 0.25)
        self.random_add(options, "H", 0.25)
        self.random_add(options, "J", 0.75)
        self.random_add(options, "K", 0.50)
        self.random_add(options, "M", 0.25)
        self.random_add(options, "Mn", 0.25)
        self.random_add(options, "R", 0.25)
        self.random_add(options, "S", 0.25)
        self.random_add(options, "Sz", 0.25)
        self.random_add(options, "V", 0.75)
        self.random_add(options, "W", 0.25)
        self.random_add(options, "Y", 0.75)
        return random.choice(options)

    def vv(self):
        options = [
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
        ]
        self.random_add(options, "ey", 0.03)
        self.random_add(options, "iou", 0.03)
        self.random_add(options, "oi", 0.03)
        self.random_add(options, "y", 0.03)
        return random.choice(options)

    def end(self):
        options = [
            "k",
            "l",
            "l",
            "l",
            "m",
            "n",
            "n",
            "n",
            "n",
            "n",
            "r",
            "r",
            "r",
            "s",
            "s",
            "s",
            "s",
            "s",
            "t",
            "t",
        ]
        self.random_add(options, "c", 0.75)
        self.random_add(options, "d", 0.75)
        self.random_add(options, "f", 0.50)
        self.random_add(options, "k", 0.75)
        self.random_add(options, "l", 0.75)
        self.random_add(options, "lt", 0.25)
        self.random_add(options, "n", 0.75)
        self.random_add(options, "nd", 0.25)
        self.random_add(options, "ns", 0.25)
        self.random_add(options, "p", 0.25)
        self.random_add(options, "q", 0.25)
        self.random_add(options, "r", 0.75)
        self.random_add(options, "rn", 0.25)
        self.random_add(options, "sh", 0.25)
        self.random_add(options, "sm", 0.25)
        self.random_add(options, "th", 0.25)
        self.random_add(options, "v", 0.25)
        self.random_add(options, "a", 0.15)
        self.random_add(options, "e", 0.15)
        self.random_add(options, "i", 0.25)
        return random.choice(options)

    def single(self):
        return f"{self.first()}{self.vv()}{self.end()}"

    def prompt(self):
        options = [
            f"{self.house()} {self.firstsyl()}{self.lastsyl()}",
            f"{self.house()} {self.firstsyl()}{self.lastsyl()}",
            f"{self.house()} {self.firstsyl()}{self.midsyl()}{self.lastsyl()}",
        ]
        self.random_add(options, f"{self.house()} {self.single()}", 0.09)
        self.random_add(
            options,
            f"{self.house()} {self.firstsyl()}{self.midsyl()}{self.lastsyl()}",
            0.25,
        )
        self.random_add(
            options,
            f"{self.house()} {self.firstsyl()}{self.midsyl()}{self.midsyl()}{self.lastsyl()}",
            0.08,
        )
        return random.choice(options)
