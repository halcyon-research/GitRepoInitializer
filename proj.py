#!/usr/bin/python

import os
import argparse
import json
import emoji


data = {}  
data['project'] = []
parser = argparse.ArgumentParser()
parser.add_argument("init")
args = parser.parse_args()

if args.init:
    name = input('Project Name: ')
    strippedName = name.replace(" ", "")
    author = input('Author: ')
    version = input('Version: ')
    description = input('Description: ')
    os.system('clear')
    os.system('mkdir ' + strippedName)
    os.chdir(strippedName)
    os.system('git init')

    f = open("README.md", "w")
    f.write("# " + strippedName + "\n")
    f.write(description + "\n")
    f.write("## Author" + "\n")
    f.write(author + "\n") 
    f.close()

    githubName = input("Enter Github Username: ")

    command = "curl -u '" + githubName + "' https://api.github.com/user/repos -d '{\"name\":\"" + strippedName + "\"}'"

    #print(command)
    #curl -u 'USER' https://api.github.com/user/repos -d '{"name":"REPO"}'
    #git remote add origin git@github.com:USER/REPO.git
    #https://github.com/michaelpeterswa/testProject4.git
    #git push origin master
    
    gitRemote = "https://github.com/" + githubName + "/" + strippedName + ".git"
    gitLink = "https://github.com/" + githubName + "/" + strippedName 

    data['project'].append({'author': author,
                            'projectName': name,
                            'version': version,
                            'description': description,
                            'githubLink': gitLink
                            })

    with open('info.json', 'w') as outfile:  
        json.dump(data, outfile, indent=4)

    os.system('git add .')
    os.system('git commit -m "first commit made with RepoCreator"')
    os.system(command)
    os.system('git remote add origin ' + gitRemote)
    os.system('git push -u origin master')

    


    os.system('clear')
    print(emoji.emojize(':zap: Repository Creator Finished Successfully :zap:', use_aliases=True))
    print("Repository name: " + strippedName)
    print("Author: " + author)
    print("Version: " + version)
    print("Description: " + description)
    print("")
    print(gitLink)
