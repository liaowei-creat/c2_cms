import pytest

from c2_cms.Page.sellablegroup_page import SellableGroupPage


class TestSellablegroup:
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    # 编辑sellablegroup的中文name
    @pytest.mark.parametrize('name', ['BBQ'])
    def test_edit_sellablegroup(self, local_storage, name):
        text = SellableGroupPage(local_storage) \
            .click_sellablegroup_edit(name) \
            .edit_name_zn('coke2') \
            .click_btn_confirm() \
            .confirm_info()
        assert 'Operate Success!' == text

    # 查看详情页
    @pytest.mark.parametrize('name', ['BBQ'])
    def test_view_detail(self, local_storage, name):
        content, sellablegroup_id = SellableGroupPage(local_storage) \
            .click_sellablegroup_view(name) \
            .get_sellablegroup_info()
        assert str(sellablegroup_id) in content