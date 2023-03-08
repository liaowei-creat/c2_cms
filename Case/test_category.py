import pytest

from c2_cms.Page.category_page import CategoryPage


class TestCategory:
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    # 编辑category的中文name
    @pytest.mark.parametrize('name', ['12'])
    def test_edit_categoru(self, local_storage, name):
        text = CategoryPage(local_storage) \
            .click_category_edit(name) \
            .edit_name_zn('coke2') \
            .click_btn_confirm() \
            .confirm_info()
        assert 'Operate Success!' == text

    # 查看详情页
    @pytest.mark.parametrize('name', ['12'])
    def test_view_detail(self, local_storage, name):
        content, category_id = CategoryPage(local_storage) \
            .click_category_view(name) \
            .get_category_info()
        assert str(category_id) in content