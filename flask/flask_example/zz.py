from git import Repo

repo = Repo('/Users/songsong/Documents/program/py3test')
if repo.git.diff(name_only=True) or repo.untracked_files:
    repo.git.pull()
    repo.git.add('.')
    repo.git.commit('-am', '提交，任务id:%s,request_id:%s,任务owner:%s,审核人:%s')
    repo.git.push()
    repo.close()
