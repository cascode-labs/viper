# Configuration

The viper environment configuration is declared as a part of a project's "pyproject.toml" or in a "viper.toml" file.  This configuration can then be accessed from the command line using the `viper config` command .   `viper config` will display the full configuration and providing the key(s) to be read will select a subset of it.

See the [configuration reference](reference/viper_configuration.md) for more details on the keys in the configuration.

## Example Config File

``` toml
--8<-- "docs/viper.toml:2"
```
