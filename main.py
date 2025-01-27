import uuid

# Chỉ tạo ra uuid dạng v4

def generate_uuid_v4():
    """random uuid"""
    return str(uuid.uuid4())

def generate_multiple_uuids(count):
    """list of uuid"""
    return [generate_uuid_v4() for _ in range(count)]

def save_uuids_to_file(filename, uuids):
    """save a list"""
    try:
        with open(filename, "w") as file:
            file.write("\n".join(uuids))
        print(f"Luu {len(uuids)} uuid vào {filename}")
    except Exception as e:
        print(f"Loi!: {e}")

print("dung /start de bat dau và /exit thoat.")

while True:
    command = input("nhap lenh vao day: ").strip()
    if command.lower() == "/start":
        print("trinh tao uuid(v4) da khoi dong! dung /taoidv4, /taonhieuidv4, /save, hoac /exit de thoat.")
        current_uuids = []  
        while True:
            sub_command = input("nhap lenh: ").strip()
            if sub_command.lower() == "/taoidv4":
                print(f"random uuid: {generate_uuid_v4()}")
            elif sub_command.lower() == "/taonhieuidv4":
                try:
                    count = int(input("dien so luong uuidv4 can tao: ").strip())
                    if count > 0:
                        current_uuids = generate_multiple_uuids(count)
                        print(f"da tao {count} uuid:")
                        print("\n".join(current_uuids))
                    else:
                        print("nhap so luong.")
                except ValueError:
                    print("chi nhap so!")
            elif sub_command.lower() == "/save":
                if current_uuids:
                    filename = input("nhap ten de luu file uuid da tao (vd: uuid.txt): ").strip()
                    save_uuids_to_file(filename, current_uuids)
                else:
                    print("ko có uuid nao dc tao ca:/ dung /taonhieuidv4 de tao uuid truoc")
            elif sub_command.lower() == "/exit":
                print("dang thoat...")
                exit()
            else:
                print("sai lenh! dung /taoidv4, /taonhieuidv4, /save, hoac /exit de thoat.")
    elif command.lower() == "/exit":
        print("dang thoat...")
        break
    else:
        print("sai lenh! dung /start de bat dau và /exit thoat.")
