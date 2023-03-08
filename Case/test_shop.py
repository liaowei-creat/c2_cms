import pytest

from c2_cms.Page.shop_page import ShopPage


class TestShop:
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    #新建shop
    @pytest.mark.parametrize('name_en,name_cn', [('seafood', '海鲜')])
    def test_create_shop(self,local_storage,name_en,name_cn):
        content = ShopPage(local_storage)\
            .click_create_shop()\
            .fill_create_shop(name_en,name_cn)\
            .click_btn_confirm()\
            .confirm_info()
        assert 'Operate Success!' == content

    # 编辑shop的中文name
    @pytest.mark.parametrize('name', ['123'])
    def test_edit_categoru(self, local_storage, name):
        text = ShopPage(local_storage) \
            .click_shop_edit(name) \
            .edit_name_zn('coke2') \
            .click_btn_confirm() \
            .confirm_info()
        assert 'Operate Success!' == text

    # 查看详情页
    @pytest.mark.parametrize('name', ['123'])
    def test_view_detail(self, local_storage, name):
        content, shop_id = ShopPage(local_storage) \
            .click_shop_view(name) \
            .get_shop_info()
        assert str(shop_id) in content

    #删除shop
    @pytest.mark.parametrize('name, tab_name',[('seafood', 'Deleted')])
    def test_delete_shop(self, local_storage, name, tab_name):
        content = ShopPage(local_storage)\
            .click_delete_shop(name)\
            .click_list_confirm()\
            .click_top_tab(tab_name)\
            .get_shop_name(name)
        assert content == name

    #复原shop
    @pytest.mark.parametrize('name, tab_name', [('seafood', 'Deleted')])
    def test_restore_shop(self, local_storage, name, tab_name):
        content = ShopPage(local_storage)\
            .click_top_tab(tab_name)\
            .click_restore_shop(name)\
            .click_list_confirm()\
            .click_top_tab('All')\
            .get_shop_name(name)
        assert content == name

    #下架shop
    @pytest.mark.parametrize('name, tab_name', [('seafood', 'Inactive')])
    def test_inactive_shop(self, local_storage, name, tab_name):
        content = ShopPage(local_storage)\
            .click_inactive_shop(name)\
            .click_top_tab(tab_name)\
            .get_shop_name(name)
        assert content == name

    #上架shop
    @pytest.mark.parametrize('name, tab_name', [('seafood', 'Inactive')])
    def test_active_shop(self, local_storage, name, tab_name):
        content = ShopPage(local_storage)\
            .click_top_tab(tab_name)\
            .click_inactive_shop(name)\
            .click_top_tab('Active')\
            .get_shop_name(name)
        assert content == name