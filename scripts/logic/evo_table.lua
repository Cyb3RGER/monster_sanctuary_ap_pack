EVO_TABLE = {
    ["blob"] = {{ Monster = "king_blob", Catalyst = "majestic_crown" }},
    ["magmapillar"] = {{ Monster = "magmamoth", Catalyst = "cocoon" }},
    ["rocky"] = {{ Monster = "mega_rock", Catalyst = "giant_seed" }},
    ["vaero"] = {{ Monster = "silvaero", Catalyst = "silver_feather" }},
    ["monk"] = {{ Monster = "ascendant", Catalyst = "primordial_branch" }},
    ["grummy"] = {{ Monster = "grulu", Catalyst = "stardust" }},
    ["fungi"] = {{ Monster = "fumagus", Catalyst = "druid_soul" }},
    ["minitaur"] = {{ Monster = "megataur", Catalyst = "shard_of_winter" }},
    ["crackle_knight"] = {{ Monster = "sizzle_knight", Catalyst = "sun_stone" }},
    ["mad_eye"] = {{ Monster = "mad_lord", Catalyst = "demonic_pact" }},
    ["glowfly"] = {{ Monster = "glowdra", Catalyst = "volcanic_ash" }},
    ["ice_blob"] = {{ Monster = "king_blob", Catalyst = "majestic_crown" }},
    ["ninki"] = {{ Monster = "ninki_nanka", Catalyst = "magical_clay" }},
    ["lava_blob"] = {{ Monster = "king_blob", Catalyst = "majestic_crown" }},
    ["draconov"] = {{ Monster = "dracogran", Catalyst = "fire_stone" }, { Monster = "draconov", Catalyst = "ice_stone" }, { Monster = "draconoir", Catalyst = "dark_stone" }, { Monster = "dracomer", Catalyst = "deep_stone" }},
    ["rainbow_blob"] = {{ Monster = "king_blob", Catalyst = "majestic_crow" }},
    ["tar_blob"] = {{ Monster = "king_blob", Catalyst = "majestic_crown" }},
}

CHILD_TABLE = {
    ["king_blob"] = {"blob", "ice_blob", "lava_blob", "rainbow_blob", "tar_blob"},
    ["magmamoth"] = {"magmapillar"},
    ["mega_rock"] = {"rocky"},
    ["silvaero"] = {"vaero"},
    ["ascendant"] = {"monk"},
    ["grulu"] = {"grummy"},
    ["fumagus"] = {"fungi"},
    ["megataur"] = {"minitaur"},
    ["sizzle_knight"] = {"crackle_knight"},
    ["mad_lord"] = {"mad_eye"},
    ["glowdra"] = {"glowfly"},
    ["ninki_nanka"] = {"ninki"},
    ["dracogran"] = {"draconov"},
    ["draconov"] = {"draconov"},
    ["draconoir"] = {"draconov"},
    ["dracomer"] = {"draconov"},
}