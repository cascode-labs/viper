from unittest.mock import patch
from viper.project.sp import start_project
import os


def test_start_project():
    with patch('subprocess.run') as mock_run:
        start_project('ids_dev')
        mock_run.assert_called_once()
        mock_run.assert_called_with(["sp_tcsh",'ids_dev',"None", "False", "None"],env=os.environ)
