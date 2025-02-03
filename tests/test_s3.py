import unittest
from s3_integration import upload_to_s3
from unittest.mock import patch

class TestS3Integration(unittest.TestCase):

    @patch('s3_integration.s3_client.put_object')
    def test_upload_to_s3(self, mock_put_object):
        mock_put_object.return_value = {}
        data = {"key": "value"}
        file_name = "test_file"
        upload_to_s3(data, file_name)
        mock_put_object.assert_called_with(
            Bucket='matrix.fish',
            Key=f'interactions/{file_name}.json',
            Body='{"key": "value"}',
            ContentType='application/json'
        )

if __name__ == '__main__':
    unittest.main()