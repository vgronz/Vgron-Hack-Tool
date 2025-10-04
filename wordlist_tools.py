from core import VgronTool, VgronToolsCollection


class bobsrck(VgronTool):
    TITLE = "Bobs RCK"
    DESCRIPTION = "This attack tool is used to brute force passwords using a dictionary attack."

    INSTALL_COMMANDS = ["git clone https://github.com/r3nt0n/bopscrk.git",
                        "cd bopscrk && pip install -r requirements.txt"]

    RUN_COMMANDS = ["python ./bopscrk/bopscrk/bopscrk.py -i"]

class WordlistTools(VgronToolsCollection):
    TITLE = "wordlist tools"
    DESCRIPTION = "Password tools are a collection of tools that can be used to brute force passwords."
    TOOLS = [
        bobsrck()
    ]