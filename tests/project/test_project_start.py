import os
from unittest.mock import patch
from viper.project.start import start_project


def test_start_project():
    with patch('subprocess.run') as mock_run:
        start_project('ids_dev')
        mock_run.assert_called_once()
        mock_run.assert_called_with(
            ["sp_bash",'ids_dev',"None", "False", "None"],
            env=os.environ, check=True)
