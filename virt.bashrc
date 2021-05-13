#!/bin/bash
# virt Bash initialization
gp() { /rds/prod/custom/cad/bin/grep_prj $1; }
alias dev="conda activate dev"
cds() { cd /prj/crdc_dev/${USER}/$@; }

# Setup git
export PATH="/usr/local/pkg/git/current/bin:${PATH}"

# Setup Conda
if [ -d "/prj/crdc_dev/${USER}/IDS-conda/envs/anaconda" ]; then
	export IDS_ROOT_ANACONDA="/prj/crdc_dev/${USER}/IDS-conda/envs/anaconda"
else
	export IDS_ROOT_ANACONDA="/prj/ids/ids-conda/envs/anaconda"
fi

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$("${IDS_ROOT_ANACONDA}/bin/conda" 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "{IDS_ROOT_ANACONDA}/etc/profile.d/conda.sh" ]; then
        . "{IDS_ROOT_ANACONDA}/etc/profile.d/conda.sh"
    else
        export PATH="{IDS_ROOT_ANACONDA}/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

