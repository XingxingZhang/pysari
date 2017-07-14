
from sari.SARI import SARIsent

ssent = "About 95 species are currently accepted ."
csent1 = "About 95 you now get in ."
csent2 = "About 95 species are now agreed ."
csent3 = "About 95 species are currently agreed ."
rsents = ["About 95 species are currently known .", "About 95 species are now accepted .", "95 species are now accepted ."]

print SARIsent(ssent, csent1, rsents)
print SARIsent(ssent, csent2, rsents)
print SARIsent(ssent, csent3, rsents)

