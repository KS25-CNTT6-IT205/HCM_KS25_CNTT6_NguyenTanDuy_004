class Order:
    def __init__(self, id, customer_name, product_name, unit_price, quantity, shipping_fee, voucher):
        self.id = id
        self.customer_name = customer_name
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.shipping_fee = shipping_fee
        self.voucher = voucher
        self.calculate_total_amount()
        self.classify_order()

    def calculate_total_amount(self):
        self.total_amount = self.unit_price * self.quantity + self.shipping_fee - self.voucher

    def classify_order(self):
        if self.total_amount >= 10000000:
            self.order_type = 'VIP'
        elif self.total_amount >= 2000000:
            self.order_type = 'Lớn'
        elif self.total_amount >= 500000:
            self.order_type = 'Trung bình'
        else: self.order_type = 'Nhỏ'

class OrderManager:
    def __init__(self):
        self.orders: list[Order] = []

    def show_all(self):
        try:
            if not self.orders:
                raise EmptyList("Bạn không thể thao tác với dnah sách rỗng!")
            print(f"{"Mã đơn hàng":<15} | {"Tên khách hàng":<25} | {"Tên sản phẩm":<20} | {"Đơn giá":<12} | {"Số lượng":<8} | {"Phí vận chuyển":<15} | {"Voucher":12} | {"Tổng tiền":<15} | {"Phân loại đơn hàng":<20}")
            print("=" * 170)
            for value in self.orders:
                print(f"{value.id:<15} | {value.customer_name:<25} | {value.product_name:<20} | {value.unit_price:<12} | {value.quantity:<8} | {value.shipping_fee:<15} | {value.voucher:<12} | {value.total_amount:<15} | {value.order_type:<20}")
            else:
                print("\nHiển thị thành công toàn bộ đơn hàng!")
                return
        except EmptyList as exc_emp_list:
            print(exc_emp_list)

    def add_order(self):
        while True:
            or_id = input("Nhập mã đơn hàng: ").strip()
            if not or_id:
                print("Nhập liệu không được để trống! Nhập lại!")
                continue

            for value in self.orders:
                if value.id == or_id:
                    print("Mã đơn hàng đã tồn tại! Nhập lại!")
                    break
            else:
                break

        while True:
            cus_name = input("Nhập tên khách hàng: ").strip()
            if not cus_name:
                print("Nhập liệu không được để trống! Nhập lại!")
                continue
            break

        while True:
            pro_name = input("Nhập tên đơn hàng: ").strip()
            if not pro_name:
                print("Nhập liệu không được để trống! Nhập lại!")
                continue
            break

        while True:
            try:
                or_unit_price = float(input("Nhập đơn giá của sản phẩm: ").strip())
                if not or_unit_price:
                    print("Nhập liệu không được để trống! Nhập lại!")
                    continue
                if or_unit_price <= 0:
                    print("Đơn giá nhập không hợp lệ! Nhập lại!")
                    continue
                break
            except ValueError:
                print("Nhập kiểu dữ liệu không phù hợp! Nhập lại!")
                continue

        while True:
            try:
                or_quantity = int(input("Nhập số lượng của sản phẩm: ").strip())
                if not or_quantity:
                    print("Nhập liệu không được để trống! Nhập lại!")
                    continue
                if or_quantity < 1 or or_quantity > 1000:
                    print("Số lượng nhập không hợp lệ! Nhập lại!")
                    continue
                break
            except ValueError:
                print("Nhập kiểu dữ liệu không phù hợp! Nhập lại!")
                continue

        while True:
            try:
                or_fee = float(input("Nhập phí vận chuyển của sản phẩm: ").strip())
                if not or_fee:
                    print("Nhập liệu không được để trống! Nhập lại!")
                    continue
                if or_fee <= 0:
                    print("Số lượng nhập không hợp lệ! Nhập lại!")
                    continue
                break
            except ValueError:
                print("Nhập kiểu dữ liệu không phù hợp! Nhập lại!")
                continue

        while True:
            try:
                or_voucher = float(input("Nhập voucher của sản phẩm: ").strip())
                if not or_voucher:
                    print("Nhập liệu không được để trống! Nhập lại!")
                    continue
                if or_voucher <= 0:
                    print("Số lượng nhập không hợp lệ! Nhập lại!")
                    continue
                break
            except ValueError:
                print("Nhập kiểu dữ liệu không phù hợp! Nhập lại!")
                continue

        new_order = Order(or_id, cus_name, pro_name, or_unit_price, or_quantity, or_fee, or_voucher)

        self.orders.append(new_order)

        print("Thêm đơn hàng mới thành công!")
        


    def update_order(self):
        try:
            if not self.orders:
                raise EmptyList("Bạn không thể thao tác với dnah sách rỗng!")
            while True:
                or_id = input("Nhập mã đơn hàng: ").strip()
                if not or_id:
                    print("Nhập liệu không được để trống! Nhập lại!")
                    continue

                for value in self.orders:
                    if value.id == or_id:
                        print(f"Đã tìm thấy đơn hàng: {value.id} - {value.customer_name} - {value.product_name} - {value.total_amount}")
                        while True:
                            try:
                                or_unit_price = float(input("Nhập đơn giá của sản phẩm: ").strip())
                                if not or_unit_price:
                                    print("Nhập liệu không được để trống! Nhập lại!")
                                    continue
                                if or_unit_price <= 0:
                                    print("Đơn giá nhập không hợp lệ! Nhập lại!")
                                    continue
                                break
                            except ValueError:
                                print("Nhập kiểu dữ liệu không phù hợp! Nhập lại!")
                                continue

                        while True:
                            try:
                                or_quantity = int(input("Nhập số lượng của sản phẩm: ").strip())
                                if not or_quantity:
                                    print("Nhập liệu không được để trống! Nhập lại!")
                                    continue
                                if or_quantity < 1 or or_quantity > 1000:
                                    print("Số lượng nhập không hợp lệ! Nhập lại!")
                                    continue
                                break
                            except ValueError:
                                print("Nhập kiểu dữ liệu không phù hợp! Nhập lại!")
                                continue

                        while True:
                            try:
                                or_fee = float(input("Nhập phí vận chuyển của sản phẩm: ").strip())
                                if not or_fee:
                                    print("Nhập liệu không được để trống! Nhập lại!")
                                    continue
                                if or_fee <= 0:
                                    print("Số lượng nhập không hợp lệ! Nhập lại!")
                                    continue
                                break
                            except ValueError:
                                print("Nhập kiểu dữ liệu không phù hợp! Nhập lại!")
                                continue

                        while True:
                            try:
                                or_voucher = float(input("Nhập voucher của sản phẩm: ").strip())
                                if not or_voucher:
                                    print("Nhập liệu không được để trống! Nhập lại!")
                                    continue
                                if or_voucher <= 0:
                                    print("Số lượng nhập không hợp lệ! Nhập lại!")
                                    continue
                                break
                            except ValueError:
                                print("Nhập kiểu dữ liệu không phù hợp! Nhập lại!")
                                continue

                        value.unit_price = or_unit_price
                        value.quantity = or_quantity
                        value.shipping_fee = or_fee
                        value.voucher = or_voucher

                        value.calculate_total_amount()
                        value.classify_order()

                        print("Cập nhật thành công!")
                        return
                else:
                    raise EmptyValue("Bạn đang nhập một mã sản phẩm không tồn tại!")
        except EmptyValue as exc_emp_value:
            print(exc_emp_value)
        except EmptyList as exc_emp_list:
            print(exc_emp_list)

    def delete_order(self):
        try:
            if not self.orders:
                raise EmptyList("Bạn không thể thao tác với dnah sách rỗng!")
            while True:
                or_id = input("Nhập mã đơn hàng: ").strip()
                if not or_id:
                    print("Nhập liệu không được để trống! Nhập lại!")
                    continue

                for value in self.orders:
                    if value.id == or_id:
                        print(f"Đã tìm thấy đơn hàng: {value.id} - {value.customer_name} - {value.product_name} - {value.total_amount}")
                        while True:
                            try:
                                confirm = input("Bạn có chắc chăn muốn xóa đơn hàng này không? (Y/N): ").strip().upper()
                                match confirm:
                                    case "Y":
                                        self.orders.remove(value)
                                        print("Xóa thành công đơn hàng!")
                                        return
                                    case "N":
                                        print("Hoàn thành với thao tác không xóa!")
                                        return
                                    case _:
                                        raise WrongChoice("Nhập liệu xác nhận không hợp lệ! Nhập lại!")
                            except WrongChoice as exc_choice:
                                print(exc_choice)
                else:
                    raise EmptyValue("Bạn đang nhập một mã sản phẩm không tồn tại!")
        except EmptyValue as exc_emp_value:
            print(exc_emp_value)
        except EmptyList as exc_emp_list:
            print(exc_emp_list)

    def search_order(self):
        try:
            if not self.orders:
                raise EmptyList("Bạn không thể thao tác với dnah sách rỗng!")
            while True:
                search_name = input("Nhập tên khách hàng: ").strip()
                if not search_name:
                    print("Nhập liệu không được để trống! Nhập lại!")
                    continue
                break

            flag = False
            print("Đang tìm kiếm...")
            print(f"{"Mã đơn hàng":<15} | {"Tên khách hàng":<25} | {"Tên sản phẩm":<20} | {"Đơn giá":<12} | {"Số lượng":<8} | {"Phí vận chuyển":<15} | {"Voucher":12} | {"Tổng tiền":<15} | {"Phân loại đơn hàng":<20}")
            print("=" * 170)
            for value in self.orders:
                if search_name in value.customer_name:
                    print(f"{value.id:<15} | {value.customer_name:<25} | {value.product_name:<20} | {value.unit_price:<12} | {value.quantity:<8} | {value.shipping_fee:<15} | {value.voucher:<12} | {value.total_amount:<15} | {value.order_type:<20}")
                    flag = True
            else: 
                print("Hoàn thành thao tác tìm kiếm")
            
            if not flag:
                print("Không tìm thấy đơn phù hợp!")
        except EmptyList as exc_emp_list:
            print(exc_emp_list)
            

class WrongChoice(Exception):
    """Lớp này dùng khi nhập sai menu"""
    pass

class EmptyList(Exception):
    """Lớp này dùng khi cố thao tác với danh sách rỗng"""
    pass

class EmptyValue(Exception):
    """Lớp này dùng nếu không tồn tại một giá trị cần tìm"""
    pass

class TotalLessThanZero(Exception):
    """Lớp này dùng nếu total_amounr < 0"""
    pass

def main():
    current_manager = OrderManager()
    # dữ liệu mẫu:
    current_manager.orders = [
        Order("OD001", "Nguyen Van A", "Dau goi dau", 150000, 3, 20000, 5000),
        Order("OD002", "Tran Thi Lua", "May xay", 800000, 1, 35000, 20000)
    ]
    while True:
        try:
            print()
            print(' MENU '.center(50, "="))
            print("1. Hiển thị danh sách đơn hàng\n" \
            "2. Thêm đơn hàng mới\n" \
            "3. Cập nhật đơn hàng\n" \
            "4. Xóa đơn hàng\n" \
            "5. Tìm kiếm đơn hàng\n" \
            "6. Thoát")
            print("=" * 50)

            choice = input("Nhập lựa chọn của bạn: ").strip()

            match choice:
                case '1':
                    current_manager.show_all()
                case '2':
                    current_manager.add_order()
                case '3':
                    current_manager.update_order()
                case '4':
                    current_manager.delete_order()
                case '5':
                    current_manager.search_order()
                case '6':
                    print("Cảm ơn bạn đã sử dụng hệ thống quản lý đơn hàng!")
                    return
                case _:
                    raise WrongChoice("Bạn đang cố nhập một lựa chọn ngoài menu! Nhập lại!")
        except WrongChoice as exc_choice:
            print(exc_choice)

if __name__ == "__main__":
    main()