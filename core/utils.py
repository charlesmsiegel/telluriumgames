from random import choice, randint

import requests

from telluriumgames.secrets import API_KEY


def check_floor_ceiling(x, floor, ceiling):
    if x < floor:
        return floor
    if x > ceiling:
        return ceiling
    return x


def weighted_choice(dictionary, floor=0, ceiling=5):
    d = {
        k: check_floor_ceiling(v, floor=floor, ceiling=ceiling)
        for k, v in dictionary.items()
    }
    l = []
    for key, value in d.items():
        for _ in range(value + 1):
            for __ in range(value + 1):
                l.append(key)
    return choice(l)


def cod_dice(number_of_dice, again_minimum=10):
    if number_of_dice < 0:
        chance_die = randint(1, 10)
        if chance_die == 1:
            return chance_die, -1
        if chance_die == 10:
            return chance_die, 1
        return chance_die, 0
    roll = [randint(1, 10) for _ in range(number_of_dice)]
    num_agains = sum(x >= again_minimum for x in roll)
    while num_agains > 0:
        new_dice = [randint(1, 10) for _ in range(num_agains)]
        roll.extend(new_dice)
        num_agains = sum(x >= again_minimum for x in new_dice)
    return roll, sum(x >= 8 for x in roll)


def add_dot(character, trait, maximum):
    if getattr(character, trait) < maximum:
        setattr(character, trait, getattr(character, trait) + 1)
        character.save()
        return True
    return False


def random_name(gender, ethnicity="English"):
    usage = ethnicity_to_code[ethnicity]
    if gender == "mf":
        req_string = f"http://www.behindthename.com/api/random.json?usage={usage}&number=1&randomsurname=yes&key={API_KEY}"
    else:
        req_string = f"http://www.behindthename.com/api/random.json?gender={gender}&usage={usage}&number=1&randomsurname=yes&key={API_KEY}"
    try:
        return " ".join(requests.get(req_string).json()["names"])
    except KeyError:
        return f"Random Name {randint(0, 100000000000)}"


def random_ethnicity():
    return choice(list(ethnicity_to_code.keys()))


ethnicity_to_code = {
    "Akan": "aka",
    "Albanian": "alb",
    "Algonquin": "alg",
    "Indigenous American": "ame",
    # "New World Mythology": "amem",
    "Amharic": "amh",
    "Ancient": "anci",
    "Apache": "apa",
    "Arabic": "ara",
    "Armenian": "arm",
    "Assamese": "asm",
    "Asturian": "ast",
    # "Astronomy": "astr",
    "Indigenous Australian": "aus",
    "Avar": "ava",
    "Aymara": "aym",
    "Azerbaijani": "aze",
    "Balinese": "bal",
    "Basque": "bas",
    "Belarusian": "bel",
    "Bengali": "ben",
    "Berber": "ber",
    "Bhutanese": "bhu",
    # "Biblical (All)": "bibl",
    "Bosnian": "bos",
    "Breton": "bre",
    "Bashkir": "bsh",
    "Bulgarian": "bul",
    "Burmese": "bur",
    "Catalan": "cat",
    "Ancient Celtic": "cela",
    # "Celtic Mythology": "celm",
    "Chewa": "cew",
    "Chamorro": "cha",
    "Chechen": "che",
    "Chinese": "chi",
    "Cherokee": "chk",
    "Choctaw": "cht",
    "Cheyenne": "chy",
    "Circassian": "cir",
    "Comorian": "cmr",
    "Comanche": "com",
    "Coptic": "cop",
    "Cornish": "cor",
    "Cree": "cre",
    "Croatian": "cro",
    "Corsican": "crs",
    "Czech": "cze",
    "Danish": "dan",
    "Dhivehi": "dhi",
    "Dutch": "dut",
    "Ancient Egyptian": "egya",
    # "Egyptian Mythology": "egym",
    "English": "eng",
    "Anglo-Saxon": "enga",
    "Esperanto": "esp",
    "Estonian": "est",
    "Ethiopian": "eth",
    "Ewe": "ewe",
    "Faroese": "fae",
    # "Fairy": "fairy",
    "Fijian": "fij",
    "Filipino": "fil",
    "Finnish": "fin",
    "Flemish": "fle",
    # "Gluttakh": "fntsg",
    # "Monstrall": "fntsm",
    # "Romanto": "fntsr",
    # "Simitiq": "fntss",
    # "Tsang": "fntst",
    # "Xalaxxi": "fntsx",
    "French": "fre",
    "Frisian": "fri",
    "Fula": "ful",
    "Ga": "gaa",
    "Galician": "gal",
    "Ganda": "gan",
    "Georgian": "geo",
    "German": "ger",
    "Ancient Germanic": "gmca",
    "Goth": "goth",
    "Greek": "gre",
    "Ancient Greek": "grea",
    # "Greek Mythology": "grem",
    "Greenlandic": "grn",
    "Guarani": "gua",
    "Gujarati": "guj",
    "Hausa": "hau",
    "Hawaiian": "haw",
    # "Hillbilly": "hb",
    "Hebrew": "heb",
    "Hindi": "hin",
    # "Hippy": "hippy",
    "History": "hist",
    "Hmong": "hmo",
    "Hungarian": "hun",
    "Ibibio": "ibi",
    "Icelandic": "ice",
    "Igbo": "igb",
    "Indian": "ind",
    # "Hindu Mythology": "indm",
    "Ingush": "ing",
    "Indonesian": "ins",
    "Inuit": "inu",
    "Irish": "iri",
    "Iroquois": "iro",
    "Italian": "ita",
    "Japanese": "jap",
    "Javanese": "jav",
    "Jèrriais": "jer",
    "Jewish": "jew",
    "Kannada": "kan",
    "Kazakh": "kaz",
    "Khmer": "khm",
    "Kiga": "kig",
    "Kikuyu": "kik",
    "Kreatyve": "kk",
    "Kongo": "kon",
    "Korean": "kor",
    "Kurdish": "kur",
    "Kyrgyz": "kyr",
    "Lao": "lao",
    "Latvian": "lat",
    "Limburgish": "lim",
    # "Literature": "lite",
    # "Arthurian Romance": "litk",
    "Lithuanian": "lth",
    "Luhya": "luh",
    "Luo": "luo",
    "Macedonian": "mac",
    "Maguindanao": "mag",
    "Maltese": "mal",
    "Manx": "man",
    "Maori": "mao",
    "Mapuche": "map",
    "Mari": "mar",
    "Mayan": "may",
    "Mbundu": "mbu",
    "Medieval": "medi",
    "Malayalam": "mlm",
    "Malay": "mly",
    "Mohawk": "moh",
    "Mongolian": "mon",
    "Mormon": "morm",
    "Marathi": "mrt",
    "Mwera": "mwe",
    # "Mythology": "myth",
    "Nahuatl": "nah",
    "Navajo": "nav",
    "Ndebele": "nde",
    "Ancient Near Eastern": "neaa",
    # "Near Eastern Mythology": "neam",
    "Nepali": "nep",
    "Norwegian": "nor",
    "Norman": "nrm",
    "Nuu-chah-nulth": "nuu",
    "Occitan": "occ",
    "Odia": "odi",
    "Ojibwe": "oji",
    "Oneida": "one",
    "Oromo": "oro",
    "Ossetian": "oss",
    "Pashto": "pas",
    "Picard": "pcd",
    "Persian": "per",
    # "Pet": "pets",
    "Pintupi": "pin",
    "Polish": "pol",
    # "Popular Culture": "popu",
    "Portuguese": "por",
    "Powhatan": "pow",
    "Punjabi": "pun",
    "Quechua": "que",
    # "Rapper": "rap",
    "Romanian": "rmn",
    "Ancient Roman": "roma",
    # "Roman Mythology": "romm",
    "Russian": "rus",
    "Sami": "sam",
    "Sardinian": "sar",
    "Low German": "sax",
    "Ancient Scandinavian": "scaa",
    # "Norse Mythology": "scam",
    "Scottish": "sco",
    "Scots": "sct",
    "Seneca": "sen",
    "Serbian": "ser",
    "Shawnee": "sha",
    "Shona": "sho",
    "Sicilian": "sic",
    "Siksika": "sik",
    "Sinhalese": "sin",
    "Sioux": "sio",
    "Slavic": "sla",
    # "Slavic Mythology": "slam",
    "Slovak": "slk",
    "Slovene": "sln",
    "Samoan": "smn",
    "Somali": "som",
    "Sorbian": "sor",
    "Sotho": "sot",
    "Spanish": "spa",
    "Swahili": "swa",
    "Swedish": "swe",
    "Swazi": "swz",
    "Tagalog": "tag",
    "Tahitian": "tah",
    "Tajik": "taj",
    "Tamil": "tam",
    "Tatar": "tat",
    "Tausug": "tau",
    "Telugu": "tel",
    "Thai": "tha",
    # "Theology": "theo",
    "Tibetan": "tib",
    "Turkmen": "tkm",
    "Tongan": "ton",
    "Tooro": "too",
    # "Transformer": "trans",
    "Tswana": "tsw",
    "Tumbuka": "tum",
    "Tupi": "tup",
    "Turkish": "tur",
    "Ukrainian": "ukr",
    "Urdu": "urd",
    "Urhobo": "urh",
    "American": "usa",
    "Uyghur": "uyg",
    "Uzbek": "uzb",
    "Various": "vari",
    "Vietnamese": "vie",
    "Welsh": "wel",
    # "Witch": "witch",
    # "Wrestler": "wrest",
    "Xhosa": "xho",
    "Yao": "yao",
    "Yolngu": "yol",
    "Yoruba": "yor",
    "Zapotec": "zap",
    "Zulu": "zul",
}
