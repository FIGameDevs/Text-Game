from ..Utils import directions, noun_specifiers
from ..Utils.English import numbers
from .connected_players import Connected
from ..Core import global_commands, personal_commands


def start_parse(inp_words: list, connected: Connected):
    print("parsing")
    for k,v in global_commands.get_globals().items():
        if k[:3] == "cmd":
            name = k.split("_")
            found = True
            for i in range(len(name)-1):
                if name[i+1] != inp_words[i]:
                    found = False
                    break
            if found:
                v(connected)
                print("Function found")
    pass
