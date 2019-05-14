from git import Repo

repo = Repo('/Users/songsong/Documents/program/py3test')
git = repo.git

print(git.diff(name_only=True))
print(repo.untracked_files)


print(git.status())
repo.commit()