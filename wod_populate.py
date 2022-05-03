from wod.models import MageFaction, Paradigm, Practice, Instrument
from core.models import Medium, Material, Language

english = Language.objects.create(name="English", frequency=141264)
german = Language.objects.create(name="German", frequency=20058)
french = Language.objects.create(name="French", frequency=19617)
spanish = Language.objects.create(name="Spanish", frequency=17669)
japanese = Language.objects.create(name="Japanese", frequency=13530)
Language.objects.create(name="Russian", frequency=11837)
Language.objects.create(name="Italian", frequency=8672)
chinese = Language.objects.create(name="Chinese", frequency=8439)
Language.objects.create(name="Portuguese", frequency=5765)
farsi = Language.objects.create(name="Persian", frequency=4727)
Language.objects.create(name="Polish", frequency=4551)
arabic = Language.objects.create(name="Arabic", frequency=4535)
Language.objects.create(name="Dutch", frequency=4436)
Language.objects.create(name="Ukrainian", frequency=3228)
hebrew = Language.objects.create(name="Hebrew", frequency=3059)
Language.objects.create(name="Swedish", frequency=2918)
Language.objects.create(name="Indonesian", frequency=2700)
Language.objects.create(name="Czech", frequency=2401)
korean = Language.objects.create(name="Korean", frequency=2013)
Language.objects.create(name="Finnish", frequency=1956)
Language.objects.create(name="Hungarian", frequency=1858)
vietnamese = Language.objects.create(name="Vietnamese", frequency=1798)
Language.objects.create(name="Catalan", frequency=1773)
Language.objects.create(name="Norwegian (Bokmål)", frequency=1608)
thai = Language.objects.create(name="Thai", frequency=1453)
hindi = Language.objects.create(name="Hindi", frequency=1406)
Language.objects.create(name="Danish", frequency=1151)
Language.objects.create(name="Romanian", frequency=1128)
greek = Language.objects.create(name="Greek", frequency=1102)
koine_greek = Language.objects.create(name="Koine Greek", frequency=0)
Language.objects.create(name="Serbian", frequency=1082)
Language.objects.create(name="Bengali", frequency=996)
Language.objects.create(name="Simple English", frequency=855)
Language.objects.create(name="Turkish", frequency=803)
Language.objects.create(name="Bulgarian", frequency=793)
Language.objects.create(name="Armenian", frequency=785)
Language.objects.create(name="Azerbaijani", frequency=668)
Language.objects.create(name="Basque", frequency=660)
Language.objects.create(name="Estonian", frequency=648)
Language.objects.create(name="Croatian", frequency=554)
Language.objects.create(name="Slovak", frequency=552)
Language.objects.create(name="Malay", frequency=519)
Language.objects.create(name="Galician", frequency=462)
Language.objects.create(name="Slovenian", frequency=426)
Language.objects.create(name="Tamil", frequency=401)
Language.objects.create(name="Esperanto", frequency=390)
Language.objects.create(name="Malayalam", frequency=361)
Language.objects.create(name="Lithuanian", frequency=359)
Language.objects.create(name="Marathi", frequency=355)
Language.objects.create(name="Georgian", frequency=327)
Language.objects.create(name="Albanian", frequency=301)
Language.objects.create(name="Kannada", frequency=300)
Language.objects.create(name="Latvian", frequency=297)
Language.objects.create(name="Urdu", frequency=274)
Language.objects.create(name="Belarusian", frequency=268)
Language.objects.create(name="Macedonian", frequency=260)
Language.objects.create(name="Cantonese", frequency=254)
Language.objects.create(name="Kazakh", frequency=233)
Language.objects.create(name="Serbo-Croatian", frequency=203)
Language.objects.create(name="Icelandic", frequency=191)
Language.objects.create(name="Bosnian", frequency=187)
Language.objects.create(name="Cebuano", frequency=172)
Language.objects.create(name="Telugu", frequency=170)
Language.objects.create(name="Afrikaans", frequency=166)
Language.objects.create(name="Norwegian (Nynorsk)", frequency=162)
latin = Language.objects.create(name="Latin", frequency=158)
Language.objects.create(name="Asturian", frequency=158)
welsh = Language.objects.create(name="Welsh", frequency=154)
Language.objects.create(name="Tagalog", frequency=145)
Language.objects.create(name="Javanese", frequency=136)
Language.objects.create(name="Konkani", frequency=136)
sanskrit = Language.objects.create(name="Sanskrit", frequency=134)
Language.objects.create(name="Uzbek", frequency=129)
swahili = Language.objects.create(name="Swahili", frequency=129)
Language.objects.create(name="Belarusian (Taraškievica)", frequency=122)
Language.objects.create(name="Breton", frequency=115)
Language.objects.create(name="Mongolian", frequency=115)
Language.objects.create(name="Burmese", frequency=114)
Language.objects.create(name="Egyptian Arabic", frequency=110)
egyptian = Language.objects.create(name="Ancient Egyptian", frequency=0)
irish = Language.objects.create(name="Irish", frequency=108)
Language.objects.create(name="Eastern Punjabi", frequency=108)
Language.objects.create(name="Scots", frequency=106)
Language.objects.create(name="Kurdish (Sorani)", frequency=105)
Language.objects.create(name="Nepali", frequency=100)
Language.objects.create(name="Luxembourgish", frequency=97)
Language.objects.create(name="Southern Azerbaijani", frequency=95)
Language.objects.create(name="Alemannic", frequency=94)
Language.objects.create(name="Occitan", frequency=92)
Language.objects.create(name="Tatar", frequency=88)
Language.objects.create(name="Gujarati", frequency=84)
Language.objects.create(name="Classical Chinese", frequency=83)
Language.objects.create(name="Bashkir", frequency=82)
Language.objects.create(name="Waray", frequency=81)
Language.objects.create(name="Assamese", frequency=78)
Language.objects.create(name="Sundanese", frequency=76)
Language.objects.create(name="Somali", frequency=76)
Language.objects.create(name="Kirghiz", frequency=74)
Language.objects.create(name="Khmer", frequency=72)
Language.objects.create(name="West Frisian", frequency=71)
Language.objects.create(name="Aragonese", frequency=69)
Language.objects.create(name="Min Nan", frequency=68)
Language.objects.create(name="Tajik", frequency=68)
Language.objects.create(name="Sinhalese", frequency=68)
Language.objects.create(name="Bavarian", frequency=67)
Language.objects.create(name="Minangkabau", frequency=65)
Language.objects.create(name="Kurdish (Kurmanji)", frequency=63)
Language.objects.create(name="Odia", frequency=62)
Language.objects.create(name="Yiddish", frequency=55)
Language.objects.create(name="Low Saxon", frequency=52)
Language.objects.create(name="Wu", frequency=52)
Language.objects.create(name="Amharic", frequency=50)
Language.objects.create(name="Interlingua", frequency=48)
Language.objects.create(name="Anglo-Saxon", frequency=48)
Language.objects.create(name="Lombard", frequency=47)
afghan = Language.objects.create(name="Pashto", frequency=47)
Language.objects.create(name="Malagasy", frequency=45)
Language.objects.create(name="Bhojpuri", frequency=44)
Language.objects.create(name="Venetian", frequency=43)
Language.objects.create(name="Ido", frequency=42)
Language.objects.create(name="Sindhi", frequency=42)
Language.objects.create(name="Maltese", frequency=42)
Language.objects.create(name="Western Punjabi", frequency=41)
Language.objects.create(name="Faroese", frequency=41)
Language.objects.create(name="Chechen", frequency=40)
Language.objects.create(name="Limburgish", frequency=40)
Language.objects.create(name="Chuvash", frequency=38)
Language.objects.create(name="Central Bicolano", frequency=38)
Language.objects.create(name="Turkmen", frequency=38)
yoruba = Language.objects.create(name="Yoruba", frequency=37)
Language.objects.create(name="Maithili", frequency=37)
Language.objects.create(name="Sicilian", frequency=36)
Language.objects.create(name="Haitian", frequency=34)
Language.objects.create(name="Mazandarani", frequency=34)
Language.objects.create(name="Sakha", frequency=34)
quechua = Language.objects.create(name="Quechua", frequency=33)
Language.objects.create(name="West Flemish", frequency=33)
Language.objects.create(name="Mingrelian", frequency=32)
Language.objects.create(name="Fiji Hindi", frequency=32)
Language.objects.create(name="Zulu", frequency=32)
Language.objects.create(name="Bishnupriya Manipuri", frequency=31)
gaelic = Language.objects.create(name="Scottish Gaelic", frequency=31)
Language.objects.create(name="Tibetan", frequency=31)
Language.objects.create(name="Piedmontese", frequency=30)
Language.objects.create(name="Zazaki", frequency=30)
Language.objects.create(name="Dutch Low Saxon", frequency=30)
Language.objects.create(name="Volapük", frequency=29)
Language.objects.create(name="Newar", frequency=29)
Language.objects.create(name="Upper Sorbian", frequency=29)
Language.objects.create(name="Hakka", frequency=29)
Language.objects.create(name="Santali", frequency=29)
Language.objects.create(name="Samogitian", frequency=28)
Language.objects.create(name="Banyumasan", frequency=27)
Language.objects.create(name="Northern Sami", frequency=27)
Language.objects.create(name="Sardinian", frequency=27)
Language.objects.create(name="Lao", frequency=27)
Language.objects.create(name="Igbo", frequency=27)
Language.objects.create(name="Acehnese", frequency=26)
Language.objects.create(name="Northern Luri", frequency=26)
Language.objects.create(name="Old Church Slavonic", frequency=26)
Language.objects.create(name="North Frisian", frequency=25)
Language.objects.create(name="Rusyn", frequency=25)
Language.objects.create(name="Crimean Tatar", frequency=25)
Language.objects.create(name="Ligurian", frequency=25)
Language.objects.create(name="Hausa", frequency=25)
Language.objects.create(name="Tulu", frequency=25)
Language.objects.create(name="Cherokee", frequency=25)
Language.objects.create(name="Xhosa", frequency=25)
Language.objects.create(name="Ilocano", frequency=24)
Language.objects.create(name="Meadow Mari", frequency=24)
Language.objects.create(name="Vepsian", frequency=24)
Language.objects.create(name="Picard", frequency=24)
Language.objects.create(name="Interlingue", frequency=24)
Language.objects.create(name="Ladino", frequency=24)
Language.objects.create(name="Emilian-Romagnol", frequency=23)
Language.objects.create(name="Ossetian", frequency=23)
Language.objects.create(name="Extremaduran", frequency=23)
Language.objects.create(name="Buginese", frequency=22)
Language.objects.create(name="Silesian", frequency=22)
Language.objects.create(name="Maori", frequency=22)
Language.objects.create(name="Corsican", frequency=22)
Language.objects.create(name="Kashubian", frequency=22)
Language.objects.create(name="Friulian", frequency=22)
Language.objects.create(name="Manx", frequency=21)
Language.objects.create(name="Chavacano", frequency=21)
Language.objects.create(name="Doteli", frequency=21)
Language.objects.create(name="Buryat", frequency=21)
Language.objects.create(name="Neapolitan", frequency=20)
Language.objects.create(name="Erzya", frequency=20)
Language.objects.create(name="Lezgian", frequency=20)
Language.objects.create(name="Guarani", frequency=20)
Language.objects.create(name="Romansh", frequency=20)
Language.objects.create(name="Papiamentu", frequency=20)
Language.objects.create(name="Pennsylvania German", frequency=20)
Language.objects.create(name="Min Dong", frequency=19)
Language.objects.create(name="Kapampangan", frequency=19)
nahuatl = Language.objects.create(name="Nahuatl", frequency=19)
Language.objects.create(name="Gan", frequency=19)
Language.objects.create(name="Cornish", frequency=19)
Language.objects.create(name="Mirandese", frequency=19)
Language.objects.create(name="Lingua Franca Nova", frequency=19)
Language.objects.create(name="Lower Sorbian", frequency=19)
Language.objects.create(name="Divehi", frequency=19)
Language.objects.create(name="Gorontalo", frequency=19)
Language.objects.create(name="Zhuang", frequency=19)
Language.objects.create(name="Gothic", frequency=19)
Language.objects.create(name="Dzongkha", frequency=19)
Language.objects.create(name="Walloon", frequency=18)
Language.objects.create(name="Komi", frequency=18)
Language.objects.create(name="Uyghur", frequency=18)
Language.objects.create(name="Abkhazian", frequency=18)
Language.objects.create(name="Wolof", frequency=18)
Language.objects.create(name="Atikamekw", frequency=18)
Language.objects.create(name="Norman", frequency=17)
Language.objects.create(name="Livvi-Karelian", frequency=17)
Language.objects.create(name="Palatinate German", frequency=17)
Language.objects.create(name="Avar", frequency=17)
Language.objects.create(name="Tuvan", frequency=17)
Language.objects.create(name="Aromanian", frequency=17)
Language.objects.create(name="Chichewa", frequency=17)
Language.objects.create(name="Hill Mari", frequency=16)
Language.objects.create(name="Zeelandic", frequency=16)
Language.objects.create(name="Udmurt", frequency=16)
Language.objects.create(name="Shona", frequency=16)
Language.objects.create(name="Saterland Frisian", frequency=16)
Language.objects.create(name="Lingala", frequency=16)
Language.objects.create(name="Kabyle", frequency=16)
Language.objects.create(name="Ripuarian", frequency=16)
Language.objects.create(name="Gagauz", frequency=16)
Language.objects.create(name="Banjar", frequency=16)
Language.objects.create(name="Bislama", frequency=16)
oromo = Language.objects.create(name="Oromo", frequency=16)
Language.objects.create(name="Norfolk", frequency=16)
Language.objects.create(name="Twi", frequency=16)
Language.objects.create(name="Akan", frequency=16)
Language.objects.create(name="Dinka", frequency=16)
Language.objects.create(name="Gilaki", frequency=15)
Language.objects.create(name="Hawaiian", frequency=15)
Language.objects.create(name="Franco-Provençal", frequency=15)
Language.objects.create(name="Romani", frequency=15)
Language.objects.create(name="Chamorro", frequency=15)
Language.objects.create(name="Aymara", frequency=14)
Language.objects.create(name="Komi-Permyak", frequency=14)
Language.objects.create(name="Greenlandic", frequency=14)
aramaic = Language.objects.create(name="Aramaic", frequency=14)
Language.objects.create(name="Tetum", frequency=14)
Language.objects.create(name="Latgalian", frequency=14)
Language.objects.create(name="Bambara", frequency=14)
Language.objects.create(name="Adyghe", frequency=14)
Language.objects.create(name="Tarantino", frequency=13)
Language.objects.create(name="Võro", frequency=13)
Language.objects.create(name="Kalmyk", frequency=13)
Language.objects.create(name="Ingush", frequency=13)
Language.objects.create(name="Pontic", frequency=13)
Language.objects.create(name="Kinyarwanda", frequency=12)
Language.objects.create(name="Tok Pisin", frequency=12)
Language.objects.create(name="Lojban", frequency=12)
Language.objects.create(name="Luganda", frequency=12)
Language.objects.create(name="Kirundi", frequency=12)
Language.objects.create(name="Pangasinan", frequency=11)
Language.objects.create(name="Kabiye", frequency=11)
Language.objects.create(name="Nauruan", frequency=11)
Language.objects.create(name="Tahitian", frequency=11)
Language.objects.create(name="Moksha", frequency=11)
Language.objects.create(name="Cheyenne", frequency=11)
Language.objects.create(name="Tsonga", frequency=11)
Language.objects.create(name="Sesotho", frequency=11)
Language.objects.create(name="Fijian", frequency=11)
Language.objects.create(name="Inuktitut", frequency=11)
Language.objects.create(name="Cree", frequency=11)
Language.objects.create(name="Samoan", frequency=10)
Language.objects.create(name="Tswana", frequency=10)
Language.objects.create(name="Swati", frequency=10)
navaho = Language.objects.create(name="Navajo", frequency=9)
Language.objects.create(name="Karachay-Balkar", frequency=9)
Language.objects.create(name="Karakalpak", frequency=9)
Language.objects.create(name="Novial", frequency=9)
Language.objects.create(name="Jamaican Patois", frequency=9)
Language.objects.create(name="Kabardian", frequency=9)
Language.objects.create(name="Kikuyu", frequency=9)
Language.objects.create(name="Sranan", frequency=9)
Language.objects.create(name="Kashmiri", frequency=9)
Language.objects.create(name="Tongan", frequency=8)
Language.objects.create(name="Inupiak", frequency=8)
Language.objects.create(name="Northern Sotho", frequency=7)
Language.objects.create(name="Lak", frequency=7)
Language.objects.create(name="Kongo", frequency=7)
Language.objects.create(name="Tumbuka", frequency=7)
Language.objects.create(name="Sango", frequency=7)
Language.objects.create(name="Fula", frequency=7)
Language.objects.create(name="Pali", frequency=6)
Language.objects.create(name="Ewe", frequency=6)
Language.objects.create(name="Venda", frequency=6)
Language.objects.create(name="Tigrinya", frequency=6)
Language.objects.create(name="Herero", frequency=1)
Language.objects.create(name="Ndonga", frequency=0)
Language.objects.create(name="Choctaw", frequency=0)
Language.objects.create(name="Marshallese", frequency=0)
Language.objects.create(name="Kuanyama", frequency=0)
Language.objects.create(name="Nuosu", frequency=0)
Language.objects.create(name="Hiri Motu", frequency=0)
Language.objects.create(name="Afar", frequency=0)
Language.objects.create(name="Muscogee", frequency=0)
Language.objects.create(name="Kanuri", frequency=0)
algonquin = Language.objects.create(name="Algonquin", frequency=0)
mayan = Language.objects.create(name="Mayan", frequency=0)
iroquois = Language.objects.create(name="Iroquois", frequency=0)
sioux = Language.objects.create(name="Sioux", frequency=0)
anguthimri = Language.objects.create(name="Anguthimri", frequency=0)

bone = Material.objects.create(name="Bone")
cloth = Material.objects.create(name="Cloth")
iron = Material.objects.create(name="Iron")
leather = Material.objects.create(name="Leather")
paper = Material.objects.create(name="Paper")
parchment = Material.objects.create(name="Parchment")
steel = Material.objects.create(name="Steel")
vellum = Material.objects.create(name="Vellum")
wood = Material.objects.create(name="Wood")

book = Medium.objects.create(name="Book")
ebook = Medium.objects.create(name="eBook", length_modifier_type="division", length_modifier=1)
flash_drive = Medium.objects.create(name="Flash Drive", length_modifier_type="division", length_modifier=1)
scrolls = Medium.objects.create(name="Scrolls", length_modifier_type="division", length_modifier=1)
software = Medium.objects.create(name="Software", length_modifier_type="division", length_modifier=1)
tablets = Medium.objects.create(name="Tablets", length_modifier_type="division", length_modifier=1)

armor = Instrument.objects.create(name="Armor")
artwork = Instrument.objects.create(name="Artwork")
atrocity = Instrument.objects.create(name="Atrocity")
blessings = Instrument.objects.create(name="Blessings and curses")
blood = Instrument.objects.create(name="Blood and fluids")
body_modification = Instrument.objects.create(name="Body Modification")
bodywork = Instrument.objects.create(name="Bodywork")
bones = Instrument.objects.create(name="Bones and remains")
books = Instrument.objects.create(name="Books and periodicals")
brain_computer_interface = Instrument.objects.create(name="Brain/Computer interface")
brews = Instrument.objects.create(name="Brews and concoctions")
cannibalism = Instrument.objects.create(name="Cannibalism")
cards = Instrument.objects.create(name="Cards and instruments of chance")
celestial_alignments = Instrument.objects.create(name="Celestial alignments")
circles = Instrument.objects.create(name="Circles and designs")
computer_gear = Instrument.objects.create(name="Computer gear")
cosmetics = Instrument.objects.create(name="Cosmetics")
crossroads = Instrument.objects.create(name="Crossroads and crossing-days")
cups = Instrument.objects.create(name="Cups and vessels")
cybernetic_implants = Instrument.objects.create(name="Cybernetic Implants")
dances = Instrument.objects.create(name="Dances and movement")
devices = Instrument.objects.create(name="Devices and machines")
drugs = Instrument.objects.create(name="Drugs and poisons")
elements = Instrument.objects.create(name="Elements")
energy = Instrument.objects.create(name="Energy")
eye_contact = Instrument.objects.create(name="Eye contact")
fashion = Instrument.objects.create(name="Fashion")
food = Instrument.objects.create(name="Food and drink")
formulae = Instrument.objects.create(name="Formulae and math")
gadgets = Instrument.objects.create(name="Gadgets and inventions")
gems = Instrument.objects.create(name="Gems and stones")
genetic_manipulation = Instrument.objects.create(name="Genetic Manipulation")
group_rites = Instrument.objects.create(name="Group rites")
herbs = Instrument.objects.create(name="Herbs and plants")
household_tools = Instrument.objects.create(name="Household tools")
hypersigils = Instrument.objects.create(name="Hypersigils")
internet_activity = Instrument.objects.create(name="Internet Activity")
knots = Instrument.objects.create(name="Knots and ropes")
labs = Instrument.objects.create(name="Labs and gear")
languages = Instrument.objects.create(name="Languages")
management = Instrument.objects.create(name="Management and HR")
mass_media = Instrument.objects.create(name="Mass media")
medical_procedures = Instrument.objects.create(name="Medical Procedures")
meditation = Instrument.objects.create(name="Meditation")
money = Instrument.objects.create(name="Money and wealth")
music = Instrument.objects.create(name="Music")
mutilation = Instrument.objects.create(name="Mutilation")
nanotech = Instrument.objects.create(name="Nanotech")
numbers = Instrument.objects.create(name="Numbers and numerology")
offerings = Instrument.objects.create(name="Offerings and sacrifices")
ordeals = Instrument.objects.create(name="Ordeals and exertions")
perversion = Instrument.objects.create(name="Perversion")
prayers = Instrument.objects.create(name="Prayers and invocations")
sacred_iconography = Instrument.objects.create(name="Sacred iconography")
sex = Instrument.objects.create(name="Sex and sensuality")
social_dominion = Instrument.objects.create(name="Social domination")
symbols = Instrument.objects.create(name="Symbols")
thought_forms = Instrument.objects.create(name="Thought-forms")
torment = Instrument.objects.create(name="Torment")
toys = Instrument.objects.create(name="Toys")
transgression = Instrument.objects.create(name="Transgression")
tricks = Instrument.objects.create(name="Tricks and illusions")
trolling = Instrument.objects.create(name="Trolling and Cyberbullying")
true_names = Instrument.objects.create(name="True Names")
vehicles = Instrument.objects.create(name="Vehicles")
violation = Instrument.objects.create(name="Violation")
voice = Instrument.objects.create(name="Voice and vocalizations")
wands = Instrument.objects.create(name="Wands and staves")
weapons = Instrument.objects.create(name="Weapons")
writings = Instrument.objects.create(name="Writings, inscriptions and runes")

abyssalism = Practice.objects.create(
    name="Abyssalism", abilities=["Cosmology", "Engimas", "Subterfuge"]
)
abyssalism.instruments.add(
    atrocity,
    artwork,
    blood,
    bones,
    books,
    brews,
    cannibalism,
    celestial_alignments,
    circles,
    cybernetic_implants,
    perversion,
    cups,
    dances,
    devices,
    drugs,
    elements,
    eye_contact,
    fashion,
    formulae,
    group_rites,
    languages,
    meditation,
    music,
    offerings,
    ordeals,
    sex,
    symbols,
    thought_forms,
    torment,
    transgression,
    violation,
    voice,
    weapons,
    writings,
)
abyssalism.save()
alchemy = Practice.objects.create(
    name="Alchemy",
    abilities=[
        "Art",
        "Crafts",
        "Cryptography",
        "Enigmas",
        "Esoterica",
        "Medicine",
        "Pharmacopeia",
        "Science",
    ],
)
alchemy.instruments.add(books, brews, circles, devices, drugs, formulae, labs)
alchemy.save()
animalism = Practice.objects.create(
    name="Animalism",
    abilities=[
        "Athletics",
        "Awareness",
        "Brawl",
        "Crafts",
        "Esoterica",
        "Hunting",
        "Martial Arts",
        "Stealth",
        "Survival",
    ],
)
animalism.instruments.add(
    armor,
    artwork,
    blood,
    bones,
    brews,
    circles,
    cups,
    dances,
    drugs,
    eye_contact,
    fashion,
    food,
    herbs,
    languages,
    voice,
    music,
    offerings,
    prayers,
    ordeals,
    social_dominion,
    symbols,
    thought_forms,
    weapons,
    devices,
    gadgets,
    body_modification,
    cybernetic_implants,
    genetic_manipulation,
    medical_procedures,
    computer_gear,
)
animalism.save()
art_of_desire = Practice.objects.create(
    name="Art of Desire/Hyperconomics",
    abilities=[
        "Academics",
        "Athletics",
        "Awareness",
        "Carousing",
        "Etiquette",
        "Expression",
        "Finance",
        "Intimidation",
        "Leadership",
        "Martial Arts",
        "Media",
        "Politics",
        "Seduction",
        "Subterfuge",
    ],
)
art_of_desire.instruments.add(
    cards,
    cosmetics,
    dances,
    eye_contact,
    fashion,
    gadgets,
    mass_media,
    money,
    sex,
    social_dominion,
    vehicles,
    voice,
    weapons,
)
art_of_desire.save()
bardism = Practice.objects.create(
    name="Bardism",
    abilities=[
        "Academica",
        "Awareness",
        "Cosmology",
        "Crafts",
        "Empathy",
        "Enigmas",
        "Expression",
        "Seduction",
        "Technology",
    ],
)
bardism.instruments.add(
    artwork,
    dances,
    drugs,
    food,
    energy,
    eye_contact,
    fashion,
    group_rites,
    mass_media,
    meditation,
    ordeals,
    prayers,
    sex,
    symbols,
    tricks,
    true_names,
    voice,
)
bardism.save()
black_mass = Practice.objects.create(
    name="The Black Mass",
    abilities=["Esoterica", "Intimidation", "Occult", "Subterfuge", "Theology", "Vice"],
)
black_mass.instruments.add(
    atrocity,
    blood,
    bones,
    books,
    brews,
    circles,
    perversion,
    cups,
    dances,
    drugs,
    group_rites,
    languages,
    music,
    offerings,
    ordeals,
    sex,
    symbols,
    transgression,
    voice,
    weapons,
)
black_mass.save()
chaos_magick = Practice.objects.create(
    name="Chaos Magick",
    abilities=[
        "Art",
        "Awareness",
        "Carousing",
        "Computer",
        "Esoterica",
        "Expression",
        "Lucid Dreaming",
        "Meditation",
        "Pharmacopeia",
        "Streetwise",
        "Technology",
    ],
)
chaos_magick.instruments.add(*list(Instrument.objects.all()))
chaos_magick.save()
craftwork = Practice.objects.create(
    name="Craftwork",
    abilities=[
        "Academics",
        "Art",
        "Computers",
        "Crafts",
        "Energy Weapons",
        "Esoterica",
        "Hypertech",
        "Research",
        "Science",
        "Technology",
    ],
)
craftwork.instruments.add(
    artwork,
    blood,
    books,
    computer_gear,
    devices,
    elements,
    gadgets,
    household_tools,
    labs,
    symbols,
    weapons,
)
craftwork.save()
crazy_wisdom = Practice.objects.create(
    name="Crazy Wisdom",
    abilities=[
        "Art",
        "Athletics",
        "Carousing",
        "Esoterica",
        "Lucid Dreaming",
        "Meditation",
        "Pharmacopeia",
        "Survival",
    ],
)
crazy_wisdom.instruments.add(
    blood,
    bones,
    brain_computer_interface,
    dances,
    drugs,
    music,
    ordeals,
    sex,
    social_dominion,
    thought_forms,
    toys,
    tricks,
    voice,
)
crazy_wisdom.save()
cybernetics = Practice.objects.create(
    name="Cybernetics",
    abilities=[
        "Academics",
        "Biotech",
        "Computer",
        "Crafts",
        "Energy Weapons",
        "Hypertech",
        "Media",
        "Politics",
        "Science",
        "Technology",
    ],
)
cybernetics.instruments.add(
    books,
    brain_computer_interface,
    computer_gear,
    devices,
    gadgets,
    labs,
    languages,
    mass_media,
    nanotech,
    numbers,
    weapons,
    writings,
)
cybernetics.save()
demonism = Practice.objects.create(
    name="Demonism",
    abilities=[
        "Cosmology",
        "Esoterica",
        "Intimidation",
        "Lore",
        "Occult",
        "Subterfuge",
        "Weird Science",
    ],
)
demonism.instruments.add(
    atrocity,
    blood,
    bones,
    books,
    brews,
    celestial_alignments,
    circles,
    perversion,
    cups,
    dances,
    drugs,
    elements,
    formulae,
    group_rites,
    languages,
    meditation,
    music,
    offerings,
    ordeals,
    sex,
    symbols,
    thought_forms,
    transgression,
    voice,
    weapons,
    writings,
)
demonism.save()
dominion = Practice.objects.create(
    name="Dominion",
    abilities=[
        "Academics",
        "Art",
        "Belief Systems",
        "Empathy",
        "Expression",
        "Intimidation",
        "Leadership",
        "Media",
        "Politics",
        "Seduction",
        "Technology",
    ],
)
dominion.instruments.add(
    artwork,
    brain_computer_interface,
    eye_contact,
    fashion,
    group_rites,
    languages,
    mass_media,
    music,
    social_dominion,
    symbols,
    thought_forms,
    tricks,
    voice,
)
dominion.save()
elementalism = Practice.objects.create(
    name="Elementalism",
    abilities=[
        "Art",
        "Athletics",
        "Awareness",
        "Crafts",
        "Empathy",
        "Esoterica",
        "Meditation",
        "Survival",
    ],
)
elementalism.instruments.add(
    armor,
    bones,
    blood,
    brews,
    dances,
    drugs,
    elements,
    energy,
    herbs,
    household_tools,
    knots,
    meditation,
    music,
    prayers,
    offerings,
    ordeals,
    symbols,
    weapons,
    writings,
)
elementalism.save()
faith = Practice.objects.create(
    name="Faith",
    abilities=[
        "Academics",
        "Awareness",
        "Belief Systems",
        "Cosmology",
        "Empathy",
        "Enigmas",
        "Esoterica",
        "Expression",
        "Medicine",
    ],
)
faith.instruments.add(
    blessings,
    books,
    cups,
    energy,
    food,
    group_rites,
    music,
    offerings,
    ordeals,
    prayers,
    sacred_iconography,
    symbols,
    thought_forms,
    voice,
    writings,
)
faith.save()
feralism = Practice.objects.create(
    name="Feralism",
    abilities=[
        "Animal Kinship",
        "Athletics",
        "Brawl",
        "Hunting",
        "Intimidation",
        "Stealth",
        "Survival",
    ],
)
feralism.instruments.add(
    atrocity,
    blood,
    bodywork,
    body_modification,
    bones,
    cannibalism,
    dances,
    drugs,
    fashion,
    food,
    group_rites,
    mutilation,
    offerings,
    ordeals,
    sex,
    social_dominion,
    thought_forms,
    weapons,
)
feralism.save()
god_bonding = Practice.objects.create(
    name="God-Bonding",
    abilities=[
        "Awareness",
        "Belief Systems",
        "Cosmology",
        "Empathy",
        "Enigmas",
        "Esoterica",
        "Expression",
        "Lucid Dreaming",
        "Medicine",
        "Meditation",
    ],
)
god_bonding.instruments.add(
    blessings,
    blood,
    elements,
    group_rites,
    music,
    offerings,
    ordeals,
    prayers,
    sacred_iconography,
    voice,
    weapons,
)
god_bonding.save()
goetia = Practice.objects.create(
    name="Goetia",
    abilities=[
        "Academics",
        "Art",
        "Cosmology",
        "Enigmas",
        "Esoterica",
        "High Ritual",
        "Lore",
        "Research",
        "Occult",
    ],
)
goetia.instruments.add(
    blood,
    bones,
    books,
    celestial_alignments,
    circles,
    perversion,
    cups,
    dances,
    drugs,
    elements,
    formulae,
    group_rites,
    languages,
    meditation,
    music,
    offerings,
    ordeals,
    sex,
    symbols,
    thought_forms,
    transgression,
    voice,
    weapons,
    writings,
)
goetia.save()
gutter_magick = Practice.objects.create(
    name="Gutter Magick",
    abilities=[
        "Animal Kinship",
        "Area Knowledge",
        "Art",
        "Crafts",
        "Expression",
        "Firearms",
        "Intimidation",
        "Pharmacopeia",
        "Streetwise",
        "Survival",
        "Technology",
    ],
)
gutter_magick.instruments.add(
    artwork,
    blood,
    bones,
    cards,
    dances,
    drugs,
    eye_contact,
    fashion,
    herbs,
    household_tools,
    music,
    offerings,
    sex,
    social_dominion,
    symbols,
    thought_forms,
    toys,
    tricks,
    weapons,
    vehicles,
)
gutter_magick.save()
high_ritual_magick = Practice.objects.create(
    name="High Ritual Magick",
    abilities=[
        "Academics",
        "Belief Systems",
        "Cosmology",
        "Crafts",
        "Expression" "Esoterica",
        "Investigation",
        "Leadership",
        "Meditation",
        "Occult",
        "Research",
    ],
)
high_ritual_magick.instruments.add(
    books,
    celestial_alignments,
    circles,
    computer_gear,
    cups,
    elements,
    eye_contact,
    fashion,
    gems,
    dances,
    languages,
    meditation,
    numbers,
    offerings,
    prayers,
    social_dominion,
    symbols,
    thought_forms,
    true_names,
    wands,
    weapons,
    writings,
)
high_ritual_magick.save()
hypertech = Practice.objects.create(
    name="Hypertech",
    abilities=[
        "Academics",
        "Computer",
        "Crafts",
        "Hypertech",
        "Investigation",
        "Medicine",
        "Research",
        "Science",
        "Technology",
    ],
)
hypertech.instruments.add(
    books,
    brain_computer_interface,
    computer_gear,
    devices,
    household_tools,
    gadgets,
    labs,
    nanotech,
    writings,
)
hypertech.save()
infernal_science = Practice.objects.create(
    name="Infernal Sciences",
    abilities=[
        "Biotech",
        "Computer",
        "Crafts",
        "Firearms",
        "Gunsmith",
        "Hypertech",
        "Jury-Rigging",
        "Mass Media",
        "Medicine",
        "Newspeak",
        "Science",
        "Weird Science",
        "Technology",
    ],
)
infernal_science.instruments.add(
    armor,
    atrocity,
    body_modification,
    brain_computer_interface,
    computer_gear,
    cybernetic_implants,
    devices,
    drugs,
    formulae,
    gadgets,
    genetic_manipulation,
    internet_activity,
    labs,
    languages,
    management,
    mass_media,
    medical_procedures,
    money,
    mutilation,
    nanotech,
    social_dominion,
    trolling,
    vehicles,
    weapons,
)
infernal_science.save()
invigoration = Practice.objects.create(
    name="Invigoration",
    abilities=[
        "Athletics",
        "Biotech",
        "Brawl",
        "Esoterica",
        "Lucid Dreaming",
        "Martial Arts",
        "Medicine",
        "Meditation",
        "Science",
    ],
)
invigoration.instruments.add(
    blood,
    bodywork,
    brain_computer_interface,
    brews,
    dances,
    devices,
    gadgets,
    drugs,
    energy,
    eye_contact,
    fashion,
    food,
    herbs,
    labs,
    meditation,
    money,
    nanotech,
    sex,
    social_dominion,
    thought_forms,
    voice,
)
invigoration.save()
maleficia = Practice.objects.create(
    name="Maleficia",
    abilities=[
        "Cosmology",
        "Enigmas",
        "Esoterica",
        "Expression",
        "Intimidation",
        "Melee",
        "Occult",
        "Pharmacopeia",
        "Seduction",
        "Torture",
    ],
)
maleficia.instruments.add(
    artwork,
    blood,
    bodywork,
    bones,
    circles,
    cups,
    blessings,
    elements,
    eye_contact,
    drugs,
    gems,
    group_rites,
    music,
    offerings,
    prayers,
    sex,
    voice,
    weapons,
)
maleficia.save()
martial_arts = Practice.objects.create(
    name="Martial Arts",
    abilities=[
        "Acrobatics",
        "Alertness",
        "Athletics",
        "Awareness",
        "Esoterica",
        "Etiquette",
        "Intimidation",
        "Martial Arts",
        "Medicine",
        "Meditation",
        "Melee",
    ],
)
martial_arts.instruments.add(
    bodywork,
    dances,
    energy,
    herbs,
    meditation,
    ordeals,
    symbols,
    wands,
    weapons,
    voice,
)
martial_arts.save()
medicine_work = Practice.objects.create(
    name="Medicine-Work",
    abilities=[
        "Academics",
        "art",
        "Awareness",
        "Empathy",
        "Esoterica",
        "Medicine",
        "Meditation",
        "Pharmacopeia",
        "Science",
        "Technology",
    ],
)
medicine_work.instruments.add(
    artwork,
    blessings,
    blood,
    bodywork,
    bones,
    books,
    brews,
    computer_gear,
    cups,
    dances,
    devices,
    drugs,
    group_rites,
    herbs,
    labs,
    languages,
    meditation,
    music,
    offerings,
    prayers,
    social_dominion,
    voice,
    weapons,
)
medicine_work.save()
mediumship = Practice.objects.create(
    name="Mediumship",
    abilities=[
        "Awareness",
        "Belief Systems",
        "Cosmology",
        "Empathy",
        "Enigmas",
        "Esoterica",
        "Expression",
        "Intimidation",
        "Investigation",
        "Linguistics",
        "Lucid Dreaming",
        "Meditation",
        "Occult",
        "Research",
    ],
)
mediumship.instruments.add(
    artwork,
    blood,
    bodywork,
    bones,
    brews,
    dances,
    drugs,
    eye_contact,
    fashion,
    gems,
    herbs,
    languages,
    meditation,
    ordeals,
    sex,
    social_dominion,
    voice,
    writings,
)
mediumship.save()
psionics = Practice.objects.create(
    name="Psionics",
    abilities=[
        "Alertness",
        "Awareness",
        "Empathy",
        "Enigmas",
        "Esoterica",
        "Intimidation",
        "Lucid Dreaming",
        "Martial Arts",
        "Meditation",
    ],
)
psionics.instruments.add(
    bodywork,
    brain_computer_interface,
    devices,
    nanotech,
    cards,
    dances,
    drugs,
    energy,
    eye_contact,
    fashion,
    formulae,
    numbers,
    group_rites,
    music,
    languages,
    management,
    meditation,
    sex,
    social_dominion,
    symbols,
    thought_forms,
    true_names,
    voice,
)
psionics.save()
reality_hacking = Practice.objects.create(
    name="Reality Hacking",
    abilities=[
        "Academics",
        "Art",
        "Belief Systems",
        "Computer",
        "Expression",
        "Government",
        "Media",
        "Politics",
        "Science",
        "Subterfuge",
        "Technology",
    ],
)
reality_hacking.instruments.add(
    artwork,
    books,
    brain_computer_interface,
    computer_gear,
    devices,
    drugs,
    eye_contact,
    group_rites,
    languages,
    mass_media,
    money,
    music,
    nanotech,
    sex,
    social_dominion,
    symbols,
    thought_forms,
    tricks,
    voice,
    weapons,
)
reality_hacking.save()
shamanism = Practice.objects.create(
    name="Shamanism",
    abilities=[
        "Alertness",
        "Art",
        "Cosmology",
        "Enigmas",
        "Esoterica",
        "Expression",
        "Lucid Dreaming",
        "Medicine",
        "Pharmacopeia",
        "Streetwise",
        "Survival",
    ],
)
shamanism.instruments.add(
    blood,
    bones,
    computer_gear,
    dances,
    drugs,
    elements,
    herbs,
    household_tools,
    offerings,
    ordeals,
    sex,
    thought_forms,
    toys,
    true_names,
    voice,
    weapons,
)
shamanism.save()
voudoun = Practice.objects.create(
    name="Voudoun",
    abilities=[
        "Art",
        "Athletics",
        "Awareness",
        "Belief Systems",
        "Carousing",
        "Crafts",
        "Empathy",
        "Intimidation",
        "Lucid Dreaming",
        "Medicine",
        "Meditation",
        "Streetwise",
    ],
)
voudoun.instruments.add(
    artwork,
    blessings,
    blood,
    bones,
    cards,
    cups,
    crossroads,
    dances,
    drugs,
    elements,
    eye_contact,
    fashion,
    group_rites,
    herbs,
    household_tools,
    knots,
    languages,
    meditation,
    music,
    offerings,
    prayers,
    sex,
    symbols,
    true_names,
    voice,
    wands,
    weapons,
    writings,
)
voudoun.save()
weird_science = Practice.objects.create(
    name="Weird Science",
    abilities=[
        "Academics",
        "Crafts",
        "Esoterica",
        "Energy Weapons",
        "Hypertech",
        "Research",
        "Science",
        "Technology",
    ],
)
weird_science.instruments.add(
    armor,
    books,
    bones,
    brain_computer_interface,
    celestial_alignments,
    computer_gear,
    devices,
    elements,
    gadgets,
    labs,
    languages,
    numbers,
    toys,
    vehicles,
    weapons,
    writings,
)
weird_science.save()
witchcraft = Practice.objects.create(
    name="Witchcraft",
    abilities=[
        "Academics",
        "Animal Kinship",
        "Art",
        "Awareness",
        "Crafts",
        "Medicine",
        "Meditation",
        "Occult",
        "Pharmacopeia",
    ],
)
witchcraft.instruments.add(
    artwork,
    blessings,
    blood,
    bodywork,
    bones,
    books,
    brews,
    cards,
    celestial_alignments,
    circles,
    crossroads,
    cups,
    dances,
    drugs,
    elements,
    eye_contact,
    group_rites,
    household_tools,
    knots,
    music,
    offerings,
    sex,
    social_dominion,
    symbols,
    true_names,
    wands,
    weapons,
    writings,
)
witchcraft.save()
vamamarga = Practice.objects.create(
    name="Vamamarga",
    abilities=[
        "Athletics",
        "Esoterica",
        "Intimidation",
        "Medicine",
        "Meditation",
        "Survival",
    ],
)
vamamarga.instruments.add(
    blood,
    bodywork,
    body_modification,
    bones,
    cannibalism,
    dances,
    drugs,
    fashion,
    food,
    mutilation,
    offerings,
    ordeals,
    perversion,
    sex,
    social_dominion,
    violation,
    weapons,
)
vamamarga.save()
yoga = Practice.objects.create(
    name="Yoga",
    abilities=[
        "Athletics",
        "Awareness",
        "Enigmas",
        "Esoterica",
        "Expression",
        "Medicine",
        "Meditation",
        "Survival",
    ],
)
yoga.instruments.add(
    bodywork,
    circles,
    dances,
    energy,
    languages,
    meditation,
    music,
    ordeals,
    prayers,
    sex,
    symbols,
    thought_forms,
    voice,
    writings,
)
yoga.save()

a_mechanistic_cosmos = Paradigm.objects.create(name="A Mechanistic Cosmos",)
a_mechanistic_cosmos.practices.add(
    alchemy,
    art_of_desire,
    chaos_magick,
    craftwork,
    cybernetics,
    dominion,
    high_ritual_magick,
    hypertech,
    medicine_work,
    reality_hacking,
    weird_science,
    yoga,
    animalism,
)
a_mechanistic_cosmos.save()
gods_and_monsters = Paradigm.objects.create(name="A World of Gods and Monsters",)
gods_and_monsters.practices.add(
    chaos_magick,
    craftwork,
    crazy_wisdom,
    dominion,
    faith,
    gutter_magick,
    high_ritual_magick,
    hypertech,
    maleficia,
    martial_arts,
    medicine_work,
    reality_hacking,
    shamanism,
    voudoun,
    witchcraft,
    yoga,
    bardism,
    god_bonding,
    mediumship,
    abyssalism,
    demonism,
    goetia,
)
gods_and_monsters.save()
aliens_make_us = Paradigm.objects.create(name="Aliens Make Us What We Are")
aliens_make_us.practices.add(
    chaos_magick,
    craftwork,
    crazy_wisdom,
    cybernetics,
    faith,
    hypertech,
    invigoration,
    maleficia,
    martial_arts,
    mediumship,
    psionics,
    reality_hacking,
    weird_science,
    yoga,
    infernal_science,
)
aliens_make_us.save()
all_power_from_god = Paradigm.objects.create(name="All Power Comes From God(s)")
all_power_from_god.practices.add(
    bardism,
    dominion,
    elementalism,
    faith,
    god_bonding,
    gutter_magick,
    high_ritual_magick,
    maleficia,
    martial_arts,
    medicine_work,
    mediumship,
    voudoun,
    witchcraft,
)
all_power_from_god.save()
all_power_from_sin = Paradigm.objects.create(name="All Power Comes From Sin")
all_power_from_sin.practices.add(
    high_ritual_magick,
    witchcraft,
    shamanism,
    mediumship,
    voudoun,
    animalism,
    abyssalism,
    black_mass,
    demonism,
    goetia,
    vamamarga,
)
all_power_from_sin.save()
all_the_worlds_a_stage = Paradigm.objects.create(name="All the World's a Stage")
all_the_worlds_a_stage.practices.add(
    art_of_desire,
    bardism,
    crazy_wisdom,
    dominion,
    gutter_magick,
    hypertech,
    invigoration,
    mediumship,
    psionics,
    reality_hacking,
    weird_science,
)
all_the_worlds_a_stage.save()
ancestor_veneration = Paradigm.objects.create(name="Ancestor Veneration")
ancestor_veneration.practices.add(
    bardism, faith, medicine_work, mediumship, shamanism, voudoun, witchcraft
)
ancestor_veneration.save()
ancient_wisdom = Paradigm.objects.create(name="Ancient Wisdom is the Key")
ancient_wisdom.practices.add(
    alchemy,
    animalism,
    bardism,
    craftwork,
    crazy_wisdom,
    dominion,
    elementalism,
    god_bonding,
    high_ritual_magick,
    invigoration,
    maleficia,
    medicine_work,
    mediumship,
    psionics,
    shamanism,
    witchcraft,
    yoga,
    abyssalism,
    demonism,
    feralism,
    goetia,
    vamamarga,
)
ancient_wisdom.save()
barbarism_is_true = Paradigm.objects.create(name="Barbarism is the Truest State of Man")
barbarism_is_true.practices.add(
    dominion,
    martial_arts,
    witchcraft,
    animalism,
    god_bonding,
    craftwork,
    cybernetics,
    reality_hacking,
    demonism,
    feralism,
    vamamarga,
)
barbarism_is_true.save()
bring_back_the_golden_age = Paradigm.objects.create(name="Bring Back the Golden Age!",)
bring_back_the_golden_age.practices.add(
    alchemy,
    art_of_desire,
    craftwork,
    dominion,
    faith,
    high_ritual_magick,
    maleficia,
    martial_arts,
    medicine_work,
    reality_hacking,
    shamanism,
    voudoun,
    weird_science,
    witchcraft,
    yoga,
    bardism,
    god_bonding,
    goetia,
)
bring_back_the_golden_age.save()
consciousness_is_reality = Paradigm.objects.create(
    name="Consciousness is the Only True Reality"
)
consciousness_is_reality.practices.add(
    alchemy,
    art_of_desire,
    chaos_magick,
    crazy_wisdom,
    dominion,
    high_ritual_magick,
    hypertech,
    invigoration,
    martial_arts,
    mediumship,
    psionics,
    reality_hacking,
    yoga,
    infernal_science,
    vamamarga,
)
consciousness_is_reality.save()
cosmic_horror = Paradigm.objects.create(name="Cosmic Horror is the Only Truth")
cosmic_horror.practices.add(
    witchcraft,
    shamanism,
    elementalism,
    mediumship,
    voudoun,
    chaos_magick,
    gutter_magick,
    high_ritual_magick,
    dominion,
    martial_arts,
    abyssalism,
    black_mass,
    demonism,
    feralism,
    goetia,
    infernal_science,
    vamamarga,
)
cosmic_horror.save()
divine_and_alive = Paradigm.objects.create(name="Creation's Divine and Alive",)
divine_and_alive.practices.add(
    alchemy,
    chaos_magick,
    craftwork,
    crazy_wisdom,
    faith,
    gutter_magick,
    martial_arts,
    medicine_work,
    reality_hacking,
    shamanism,
    voudoun,
    witchcraft,
    yoga,
    bardism,
    elementalism,
    feralism,
    vamamarga,
)
divine_and_alive.save()
divine_order_earthly_chaos = Paradigm.objects.create(
    name="Divine Order and Earthly Chaos",
)
divine_order_earthly_chaos.practices.add(
    alchemy,
    art_of_desire,
    chaos_magick,
    craftwork,
    crazy_wisdom,
    dominion,
    faith,
    gutter_magick,
    high_ritual_magick,
    hypertech,
    maleficia,
    martial_arts,
    medicine_work,
    reality_hacking,
    shamanism,
    voudoun,
    weird_science,
    witchcraft,
    yoga,
    elementalism,
    god_bonding,
)
divine_order_earthly_chaos.save()
embrace_the_threshold = Paradigm.objects.create(name="Embrace the Threshold")
embrace_the_threshold.practices.add(
    alchemy,
    bardism,
    chaos_magick,
    crazy_wisdom,
    gutter_magick,
    faith,
    invigoration,
    maleficia,
    psionics,
    reality_hacking,
    yoga,
    infernal_science,
)
embrace_the_threshold.save()
everyones_against_me = Paradigm.objects.create(
    name="Everyone's Against Me, so Whatever I do is Justified"
)
everyones_against_me.practices.add(
    art_of_desire,
    bardism,
    chaos_magick,
    cybernetics,
    dominion,
    gutter_magick,
    reality_hacking,
    black_mass,
    demonism,
    infernal_science,
)
everyones_against_me.save()
everything_is_chaos = Paradigm.objects.create(name="Everything is Chaos",)
everything_is_chaos.practices.add(
    chaos_magick,
    crazy_wisdom,
    dominion,
    gutter_magick,
    hypertech,
    maleficia,
    martial_arts,
    medicine_work,
    reality_hacking,
    witchcraft,
    bardism,
    abyssalism,
    feralism,
    goetia,
    infernal_science,
    vamamarga,
)
everything_is_chaos.save()
everything_is_data = Paradigm.objects.create(name="Everything is Data",)
everything_is_data.practices.add(
    alchemy,
    art_of_desire,
    cybernetics,
    high_ritual_magick,
    hypertech,
    reality_hacking,
    weird_science,
    animalism,
    psionics,
    infernal_science,
)
everything_is_data.save()
everything_is_an_illusion = Paradigm.objects.create(
    name="Everything's an Illusion, Prison, or Mistake"
)
everything_is_an_illusion.practices.add(
    art_of_desire,
    chaos_magick,
    craftwork,
    crazy_wisdom,
    cybernetics,
    faith,
    gutter_magick,
    high_ritual_magick,
    maleficia,
    martial_arts,
    medicine_work,
    reality_hacking,
    shamanism,
    voudoun,
    witchcraft,
    yoga,
    animalism,
    bardism,
    god_bonding,
    invigoration,
    mediumship,
    psionics,
    abyssalism,
    goetia,
    vamamarga,
)
everything_is_an_illusion.save()
evil_is_necessary = Paradigm.objects.create(name="Evil is Necessary, and so I am Evil")
evil_is_necessary.practices.add(
    art_of_desire,
    black_mass,
    chaos_magick,
    gutter_magick,
    high_ritual_magick,
    reality_hacking,
    witchcraft,
    voudoun,
    abyssalism,
    black_mass,
    demonism,
    feralism,
    infernal_science,
)
evil_is_necessary.save()
existence_is_unknowable = Paradigm.objects.create(
    name="Existence is Unknowable, Irrational, and Sublime"
)
existence_is_unknowable.practices.add(
    animalism,
    bardism,
    chaos_magick,
    dominion,
    elementalism,
    martial_arts,
    psionics,
    shamanism,
    weird_science,
    yoga,
    abyssalism,
    demonism,
    feralism,
    goetia,
    infernal_science,
    vamamarga,
)
existence_is_unknowable.save()
forbidden_wisdom = Paradigm.objects.create(
    name="Forbidden Wisdom is the Truest Source of Power"
)
forbidden_wisdom.practices.add(
    animalism,
    bardism,
    black_mass,
    chaos_magick,
    cybernetics,
    dominion,
    god_bonding,
    gutter_magick,
    high_ritual_magick,
    invigoration,
    reality_hacking,
    weird_science,
    witchcraft,
    yoga,
    black_mass,
    abyssalism,
    demonism,
    feralism,
    goetia,
    infernal_science,
    vamamarga,
)
forbidden_wisdom.save()
holographic_reality = Paradigm.objects.create(name="Holographic Reality")
holographic_reality.practices.add(
    chaos_magick,
    crazy_wisdom,
    cybernetics,
    hypertech,
    reality_hacking,
    weird_science,
    witchcraft,
    yoga,
    infernal_science,
)
holographic_reality.save()
i_am_all = Paradigm.objects.create(name="I am All")
i_am_all.practices.add(
    art_of_desire,
    chaos_magick,
    dominion,
    elementalism,
    gutter_magick,
    invigoration,
    psionics,
    reality_hacking,
    weird_science,
    abyssalism,
    infernal_science,
)
i_am_all.save()
im_a_predator = Paradigm.objects.create(name="I'm a Predator, and the World is My Prey")
im_a_predator.practices.add(
    animalism,
    art_of_desire,
    dominion,
    invigoration,
    martial_arts,
    psionics,
    voudoun,
    witchcraft,
    feralism,
    infernal_science,
)
im_a_predator.save()
indulgence = Paradigm.objects.create(name="Indulgence is Nature's Only Law")
indulgence.practices.add(
    animalism,
    art_of_desire,
    black_mass,
    dominion,
    elementalism,
    faith,
    invigoration,
    high_ritual_magick,
    witchcraft,
    black_mass,
    abyssalism,
    demonism,
    feralism,
    goetia,
    vamamarga,
)
indulgence.save()
have_faith = Paradigm.objects.create(name="It's All Good - Have Faith!",)
have_faith.practices.add(
    craftwork,
    crazy_wisdom,
    faith,
    gutter_magick,
    medicine_work,
    shamanism,
    weird_science,
    witchcraft,
    yoga,
    bardism,
    god_bonding,
    mediumship,
    psionics,
)
have_faith.save()
might_is_right = Paradigm.objects.create(name="Might Is Right",)
might_is_right.practices.add(
    alchemy,
    art_of_desire,
    chaos_magick,
    craftwork,
    cybernetics,
    dominion,
    gutter_magick,
    high_ritual_magick,
    hypertech,
    maleficia,
    martial_arts,
    reality_hacking,
    voudoun,
    weird_science,
    witchcraft,
    yoga,
    animalism,
    elementalism,
    invigoration,
    psionics,
    abyssalism,
    black_mass,
    demonism,
    feralism,
    infernal_science,
)
might_is_right.save()
one_way_trip_to_oblivion = Paradigm.objects.create(name="One Way Trip to Oblivion",)
one_way_trip_to_oblivion.practices.add(
    art_of_desire,
    chaos_magick,
    crazy_wisdom,
    cybernetics,
    dominion,
    gutter_magick,
    maleficia,
    reality_hacking,
    voudoun,
    witchcraft,
    bardism,
    abyssalism,
    goetia,
)
one_way_trip_to_oblivion.save()
only_the_strongest = Paradigm.objects.create(
    name="Only the Strongest Deserve to Survive"
)
only_the_strongest.practices.add(
    animalism,
    art_of_desire,
    craftwork,
    cybernetics,
    dominion,
    hypertech,
    invigoration,
    martial_arts,
    psionics,
    reality_hacking,
    weird_science,
    witchcraft,
    demonism,
    feralism,
    infernal_science,
    vamamarga,
)
only_the_strongest.save()
people_are_shit = Paradigm.objects.create(name="People are Shit")
people_are_shit.practices.add(*list(Practice.objects.all()))
people_are_shit.save()
rebellion = Paradigm.objects.create(name="Rebellion is the Road to Transcendence")
rebellion.practices.add(
    bardism,
    black_mass,
    chaos_magick,
    dominion,
    gutter_magick,
    psionics,
    reality_hacking,
    yoga,
    black_mass,
    abyssalism,
    demonism,
    infernal_science,
    vamamarga,
)
rebellion.save()
stormtroopers_of_the_abyss = Paradigm.objects.create(
    name="We are Stormtroopers of the Abyss"
)
stormtroopers_of_the_abyss.practices.add(
    animalism,
    black_mass,
    god_bonding,
    dominion,
    elementalism,
    invigoration,
    martial_arts,
    mediumship,
    shamanism,
    witchcraft,
    voudoun,
    black_mass,
    abyssalism,
    demonism,
    feralism,
    goetia,
)
stormtroopers_of_the_abyss.save()
tech_holds_all_answers = Paradigm.objects.create(name="Tech Holds All Answers",)
tech_holds_all_answers.practices.add(
    alchemy,
    art_of_desire,
    craftwork,
    cybernetics,
    dominion,
    high_ritual_magick,
    hypertech,
    martial_arts,
    medicine_work,
    reality_hacking,
    weird_science,
    yoga,
    animalism,
    invigoration,
    infernal_science,
)
tech_holds_all_answers.save()
transcend_limits = Paradigm.objects.create(name="Transcend Your Limits")
transcend_limits.practices.add(
    art_of_desire,
    bardism,
    crazy_wisdom,
    dominion,
    high_ritual_magick,
    invigoration,
    maleficia,
    psionics,
    reality_hacking,
    voudoun,
    witchcraft,
    yoga,
    infernal_science,
    vamamarga,
)
transcend_limits.save()
turning_the_keys = Paradigm.objects.create(name="Turning the Keys to Reality")
turning_the_keys.practices.add(
    alchemy,
    art_of_desire,
    craftwork,
    dominion,
    elementalism,
    god_bonding,
    high_ritual_magick,
    invigoration,
    medicine_work,
    psionics,
    reality_hacking,
    yoga,
    demonism,
)
turning_the_keys.save()
we_are_meant_to_be_wild = Paradigm.objects.create(name="We Are Meant to be Wild")
we_are_meant_to_be_wild.practices.add(
    animalism,
    bardism,
    crazy_wisdom,
    dominion,
    elementalism,
    invigoration,
    shamanism,
    witchcraft,
    yoga,
    feralism,
)
we_are_meant_to_be_wild.save()
we_are_not_men = Paradigm.objects.create(name="We Are Not Men!")
we_are_not_men.practices.add(
    art_of_desire,
    cybernetics,
    dominion,
    elementalism,
    high_ritual_magick,
    hypertech,
    invigoration,
    martial_arts,
    psionics,
    reality_hacking,
    weird_science,
)
we_are_not_men.save()
we_are_god = Paradigm.objects.create(name="We're All God(s) in Disguise")
we_are_god.practices.add(
    alchemy,
    crazy_wisdom,
    faith,
    god_bonding,
    high_ritual_magick,
    invigoration,
    martial_arts,
    mediumship,
    psionics,
    witchcraft,
    yoga,
)
we_are_god.save()


traditions = MageFaction.objects.create(name="Traditions")
ab = MageFaction.objects.create(name="Akashayana", parent=traditions, affinities=["Life", "Mind"], founded=-3000)
ab.paradigms.add(bring_back_the_golden_age, everything_is_an_illusion, have_faith, might_is_right)
ab.practices.add(alchemy, craftwork, faith, yoga, dominion, martial_arts)
ab.languages.add(chinese, japanese, korean, vietnamese, thai)
ab.materials.add(paper, vellum, parchment, leather, cloth, wood, steel)
ab.media.add(book, scrolls)
ab.save()
MageFaction.objects.create(name="Shi-Ren", parent=ab)
MageFaction.objects.create(name="Li-Hai", parent=ab)
MageFaction.objects.create(name="Kannagara", parent=ab)
MageFaction.objects.create(name="Jnani", parent=ab)
MageFaction.objects.create(name="Vajrapani", parent=ab)
cc = MageFaction.objects.create(
    name="Celestial Chorus", parent=traditions, affinities=["Forces", "Prime", "Spirit"], founded=-1500
)
cc.paradigms.add(divine_and_alive, divine_order_earthly_chaos, have_faith)
cc.practices.add(faith, high_ritual_magick, bardism)
cc.languages.add(arabic, hebrew, aramaic, latin, koine_greek)
cc.materials.add(paper, vellum, parchment, leather, cloth, wood, steel)
cc.media.add(book, tablets, scrolls)
cc.save()
MageFaction.objects.create(name="The Guardian Orders", parent=cc)
MageFaction.objects.create(name="The Theological Orders", parent=cc)
MageFaction.objects.create(name="Other Factions", parent=cc)
cox = MageFaction.objects.create(
    name="Cult of Ecstasy", parent=traditions, affinities=["Life", "Mind", "Time"], founded=0
)
cox.paradigms.add(divine_and_alive, everything_is_data, everything_is_an_illusion, have_faith)
cox.practices.add(crazy_wisdom, gutter_magick, yoga, cybernetics, hypertech, bardism)
cox.languages.add(farsi, hindi, afghan, french)
cox.materials.add(paper, vellum, parchment, leather, cloth, wood, steel)
cox.media.add(book, scrolls)
cox.save()
MageFaction.objects.create(name="Historical Factions", parent=cox)
MageFaction.objects.create(name="Dissidents Against Ananda", parent=cox)
MageFaction.objects.create(name="Progressivists", parent=cox)
MageFaction.objects.create(name="Political Factions", parent=cox)
ds = MageFaction.objects.create(name="Dreamspeakers", parent=traditions, affinities=["Forces", "Life", "Matter", "Spirit"], founded=-4000)
ds.paradigms.add(gods_and_monsters, bring_back_the_golden_age, divine_and_alive, might_is_right)
ds.practices.add(medicine_work, craftwork, shamanism, crazy_wisdom, faith)
ds.languages.add(quechua, spanish, swahili, yoruba, oromo, nahuatl, mayan, algonquin, iroquois, navaho, sioux, anguthimri)
ds.materials.add(paper, vellum, parchment, leather, cloth, wood, steel)
ds.media.add(book, tablets, scrolls)
ds.save()
MageFaction.objects.create(name="Baruti", parent=ds)
MageFaction.objects.create(name="Ghost Wheel Society", parent=ds)
MageFaction.objects.create(name="Keepers of the Sacred Flame", parent=ds)
MageFaction.objects.create(name="Red Spear Society", parent=ds)
MageFaction.objects.create(name="Spirit Smiths", parent=ds)
MageFaction.objects.create(name="Solitaries", parent=ds)
MageFaction.objects.create(name="Independents", parent=ds)
eu = MageFaction.objects.create(name="Euthanatos", parent=traditions, affinities=["Entropy", "Life", "Spirit"], founded=-3000)
eu.paradigms.add(divine_and_alive, divine_order_earthly_chaos, everything_is_an_illusion, have_faith)
eu.practices.add(crazy_wisdom, faith, high_ritual_magick, medicine_work, reality_hacking, martial_arts, shamanism, voudoun, yoga)
eu.languages.add(hindi, sanskrit, greek)
eu.materials.add(paper, vellum, parchment, leather, cloth, wood, steel)
eu.media.add(book, scrolls)
eu.save()
MageFaction.objects.create(name="Chakravanti", parent=eu)
MageFaction.objects.create(name="Madzimbabwe", parent=eu)
MageFaction.objects.create(name="Vrati", parent=eu)
MageFaction.objects.create(name="Aided", parent=eu)
MageFaction.objects.create(name="Hierchthonoi", parent=eu)
ooh = MageFaction.objects.create(
    name="Order of Hermes", parent=traditions, affinities=["Forces"], founded=750
)
ooh.paradigms.add(a_mechanistic_cosmos, bring_back_the_golden_age, divine_order_earthly_chaos, might_is_right, tech_holds_all_answers)
ooh.practices.add(alchemy, dominion, high_ritual_magick)
ooh.languages.add(hebrew, arabic, latin, greek, aramaic, egyptian)
ooh.materials.add(paper, vellum, parchment, leather, cloth, wood, steel, iron)
ooh.media.add(book, scrolls)
ooh.save()
MageFaction.objects.create(name="House Bonisagus", parent=ooh)
MageFaction.objects.create(name="House Ex Miscellanea", parent=ooh)
MageFaction.objects.create(name="House Flambeau", parent=ooh)
MageFaction.objects.create(name="House Fortunae", parent=ooh)
MageFaction.objects.create(name="House Quaesitor", parent=ooh)
MageFaction.objects.create(name="House Shaea", parent=ooh)
MageFaction.objects.create(name="House Solificati", parent=ooh)
MageFaction.objects.create(name="House Tytalus", parent=ooh)
MageFaction.objects.create(name="House Verditius", parent=ooh)
soe = MageFaction.objects.create(
    name="Society of Ether", parent=traditions, affinities=["Forces", "Matter", "Prime"], founded=1200
)
soe.paradigms.add(a_mechanistic_cosmos, everything_is_data, everything_is_an_illusion, might_is_right, tech_holds_all_answers)
soe.practices.add(alchemy, craftwork, cybernetics, hypertech, reality_hacking, weird_science)
soe.languages.add(french, latin)
soe.materials.add(leather, cloth, wood, steel, bone)
soe.media.add(book, flash_drive, ebook, software)
soe.save()
MageFaction.objects.create(name="The Royal Ethernautical Society", parent=soe)
MageFaction.objects.create(name="The Cybernetic Research Institute", parent=soe)
MageFaction.objects.create(name="Utopians", parent=soe)
MageFaction.objects.create(name="Adventurers", parent=soe)
MageFaction.objects.create(name="Dissidents", parent=soe)
verb = MageFaction.objects.create(
    name="Verbena", parent=traditions, affinities=["Forces", "Life"], founded=-2000
)
verb.paradigms.add(
    gods_and_monsters,
    bring_back_the_golden_age,
    divine_and_alive,
    everything_is_chaos,
    might_is_right,
)
verb.practices.add(
    witchcraft,
    voudoun,
    dominion,
    weird_science,
    chaos_magick,
    yoga,
    martial_arts,
    high_ritual_magick,
    cybernetics,
    art_of_desire,
    craftwork,
    medicine_work,
    hypertech,
)
verb.languages.add(irish, gaelic, welsh)
verb.materials.add(paper, vellum, parchment, leather, cloth, wood, steel)
verb.media.add(book, tablets)
verb.save()
MageFaction.objects.create(name="Moon-Seekers", parent=verb)
MageFaction.objects.create(name="Gardeners of the Tree", parent=verb)
MageFaction.objects.create(name="Life Weavers", parent=verb)
MageFaction.objects.create(name="Twisters of Fate", parent=verb)
va = MageFaction.objects.create(
    name="Virtual Adepts", parent=traditions, affinities=["Correspondence", "Forces"], founded=1880
)
va.paradigms.add(a_mechanistic_cosmos, everything_is_data)
va.practices.add(
    reality_hacking,
    cybernetics,
    hypertech,
    weird_science,
    martial_arts,
    chaos_magick,
    gutter_magick,
)
va.languages.add()
va.materials.add(leather, cloth, steel)
va.media.add(book, ebook, software, flash_drive)
va.save()
MageFaction.objects.create(name="Reality Coders", parent=va)
MageFaction.objects.create(name="Cyberpunks", parent=va)
MageFaction.objects.create(name="Chaoticians", parent=va)
MageFaction.objects.create(name="Cypherpunks", parent=va)
MageFaction.objects.create(name="Nexplorers", parent=va)

da = MageFaction.objects.create(name="The Disparate Alliance")
hollow_ones = MageFaction.objects.create(
    name="Hollow Ones",
    parent=da,
    affinities=[
        "Correspondence",
        "Time",
        "Spirit",
        "Matter",
        "Forces",
        "Life",
        "Entropy",
        "Prime",
        "Mind",
    ],
)
hollow_ones.paradigms.add(
    everything_is_chaos,
    everything_is_an_illusion,
    one_way_trip_to_oblivion,
    have_faith,
)
hollow_ones.practices.add(chaos_magick, gutter_magick)
hollow_ones.save()
orphans = MageFaction.objects.create(
    name="Orphans",
    parent=da,
    affinities=[
        "Correspondence",
        "Time",
        "Spirit",
        "Matter",
        "Forces",
        "Life",
        "Entropy",
        "Prime",
        "Mind",
    ],
)
orphans.paradigms.add(*list(Paradigm.objects.all()))
orphans.practices.add(*list(Practice.objects.all()))
orphans.save()
kopa_loei = MageFaction.objects.create(
    name="Kopa Loei",
    parent=da,
    affinities=[
        "Correspondence",
        "Time",
        "Spirit",
        "Matter",
        "Forces",
        "Life",
        "Entropy",
        "Prime",
        "Mind",
    ],
)
kopa_loei.paradigms.add(divine_and_alive, divine_order_earthly_chaos)
kopa_loei.practices.add(shamanism, witchcraft, high_ritual_magick)
kopa_loei.save()
taftani = MageFaction.objects.create(
    name="Taftani", parent=da, affinities=["Forces", "Matter", "Prime", "Spirit"]
)
taftani.paradigms.add(divine_order_earthly_chaos, might_is_right)
taftani.practices.add(
    alchemy,
    craftwork,
    high_ritual_magick,
    crazy_wisdom,
    art_of_desire,
    dominion,
    hypertech,
)
taftani.save()
wulung = MageFaction.objects.create(
    name="Wu Lung", parent=da, affinities=["Spirit", "Forces", "Matter", "Life"]
)
wulung.paradigms.add(divine_order_earthly_chaos, bring_back_the_golden_age)
wulung.practices.add(high_ritual_magick, alchemy, martial_arts)
wulung.save()
ngoma = MageFaction.objects.create(
    name="Ngoma", parent=da, affinities=["Life", "Mind", "Prime", "Spirit"]
)
ngoma.paradigms.add(divine_order_earthly_chaos, tech_holds_all_answers)
ngoma.practices.add(
    high_ritual_magick,
    alchemy,
    hypertech,
    medicine_work,
    craftwork,
    reality_hacking,
    art_of_desire,
)
ngoma.save()
ahl_i_batin = MageFaction.objects.create(
    name="Ahl-i-Batin", parent=da, affinities=["Correspondence", "Mind"]
)
ahl_i_batin.paradigms.add(
    divine_order_earthly_chaos, have_faith, everything_is_an_illusion
)
ahl_i_batin.practices.add(
    faith,
    crazy_wisdom,
    alchemy,
    high_ritual_magick,
    yoga,
    gutter_magick,
    reality_hacking,
    chaos_magick,
)
ahl_i_batin.save()
bataa = MageFaction.objects.create(
    name="Bata'a", parent=da, affinities=["Spirit", "Life"]
)
bataa.paradigms.add(divine_and_alive, everything_is_chaos, gods_and_monsters)
bataa.practices.add(
    voudoun,
    faith,
    medicine_work,
    craftwork,
    gutter_magick,
    shamanism,
    weird_science,
    dominion,
    maleficia,
    martial_arts,
)
bataa.save()
cok = MageFaction.objects.create(
    name="Children of Knowledge",
    parent=da,
    affinities=["Matter", "Forces", "Prime", "Entropy"],
)
cok.paradigms.add(everything_is_chaos, everything_is_data, everything_is_an_illusion)
cok.practices.add(
    alchemy, craftwork, crazy_wisdom, art_of_desire, chaos_magick, hypertech
)
cok.save()
soh = MageFaction.objects.create(
    name="Sisters of Hippolyta", parent=da, affinities=["Life", "Mind"]
)
soh.paradigms.add(divine_and_alive, might_is_right, have_faith)
soh.practices.add(
    medicine_work, witchcraft, shamanism, high_ritual_magick, craftwork, martial_arts
)
soh.save()
templars = MageFaction.objects.create(
    name="Templar Knights", parent=da, affinities=["Forces", "Life", "Mind", "Prime"]
)
templars.paradigms.add(gods_and_monsters, divine_order_earthly_chaos, might_is_right)
templars.practices.add(faith, martial_arts, dominion, craftwork, hypertech)
templars.save()

tu = MageFaction.objects.create(name="Technocratic Union",)
itx = MageFaction.objects.create(
    name="Iteration X", parent=tu, affinities=["Forces", "Matter", "Time"]
)
itx.paradigms.add(a_mechanistic_cosmos, tech_holds_all_answers, everything_is_data)
itx.practices.add(
    cybernetics,
    hypertech,
    craftwork,
    martial_arts,
    dominion,
    art_of_desire,
    reality_hacking,
)
itx.save()
nwo = MageFaction.objects.create(
    name="New World Order", parent=tu, affinities=["Mind", "Correspondence"]
)
nwo.paradigms.add(gods_and_monsters, might_is_right, tech_holds_all_answers)
nwo.practices.add(dominion, martial_arts, hypertech, bardism)
nwo.save()
syn = MageFaction.objects.create(
    name="The Syndicate", parent=tu, affinities=["Entropy", "Mind", "Prime"]
)
syn.paradigms.add(might_is_right, one_way_trip_to_oblivion)
syn.practices.add(art_of_desire, martial_arts, dominion, bardism)
syn.save()
prog = MageFaction.objects.create(
    name="Progenitors", parent=tu, affinities=["Life", "Entropy", "Mind"]
)
prog.paradigms.add(might_is_right, divine_and_alive)
prog.practices.add(weird_science, medicine_work, cybernetics, hypertech)
prog.save()
ve = MageFaction.objects.create(
    name="Void Engineers", parent=tu, affinities=["Spirit", "Correspondence", "Forces"]
)
ve.paradigms.add(tech_holds_all_answers, gods_and_monsters, everything_is_chaos)
ve.practices.add(hypertech, cybernetics, craftwork, reality_hacking, weird_science)
ve.save()
MageFaction.objects.create(name="BioMechanics", parent=itx)
MageFaction.objects.create(name="Statisticians", parent=itx)
MageFaction.objects.create(name="Time-Motion Managers", parent=itx)
MageFaction.objects.create(name="Macrotechnicians", parent=itx)
MageFaction.objects.create(name="Ivory Tower", parent=nwo)
MageFaction.objects.create(name="The Operatives", parent=nwo)
MageFaction.objects.create(name="The Watchers", parent=nwo)
MageFaction.objects.create(name="The Feed", parent=nwo)
MageFaction.objects.create(name="Division Q", parent=nwo)
MageFaction.objects.create(name="Media Control", parent=syn)
MageFaction.objects.create(name="Financiers", parent=syn)
MageFaction.objects.create(name="Enforcers", parent=syn)
MageFaction.objects.create(name="Disbursements", parent=syn)
MageFaction.objects.create(name="Pharmacopoeists", parent=prog)
MageFaction.objects.create(name="Applied Science", parent=prog)
MageFaction.objects.create(name="FACADE Engineers", parent=prog)
MageFaction.objects.create(name="Genegineers", parent=prog)
MageFaction.objects.create(name="Earth Frontier Division", parent=ve)
MageFaction.objects.create(name="Research and Execution", parent=ve)
MageFaction.objects.create(name="Neutralization Specialization Corps", parent=ve)
MageFaction.objects.create(name="Border Corps Division", parent=ve)
MageFaction.objects.create(name="Pan-Dimension Corps", parent=ve)
