# Add .SKILL library
mkdir -p "${PREFIX}/lib/skill"
for item in "viper.lmgrinit" "README.md"; do
	cp -rf "${RECIPE_DIR}/../${item}" \
       "${PREFIX}/lib/skill"
done

# Run scripts
mkdir -p "${PREFIX}/bin"
for item in "tsp" "bsp" "ssp"; do
  cp -rf "${RECIPE_DIR}/../bin" \
         "${PREFIX}/bin"
done

# skill init script
cp -f "${RECIPE_DIR}/../viper.init.il" \
       "${PREFIX}/lib/skill/viper.init.ils"
# Library Manager init script
cp -f "${RECIPE_DIR}/../viper.lmgrinit" \
       "${PREFIX}/lib/skill/viper.lmgrinit"

# Copy the [de]activate scripts to $PREFIX/etc/conda/[de]activate.d.
# This will allow them to be run on environment activation.
for CHANGE in "activate" "deactivate"; do
    mkdir -p "${PREFIX}/etc/conda/${CHANGE}.d"
    cp "${RECIPE_DIR}/${CHANGE}.sh" \
       "${PREFIX}/etc/conda/${CHANGE}.d/${PKG_NAME}_${CHANGE}.sh"
    cp "${RECIPE_DIR}/${CHANGE}.csh" \
       "${PREFIX}/etc/conda/${CHANGE}.d/${PKG_NAME}_${CHANGE}.csh"
done
$PYTHON setup.py install
