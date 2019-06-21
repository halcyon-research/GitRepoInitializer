# GitRepoInitializer
This python script helps efficiently create and attach a folder to a remote Github repository. All from the command line!

> Repository for my repository generator program. This program creates a project folder, a standard README.md, an information file, and then begins the process of creating and pushing to the new remote GitHub repo. Then the program displays to the user that the operation completed successfully with the parameters they provided.

## Installation

```
git clone https://github.com/michaelpeterswa/GitRepoInitializer.git
```
Or download the file manually. Then create a symbolic link to a folder in the system path for the program.
Then change directories to where the new link is located, change the permissions, and the program is ready to use!
```
ln -s ~/GitRepoInitializer/proj.py /usr/.local/bin/proj
cd /usr/.local/bin
sudo chmod +x proj
cd ~
proj init
```

## Release History

* 0.1
    * Opened Repository (06.15.19)

## Meta

Michael Peters – michael@michaelpeterswa.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/michaelpeterswa](https://github.com/michaelpeterswa)
