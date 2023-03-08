import pytest

from c2_cms.Page.bundle_page import BundlePage


class TestBundle:

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    # 编辑bundle的中文name
    @pytest.mark.parametrize('name', ['12'])
    def test_edit_product(self, local_storage, name):
        text = BundlePage(local_storage)\
            .click_bundle_edit(name)\
            .edit_name_zn('coke2')\
            .click_btn_confirm()\
            .confirm_info()
        assert 'Operate Success!' == text

    # 查看详情页
    @pytest.mark.parametrize('name', ['12'])
    def test_view_detail(self, local_storage, name):
        content, product_id = BundlePage(local_storage)\
            .click_bundle_view(name)\
            .get_bundle_info()
        assert str(product_id) in content