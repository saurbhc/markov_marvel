import markovify

def generate_sentence(state_size=3):
    # Get raw text as string.
    print("OPENING FILES")
    with open("Ant-Man.And.The.Wasp.txt") as Ant_Man_And_The_Wasp_f:
        print("...Opening Ant_Man_And_The_Wasp_f_text")
        Ant_Man_And_The_Wasp_f_text = Ant_Man_And_The_Wasp_f.read()
    with open("Ant-Man.txt") as Ant_Man_f:
        print("...Opening Ant_Man_f_text")
        Ant_Man_f_text = Ant_Man_f.read()
    with open("Avengers.Age.of.Ultron.txt") as Avengers_Age_of_Ultron_f:
        print("...Opening Avengers_Age_of_Ultron_f_text")
        Avengers_Age_of_Ultron_f_text = Avengers_Age_of_Ultron_f.read()
    with open("Avengers.Endgame.txt") as Avengers_Endgame_f:
        print("...Opening Avengers_Endgame_f_text")
        Avengers_Endgame_f_text = Avengers_Endgame_f.read()
    with open("Avengers.Infinity.War.txt") as Avengers_Infinity_War_f:
        print("...Opening Avengers_Infinity_War_f_text")
        Avengers_Infinity_War_f_text = Avengers_Infinity_War_f.read()
    with open("Avengers.txt") as Avengers_f:
        print("...Opening Avengers_f_text")
        Avengers_f_text = Avengers_f.read()
    with open("Black.Panther.txt") as Black_Panther_f:
        print("...Opening Black_Panther_f_text")
        Black_Panther_f_text = Black_Panther_f.read()
    with open("Captain.America.Civil.War.txt") as Captain_America_Civil_War_f:
        print("...Opening Captain_America_Civil_War_f_text")
        Captain_America_Civil_War_f_text = Captain_America_Civil_War_f.read()
    with open("Captain.America.The.First.Avenger.txt") as Captain_America_The_First_Avenger_f:
        print("...Opening Captain_America_The_First_Avenger_f_text")
        Captain_America_The_First_Avenger_f_text = Captain_America_The_First_Avenger_f.read()
    with open("Captain.America.The.Winter.Soldier.txt") as Captain_America_The_Winter_Soldier_f:
        print("...Opening Captain_America_The_Winter_Soldier_f_text")
        Captain_America_The_Winter_Soldier_f_text = Captain_America_The_Winter_Soldier_f.read()
    with open("Captain.Marvel.txt") as Captain_Marvel_f:
        print("...Opening Captain_Marvel_f_text")
        Captain_Marvel_f_text = Captain_Marvel_f.read()
    with open("Doctor.Strange.txt") as Doctor_Strange_f:
        print("...Opening Doctor_Strange_f_text")
        Doctor_Strange_f_text = Doctor_Strange_f.read()
    with open("Guardians.of.the.Galaxy.Vol.2.txt") as Guardians_of_the_Galaxy_Vol_2_f:
        print("...Opening Guardians_of_the_Galaxy_Vol_2_f_text")
        Guardians_of_the_Galaxy_Vol_2_f_text = Guardians_of_the_Galaxy_Vol_2_f.read()
    with open("Guardians.of.the.Galaxy.txt") as Guardians_of_the_Galaxy_f:
        print("...Opening Guardians_of_the_Galaxy_f_text")
        Guardians_of_the_Galaxy_f_text = Guardians_of_the_Galaxy_f.read()
    with open("Iron-Man.2.txt") as Iron_Man_2_f:
        print("...Opening Iron_Man_2_f_text")
        Iron_Man_2_f_text = Iron_Man_2_f.read()
    with open("Iron-Man.3.txt") as Iron_Man_3_f:
        print("...Opening Iron_Man_3_f_text")
        Iron_Man_3_f_text = Iron_Man_3_f.read()
    with open("Iron-Man.txt") as Iron_Man_f:
        print("...Opening Iron_Man_f_text")
        Iron_Man_f_text = Iron_Man_f.read()
    with open("Spider-Man.Far.From.Home.txt") as Spider_Man_Far_From_Home_f:
        print("...Opening Spider_Man_Far_From_Home_f_text")
        Spider_Man_Far_From_Home_f_text = Spider_Man_Far_From_Home_f.read()
    with open("Spider-Man.Homecoming.txt") as Spider_Man_Homecoming_f:
        print("...Opening Spider_Man_Homecoming_f_text")
        Spider_Man_Homecoming_f_text = Spider_Man_Homecoming_f.read()
    with open("The.Incredible.Hulk.txt") as The_Incredible_Hulk_f:
        print("...Opening The_Incredible_Hulk_f_text")
        The_Incredible_Hulk_f_text = The_Incredible_Hulk_f.read()
    with open("Thor.Ragnarok.txt") as Thor_Ragnarok_f:
        print("...Opening Thor_Ragnarok_f_text")
        Thor_Ragnarok_f_text = Thor_Ragnarok_f.read()
    with open("Thor.The.Dark.World.txt") as Thor_The_Dark_World_f:
        print("...Opening Thor_The_Dark_World_f_text")
        Thor_The_Dark_World_f_text = Thor_The_Dark_World_f.read()
    with open("Thor.txt") as Thor_f:
        print("...Opening Thor_f_text")
        Thor_f_text = Thor_f.read()

    # Build the model.
    print("BUILDING THE MODEL(s)")
    print("...Building model Ant_Man_And_The_Wasp_f_text_model")
    Ant_Man_And_The_Wasp_f_text_model = markovify.Text(Ant_Man_And_The_Wasp_f_text, state_size=state_size)
    print("...Building model Ant_Man_f_text_model")
    Ant_Man_f_text_model = markovify.Text(Ant_Man_f_text, state_size=state_size)
    print("...Building model Avengers_Age_of_Ultron_f_text_model")
    Avengers_Age_of_Ultron_f_text_model = markovify.Text(Avengers_Age_of_Ultron_f_text, state_size=state_size)
    print("...Building model Avengers_Endgame_f_text_model")
    Avengers_Endgame_f_text_model = markovify.Text(Avengers_Endgame_f_text, state_size=state_size)
    print("...Building model Avengers_Infinity_War_f_text_model")
    Avengers_Infinity_War_f_text_model = markovify.Text(Avengers_Infinity_War_f_text, state_size=state_size)
    print("...Building model Avengers_f_text_model")
    Avengers_f_text_model = markovify.Text(Avengers_f_text, state_size=state_size)
    print("...Building model Black_Panther_f_text_model")
    Black_Panther_f_text_model = markovify.Text(Black_Panther_f_text, state_size=state_size)
    print("...Building model Captain_America_Civil_War_f_text_model")
    Captain_America_Civil_War_f_text_model = markovify.Text(Captain_America_Civil_War_f_text, state_size=state_size)
    print("...Building model Captain_America_The_First_Avenger_f_text_model")
    Captain_America_The_First_Avenger_f_text_model = markovify.Text(Captain_America_The_First_Avenger_f_text, state_size=state_size)
    print("...Building model Captain_America_The_Winter_Soldier_f_text_model")
    Captain_America_The_Winter_Soldier_f_text_model = markovify.Text(Captain_America_The_Winter_Soldier_f_text, state_size=state_size)
    print("...Building model Captain_Marvel_f_text_model")
    Captain_Marvel_f_text_model = markovify.Text(Captain_Marvel_f_text, state_size=state_size)
    print("...Building model Doctor_Strange_f_text_model")
    Doctor_Strange_f_text_model = markovify.Text(Doctor_Strange_f_text, state_size=state_size)
    print("...Building model Guardians_of_the_Galaxy_Vol_2_f_text_model")
    Guardians_of_the_Galaxy_Vol_2_f_text_model = markovify.Text(Guardians_of_the_Galaxy_Vol_2_f_text, state_size=state_size)
    print("...Building model Guardians_of_the_Galaxy_f_text_model")
    Guardians_of_the_Galaxy_f_text_model = markovify.Text(Guardians_of_the_Galaxy_f_text, state_size=state_size)
    print("...Building model Iron_Man_2_f_text_model")
    Iron_Man_2_f_text_model = markovify.Text(Iron_Man_2_f_text, state_size=state_size)
    print("...Building model Iron_Man_3_f_text_model")
    Iron_Man_3_f_text_model = markovify.Text(Iron_Man_3_f_text, state_size=state_size)
    print("...Building model Iron_Man_f_text_model")
    Iron_Man_f_text_model = markovify.Text(Iron_Man_f_text, state_size=state_size)
    print("...Building model Spider_Man_Far_From_Home_f_text_model")
    Spider_Man_Far_From_Home_f_text_model = markovify.Text(Spider_Man_Far_From_Home_f_text, state_size=state_size)
    print("...Building model Spider_Man_Homecoming_f_text_model")
    Spider_Man_Homecoming_f_text_model = markovify.Text(Spider_Man_Homecoming_f_text, state_size=state_size)
    print("...Building model The_Incredible_Hulk_f_text_model")
    The_Incredible_Hulk_f_text_model = markovify.Text(The_Incredible_Hulk_f_text, state_size=state_size)
    print("...Building model Thor_Ragnarok_f_text_model")
    Thor_Ragnarok_f_text_model = markovify.Text(Thor_Ragnarok_f_text, state_size=state_size)
    print("...Building model Thor_The_Dark_World_f_text_model")
    Thor_The_Dark_World_f_text_model = markovify.Text(Thor_The_Dark_World_f_text, state_size=state_size)
    print("...Building model Thor_f_text_model")
    Thor_f_text_model = markovify.Text(Thor_f_text, state_size=state_size)

    print("COMBINING MODELS")
    model_combo = markovify.combine(
        [Ant_Man_And_The_Wasp_f_text_model, Ant_Man_f_text_model, Avengers_Age_of_Ultron_f_text_model, Avengers_Endgame_f_text_model, Avengers_Infinity_War_f_text_model, Avengers_f_text_model, Black_Panther_f_text_model, Captain_America_Civil_War_f_text_model, Captain_America_The_First_Avenger_f_text_model, Captain_America_The_Winter_Soldier_f_text_model, Captain_Marvel_f_text_model, Doctor_Strange_f_text_model, Guardians_of_the_Galaxy_Vol_2_f_text_model, Guardians_of_the_Galaxy_f_text_model, Iron_Man_2_f_text_model, Iron_Man_3_f_text_model, Iron_Man_f_text_model, Spider_Man_Far_From_Home_f_text_model, Spider_Man_Homecoming_f_text_model, The_Incredible_Hulk_f_text_model, Thor_Ragnarok_f_text_model, Thor_The_Dark_World_f_text_model, Thor_f_text_model],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    )

    print("MAKING SENTENCE")
    print(model_combo.make_sentence())

if __name__ == "__main__":
    exit(generate_sentence(state_size=10))