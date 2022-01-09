#!/bin/bash
help() {
   echo ""
   echo "VIPER INSTALLER"
   echo " install_viper.sh [options] containing_path"
   echo "  Creates a viper site environment at:"
   echo "  containing_path/virt_base"
   echo ""
   echo " Options:"
   echo "   -b --base: Name of base environment directory"
   echo "      Default is viper_site"
   echo "   -f --file: Path to a conda env yaml file"
   echo "      Default is envs/environment-virt.yml"
   echo "   -h --help: Display this help message.It is also "
   echo "      displayed when called without any arguments"
   echo "   -n --name: Name of main user conda environment"
   echo "      Default is virt_base"
   echo "   -c --conda"
   echo ""
   exit 2
}

# constants
CONDA_INSTALL_FILE="Miniconda3-latest-Linux-x86_64.sh"
URL="https://repo.anaconda.com/miniconda/${CONDA_INSTALL_FILE}"
DOWNLOAD_SAVE_PATH="/tmp/virt/downloads"

# defaults
FORCE_DOWNLOAD=false
ENV_YAML_PATH="/envs/environment-virt.yml"
BASE_ENV_NAME="virt_base"
USER_ENV_NAME="virt"
BUILD_PROD=false
CONDARC_PATH="./.condarc"

# Parse Input Options
PARSED_ARGUMENTS=$(getopt -s 'bash' -o dfnph \
  -l download,file,name,prod,help -- "$@")
VALID_ARGUMENTS=$?
if [ "$VALID_ARGUMENTS" != "0" ]; then
   help
fi
eval set -- "$PARSED_ARGUMENTS"
while true ; do
  case "$1" in
    -b | --base) BASE_ENV_NAME="$2" ; shift 2 ;;
    --condarc) CONDARC_PATH="$2" ; shift 2 ;;
    -d | --download) FORCE_DOWNLOAD=true  ; shift   ;;
    -f | --file) ENV_YAML_PATH="$2" ; shift 2 ;;
    -n | --name) USER_ENV_NAME="$2" ; shift 2 ;;
    -p | --prod) BASE_ENV_NAME=("virt_base_a" "virt_base_b") ; BUILD_PROD=true  ; shift   ;;
    -h | --help) help              ; shift   ;;
    # -- means the end of the arguments; drop this, and break out of the while loop
    --) shift; break ;;
    # If invalid options were passed, then getopt should have reported an error,
    # which we checked as VALID_ARGUMENTS when getopt was called...
    *) echo "Unexpected option: $1 - this should not happen."
       usage ; exit 2 ;;
  esac
done
CONTAINING_PATH="$1"

# Download Miniconda installer
if [ ! -f "${DOWNLOAD_PATH}/${CONDA_INSTALL_FILE}" ] || \
   [ "${FORCE_DOWNLOAD}" = true ]; then
  mkdir ${DOWNLOAD_SAVE_PATH}
  wget $URL -P ${DOWNLOAD_SAVE_PATH}
fi

# Create base envs
for ENV_NAME in "${BASE_ENV_NAME[@]}"; do
  BASE_ENV_PATH="${CONTAINING_PATH}/${ENV_NAME}"
  # remove the existing env
  if [ -d "${BASE_ENV_PATH}" ]; then
    echo "Removing existing ${ENV_NAME} environment"
    rm -rf "${BASE_ENV_PATH}"
    echo "   Removed existing base env"
  fi

  # Install miniconda
  INSTALLER_PATH="${DOWNLOAD_SAVE_PATH}/${CONDA_INSTALL_FILE}"
  sha256sum "${INSTALLER_PATH}"
  bash "${INSTALLER_PATH}" \
        -b -p "${BASE_ENV_PATH}"

  # Activate conda base env
  source "${BASE_ENV_PATH}/etc/profile.d/conda.sh"
  conda activate

  # Copy .condarc
  cp -f "${CONDARC_PATH}" "${BASE_ENV_PATH}/"

  # Add user environment
  conda env create \
    -n "${USER_ENV_NAME}" \
    -f "${ENV_YAML_PATH}"
done

# Create production symbolic link
if [ "${BUILD_PROD}" = true ]; then
  ln -sfT "${CONTAINING_PATH}/virt_base_a" "${CONTAINING_PATH}/virt_base"
fi

exit 0
