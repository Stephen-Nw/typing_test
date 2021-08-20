samples = [
    "The natural food for the dairy cow in summer is grass, and where rich, succulent grass and clover grow in "
    "abundance, as on the fertile meadows of Holland and the Channel Islands, or the Swiss Alps, the highly cultivated"
    " Danish farms, the eastern and middle-western states of America, etc., dairying early reached its highest "
    "development.As the value of milk and its products for human food became more generally recognized and "
    "all-the-year-round production was forced, it was found necessary to feed the cows heavily in winter too, "
    "not only hay, but also grain and succulent food such as beets and corn-ensilage (green corn cut, stalks, "
    "cobs and all, and packed in a silo), and science was taken into play to formulate Balanced Rations containing "
    "the proper amounts and proportions of the various nutrients—Protein, Fat and Carbohydrates.",

    "Many proponents of all three viewpoints remain convinced of the validity of their position.It is now clear that "
    "the cornucopian viewpoint is incosistent with finiteness of resources, environmental effects, and the unlikely "
    "prospect of developing totally new energy technologies.The futilitarian approach is unacceptably defeatist."
    "Transforming to a new era of energy supply and use is essential for America and the world. In following the "
    "transformarian approach, it is important to make the correct transformations. To do so requires some familiarity "
    "with technical issues.Discussions about technology with individuals who are not familiar with the underlying "
    "science are difficult.Such is the case in discussion about energy.Non-specialists may even question whether "
    "they need to make an effort.",

    "Atoms combine to form molecules.Molecules may be combinations of atoms of the same type or of dissimilar atoms.The"
    "formation of molecules depends on the outer electrons in atoms, called the valence electrons.If the number of "
    "valence electrons is less than the maximum number that the outer shell can hold, the atom can interact with other "
    "available atoms to increase or decrease the outer shell electron population to achieve a filled outer shell. "
    "Electrons may be taken from or given to other atoms to provide filled outer shells. These bonds are called "
    "ionic bonds.Electrons may also be shared between participating atoms to provide filled outer shells.These bonds "
    "are called covalent bonds."
]


def result_analysis(secs, num_char, wpm):
    """Text to display user typing analysis"""
    results = "Well done!! \n\n" \
              f"You typed for {secs} seconds \n\n" \
              f"You typed {num_char} characters.\n\n" \
              f"Your typing speed is {wpm} words per minute!!"
    return results


def instructions():
    """Application instructions"""
    instruction = "Instructions: Click the button below to start. Type your text in the blank entry field. Type" \
                  " for as long as you wish. Hit Enter when done to receive an analysis of your typing skills"
    return instruction

