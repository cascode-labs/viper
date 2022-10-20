#!/bin/bash
help() {
  echo ""
  echo "VIPER INSTALLER"
  echo " install-viper-linux-x86_64.sh [options] site_path"
  echo "  Creates a viper site environment at site_path"
  echo ""
  echo " Options:"
  echo "   -d --download: Path to a 'download' folder containing the "
  echo "      Mambaforge install script and viper.yml file"
  echo "   -f --file: A conda environment yaml file defining a custom set of"
  echo "      packages to install into the user's terminal viper environment"
  echo "   -h --help: Display this help message. It is also "
  echo "      displayed when called without any arguments"
  echo ""
  exit 0
}

# constants
MINIFORGE_URL_ROOT=\
"https://github.com/conda-forge/miniforge/releases/latest/download"
MAMBAFORGE_INSTALL_FILE="Mambaforge-Linux-x86_64.sh"
MAMBAFORGE_URL="${MINIFORGE_URL_ROOT}/${MAMBAFORGE_INSTALL_FILE}"
# MAMBAFORGE_HASH_FILE="${MAMBAFORGE_INSTALL_FILE}.sha256"
# MAMBAFORGE_URL_HASH="${MINIFORGE_URL_ROOT}/${MAMBAFORGE_HASH_FILE}"
VIPER_URL_ROOT=\
"https://github.com/cascode-labs/viper/releases/latest/download"
VIPER_ENV_YML_FILE="viper.yml"
VIPER_ENV_YML_URL="${VIPER_URL_ROOT}/${VIPER_ENV_YML_FILE}"

# defaults
BASE_ENV_NAME="viper_base"
USER_ENV_YML_PATH=""

# Parse Input Options
PARSED_ARGUMENTS=$(getopt -s 'bash' \
  -o dfnph \
  -l download,file,name,prod,help -- "$@")
VALID_ARGUMENTS=$?
if [ "$VALID_ARGUMENTS" != "0" ]; then
   help
fi
eval set -- "$PARSED_ARGUMENTS"
while true ; do
  case "$1" in
    -f | --file) USER_ENV_YML_PATH="$2" ; shift 2 ;;
    -h | --help) help              ; shift   ;;
    # -- means the end of the arguments; drop this, and break out of the while loop
    --) shift; break ;;
    # If invalid options were passed, then getopt should have reported an error,
    # which we checked as VALID_ARGUMENTS when getopt was called...
    *) echo "Unexpected option: $1 - this should not happen."
       usage ; exit 2 ;;
  esac
done
SITE_PATH="$1"



# Create folder structure
ENVS_PATH="${SITE_PATH}/envs"
PRJS_PATH="${SITE_PATH}/prjs"
TMP_PATH="/tmp/viper"
TMP_DOWNLOADS_PATH="${TMP_PATH}/downloads"
VIPER_PATHS=("${ENVS_PATH}" "${PRJS_PATH}" "${TMP_PATH}" \
             "${TMP_DOWNLOADS_PATH}")
for viper_folder in "${VIPER_PATHS[@]}"; do
  mkdir -p "${viper_folder}"
done
# Download and install Mambaforge
wget -O "${MAMBAFORGE_INSTALL_FILE}" \
     -P "${TMP_DOWNLOADS_PATH}" \
     "${MAMBAFORGE_URL}"
# wget -O "${MAMBAFORGE_HASH_FILE}" \
#      -P "${TMP_DOWNLOADS_PATH}" \
#      "${MAMBAFORGE_URL_HASH}"
BASE_PREFIX="${ENVS_PATH}/${BASE_ENV_NAME}"
INSTALLER_PATH="${TMP_DOWNLOADS_PATH}/${MAMBAFORGE_INSTALL_FILE}"
# INSTALLER_HASH_PATH="${TMP_DOWNLOADS_PATH}/${MAMBAFORGE_HASH_FILE}"
# sha256sum --check "$INSTALLER_HASH_PATH" "${INSTALLER_PATH}"
bash "${INSTALLER_PATH}" \
      -b -p "${BASE_PREFIX}"

# Setup base environment to place all the envs in $ENVS_PATH
echo "envs_dirs:" >> "${BASE_PREFIX}/.condarc"
echo "  - ${ENVS_PATH}" >> "${BASE_PREFIX}/.condarc"

# Create user terminal environment
# shellcheck disable=SC1091
source "${BASE_PREFIX}/etc/profile.d/conda.sh"
# shellcheck disable=SC1091
source "${BASE_PREFIX}/etc/profile.d/mamba.sh"
if [ -z "${USER_ENV_YML_PATH}" ]; then
  wget "${VIPER_ENV_YML_URL}" -P "${TMP_DOWNLOADS_PATH}"
  USER_ENV_YML_PATH="${TMP_DOWNLOADS_PATH}/${VIPER_ENV_YML_FILE}"
fi
mamba env create -f "${USER_ENV_YML_PATH}"
