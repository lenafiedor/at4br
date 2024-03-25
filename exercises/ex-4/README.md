# at4br-ex4


## :woman_technologist: Basic info
- author's name: Lena Fiedor
- occupation: bioinformatics student, sailor, ballet dancer
- date of the exercise session: 20 III 24r
- partially inspired by: [Oh Shit, Git!?!](https://ohshitgit.com)


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
Time to create a new branch.
- to create a new branch, use `git checkout &lt;branch-name&gt;`

### Other useful commands
Some extra functionalities to help you become a git expert.
- `git status` - displays the status of working directory and staging area; for checking which files are tracked and which are staged for commit
- `git log` - displays the commit logs
- `git diff` - displays the changes between two commits, branches, commit and working tree etc.
- `git pull` - pulls changes from remote repository to your local directory; useful when working in a github flow model

### :skull: Ooooops, something went wrong...
- You desperately need a time machine to come back to a particular version or want to restore accidentally deleted files?

```
git reflog
git reset HEAD@{index}
```
- You've just commited some files and did a typo? You can actually edit an existing commit by using **--amend --no-edit flags**:

```
git add <filename>
git commit --amend --no-edit
```

- You want to change the message of your last commit? Use:

```
git commit --amend
```

And simply follow the displayed instructions.

### :bulb: Commands summary with flags

Usage: `git <command> <flags>`

| Command | Functionality | Useful flags (-short / --full-name) |
| ------- | ------------- | ----- |
| **init** | initialize a new git repository | none |
| **add** | add changes to commit | `-A / --all` (adds all changes, including untracked and deleted files), `-u / --update` (adds only modified and deleted files, but not untracked) |
| **commit** | commit changes | `-m / --message` (allows to specify the commit message without using text editor), `-a / --all` (stages changes automatically before commiting, equivalent to git add -u & git commit), `--amend` (edit the previous commit without creating a new one) |
| **push** | push existing changes to the remote repository | `-u / --set-upstream origin <branch-name>` (sets the upstream branch for current local branch, enabling using git push without specyfying branch names in the future) |
| **pull** | pull changes from remote to local repository | `-r / --rebase` (rebase your branch instead of merging to keep linear history by moving your local commits on top of the updated remote commits) |
| **reflog** | display information stored in reference logs (list of actions that affected the HEAD reference) | none |
| **log** | display commit history of the entire repository | `--oneline` (conenses each commit to a single line), `-n / --max-count` (limits the number of commits displayed), `--all` (show commits from all of the branches) `--grep=<pattern>` (searches commit messages for the specified pattern) |
| **reset** | move the HEAD to a specific commit from the past | none |
| **checkout \[&lt;branch-name&gt;\]** | check info about current branch; with **&lt;branch-name&gt;** parameter - switch to another branch | `-b / -B &lt;branch-name&gt;` (creates new branch and switches to it if branch does not exist) |


## :alien: Usage of AI
I hereby declare usage of ChatGPT 3.5 on account of finding useful flags for particular git commands.
