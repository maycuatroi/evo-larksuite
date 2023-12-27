from evo_larksuite.entities.table import LarkTable


class LarkBase:
    def __init__(self, base_id):
        self.base_id = base_id

    def get_table(self, table_id):
        return LarkTable(self.base_id, table_id)


if __name__ == "__main__":
    lark_base = LarkBase("BASE_ID")
    table = lark_base.get_table("tbliVkQwKVl9pr0n")
    records = table.add_records(
        [
            {
                "fields": {
                    "CompanyID": "1",
                    "Company Name": "test",
                }
            }
        ]
    )
    print(records)
