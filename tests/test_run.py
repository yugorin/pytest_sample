"""pytest sample code. do it ad terminal 
   pytest tests/test_run.py --cov=src --cov-report term-missing -s 
"""
import os
import pytest
from src.run import Cal

IS_RELESE = True


class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = Cal()
        cls.test_file_name = 'test.txt'

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    def setup_method(self, method):
        print('method = {}'.format(method.__name__))

    def teardown_method(self, method):
        print('method = {}'.format(method.__name__))

    # conftest.py の中でテスト実行時のパラメータを定義
    def test_add_num_and_double(self, request):
        os_name = request.config.getoption('--os-name')
        print('os_name: ', os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        else:
            print('linux')
        assert self.cal.add_num_and_double(1, 1) == 4

    # conftest.py の中でテスト実行時のパラメータを定義
    # def test_add_num_and_double(self, tmpdir):
    #     print(tmpdir)

    # conftest.py の中でテスト実行時のパラメータを定義
    # def test_add_num_and_double(self, csv_file):
    #     print(csv_file)

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, self.test_file_name)
        
        assert os.path.exists(test_file_path) is True

    # conftest.py の中でテスト実行時のパラメータを定義
    # def test_add_num_and_double(self, request):
    #     os_name = request.config.getoption('--os-name')
    #     print('os_name: ', os_name)
    #     if os_name == 'mac':
    #         print('ls')
    #     elif os_name == 'windows':
    #         print('dir')
    #     else:
    #         print('linux')
    #     assert self.cal.add_num_and_double(1, 1) == 4
    
    def test_add_num_and_double_raises(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', 1)
    
    # @pytest.mark.skip(reason='~の理由によりskip')
    # def test_add_num_and_double_raises(self):
    #     with pytest.raises(ValueError):
    #         self.cal.add_num_and_double('1', 1)
    
    # @pytest.mark.skipif(IS_RELESE==True,
    #                     reason='リリースなのでskip!')
    # def test_add_num_and_double_raises(self):
    #     with pytest.raises(ValueError):
    #         self.cal.add_num_and_double('1', 1)

