import pytest
from unittest.mock import patch, Mock
# from user import User

@patch('__main__.Database')
class TestUser:
    def test_get_current_user_details(self, mock_database_class):
        mock_database = Mock()
        mock_database.get_user_details.return_value = {'data': 'User data'}

        mock_database_class.return_value = mock_database

        user = User(database=mock_database_class())
        result = user.get_user_details('1')

        # Проверки
        assert result == {'data': 'User data'}
 