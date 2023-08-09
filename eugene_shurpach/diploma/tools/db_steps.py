class LitecartDB:

    def find_order_id_by_user_email(self, email):
        self.execute(f"SELECT id FROM lc_orders WHERE customer_email = '{email}' "
                     f"AND date_created >= DATE_ADD(NOW(), INTERVAL -215 MINUTE)")
        return self.fetchall()

    def delete_order_by_user_email(self, email):
        self.execute(f"DELETE FROM lc_orders WHERE customer_email = '{email}' "
                     f"AND date_created >= DATE_ADD(NOW(), INTERVAL -215 MINUTE)")
