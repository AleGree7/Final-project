from git import Repo
import os
import subprocess
import glob

if __name__ == '__main__':
    report_path = "C:/Users/Public"
    repo_url1 = "https://github.com/jamesmawm/Mastering-Python-for-Finance-source-codes"
    repo_url2 = "https://github.com/shashankvemuri/Finance.git"
    repo_url3 = "https://github.com/OpenBB-finance/OpenBBTerminal.git"
    all_repos = repo_url1,repo_url2, repo_url3
    for repo_url in all_repos:
        print("downloading repo: " + repo_url)
        repo_path = repo_url.split("/")[-1]

        if not os.path.exists(repo_path):
            Repo.clone_from(repo_url, repo_path)
            print("download finished")
        else:
            print("Repo exist")

        ##safety checks
        print("safety started to work...")
        os.chdir(repo_path)
        with open(report_path + '/safety' + repo_path + '.txt', 'w+') as outfile:
            subprocess.run(['safety', 'scan', '--target', './'], stdout=outfile)
        print("Safety check file provided: " + report_path + '/safety.txt')

        # bandit checks
        print("bandit started to work...")
        with open(report_path + '/bandit' + repo_path + ".txt", 'w+') as outfile:
            for cfile in glob.glob(os.getcwd() + '/**/*.py', recursive=True):
                print("bandit check file:" + cfile)
                outfile.write("-----" + cfile + "-----" + "\n")
                proc = subprocess.run(['bandit', cfile, '-ll', '-v'], stdout=outfile)
        print("bandit end his scan:" + report_path + '/bandit' + repo_path + ".txt")

        ## Pylint
        print("Pylint started to work...")
        # with open(report_path + '/pylint' + repo_path + ".txt", "w") as outfile:
        #     subprocess.run(['pylint', repo_path], stdout=outfile)
        #     print("Pylint ended work." + report_path + "/pylint.txt")

        with open(report_path + '/pylint' + repo_path + ".txt", 'w+') as outfile:
            for cfile in glob.glob(os.getcwd() + '/**/*.py', recursive=True):
                print("Pylint check file:" + cfile)
                with open(cfile, 'r') as file:
                    outfile.write("-----" + cfile + "-----" + "\n")
                    subprocess.run(['pylint', cfile], stdout=outfile)
        print("Pylint ended work." + report_path + '/pylint' + repo_path + ".txt")
