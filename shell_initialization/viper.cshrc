#!/bin/tcsh
setenv IDS_ROOT_RDS /rds/prod/HOTCODE/amslibs/oa614/cdsware/IDS
setenv IDS_ROOT_PRJ /prj/ids
setenv IDS_ROOT_FRAMEWORK "${IDS_ROOT_RDS}/IDS"

# runs the user's IDS.cshrc file
alias ids-dev "source /prj/${USER}/IDS/IDS.cshrc"
# Abbreviation for grep_prj
#alias gp "/rds/prod/custom/cad/bin/grep_prj \!*"
alias gp "grep_prj \!*"
alias dev "conda activate dev"
alias cds "cd /prj/crdc_dev/${USER}/\!*"
alias ids-index "firefox http://idshost:5050"

# Setup PyCharm
set PYCHARM_PRO_PATH="/prj/crdc_dev/${USER}/PyCharm/pycharm-2020.1.1/bin/pycharm.sh"
if ( -r "${PYCHARM_PRO_PATH}" ) then
	alias pycharm "${PYCHARM_PRO_PATH}"
else if ( `uname -r | awk '{split($0,a,"."); print a[4]}'` == el6 ) then
	alias pycharm /rds/prod/HOTCODE/tools/pycharm2018.1/bin/pycharm.sh
else
	alias pycharm /rds/prod/HOTCODE/tools/pycharm2019.3/bin/pycharm.sh
endif

# Setup Anaconda
#   If you want to move Anadaconda, then it needs to be reinstalled
#   using the instructions at https://docs.anaconda.com/anaconda/install/linux/
if ( -d "/prj/crdc_dev/${USER}/IDS-conda/envs/anaconda" && $?IDS_DEV ) then
	setenv IDS_ROOT_ANACONDA "/prj/crdc_dev/${USER}/IDS-conda/envs/anaconda"
else
	setenv IDS_ROOT_ANACONDA "${IDS_ROOT_PRJ}/ids-conda/envs/anaconda"
endif
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if ( -f "${IDS_ROOT_ANACONDA}/etc/profile.d/conda.csh" ) then
    source "${IDS_ROOT_ANACONDA}/etc/profile.d/conda.csh"
else
    setenv PATH "${IDS_ROOT_ANACONDA}/bin:$PATH"
endif
# <<< conda initialize <<<

conda activate IDS
