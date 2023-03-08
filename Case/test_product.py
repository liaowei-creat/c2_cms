import pytest

from c2_cms.Page.product_page import ProductPage


class TestProduct:
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    # 导出product
    def test_export_product(self, local_storage):
        text = ProductPage(local_storage).click_product_export().get_export_infomation()
        assert 'Export task created. Please proceed to "File Task" page to check the progress.' == text

    # 编辑product的中文name
    @pytest.mark.parametrize('name', ['coke12'])
    def test_edit_product(self, local_storage, name):
        text = ProductPage(local_storage).click_product_edit(name).edit_name_zn('coke2').click_btn_confirm().confirm_info()
        assert 'Operate Success!' == text

    # 查看详情页
    @pytest.mark.parametrize('name', ['coke12'])
    def test_view_detail(self, local_storage,name):
        content,product_id = ProductPage(local_storage).click_view(name).get_product_info()
        assert str(product_id) in content