#!/usr/bin/python3

# # # # # # # # # # # #
#               _    #
#     ___ _____(_)    #
#    / _ `/ __/ /     #
#    \_, /_/ /_/      #
#   /___/             #
#                     #
# GitRepoInitializer  #
# Michael Peters      #
# 2019 - 2020         #
# # # # # # # # # # # #

import os
import argparse
import json
import emoji
from datetime import datetime
from secrets import pat as token
from secrets import uname as username


def prettyPrinter(name, auth, ver, desc, longDesc, date, link):
    name = ":fire: Repository Name: " + name
    auth = ":books: Author: " + auth
    ver = ":bar_chart: Version: " + ver
    desc = ":page_facing_up: Description: " + desc
    longDesc = ":clipboard: Long Description: " + longDesc
    date = ":date: Date: " + date
    message = ":zap: Repository Successfully Initialized :zap:"

    print(addEmoji(message))
    print("")
    print(addEmoji(name))
    print(addEmoji(auth))
    print(addEmoji(ver))
    print(addEmoji(desc))
    print(addEmoji(longDesc))
    print(addEmoji(date))
    print("")
    print(link)


def addEmoji(str):
    return emoji.emojize(str, use_aliases=True)


def writeToJSON(name, auth, ver, desc, longDesc, date, link):
    data = {}
    data["project"] = []

    data["project"].append(
        {
            "author": auth,
            "projectName": name,
            "version": ver,
            "description": desc,
            "longDescription": longDesc,
            "githubLink": link,
            "date": date,
        }
    )

    with open("info.json", "w") as outfile:
        json.dump(data, outfile, indent=4)


def writeReadme(name, auth, ver, desc, longDesc, date, link):
    f = open("README.md", "w")
    f.write("# " + name + "\n")
    f.write(desc + "\n")
    f.write("> " + longDesc + "\n")
    f.write("## Installation" + "\n")
    f.write("```" + "\n")
    f.write("git clone " + link + "\n")
    f.write("```" + "\n")
    f.write("Or download the file manually." + "\n")
    f.write("## Release History" + "\n")
    f.write("* " + ver + "\n")
    f.write("   * " + "Opened Repository " + date + "\n")
    f.write("## Meta" + "\n")
    f.write(auth + " - *enter additional contact information here*" + "\n")
    f.write(
        "\nDistributed under the ____ license. See ``LICENSE`` for more information."
    )
    f.close()


# ---------------------------------

parser = argparse.ArgumentParser()
parser.add_argument("init")
args = parser.parse_args()

if args.init:

    # INPUTS
    name = input("Project Name: ")
    strippedName = name.replace(" ", "")
    author = input("Author: ")
    version = input("Version: ")
    description = input("Short Description: ")
    longDescription = input("Long Description: ")
    githubName = username
    date = datetime.today().strftime("%m.%d.%Y")
    dateFormatted = "(" + date + ")"

    # create, enter, and init project directory
    os.system("clear")
    os.system("mkdir " + strippedName)
    os.chdir(strippedName)
    os.system("git init")

    # format repository opening request
    command = (
        "curl "
        + '--header "Authorization: token '
        + token
        + '"'
        + ' https://api.github.com/user/repos -d \'{"name":"'
        + strippedName
        + "\"}'"
    )

    # format two links to the repository
    gitRemote = "git@github.com:" + githubName + "/" + strippedName + ".git"
    gitLink = "https://github.com/" + githubName + "/" + strippedName

    # create first files
    writeReadme(
        name, author, version, description, longDescription, dateFormatted, gitRemote
    )
    writeToJSON(name, author, version, description, longDescription, date, gitLink)

    # add, commit, create repository, connect remote, and push
    os.system(command)
    os.system("git remote add origin " + gitRemote)
    os.system("git add .")
    os.system('git commit -m "feat: first commit made with GitRepoInitializer"')
    os.system("git push -u origin master")

    # show that the process has completed successfully
    os.system("clear")
    prettyPrinter(
        strippedName, author, version, description, longDescription, date, gitLink
    )

