# at4br-ex4

## basic info
- author's name: Lena Fiedor
- occupation: bioinformatics student, sailor, ballet dancer
- date of the exercise session: 20 III 24r

## little git tutorial
Git is a version control system used for coordinating work amongst programmers working simultanously on software development.

### creating a repository
To create your first git repository, you can follow two ways:
- create a new repository (virtual storage of your project): navigate to the project directory and use the `git init` command.

```
cd path/to/your/directory
git init
```

- clone an existing repository into project directory using `git clone`:

```
git clone <repo url or ssh>
```

#### saving changes
Well done! You've just created your first git repository. Now it's time to add the first file. To do so, you will have to:
- create the file
- add file to the commit using `git add`
**Note**: there is a useful flag for that command - by typing `git add -u` you add all untracked files to a particular commit.
- commit changes by typing `git commit` - it will create a unique version of chosen files, with is own hash value; it can be restored later at any point
**Note**: usually git requires you to specify a message for a praticular commit. It can be done by using *-m flag*, just like that: `git commit -m 'your message'
- push the exsting changes to the cloud: `git push` command will update the changes you've commited on the remote repository. **Don't forget to push changes in case of fire.**
