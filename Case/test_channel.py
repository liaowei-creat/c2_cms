import pytest

from c2_cms.Page.channel_page import ChannelPage


class TestChannel:
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    # 编辑channel的中文name
    @pytest.mark.parametrize('name', ['foo   bar'])
    def test_edit_categoru(self, local_storage, name):
        text = ChannelPage(local_storage) \
            .click_channel_edit(name) \
            .edit_name_zn('coke') \
            .click_btn_confirm() \
            .confirm_info()
        assert 'Operate Success!' == text

    # 查看详情页
    @pytest.mark.parametrize('name', ['coke'])
    def test_view_detail(self, local_storage, name):
        content, shop_id = ChannelPage(local_storage) \
            .click_channel_view(name) \
            .get_channel_info()
        assert str(shop_id) in content