# Configuration

The viper environment configuration is declared in a "viper.toml".  This 
configuration can then be accessed from the command line using the 
"viper config" command .   `viper config` will display the full configuration 
and providing the key(s) to be read will select a subset of it.

See the [configuration reference](reference/viper_configuration.md) for more details
on the keys in the configuration.

## Example Config File

Basic "viper.toml" file:

``` toml
--8<-- "viper.toml:2"
```
