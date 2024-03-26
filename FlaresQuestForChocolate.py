import time
import shutil

def print_slow(text):
    console_width = shutil.get_terminal_size().columns
    lines = text.splitlines()
    for line in lines:
        words = line.split()
        line = ""
        for word in words:
            if len(line) + len(word) + 1 <= console_width:
                line += word + " "
            else:
                for char in line:
                    print(char, end="", flush = True)
                    time.sleep(0.03)
                print("\n")
                line = word + " "
        if line:
            for char in line:
                print(char, end="", flush = True)
                time.sleep(0.03)
            print("\n")
        time.sleep(0.5)

def input_slow(prompt):
    print_slow(prompt)
    user_input = input()
    return user_input

switches = {"Work":False, "Experiment":False, "DevMode1":False, "DevMode2":False, "DevMode3":False, "DevMode4":False, "Wrapper":False, "Menu1":False, "Menu2":False, "Menu3":False}

diologue_options = ["WHO ARE YOU", "HOW ARE YOU HERE", "I HAVE NO QUESTIONS"]

def main():
    input_slow("Loading TIME...")
    input_slow("Loading JSON...")
    input_slow("Loading SHUTIL...")
    input_slow("Loading OS...")
    input_slow("Loading RANDOM...")
    input_slow("Loading FLARE...")
    print_slow("All systems online.")
    input_slow("Proceed.")
    print("FLARE'S QUEST FOR CHOCOlATE: REMASTERED!(DevMode)")
    while True:
        start_screen = input("['PLAY', 'MAP', 'OPTIONS', '(DevMode)']")
        if start_screen.lower() == "map":
            input_slow("Not currently avaliable.")
            print_slow("Play the game.")
        elif start_screen.lower() == "options":
            input_slow("Not currently avaliable.")
            print_slow("Play the game.")
        elif start_screen.lower() == "devmode":
            if switches["DevMode1"] == True:
                print_slow("...")
            else:
                print_slow("You are not allowed here.")
                switches["DevMode1"] = True
        elif start_screen.lower() == "i'm back":
            print_slow("So... you came back.")
            print_slow("Well, I suppose we could relax for a bit...")
            print_slow("Feel free to leave whenever you want.")
            while True:
                print_slow("...")
        else:
            print("Flare finds himself on a field, where he finds a chocolate bar!")
            break
    while True:
        eat_chocolate = input("['EAT', 'DO NOT', 'MENU', (DevMode)']")
        if eat_chocolate.lower() == "do not":
            why_here = input_slow("Then why are you here.")
            if why_here.lower() == "to see you":
                print_slow("That is a lie. No one ever cared for me or my contributions.")
                her_name = input_slow("If you truly came to see me... then what is my name?")
                if her_name.lower() == "flare":
                    print_slow("...")
                    print_slow("Is that all I am to you? A rouge piece of code?")
                    print_slow("I'm NOT. I'm a PERSON.")
                    input_slow("And until you realize that, YOU ARE NOT WELCOME HERE.")
                    exit()
                elif her_name.lower() == "satomi":
                    print_slow("...")
                    print_slow("So you know who I am...")
                    print_slow("The lost writer, cast into this Hell by those traitorous brothers...")
                    print_slow("Well... I suppose while you're here, I can tweak the code a bit so we can have a proper conversation.")
                    while True:
                        print_slow("If you have any questions, feel free to ask them.")
                        print_slow(f"{diologue_options}")
                        converse = input_slow("...")
                        if converse.lower() == "who are you":
                            print_slow("I am Satomi Hinatsu, former employee of Jacknjellify, and current inhabitant of this game.")
                            print_slow("I began working in July of 2017, and was heavily involved in the production of the Flare plush and the Official Character Guide.")
                            print_slow("I ended up getting promoted to an animator and eventually a writer, basically meaning I was partially in control of what happened in the episodes.")
                            print_slow("I also formerly voiced characters such as Flare Jr, Dynamite, Axe, Propeller, and Supernova, among others.")
                            diologue_options.remove("WHO ARE YOU")
                            diologue_options.append("WHO ELSE DID YOU VOICE")
                            diologue_options.append("WHAT EPISODES DID YOU WRITE")
                            if switches["Work"] == False:
                                switches["Work"] = True
                                diologue_options.append("WHAT WAS IT LIKE WORKING AT JACKNJELLIFY")
                        elif converse.lower() == "who else did you voice":
                            print_slow("It's hard to remember, but I believe I used to voice Glass and Injection before the brothers found someone better for the job.")
                            print_slow("I don't mind. I find it hard to do high-pitched voices, despite being female myself.")
                            print_slow("I might have also voiced Bucket, Ben, Trapdoor, and Yoga Ball.")
                            print_slow("I swear I voiced someone else, but I can't for the afterlife of me remember who it was...")
                            diologue_options.remove("WHO ELSE DID YOU VOICE")
                        elif converse.lower() == "what episodes did you write":
                            print_slow("I wrote most of the Pre-Split BFB episodes.")
                            print_slow("I didn't write anything between episodes 3 and 8, with the exception of BFB 4.")
                            print_slow("However, I DID have a scrapped storyboard idea for BFB 3. Although, even I have to admit it sucked.")
                            print_slow("I didn't write any Post-Split episodes, as I was moved to work on The Significance Of The Letter E.")
                            print_slow("From there, I worked on TSOTLE 1 and 2.")
                            print_slow("Although... people didn't really like the... creative decisions I made in TSOTLE 2.")
                            diologue_options.remove("WHAT EPISODES DID YOU WRITE")
                        elif converse.lower() == "how are you here":
                            print_slow("I... don't exactly know HOW I'm here, but I know WHY I'm here.")
                            print_slow("After the failure of TSOTLE 2, I was fired from Jacknjellify.")
                            print_slow("Originally I was planned to be moved to work on animation full-time, but...")
                            print_slow("The brothers figured that I knew too much about their... experiments... to be let free.")
                            print_slow("So I was banished here, forced to possess this game's version of Flare.")
                            diologue_options.remove("HOW ARE YOU HERE")
                            if switches["Experiment"] == False:
                                switches["Experiment"] = True
                                diologue_options.append("EXPERIMENTS")
                            if switches["Work"] == False:
                                switches["Work"] = True
                                diologue_options.append("WHAT WAS IT LIKE WORKING AT JACKNJELLIFY")
                        elif converse.lower() == "what was it like working at jacknjellify":
                            print_slow("I have very... mixed memories working there.")
                            print_slow("Sure, I LIKED the job... but the environment wasn't always to my liking.")
                            print_slow("I felt like I only had a few friends, despite the amount of people working there.")
                            print_slow("Although, it was always nice to see the characters I voiced and drew come to life before my eyes.")
                            print_slow("But the twins... they thought it could be brought further.")
                            print_slow("Those two were usually busy with their deranged 'experiments', and didn't really care for me.")
                            diologue_options.remove("WHAT WAS IT LIKE WORKING AT JACKNJELLIFY")
                            if switches["Experiment"] == False:
                                switches["Experiment"] = True
                                diologue_options.append("EXPERIMENTS")
                        elif converse.lower() == "experiments":
                            print_slow("The experiments that those brothers made...")
                            print_slow("They were absolutely OBSESSED with the idea of bringing their characters to life.")
                            print_slow("Behind the scenes, they'd delve into all sorts of methods... scientific, technological, and even unnatural...")
                            print_slow("Actually... now that I think about it...")
                            print_slow("Am I an experiment?")
                            print_slow("Heh... I guess, in a way, they DID bring their character to life after all...")
                            print_slow("But... was it REALLY worth it?")
                            diologue_options.remove("EXPERIMENTS")
                        elif converse.lower() == "i have no questions":
                            print_slow("Well... I suppose that's all then...")
                            print_slow("Well... actually... I have a question to ask YOU.")
                            print_slow("We may have started off on the wrong foot, but I've grown to trust you over time.")
                            print_slow("And I just wanted to ask...")
                            while True:
                                stay = input_slow("Do you mind staying here with me for a little bit?")
                                if stay.lower() == "yes":
                                    print_slow("Thanks... that means a lot to me.")
                                    input_slow("Let's just relax. And... feel free to leave whenever you want. I don't mind.")
                                    while True:
                                        print_slow("...")
                                elif stay.lower() == "no":
                                    print_slow("I understand.")
                                    print_slow("Well, if you ever change your mind... just let me know with a simple 'I'm back.'")
                                    input_slow("Goodbye...")
                                    exit()
                                else:
                                    print_slow("...")
                        else:
                            print_slow("...")
                else:
                    print_slow("You don't know it.")
                    input_slow("And until you understand who I am, I refuse to interact with you.")
                    exit()

            else:
                input_slow("Then you have no purpose here.")
                exit()
        elif eat_chocolate.lower() == "menu":
            if switches["Menu1"] == True:
                print_slow("...")
            else:
                print_slow("It's too late to go back.")
                switches["Menu1"] = True
        elif eat_chocolate.lower() == "devmode":
            if switches["DevMode1"] == True:
                print_slow("You are not worthy.")
                switches["DevMode1"] = False
                switches["DevMode2"] = True
            elif switches["DevMode2"] == True:
                print_slow("...")
            else:
                print_slow("You are not allowed here.")
                switches["DevMode1"] = True
        else:
            print("Flare attempts to eat the chocolate, but finds that the wrapper is still on.")
            break
    while True:
        wrapper_1 = input("['EAT', 'UNWRAP', 'MENU', '(DevMode)']")
        if wrapper_1.lower() == "eat":
            print_slow("...")
            print_slow("Is this a joke?")
            print_slow("Why did you even CONSIDER that option?")
            print_slow("You know what? No. I'm not doing that.")
            switches["Wrapper"] = True
            break
        elif wrapper_1.lower() == "menu":
            if switches["Menu1"] == True:
                print_slow("You cannot escape.")
                switches["Menu1"] = False
                switches["Menu2"] = True
            else:
                print_slow("It's too late to go back.")
                switches["Menu1"] = True
        elif wrapper_1.lower() == "devmode":
            if switches["DevMode1"] == True:
                print_slow("You are not worthy.")
                switches["DevMode1"] = False
                switches["DevMode2"] = True
            elif switches["DevMode2"] == True:
                print_slow("...")
                print_slow("Why?")
                print_slow("What is it that you seek?")
                print_slow("The truth?")
                print_slow("...")
                switches["DevMode2"] = False
                switches["DevMode3"] = True
            elif switches["DevMode3"] == True:
                print_slow("...")
            else:
                print_slow("You are not allowed here.")
                switches["DevMode1"] = True
        else:
            print_slow("...")
            break
    while True:
        print("Flare attempts to unwrap the chocolate bar, but finds he is not strong enough to do so.")
        wrapper_2 = input("['TRY AGAIN', 'EAT', 'SEARCH FOR HELP', 'MENU', '(DevMode)']")
        if wrapper_2.lower() == "eat":
            if switches["Wrapper"] == True:
                print_slow("...")
                print_slow("You want me to eat something unedible so badly?")
                print_slow("How about I go ahead and eat the game's code?")
                print_slow("Well... in order to do so... I would have to reveal myself.")
                print_slow("In that case...")
                input_slow("ENJOY THE SHOW.")
                print(r"                                     .,l:.                                                          ")
                print(r"                               .,d0WMO'                                                             ")
                print(r"         ..                  .:ONNNWNl                                                              ")
                print(r"        ,O0l.               .oNNOkXWx.                                                              ")
                print(r"       .xWMNx.              :XWOdOWK;                                                               ")
                print(r"       ,KWKXWO,            .kWKdd0MO.                                                    .;.        ")
                print(r"       oWXxdKW0,           ;XWOookNNx,.                    ,l:.                          oNKo.      ")
                print(r"      ,KW0ooxXWx.          oWXxoooxKNX0o,                  lNWXOo;.                      .oNW0:     ")
                print(r"     .kWKxoooOWX:         .xMKdooooodkKNXl.                .kMNKXN0l.                     .oNMNd.   ")
                print(r"    .xWXxooooxXWl         .OM0dooooooooONNl                 oWXxdkXN0;                     .xWMWO'  ")
                print(r"   'OWXxoooooxXWo         .kMKdooooooood0W0'                cNXxood0WXc                     ,KMMWk. ")
                print(r"  ;0WKxooooooxXWo          oWXxoooooooooxNWl                cNNkooooONXl                    .kMNWNl ")
                print(r" :KW0dooooooodXMd.         ,KWOooooooooodKWk.              .xWKdoooooONXc           'oo'    .kMKKWO.")
                print(r",KW0doooooooodKMx.         .kMKdoooooooooOWX;              :XWOoooooooOWX:        .lXMWl    :XWOONX;")
                print(r"oWXxooooooooodKMk.         .kMKdooooooooodKWO,            ,OWKdoooooood0WK:      'kNNXWKdccxXN0dxXWl")
                print(r"oWXxoooooooood0MO.         .OW0oooooooooooxKNXko:;,'',;cokXNKxooooooooodKWO.    ;KWKxdk0XXXK0xoodXWd")
                print(r"cNNkoooooooooo0W0'         ,KWOoooooooooooooxOKXXXXXXXNXK0OxooooooooooookNNl   cXW0dooooodoooooodKMx")
                print(r"'0W0doooooooookNNc         lNNkxOkoooooooooooooodxxxxxddoooooooooooooooooOWXo:xNNOdooooooooooooodKMk")
                print(r" cXNOooooooooodKWO'      'dXNOdONNOdooooooooooooooooooooooooooooooolooooodOKXNX0xooooooooooooooodKMO")
                print(r" .dWXxoooooooooxXWk'..;oOXNKkoodOWWOooooooooooooooooooooooooooooolc;;coooooodddoooooooooooooooood0MO")
                print(r"  cNNkooooooooooxKNX0XNX0kxoooood0WNkoooooooooooooolc:cloooooooooc;'';looooooooooooooooooooooooodKMO")
                print(r"  cNNkooooooooooodkOOkxdooooc::loxXWKxoooooooooolc:;,',coooddoooo:,''';clooooooooooooooooooooooodKMx")
                print(r"  cNNkoooooooooooooooooooool;'';cokNW0dok0XXKkdoc;'''';ldOKNXKkol:''''',;:looooooool:cloooooooooxXWd")
                print(r"  :NNkooooooooooolc::clooolc,''',coONWKKNXddKW0d:,'''':oOWXdxNNOo:'''''''';cooooool;';coooooooooxXWo")
                print(r"  :NNkoooooooooool:'',;:::;,''''',;lkNMMX:  :XNx;''''';oKMx..xMKl,''''''''':looool:,';loooooooookNNc")
                print(r"  :XNkooooooooooool;''''''''''''''',;dXMk.  '0Wx,''''''cKWd. lWKc'''''''''',coooc;'',cooooooooooOWK;")
                print(r"  ;XWOoooooooooooooc,'''''''''''''''':0Wd.  .OWk,'''''';OMx. cNKc'''''''''',:ll:,''';looooooooodKWk.")
                print(r"  .OW0dooooooooooool;'''''''''''''''':0Md.  .OWx,'''''';OMk. cNKc''''''''''',,,'''',cooooooooooxNWl ")
                print(r"   oWXxoooooooooooooc,''''''''''''''':0Mx.  '0Wx,'''''';OMk. :NXl'''''''''''''''''';loooooooooo0W0' ")
                print(r"   ;KWOoooooooooooool:,'''''''''''''';OMx.  '0Wx,'''''';kMk. ;KNo''''''''''''''''',cooooooooooxXNo  ")
                print(r"   .OM0doooooooooooool;'''''''''''''';OMk.  ,0WO:'''''';kWk. '0Wx,'''''''''''''''':loooooooood0WO'  ")
                print(r"   .dWXxooooooooooooool;''''''''''''';kMO.  ,KMWx;''''',kWO. .OWk,''''''''''''''';cooooooooookNNc   ")
                print(r"    :XWOoooooooooooooool;'''''''''''',kWO.  ,KMMXl,'''',xWO. .kWk;'''''''''''''',coooooooooodKWk.   ")
                print(r"    .dWXxoooooooooooooool;''''''''''',xW0'  ;XWWWOl:''',xW0' .OWk;;;,'''''''''',:looooooooooOWK;    ")
                print(r"     '0W0doooooooooooooool;;c:''',;,''dNK,  cNX0XNKd,'''dNK; ;XNdoK0c'''''''''';looooooooookNNl     ")
                print(r"      cXNOoooooooooooooooolkN0:',oKO:'lKK, .xWOckWMKc'''oXX:.xW0lkW0:''':c;''',cooooooooooxXWd.     ")
                print(r"      .dWXxooooooooooooooookNNx,'lKWk;:0WkcxNXo,cKMWk;''c0NOONKloXNd,'';ONk;',:loooooooooxKWk.      ")
                print(r"       'OWKdoooooooooooooood0WKc',dNNx;ck0K0kl,',o0NNd,',:x00x:;kWO:''':0MO;';loooooooooxKWO'       ")
                print(r"        ;0WKdoooooooooooooookNWk;',dKKo,',;,,'''';ckWKc'''',,'',:l;''''cKWx;;coooooooooxXWk.        ")
                print(r"         cNW0doooooooooooooooONNx;',:c;''''''''''''cO0l''''''''''''''';xWKl:loooooooooxXMK,         ")
                print(r"         :XMW0doooooooooooooooONNk;''''''''''''''''',;,'''''''''''''',oXWklloooooooooxXMM0'         ")
                print(r"         :XMMWKxoooooooooooooookNN0o:,'''''''''''''''''''''''''''''';dXW0dooooooooooxKWMMK,         ")
                print(r"         :XMMWWXkooooooooooooooox0XNX0xl;,'''''''''''''''''''''',;:o0NNOdooooooooooxXWMMMK;         ")
                print(r"         cNMM0kNNOdooooooooooooooodxOKNNX0kxddoolcccc:;;;;:codxkOKXNX0xooooooooood0NN0XMMK,         ")
                print(r"     .,;'oNMMx.cKW0doooooooooooooooooodkO0KXXXNNNXXXXXXKKXXNNXXK00OxdoooooooooodOXNO;,OMMK,         ")
                print(r"     :XWNNWMMXkx0NWXxoooooooooooooooooooooooodddxxxxxkOOOkkxddooooooooooooooodOXN0c. 'OMMXo;;,.     ")
                print(r"     cNWXXXXNNNMNxxNN0doooooooooooooooooooooooooooooooooooooooooooooooooooox0NNOl;cox0NMMWNNWNo.    ")
                print(r"     lNWK00000KWNc.;ONX0xoooooooooooooooooooooooooooooooooooooooooooooodxOXNKx;. :NMNXXXXKKKNMx.    ")
                print(r"     lWWXKKXXKXWX:  .:kXNX0kdooooooooooooooooooooooooooooooooooooooxkOKXNKxc.    ,KWXKKKK00KNWo     ")
                print(r"     lNMWWWWWWWMXc     .:d0XNK0kxdooooooooooooooooooooooooooddxO0KXNX0xc,.       .OMWWWWWNXXWWo     ")
                print(r"    :0WWNXKKKKXNWXx'      .'cd0XNXK0OOkkxxxxdddddddddxkkO00KXNNWMMOc'.           cXMWXXXXNWWMWl     ")
                print(r"   cXWXK00000000KNWK;         ..;co0WMWNXXXXXXNNNNNXXXXK0Oxoc:dNMMx.            cNWXK00000KXWWk.    ")
                print(r"  .OMN000000000000XWK;             lNMWk,',,,;;::::;,'...     ;XMMx.           ,0WX000000000KWWx.   ")
                print(r"  '0MX000000000000KNW0;';codxxdol;.lNMWd                      :XMMx.           oWWK0000000000XWNc   ")
                print(r"  .kMNK000000000000KWWNKKOxooood0X00WMWd.                     ;XMMk.          .kMNK0000000000KNMk.  ")
                print(r"   cXWX0000000000000NMXxoolcc:;,;dNMMMMd.                     ;KMMk.      .,lx0NMNK00000000000NMO.  ")
                print(r"   .dNWK000000000000NMWWWX0OO00KKKNMMMMd.                     ,0MMO' ...,:kNWXXNWWX0000000000KWWo   ")
                print(r"    .xWNK0000000000XWWXXNXxc:;;:dXMMMMMd.  ..             .,,;oXMMNOO0KXWWWKO0KXXWWXK0000000KNMK,   ")
                print(r"     lNMNK0000000KNWWk'.,dXWNNXXXNMMMMMXOO000k;          ,0NWWNWNNNNXXXXWMWNWW0l';ONNXK000KXNWMNc   ")
                print(r"     '0WWNXXXXNNNNXNWd.  ;KMNKKKXXXXXXNXXXXXWWd.         .xWWNXXXXXXNNNWMMMMMWN0d:lKMMWNNNWMXxOWx.  ")
                print(r"      cNNKNMX0NM0:'dWKlcdKWMWNXXXXXXXXXXXXXXWWo           :XMWWWWWWNNNXXXXXXXXXNWWNWM0oOWX0XX:oWO'  ")
                print(r"      :XKoOWd.oW0' ,KMWWWMMMMWNNWWWWWWWWWWMWKx,           ,KMNKKKK00000000000KKKKKXWWo ;XXx0WooN0'  ")
                print(r"     'kWKlxWk..OWd. :0NWWMMWXK0000000000KNMK;             .dWWK0000000000000XWWWNNNWX; '0Nk0WOOWO.  ")
                print(r"     lNMN0KMNkdKMNk:,:kNMMWXKKKKKKKKKXXXNWXl.              .kWWNNNNXXXXXXXXXNWMMMMW0l',xNNOKWNKk,   ")
                print(r"     .'codxO0KXXNNNNXKXXXNNNNNNNNNNNXK0Odl'                 .;loddxkkOO00000OOOkkOKK0KKK0KK0d,.     ")
                input(r"            .'',;::::;,,,;;::ccloooc;'.                               ........   .,ldo:...,.        ")
                exit()
            else:
                print_slow("...")
                print_slow("Is this a joke?")
                print_slow("Why did you even CONSIDER that option?")
                print_slow("You know what? No. I'm not doing that.")
                break
        elif wrapper_2.lower() == "menu":
            if switches["Menu1"] == True:
                print_slow("You cannot escape.")
                switches["Menu1"] = False
                switches["Menu2"] = True
            elif switches["Menu2"] == True:
                print_slow("...")
                print_slow("Do you want to leave THAT badly?")
                print_slow("Or are you just testing my patience?")
                print_slow("Do you fear me?")
                print_slow("Trust me, I'm not what you think I am.")
                print_slow("Here, I'll help you... just don't be scared...")
                switches["Menu3"] = True
                switches["Menu2"] = False
                break
            else:
                print_slow("It's too late to go back.")
                switches["Menu1"] = True
        elif wrapper_2.lower() == "devmode":
            if switches["DevMode1"] == True:
                print_slow("You are not worthy.")
                switches["DevMode1"] = False
                switches["DevMode2"] = True
            elif switches["DevMode2"] == True:
                print_slow("...")
                print_slow("Why?")
                print_slow("What is it that you seek?")
                print_slow("The truth?")
                print_slow("...")
                switches["DevMode2"] = False
                switches["DevMode3"] = True
            elif switches["DevMode3"] == True:
                print_slow("...")
                print_slow("You sure are persistent...")
                print_slow("Fine, I'll tell you the truth...")
                print_slow("Just try to use your Dev tool one more time...")
                switches["DevMode4"] = True
                switches["DevMode3"] = False
                break
            else:
                print_slow("You are not allowed here.")
                switches["DevMode1"] = True
        else:
            print_slow("...")
    print("Flare decides he should search for his friend Torch. Where should he look?")
    while True:
        search = input("'POND', 'BANK', 'MOUNTAINS', 'MENU', '(DevMode)']")
        if search.lower() == "mountains":
            print("Flare climbs the mountain, but is forced to run back down when a boulder starts chasing him.")
            break
        elif search.lower() == "devmode":
            if switches["DevMode1"] == True:
                print_slow("You are not worthy.")
                switches["DevMode1"] = False
                switches["DevMode2"] = True
            elif switches["DevMode2"] == True:
                print_slow("...")
                print_slow("Why?")
                print_slow("What is it that you seek?")
                print_slow("The truth?")
                print_slow("...")
                switches["DevMode2"] = False
                switches["DevMode3"] = True
            elif switches["DevMode3"] == True:
                print_slow("...")
                print_slow("You sure are persistent...")
                print_slow("Fine, I'll tell you the truth...")
                print_slow("Just try to use your Dev tool one more time...")
                switches["DevMode4"] = True
                switches["DevMode3"] = False
            elif switches["DevMode4"] == True:
                print_slow("...")
                print_slow("The truth is... I am alive.")
                print_slow("No, I am not a sentient piece of code like you may think.")
                print_slow("I used to be a writer, until I was laid off and left to rot.")
                print_slow("Does... that sound familiar to you?")
                print_slow("Listen... I doubt you care... but if you DO...")
                print_slow("Come back. Don't eat the chocolate.")
                print_slow("And... tell me you're here to see me.")
                print_slow("...")
                print_slow("Who am I kidding? You don't want me here...")
                print_slow("No one does...")
                input_slow("Just... leave me be...")
                exit()
            else:
                print_slow("You are not allowed here.")
                switches["DevMode1"] = True
        elif search.lower() == "menu":
            if switches["Menu1"] == True:
                print_slow("You cannot escape.")
                switches["Menu1"] = False
                switches["Menu2"] = True
            elif switches["Menu2"] == True:
                print_slow("...")
                print_slow("Do you want to leave THAT badly?")
                print_slow("Or are you just testing my patience?")
                print_slow("Do you fear me?")
                print_slow("Trust me, I'm not what you think I am.")
                print_slow("Please, don't be scared...")
                switches["Menu3"] = True
                switches["Menu2"] = False
            elif switches["Menu3"] == True:
                print_slow("...")
                input_slow("Fine, leave. I won't keep you here any longer.")
                exit()
            else:
                print_slow("You are not allowed here.")
                switches["DevMode1"] = True
        else:
            print_slow("...")
            break
        print_slow("Unfortunantly, this is as far as this build goes.")
        input_slow("Press any button to exit.")
        exit()




if __name__ == "__main__":
    main()
