def rev(dic):
    ndic = {}
    for k, v in dic.items():
        for item in v:
            ndic[item] = k
    return ndic


properties_most = {
    "size": ["big", "large", "sizeable", "sizable", "massive", "enormous"],
    "sizexz": ["wide", "broad", "long", "thick"],
    "sizey": ["high", "tall", "towering", "elevated"],
    "weight": ["weighty", "bulky", "fat", "chunky", "overweight", "unwieldy"],
    "price": ["expensive", "costly", "lavish", "fancy", "valuable", "pricey", "rich"],
    "detail": ["interesting", "cool", "detailed", "complex"],
    "state": ["new", "modern", "latest", "untouched", "intact"],
    "cleanliness": ["clean", "spotless", "polish", "polished", "fresh"],
    "quality": ["good", "strong", "reliable", "useful", "adept", "efficient"]

}

properties_most_rev = rev(properties_most)

properties_least = {
    "size": ["small", "tiny", "little", "miniature", "microscopic", "petite"],
    "sizexz": ["narrow", "tight", "slim", "slender", "thin"],
    "sizey": ["short", "shortened", "abbreviated", "low"],
    "weight": ["light", "buoyant", "flimsy", "lightweight", "agile", "portable"],
    "price": ["cheap", "low-cost", "economical"],
    "detail": ["undetailed", "uninteresting", "simple", "plain"],
    "state": ["broken", "old", "damaged", "cracked", "crushed", "crumbled", "defective", "smashed"],
    "cleanliness": ["filthy", "dirty", "smelly", "dusty", "muddy", "stained"],
    "quality": ["bad", "weak", "low-quality", "crappy", "shitty"]
}

properties_least_rev = rev(properties_most)
