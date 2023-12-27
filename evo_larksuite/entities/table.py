from evo_larksuite.config import LARK_BASE_URL
from evo_larksuite.entities.lark_entity import LarkEntity


class LarkTable(LarkEntity):
    def __init__(self, base_id, table_id):
        self.base_id = base_id
        self.table_id = table_id
        super().__init__()

    def get_records(self, page_size=None):
        if page_size is not None:
            page_size_params = f"?page_size={page_size}"
        else:
            page_size_params = ""
        is_has_more = True
        page_token = None
        total_items = []
        while is_has_more:
            page_token_params = f"&page_token={page_token}" if page_token else ""
            url = (
                LARK_BASE_URL
                + f"bitable/v1/apps/{self.base_id}/tables/{self.table_id}/records{page_size_params}"
            )
            res = self.send_api(url, method="GET", data={"page_token": page_token})
            data = res.get("data")
            page_token = data.get("page_token")
            is_has_more = data.get("has_more")
            total = data.get("total")
            items = data.get("items")
            total_items += items
        return total_items

    def add_records(self, records: list):
        data = {"records": records}
        url = (
            LARK_BASE_URL
            + f"bitable/v1/apps/{self.base_id}/tables/{self.table_id}/records/batch_create"
        )
        res = self.send_api(url, method="POST", data=data)
        return res
