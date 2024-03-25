# at4br-ex4

## Basic info
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
Well done! You've just created your first git repository. Now it's time to add the first file. To do so, you will have to:
- Create the file
- Add file to the commit using `git add <filename>`
</br>
> [!NOTE]
> There is a useful **-u flag** for that command - by typing `git add -u` you add all untracked files to a particular commit.

- Commit changes by typing `git commit` - it will create a unique version of chosen files, with is own hash value; it can be restored later at any point.
<br/>
> [!NOTE]
> Usually git requires you to specify a message for a praticular commit. It can be done by using **-m flag**, just like that: `git commit -m 'your message'`

- Push the exsting changes to the cloud: `git push` command will update the changes you've commited on the remote repository.
<br/>
> [!TIP]
> Don't forget to push your changes in case of fire.

```
cd path/to/your/directory
echo "print('Hello, world!') > test_file.py
git add test_file.py
git commit -m 'my first commit'
git push
```

### Other useful commands
Some extra functionalities to help you become a git expert.
- `git status` - displays the status of working directory and staging area; for checking which files are tracked and which are staged for commit
- `git log` - displays the commit logs

### Ooooops, something went wrong...
- You desperately need a time machine to come back to a particular version or want to restore accidentally deleted files?

```
git reflog
git reset HEAD@{index}
```
- You've just commited some files and did a typo? You can actually edit an existing commit by using **--amend --no-edit flags**:

```
git add <filename>
git commit --amend --no-edit
