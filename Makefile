help:
	@echo ""
	@echo "Build a IDS package or install IDS for development"
	@echo ""
	@echo "Build Packages"
	@echo "  'make Build' will build both a wheel and sdist"
	@echo "Install"
	@echo "  'make install-conda' will install a conda development environment"
	@echo "Build documentation"
	@echo "  'make auto-docs' will continuosly rebuild the docs"
	@echo "     as they are updated"
	@echo "  'make docs' will build the documentation once"
	@echo "Other tasks"
	@echo "  'make clean' will clean up the work area"
	@echo ""

.PHONY: help clean \
		build build-wheel build-sdist \
		docs auto-docs \
		install-conda install-conda-dev-only install-pip-dev

install-conda: install-conda-dev-only install-pip-dev

clean:
	rm -rf dist

build:
	flit build

publish:
	flit publish

docs:
	cd docs; make html

auto-docs:
	cd docs; ./autobuild.sh

install-conda-dev:
	mamba env create -f environment.yml

install-pip-dev:
	pip install --no-deps -e .

build-wheel:
	flit build --format wheel

build-sdist:
	flit build --format wheel

install-conda-base:
	wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh"
	exec Mambaforge-Linux-x86_64.sh
