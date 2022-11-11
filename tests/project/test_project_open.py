import os
from unittest.mock import patch
from viper.cli import open_project_cli


def test_open_project():
    with patch('subprocess.run') as mock_run:
        open_project_cli('ids_dev')
        mock_run.assert_called_once()
        mock_run.assert_called_with(
            ["sp_bash",'ids_dev',"None", "False", "None"],
            env=os.environ, check=True)
