# at4br-ex4


## :woman_technologist: Basic info
- Author's name: Lena Fiedor
- Occupation: bioinformatics student, sailor, ballet dancer
- Date of the exercise session: 20 III 24r


## Little git tutorial
Git is a version control system used for coordinating work amongst programmers working simultanously on software development.


### Creating a repository
To create your first git repository, you can follow two ways:
- Create a new repository (virtual storage of your project): navigate to the project directory and use the `git init` command.
```
cd path/to/your/directory
git init
```

- Clone an existing repository into project directory using `git clone`:
```
git clone <repo url or ssh>
```

### Saving changes
:rocket: Well done! You've just created your first git repository. Now it's time to add the first file. To do so, you will have to:
- Create the file
- Add file to the commit using `git add <filename>`
> [!NOTE]
> There is a useful **-u flag** for this command - by typing `git add <filename>` you add all untracked files to a particular commit.

- Commit changes by typing `git commit` - it will create a unique version of chosen files, with is own hash value; it can be restored later at any point.
> [!NOTE]
> Usually git requires you to specify a message for a particular commit. It can be done by using **-m flag**, just like that: `git commit -m 'your message'`

- Push the exsting changes to the cloud: `git push` command will update the changes you've commited on the remote repository.
> [!TIP]
> Don't forget to push your changes in case of fire.

```
cd path/to/your/directory
echo "print('Hello, world!') > test_file.py
git add test_file.py
git commit -m 'my first commit'
git push
```

### Creating a new branch
Using branches facilitates synchronized and collaborative work, when each developer works on a different issue / enhancement. Branch is a paralell version of a repository's development line. After you've completed the task, you can **merge branch** into main. Enough said, time to create a new branch!
- Check the branch you're currently at using `git checkout`...
- ...or list all existing branches in youtr repository by typing `git branch`
- To create a new branch, use `git branch <branch-name>`
- Alternatively, you can use `git checkout` with **-b flag** along with specified branch name; this command will also switch to the new branch
- Switch to your new branch by typing `git branch <branch-name>`

In conclusion, the following code:
```
git branch <branch-name>
git checkout <branch-name>
```
Will have the same results as:
```
git checkout -b <branch-name>
```

- To integrate changes with main, **switch to the main branch** and type `git merge <feature-branch>`; be aware of the probable merge conflicts - you do not want the other features to disappear!


### Other useful commands
Some extra functionalities to help you become a git expert.
- `git status` - displays the status of working directory and staging area; for checking which files are tracked and which are staged for commit
- `git log` - displays the commit logs
- `git diff` - displays the changes between two commits, branches, commit and working tree etc.
- `git pull` - pulls changes from remote repository to your local directory; useful when working in a github flow model

### :skull: Ooooops, something went wrong...
> Partially inspired by: [Oh Shit, Git!?!](https://ohshitgit.com)
- You desperately need a time machine to come back to a particular version or want to restore accidentally deleted files?
```
git reflog
git reset HEAD@{index}
```

- You've just commited some files and did a typo? You can actually edit an existing commit by using `--amend --no-edit flags`:
```
git add <filename>
git commit --amend --no-edit
```

- You want to change the message of your last commit? Use:
```
git commit --amend
```

And simply follow the displayed instructions.

### :bulb: Commands summary with flags (sorted alphabetically)

Usage: `git <command> <flags>`

| Command | Functionality | Useful parameters & flags (-short / --full-name) |
| ------- | ------------- | ----- |
| **add** | add changes to commit | `-A / --all` (adds all changes, including untracked and deleted files), `-u / --update` (adds only modified and deleted files, but not untracked) |
| **branch** | list (without parameters), create, rename and delete branches | `<branch-name>` (creates new branch with specified name), `-m <old-name> <new-name>` (renames branch), `-d <branch-name>` (deletes specified branch), `-r` (lists remote branches), `-a` (lists both remote and local branches) |
| **checkout \[&lt;branch-name&gt;\]** | check info about current branch; with **&lt;branch-name&gt;** parameter - switch to another branch | `-b / -B <branch-name>` (creates new branch and switches to it if branch does not exist) |
| **commit** | commit changes | `-m / --message` (allows to specify the commit message without using text editor), `-a / --all` (stages changes automatically before commiting, equivalent to git add -u & git commit), `--amend` (edits the previous commit without creating a new one) |
| **diff** | display differences between two states of the repositiry | `<commit-hash-1> <commit-hash-2>` (compares two commits), `<main-branch>` (compare the current branch with main), `--staged` (wiev changes in the staging area) |
| **init** | initialize a new git repository | none |
| **log** | display commit history of the entire repository | `--oneline` (condenses each commit to a single line), `-n / --max-count` (limits the number of commits displayed), `--all` (shows commits from all of the branches) `--grep=<pattern>` (searches commit messages for the specified pattern) |
| **merge &lt;branch-name&gt;** | merge specified branch into current branch | `--squash` (condenses all commits from feature branch into one before merging), `--abort` (quits current merge operation and restores the state of repository from before merge began), `--rebase` (integrate commits from main branch to the feature branch in order to maintain linear history) |
| **pull** | pull changes from remote to local repository | `-r / --rebase` (rebases your branch instead of merging to keep linear history by moving your local commits on top of the updated remote commits) |
| **push** | push existing changes to the remote repository | `-u / --set-upstream origin <branch-name>` (sets the upstream branch for current local branch, enabling using git push without specyfying branch names in the future) |
| **reflog** | display information stored in reference logs (list of actions that affected the HEAD reference) | none |
| **reset &lt;commit&gt;** | move the HEAD and the current branch pointer to a specific commit from the past | none |
| **status** | display the current state of the repository | `-b / --branch` (displays the name of the current branch and its relation with the upstream branch (if tracking is enabled) and number of commits ahead/behind the upstream branch) |

> [!CAUTION]
> Watch `git merge` should be performed on the main branch, while `git merge --rebase` - on the feature branch.


## Usage of AI :alien:
I hereby declare the usage of ChatGPT 3.5 for this project on account of finding useful flags for particular git commands.
