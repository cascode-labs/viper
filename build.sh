#!/bin/bash

# help
if [ $# == 0 ]; then
  echo "Builds the package"
  echo " build.sh build_prefix"
  echo "   builds the package at the specified environment"
  echo " build.sh build_prefix channel_path"
  echo "   builds the package at the specified environment"
  echo "   and releases it to the specified channel"
fi

# Parse Inputs
PROJECT="conda-virtuoso"
if [ ! "${BASE_PREFIX}" ]; then
  BASE_PREFIX="/prj/ids/ids-conda/envs/anaconda"
fi
BUILD_PREFIX="$1"
if [ $# == 2 ]; then
  CHANNEL_PATH=$2
elif [ ! "${CHANNEL_PATH}" ]; then
  CHANNEL_PATH=""
fi

# Basic Information
VER_INFO=$(cat ./version)
PWD=$(pwd)
DATE=$(date)
echo "Building $PROJECT"
echo "--------------------------"
echo " Version: $VER_INFO"
echo ' pwd: '
echo "  $PWD"
echo " Date: $DATE"
echo " BUILD_PREFIX: "
echo "  ${BUILD_PREFIX}"
echo " BASE_PREFIX: "
echo "  ${BASE_PREFIX}"
echo " CHANNEL_PATH:"
echo "  ${CHANNEL_PATH}"
echo ""

# Setup Conda
# shellcheck disable=SC1090
source "${BASE_PREFIX}/etc/profile.d/conda.sh"

# Create or update build env
if [[ -d ${BUILD_PREFIX} ]]; then
  BUILD_CMD="update"
else
  BUILD_CMD="create"
fi
conda env ${BUILD_CMD} -p "${BUILD_PREFIX}" -f ./envs/environment-build.yml
conda activate "${BUILD_PREFIX}"
echo ""
echo "Build Env Info"
echo "-----------------"
conda info
conda list
echo ""

# Build the package
echo "Build the package"
echo "-----------------"
OUTPUT_PATH=$(conda build --output conda-recipe) # Output path
echo " Package OUTPUT_PATH:"
echo "  ${OUTPUT_PATH}"
conda build \
  -c defaults \
  -c conda-forge \
  conda-recipe

# Release to channel if channel path is supplied
if [ ${CHANNEL_PATH} != "" ] && [ -f "${OUTPUT_PATH}" ]; then
  echo "RELEASE TO DEV CHANNEL"
  echo "----------------------"
  echo "Releasing to: "
  echo " ${CHANNEL_PATH}/linux-64"
  cp "$OUTPUT_PATH" "${CHANNEL_PATH}/linux-64/"
  conda index ${CHANNEL_PATH}
fi

# Generate docs
if [ -f "${OUTPUT_PATH}" ]; then
  echo "GENERATE DOCS"
  echo "-------------"
  cd docs-src
  make html
  cp
fi
