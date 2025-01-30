import uuid

def generate_uuid_v4():
    """uuidv4 random"""
    return str(uuid.uuid4())

def save_uuid_to_file(filename, uuid_value):
    """save txt"""
    if not filename.endswith(".txt"):
        filename += ".txt"  #ko cần phải điền đuôi txt
    
    try:
        with open(filename, "a", encoding="utf-8") as file:  
            file.write(uuid_value + "\n")
        print(f"✅ uuid dc lưu vào {filename}")
    except Exception as e:
        print(f"❌ error: {e}")

def reload_and_save_uuid():
    """tạo uuid ms rồi lưu vào file txt"""
    uuid_value = generate_uuid_v4()
    print(f"🔹 UUID mới: {uuid_value}")

    save_uuid_to_file("uuidsv4_single.txt", uuid_value)  # auto save

def generate_multiple_uuids():
    """tạo nhiều uuid"""
    try:
        count = int(input("nhập số lượng UUID cần tạo: ").strip())
        if count <= 0:
            print("❌ nhập số lớn hơn 0!")
            return

        uuids = [generate_uuid_v4() for _ in range(count)]
        print("🔹 list UUID đã tạo:")
        print("\n".join(uuids))

        filename = input("Điền tên file để lưu (không cần .txt): ").strip()
        save_uuid_to_file(filename, "\n".join(uuids))
    except ValueError:
        print("❌ vui lòng nhập số hợp lệ!")

def main():
    print("UUID v4 Generate (vi) - Komelab")
    print("🔹 Diền /start để bắt đầu hoặc /exit để thoát.")

    while True:
        command = input("Nhập lệnh: ").strip().lower()
        if command == "/start":
            print("✅ UUID v4 Generator đã bắt đầu. Dùng /create, /generate hoặc /exit.")
            while True:
                sub_command = input("Nhập lệnh: ").strip().lower()
                if sub_command == "/create":
                    reload_and_save_uuid()
                elif sub_command == "/generate":
                    generate_multiple_uuids()
                elif sub_command == "/exit":
                    print("👋 Thoát chương trình...")
                    exit()
                else:
                    print("❌ Đầu vào không hợp lệ. Dùng /reload, /generate hoặc /exit.")
        elif command == "/exit":
            print("👋 Đang thoát chương trình. Goodbye!")
            break
        else:
            print("❌ Đầu vào không hợp lệ. Dùng /start để bắt đầu hoặc /exit để thoát.")

if __name__ == "__main__":
    main()
