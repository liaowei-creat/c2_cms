from c2_cms.Page.promotion_page import PromotionPage


class TestPromotion:
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    #新建promotion
    def test_create_promotion(self,local_storage):
        content = PromotionPage(local_storage)\
            .click_create_promotion()\
            .fill_in_promotion('12','32')\
            .click_btn_confirm()\
            .confirm_info()
        assert 'Operate Success!' == content

    #编辑promotion
    def test_edit_promotion(self, local_storage):
        content = PromotionPage(local_storage).click_promotion_edit('12').edit_name_zn('13').click_btn_confirm().confirm_info()
        assert 'Operate Success!' == content

    #查看promotion详情页面
    def test_view_promotion_detail(self,local_storage):
        content,promotion_id = PromotionPage(local_storage)\
            .click_view('12')\
            .get_promotion_info()
        assert promotion_id in content