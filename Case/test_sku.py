import pytest

from c2_cms.Page.sku_page import SkuPage


class TestSku:
    def setup_class(self):
        pass
    def teardown_class(self):
        pass

    #导出sku
    def test_sku(self,local_storage):
        text = SkuPage(local_storage).click_sku_export().get_infomation()
        assert 'Export task created. Please proceed to "File Task" page to check the progress.' == text

    #编辑sku的中文name
    @pytest.mark.parametrize('name', ['FNB6501'])
    def test_edit_sku(self,local_storage,name):
        text = SkuPage(local_storage).click_edit().edit_name_zn(name).click_btn_confirm().confirm_info()
        assert 'Operate Success!' == text

    #查看详情页
    @pytest.mark.parametrize('sku',['FNB6501'])
    def test_view_detail(self,sku,local_storage):
        content = SkuPage(local_storage).click_view(sku).get_sku_info(sku)
        assert f'SKU: {sku}' == content